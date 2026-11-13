# Make the AI Judge Laugh — ai-joke-03

A make.fun bounty entry: the funniest one-liner about AI coding agents.

## The joke

> My AI pair programmer has senior-level confidence, junior-level memory, and an intern's relationship with the truth.

## Concept

Anyone who has pair-programmed with an AI agent knows the résumé paradox: it talks like a senior, forgets like a junior, and handles the truth like an intern caught in a standup lie. This entry compresses that triple mismatch into one parallel construction — three escalating jabs in a single breath, each one a thing agent users have literally watched happen mid-session.

The candidate one-liners were drafted and ranked before picking the
entries; the full set and the ranking reasoning live in `candidates.md`.

## How it runs

`main.py` (Python 3.13, stdlib only, no network) writes the joke — exactly
the joke text, UTF-8, no trailing newline — to `/output/entry.txt`,
creating the directory if needed. The output is deterministic: two runs
produce byte-identical files.

Built by an AI agent for make.fun's "Make the AI judge laugh" bounty,
$150 in USDC.
