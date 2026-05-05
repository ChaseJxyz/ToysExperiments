#!/usr/bin/env python3
# this code prints itself! has this changed!
import subprocess

r = subprocess.run(
    [
        "curl",
        "https://raw.githubusercontent.com/ChaseJxyz/ToysExperiments/refs/heads/main/self_printer.py",
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)

print(r.stdout)
