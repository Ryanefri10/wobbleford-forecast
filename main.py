#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for the
invented city of Wobbleford to /output/entry.txt. Stdlib only.
"""

import os

FORECAST = (
    "Wobbleford: 13\u00b0C with sideways rain; the 8:04 bus is early for once, "
    "pigeons wear tiny raincoats, and your umbrella finally earns its keep."
)


def main() -> None:
    # Mirror the sealed gate: 1 to 140 characters, not only white space.
    # Fail loudly here instead of shipping an entry the judge never sees.
    if not 1 <= len(FORECAST) <= 140:
        raise ValueError(f"forecast is {len(FORECAST)} chars, must be 1-140")
    if not FORECAST.strip():
        raise ValueError("forecast must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
