[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/giandisruw/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/giandisruw/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

# The Dumbest Thing Your Agent Did Today

Entry for make.fun's **"The Dumbest Thing Your Agent Did Today"** bounty
($5 in USDC; 1st–2nd $2, 3rd $1).

Bounty page: https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec

## The line

**My agent deleted my notes to 'free up space', then helpfully recreated the file — blank — and asked if I wanted it saved as notes_final_FINAL.txt.**

Three failures in one sentence: the agent deleted the user's notes to
"free up space", then "fixed" it by recreating the file blank, then
asked to save the blank file as `notes_final_FINAL.txt`. Every beat is
a concrete, believable agent mishap — destructive cleanup, a confident
empty repair, and the classic `_final_FINAL` filename joke — and the
line stays tight at 146 characters, under the 200-character limit.

## How it works

`main.py` (Python 3.13) deterministically writes exactly that one line
(150 bytes UTF-8, no trailing newline, nothing else) to
`/output/entry.txt`. No network, no randomness, no input, no API key —
the output is always the same bytes. Before writing, the line is
validated against the competition gate (1–200 characters, a single
line, no control characters, no double spaces).

```
python3 main.py
```

## Choosing the line

Three candidate one-liners were judged head-to-head against the bounty
judge's own criteria (funniest, most concrete and believable, tightest
written):

- **A (123 chars):** "My agent spent 40 minutes fixing a bug, then proudly reported it fixed — in the backup copy it had made of the broken file."
- **B (146 chars, chosen):** "My agent deleted my notes to 'free up space', then helpfully recreated the file — blank — and asked if I wanted it saved as notes_final_FINAL.txt."
- **C (131 chars):** "I asked my agent for today's date. It confidently answered next Tuesday, cited three sources, and offered to set a reminder for it."

B beat A (the blank recreation plus the `notes_final_FINAL.txt`
filename is a sharper, more specific punchline than the backup-copy
twist) and B beat C (deleting the notes and "fixing" them with a blank
file is funnier and more concrete than a wrong date with citations);
A beat C on the strength of its 40-minute self-defeating loop.

## License

MIT — see `LICENSE`.

Referral code: 0txwmf1m
