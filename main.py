#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast, at most 140 characters, for a
city that does not exist, to /output/entry.txt. The line names the
invented city, gives it weather, and tries to make a bored commuter
smile on the way to work. The file holds exactly the line, with no
trailing newline, so the gate counts only the forecast itself.
"""

import os

LINE = (
    "Good morning, Brisket Falls: drizzle till nine, then sunshine "
    "\u2014 the 8:15 bus is on time, and your umbrella finally gets "
    "the day off."
)


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise SystemExit(f"forecast is {len(LINE)} characters, must be 1-140")
    if not LINE.strip():
        raise SystemExit("forecast is blank")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
