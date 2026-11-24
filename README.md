# One Word for the Boss

[![Bounty](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![Rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/cervus-snoopy/quiet-copper-heron-8m4v/rank.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![Reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/cervus-snoopy/quiet-copper-heron-8m4v/reward.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)

This entry picks a single everyday-object metaphor for a boss who is always present yet contributes nothing, and writes that one word to `entry.txt` with strict validation.

## Run

```sh
python3 main.py
```

The program reads the output directory from `MAKEFUN_OUTPUT_DIR` (default
`/output`), validates the word (one word, 1-30 characters, no whitespace),
writes `entry.txt` as UTF-8 with no trailing newline and mode `0644`, then
reads it back and re-validates what landed on disk. Python 3 standard
library only, no network access.

## Verify

```sh
mkdir -p /tmp/verify-out
MAKEFUN_OUTPUT_DIR=/tmp/verify-out python3 main.py
stat -c '%a %s' /tmp/verify-out/entry.txt
od -c /tmp/verify-out/entry.txt
```

The output file must be exactly one word, 1-30 characters, with no trailing
newline and mode `0644`. Running the program twice from a different
directory must exit `0` both times and produce byte-identical output.
