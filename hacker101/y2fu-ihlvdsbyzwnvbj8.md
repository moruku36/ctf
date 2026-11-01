# Y2FuIHlvdSByZWNvbj8/ — File Dropper

## 結果

2026-11-01 に3つのフラグを提出し、Hacker101 CTF の一覧で **3/3**、合計 **190 点**を確認した。インスタンス固有の URL とフラグは公開しない。

## 観察

初期画面は「File Dropper」。フォームには `filename` とファイル選択欄がある。`filename` はアップロードするファイルの元名と別に指定でき、保存先に影響する。公開された[先行の解法](https://medium.com/@JakubLakomy/hacker101-ctf-writeup-y2fuihlvdsbyzwnvbj8-f5ecd78a3fb3)を参考に、`.php` 以外でも PHP として実行される `.phtml` と、保存名の `../` を試した。

## 解法

1. [一回限りの検証用ファイル](file-dropper-once.phtml)を作る。`flags.txt`、`../flags.txt`、`../../flags.txt` のうち存在するファイルを表示し、実行後に自分自身を削除する。
2. フォームの File Name に `../file-dropper-once.phtml` を入力し、同ファイルを選択してアップロードする。画面は「File uploaded successfully」を表示したが、通常の Files 一覧には出なかった。
3. サイトのルートにある `/file-dropper-once.phtml` を開く。`../flags.txt` からフラグ形式の値が3つ表示された。
4. ページを再読み込みすると 404 になり、検証用ファイルが削除されたことを確認した。3つのフラグを Hacker101 に提出し、一覧で 3/3 を確認した。

`filename` の `../` が保存先を一つ上の階層に移し、`.phtml` がサーバー側の PHP として実行された。ファイル名の制限だけでは、パスの移動と別の実行可能拡張子を防げないことがポイントだった。

