#!/usr/bin/env python3
"""Measures of the case "family night": what git history alone says about one day.

Usage:
    python3 measures.py --root DIR [--day 2026-10-29] [--offset +01:00] [--json FILE]

DIR holds a checkout of each repository named in REPOSITORIES, side by side.
The program only reads: it runs `git log` and `git tag`, nothing else.

What it measures, per repository, for the local day:
    commits       commits whose committer time falls on the day (all branches)
    files         distinct paths those commits touch
    tags          tags created on the day, with their times (the proxy for a release)
    decisions     decision records (decisions/NNNN-*.md) first added on the day
    moves         of those, records titled "move-to-...": a pin raise kept as a decision
    first, last   the times of the first and last commit of the day

And three cautions the numbers carry, printed beside them:
    shared        commits with the same hash in two repositories (a split history)
    carried       commits whose author time and subject recur in another repository,
                  where the hash differs (a history rewritten when it moved)
    skew          commits whose author day differs from their committer day

The hand count (hand-counts.csv) is read and tallied, not checked: a program
cannot tell which questions reached a person.
"""
import argparse
import csv
import json
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPOSITORIES = [
    "reader-ergonomics",
    "reader-ergonomics-academic",
    "reader-ergonomics-presentations",
    "reader-ergonomics-software-design",
    "reader-ergonomics-learning",
    "reader-ergonomics-topic",
    "reader-ergonomics-blueprint",
]


def parse_offset(text):
    sign = -1 if text.startswith("-") else 1
    hours, minutes = text.lstrip("+-").split(":")
    return timezone(sign * timedelta(hours=int(hours), minutes=int(minutes)))


def git(repo, *args):
    done = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=True)
    return done.stdout


def local(epoch, tz):
    return datetime.fromtimestamp(int(epoch), tz)


def read_commits(repo, tz):
    """Every commit on any branch: hash, author time, committer time, subject."""
    out = git(repo, "log", "--all", "--format=%H%x1f%at%x1f%ct%x1f%s")
    commits = []
    for line in out.splitlines():
        h, at, ct, subject = line.split("\x1f", 3)
        commits.append({"hash": h, "author": local(at, tz), "committer": local(ct, tz), "subject": subject})
    return commits


def files_touched(repo, hashes):
    """Distinct paths touched by the given commits."""
    paths = set()
    for h in hashes:
        out = git(repo, "show", "--name-only", "--format=", "--no-renames", h)
        paths.update(p for p in out.splitlines() if p)
    return paths


def decisions_added(repo, day, tz):
    """Decision records whose first commit falls on the day."""
    out = git(repo, "log", "--all", "--diff-filter=A", "--name-only", "--no-renames",
              "--format=@@%ct", "--", "decisions/")
    first = {}
    stamp = None
    for line in out.splitlines():
        if line.startswith("@@"):
            stamp = int(line[2:])
        elif line:
            name = line.rsplit("/", 1)[-1]
            if line.startswith("decisions/") and name[:4].isdigit() and name.endswith(".md"):
                first[line] = min(first.get(line, stamp), stamp)
    return sorted(p for p, s in first.items() if local(s, tz).date().isoformat() == day)


def is_move(path):
    """A record whose slug starts with move-to: a pin raise written as a decision."""
    return path.rsplit("/", 1)[-1][5:].startswith("move-to-")


def tags_on_day(repo, day, tz):
    """Tags whose creation time (annotated) or commit time (lightweight) falls on the day."""
    out = git(repo, "for-each-ref", "refs/tags", "--format=%(refname:short) %(creatordate:unix)")
    found = []
    for line in out.splitlines():
        name, stamp = line.rsplit(" ", 1)  # a tag name holds no space
        when = local(stamp, tz)
        if when.date().isoformat() == day:
            found.append((name, when.strftime("%H:%M")))
    return sorted(found, key=lambda t: t[1])


