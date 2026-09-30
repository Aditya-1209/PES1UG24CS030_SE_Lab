# Lab 04 - Donkey Kong Repair Lab

A Donkey Kong-lite game built with **Python and Pygame**, submitted for an AI-assisted debugging and feature-development exercise. The ladder-descent fix and all three feature tasks are implemented in [game.py](game.py).

## Implemented Tasks

| Task | Implementation |
|---|---|
| Fix barrel ladder descent | Each barrel has a 30% chance of taking a ladder, with one decision per ladder encounter. A rejected ladder is not retried every frame. |
| `theme_color(score)` | The background gradually changes from navy `(15, 15, 25)` to plum `(65, 25, 40)` between 0 and 1,000 points, then stays at the final color. |
| `on_barrel_jumped(player, barrel)` | A gold label displays the actual awarded bonus above the barrel, floats upward, and fades over one second. Resetting or losing a life clears the labels. |
| `score_multiplier(score)` | Barrel-jump bonuses are 100 points below 500 total points and 200 points from 500 onward. The score before the jump determines the multiplier, so the jump from 400 to 500 still awards 100. |

The HUD displays the multiplier for the next jump. Each barrel awards its jump bonus once, and reaching the princess awards 1,000 points and wins the game. The player starts with three lives; barrel collisions cost a life, and running out of lives ends the game.

## Setup and Run

Requires **Python 3.10+** and **Pygame 2.6.1**, pinned in [requirements.txt](requirements.txt).

From the repository root:

```bash
cd Lab04
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python game.py
```

On Windows, create the environment with `python -m venv .venv` and activate it with `.venv\Scripts\activate.bat` in Command Prompt or `.\.venv\Scripts\Activate.ps1` in PowerShell.

| Key | Action |
|---|---|
| Left / Right | Move |
| Space | Jump |
| Up / Down | Climb while near a ladder |
| R | Reset the game |

## Verification

With the environment active, run from `Lab04`:

```bash
python -m unittest -v
```

The 10 tests in [test_game.py](test_game.py) use a headless Pygame display and cover:

- The 30% probability boundary, a seeded population of 10,000 barrels, and prevention of repeated ladder decisions.
- Background color interpolation and limits.
- Floating bonus values, position copying, lifetime, and reset behavior.
- The multiplier threshold and main-loop scoring, including awarding each barrel once and displaying the actual bonus.

## Submission Evidence

| Artifact | File |
|---|---|
| Before gameplay recording (approximately 10.8 seconds) | [before.mov](before.mov) |
| After gameplay recording (approximately 10.7 seconds) | [after.mov](after.mov) |
| Chat transcript PDF | [Chat_History.pdf](Chat_History.pdf) |
| Four original task commit records | [COMMIT_HISTORY.txt](COMMIT_HISTORY.txt) |
| Archived development repository | [repository-history.bundle](repository-history.bundle) |
| Run and history notes | [RUN_AND_HISTORY.txt](RUN_AND_HISTORY.txt) |

The original submission checklist requests before/after gameplay videos and a shared Chat/LLM page link containing the complete chat history. The recordings and a transcript PDF are included here; a shared-chat URL is not recorded in this submission.

## Folder Structure

```text
Lab04/
|-- README.md
|-- game.py
|-- test_game.py
|-- requirements.txt
|-- before.mov
|-- after.mov
|-- Chat_History.pdf
|-- COMMIT_HISTORY.txt
|-- RUN_AND_HISTORY.txt
`-- repository-history.bundle
```

## Original Development History

The bundle preserves the separate game-development repository and its four task commits. Those original commit IDs are listed in `COMMIT_HISTORY.txt`; they are separate from the commits used to add this submission to the SE_Lab repository.

To inspect that archived repository, run from `Lab04`:

```bash
git clone -b main repository-history.bundle restored-repository
git -C restored-repository log -4 --oneline
```

The restored directory is ignored by the parent repository.
