# Cody's First Blog — 解法記録

- 実施日: 2026-10-30
- 対象: [Hacker101 CTF の Cody's First Blog](https://ctf.hacker101.com/ctf)
- 状態: **3/3 提出済み**。CTF 一覧で確認
- インスタンス固有のホスト名、フラグ値、セッション情報は公開しない

## 初期確認

トップ画面はコメント投稿欄のある小さなブログだった。最初の記事には、PHP の `include()` を使ってページを組み立てていると書かれている。HTML には次の管理者ログインへのリンクがコメントアウトされていた。

```html
<!--<a href="?page=admin.auth.inc">Admin login</a>-->
```

公式の最初のヒントは「最初に見た入力は何か」だった。入力欄はコメントの `body`。

## Flag0: PHP を含むコメントの投稿

コメント欄に次の検証用文字列を投稿した。

```php
<?php echo 'CTF_PROBE'; ?>
```

「Comment submitted and awaiting approval!」という応答に Flag0 が表示された。提出すると受理された。後でソースを確認したところ、`body` に `<?php` が含まれる場合にこのフラグを返す処理だった。投稿時点で PHP コードが実行されたわけではない。

## Flag1: 管理ページへの直接アクセス

コメントアウトされたリンクの `?page=admin.auth.inc` を開くとログインフォームが表示された。ログインフォームで単純な SQL 注入を試したが、認証には成功しなかった。ファイル名の `auth` を外して `?page=admin.inc` を開くと、認証なしで管理ページが表示され、ページ下部に Flag1 があった。提出して受理された。

## Flag2: 承認済みコメントの再解釈によるソース読み取り

管理ページには自分のコメントが承認待ちとして表示されていた。検証用コメントを承認し、次のページを開いた。

```text
/?page=http://localhost/index
```

画面に `CTF_PROBE` が現れ、承認済みコメント内の PHP が実行されたことを確認した。通常のトップ画面ではコメントの PHP は実行されない。サーバーが自分自身のページを HTTP で取得して `include()` すると、取得したページ中のコメントが PHP として再解釈される。

次に、`index.php` を Base64 で表示するコメントを投稿し、管理ページで承認した。

```php
<?php echo base64_encode(file_get_contents('index.php')); ?>
```

同じ `?page=http://localhost/index` を再読込すると Base64 の文字列が現れた。復号したソースの先頭コメントに Flag2 があり、提出した。ソースから、`page` に `.php` を付けて `include()` していること、コメントはデータベースに保存され、承認済みのものが表示されることも確認した。

CTF 一覧で Cody's First Blog は **3/3**、全体は **79点**。検証用の承認済みコメント2件は、この演習インスタンスに残っている。

## 参考

- [Cody's First Blog writeup](https://bernardoamc.com/hacker101-ctf/codys_first_blog/) — `admin.inc` とローカル HTTP ページの `include()` を手掛かりにした。各手順と結果は今回の演習環境で確認した。
