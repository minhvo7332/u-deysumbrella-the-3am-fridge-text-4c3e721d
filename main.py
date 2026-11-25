# The 3AM Fridge Text — make.fun entry (program/v1)
#
# The line: a smart fridge that has been humming all night finally speaks.
# Voice: the appliance, awake while the house sleeps, filing its complaint
# at 3am. Setup: "I've been awake all night" (the fridge never sleeps).
# Beat: the owner opens the door just to stare — the universal 3am ritual.
# Punchline: the freezer is in on it; an intervention is being staged.
# Fresh angle: no milk, no ice, no door-left-open — the joke is the fridge
# gossiping with the freezer about its owner.
import os

LINE = "3am. I've been awake all night and all you do is open me, stare, and leave. The freezer and I are staging an intervention."

# The gate only accepts 1-140 characters: refuse to write anything longer
# rather than hand the judge an invalid entry.
if len(LINE) < 1 or len(LINE) > 140 or LINE.strip() == "":
    raise SystemExit(f"entry line is {len(LINE)} chars; gate needs 1-140")

out_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod(path, 0o644)
