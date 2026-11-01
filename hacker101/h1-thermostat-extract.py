"""Extract instance-specific Hacker101 flags from an H1 Thermostat APK."""

import re
import sys
import zipfile


if len(sys.argv) != 2:
    raise SystemExit("usage: python h1-thermostat-extract.py thermostat.apk")

with zipfile.ZipFile(sys.argv[1]) as apk:
    dex = apk.read("classes.dex")

flags = sorted(set(re.findall(rb"\^FLAG\^[0-9a-f]{64}\$FLAG\$", dex, re.I)))
for flag in flags:
    print(flag.decode("ascii"))
print(f"found {len(flags)} unique flag(s)", file=sys.stderr)

