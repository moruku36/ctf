# TempImage — 調査記録（進行中）

- 実施日: 2026-11-01
- 対象: [Hacker101 CTF の TempImage](https://ctf.hacker101.com/ctf)
- 状態: **0/2、未提出**
- 演習インスタンス固有のホスト名、フラグ、Cookie、資格情報は公開しない

## 確認した画面

本人が Brave で開いていた演習インスタンスを使用した。トップには「UNREGISTERED」と「Upload image」が表示される。リンク先の `/upload.php` には画像選択とアップロードのフォームがある。

フォームは `multipart/form-data` で `/doUpload.php` にPOSTする。入力欄にはファイル本体の `file` と隠し `filename` があり、ページ内のJavaScriptは選択したファイル名を `filename` にコピーする。クライアントから送られるこの値が保存先に使われるかは、まだ検証していない。

公式ヒントの最初の文は「File uploads can be hard to pin down」。公開解説ではファイル名のパス操作と画像内のPHPコードが紹介されているが、今回のインスタンスでは未検証である。

## 停止理由

検証用の小さなPNGをローカルに作り、Brave のファイル選択からアップロードしようとした。拡張機能がローカルファイルへのアクセスを許可しておらず、ファイルの選択操作が拒否された。案内された設定は Brave の `brave://extensions` → ChatGPT 拡張機能の「Details」→「Allow access to file URLs」。

権限拒否後は別経路への切替や再試行をせず、対象へのアップロードは行っていない。検証用PNGはローカルから削除した。2つのフラグはいずれも未取得・未提出である。

## 次に確認すること

本人が上記のブラウザ設定を許可した場合、まず通常のPNGを1枚アップロードして保存先と応答を確認する。その後、`filename` の処理を演習インスタンス内で検証する。

## 参考

- [TempImage の公開解説](https://dev.to/caffiendkitten/hacker101-ctf-tempimage-13m9)
- [Hacker101 CTF](https://ctf.hacker101.com/ctf)
