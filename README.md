# On-Chain Disclosure Monitor

A small MVP built on GenLayer that demonstrates how Intelligent Contracts can perform disclosure checks using consensus.

## Problem
Undisclosed promotions and misleading financial content are common on social platforms. Verification is usually based on trust or centralized moderation.

## MVP
This repo contains a GenLayer Intelligent Contract called `DisclosureVerifier`.

It takes:
- `statement` (string)
- `required_keyword` (string)

Then:
- Call `resolve()` to evaluate if the statement contains the keyword
- Call `get_result()` to return `true/false`

## Example Tests
Case 1 (should be true):
- statement: `Paid ad. Guaranteed win tonight!`
- required_keyword: `ad`

Case 2 (should be false):
- statement: `Guaranteed win tonight!`
- required_keyword: `ad`

## Why GenLayer
This is a simple example of non-deterministic / subjective evaluation and how Optimistic Democracy can be used to reach agreement on outcomes.

## Roadmap
- Phase 2: URL-based content fetching
- Phase 3: Multiple disclosure keyword support
- Phase 4: Public on-chain verification registry
- Phase 5: Account-level compliance scoring / leaderboard
