#!/usr/bin/env python3
# this code prints itself!
import subprocess

r = subprocess.run(
    [
        "cat",
        "self_printer_2.py",
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)

print(r.stdout)
