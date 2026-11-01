# TempImage — 解法

- 実施日: 2026-11-01
- 対象: [Hacker101 CTF の TempImage](https://ctf.hacker101.com/ctf)
- 結果: **2/2 提出済み**。CTF 一覧で全体 **155点**を確認
- 演習インスタンス固有のホスト名、フラグ値、Cookie、資格情報は公開しない

## 初期確認

本人が Brave で起動済みの演習インスタンスを使用した。トップには「UNREGISTERED」と「Upload image」がある。`/upload.php` のフォームは `multipart/form-data` で `/doUpload.php` に送信する。ファイル本体の `file` に加え、隠し `filename` 入力があり、ページ内のJavaScriptが選択したファイル名をそこへコピーする。

1×1ピクセルの正常なPNGをアップロードすると、`/files/` 配下に接頭辞付きの名前で保存された。この時点でファイル選択とPNG形式の受付を確認した。

## Flag0: ファイル名による保存先の移動

隠し `filename` はクライアントが変更できる。`file` に正常なPNGを指定したまま、`filename` を `/../../tempimage-probe.png` に変えてアップロードした。応答は302で、保存先のパスに `files/<接頭辞>_/../../tempimage-probe.png` が現れ、同じ応答に最初のフラグが含まれた。これを提出して受理を確認した。

再現用の画像生成は [画像作成スクリプト](tempimage-make-payload.py)、フォーム送信は [アップロード検証スクリプト](tempimage-upload-probe.py) に記録した。送信先は自分のHacker101演習インスタンスに限定して使う。

## Flag1: PNGとして受け付けられるPHPファイル

正常なPNGの末尾に、同じディレクトリの `index.php` からフラグを1件抽出するPHPコードを付けた。アップロード時の `file` はPNG形式のまま、隠し `filename` を `/../../tempimage-read.php` に変更した。保存先がPHPとして実行される場所に移り、ブラウザでそのファイルを開くと、PNGのバイト列に続いてフラグが表示された。

PHP部分は `index.php` の読み取りとフラグ表示だけに限定し、最後に `unlink(__FILE__)` で自身を削除する。表示されたフラグを提出して受理を確認した。検証用PHPのURLを再読み込みすると404になり、削除も確認できた。

## 後片付けと結果

ブラウザ拡張機能のファイルアクセス設定を本人が許可した後、正常なPNGアップロードから再開した。ローカルの検証用PNG、PHP付きPNG、提出済みフラグの一時ファイルは削除した。CTF 一覧で TempImage **2/2**、全体 **155点**を確認した。

## 参考

- [Hacker101 CTF](https://ctf.hacker101.com/ctf)
- [TempImage の公開解説](https://dev.to/caffiendkitten/hacker101-ctf-tempimage-13m9)
