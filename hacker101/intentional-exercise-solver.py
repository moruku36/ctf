"""Build Intentional Exercise's signed flag URL from its APK.

Usage: python intentional-exercise-solver.py level13.apk
The printed URL is instance-specific; do not publish it or its flag.
"""

import hashlib
import re
import sys
import zipfile


def signed_url(apk_path):
    with zipfile.ZipFile(apk_path) as apk:
        dex = apk.read("classes.dex")

    base_match = re.search(
        rb"https://[0-9a-f]{32}\.ctf\.hacker101\.com/appRoot", dex
    )
    key_match = re.search(rb"s00p3rs3cr3tk3y", dex)
    if not base_match or not key_match:
        raise ValueError("Could not find the expected base URL and key in classes.dex")

    base = base_match.group().decode("ascii")
    key = key_match.group()
    extra_path = b"/flagBearer"
    digest = hashlib.sha256(key + extra_path).hexdigest()
    return f"{base}{extra_path.decode('ascii')}?&hash={digest}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: intentional-exercise-solver.py level13.apk")
    print(signed_url(sys.argv[1]))