def measure(root, day, tz):
    per = {}
    by_hash = defaultdict(set)
    by_key = defaultdict(set)
    for name in REPOSITORIES:
        repo = Path(root) / name
        commits = read_commits(repo, tz)
        today = [c for c in commits if c["committer"].date().isoformat() == day]
        for c in commits:
            by_hash[c["hash"]].add(name)
            by_key[(int(c["author"].timestamp()), c["subject"])].add((name, c["hash"]))
        times = sorted(c["committer"] for c in today)
        per[name] = {
            "commits_all_time": len(commits),
            "commits": len(today),
            "files": len(files_touched(repo, [c["hash"] for c in today])),
            "tags": tags_on_day(repo, day, tz),
            "decisions": decisions_added(repo, day, tz),
            "moves": 0,
            "first": times[0].strftime("%H:%M") if times else None,
            "last": times[-1].strftime("%H:%M") if times else None,
            "skew": sum(1 for c in today if c["author"].date() != c["committer"].date()),
            "_hashes": {c["hash"] for c in today},
            "_keys": {(int(c["author"].timestamp()), c["subject"], c["hash"]) for c in today},
        }
    for name, row in per.items():
        row["moves"] = sum(1 for d in row["decisions"] if is_move(d))
    shared = {h for h, names in by_hash.items() if len(names) > 1}
    for name, row in per.items():
        row["shared"] = len(row["_hashes"] & shared)
        carried = 0
        for at, subject, h in row["_keys"]:
            if any(other != name and oh != h for other, oh in by_key[(at, subject)]):
                carried += 1
        row["carried"] = carried
    distinct = set().union(*(row["_hashes"] for row in per.values()))
    work = {(at, subject) for row in per.values() for at, subject, _ in row["_keys"]}
    for row in per.values():
        del row["_hashes"], row["_keys"]
    return per, len(distinct), len(work)


def hand_counts(path):
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8")))
    return Counter(r["kind"] for r in rows), rows


def caught_by(rows):
    return Counter(r["caught_by"] for r in rows if r["kind"] == "error")


def table(per):
    head = ["repository", "commits", "files", "tags", "decisions", "moves", "first", "last", "shared", "carried", "skew"]
    lines = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for name, r in per.items():
        lines.append("| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
            name, r["commits"], r["files"], len(r["tags"]), len(r["decisions"]), r["moves"],
            r["first"] or "-", r["last"] or "-", r["shared"], r["carried"], r["skew"]))
    total = lambda k: sum(r[k] for r in per.values())
    lines.append("| all | {} | - | {} | {} | {} | - | - | {} | {} | {} |".format(
        total("commits"), sum(len(r["tags"]) for r in per.values()),
        sum(len(r["decisions"]) for r in per.values()), total("moves"), total("shared"), total("carried"), total("skew")))
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", required=True, help="folder holding the checkouts side by side")
    ap.add_argument("--day", default="2026-10-29")
    ap.add_argument("--offset", default="+01:00", help="UTC offset that defines the day")
    ap.add_argument("--hand", default=str(Path(__file__).with_name("hand-counts.csv")))
    ap.add_argument("--json", help="also write the numbers to this file")
    args = ap.parse_args(argv)
    tz = parse_offset(args.offset)
    per, distinct, work = measure(args.root, args.day, tz)
    print(f"Day {args.day}, offset {args.offset}\n")
    print(table(per))
    total = sum(r["commits"] for r in per.values())
    print(f"\nCommits summed over repositories: {total}; distinct hashes: {distinct}; distinct (author time, subject): {work}.")
    for name, r in per.items():
        for tag, when in r["tags"]:
            print(f"tag {name} {tag} {when}")
        for d in r["decisions"]:
            print(f"decision {name} {d}")
    counts = {}
    if Path(args.hand).exists():
        counts, _ = hand_counts(args.hand)
        print("\nHand count (not checked by this program):", dict(counts))
        print("Errors by who caught them:", dict(caught_by(hand_counts(args.hand)[1])))
    if args.json:
        Path(args.json).write_text(json.dumps(
            {"day": args.day, "offset": args.offset, "repositories": per,
             "summed": total, "distinct": distinct, "distinct_work": work, "hand": dict(counts), "errors_caught_by": dict(caught_by(hand_counts(args.hand)[1])) if counts else {}}, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
