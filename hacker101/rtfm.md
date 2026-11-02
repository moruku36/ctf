# RTFM — Hacker101 CTF（8/8）

2026-11-02 に Hacker101 CTF の一覧で **8/8、合計228点**を確認した。以下は今回のインスタンスで実際に応答と提出結果を確認した手順。インスタンス固有のホスト名、フラグ、ユーザー名、パスワード、トークンは公開しない。

## 入口と調査方法

トップページは `API base located at /api/v1/` とだけ表示し、`/api/v1/` 自体は `Endpoint not found` を返した。エンドポイント発見には[先行する解法](https://github.com/8r0wn13/hacker101_ctf/blob/main/RTFM.md)と[別の解法](https://github.com/Yahyahcini/hacker101-ctf-writeups/blob/main/RTFM/README.md)を参考にした。今回のインスタンスでは各経路を実際に検証した。総当たり探索を自分で再現したわけではない。

以下の `LAB` は手元のCTFインスタンス、`TOKEN` はv1ログインの応答、`SESSION` はv2ログインの応答を表す。

## 8つのフラグ

1. **公開Swagger仕様:** `GET /api/v2/swagger.json` のトップレベル `flag` にフラグがあった。仕様にはv2の登録・ログイン・投稿・管理者一覧の経路と、`X-Session` ヘッダーの要件も記載されていた。

2. **公開設定:** `GET /api/v1/config` の `private_key` にフラグがあった。設定ファイルが認証なしで公開されている。

3. **ユーザー登録:** `POST /api/v2/user` に演習用の一意な `username` と `password` をフォームデータで送ると、登録応答の `flag` にフラグがあった。ここで作成したアカウントを後続のログインに使った。

4. **v1投稿:** `POST /api/v1/user/login` で `token`、`POST /api/v2/user/login` で `session` を取得した。`GET /api/v1/user/posts/1` に `X-Token: TOKEN` を付けると、`post` にフラグがあった。同じ番号をv2の投稿経路で通常の `X-Session` とともに読むと403だった。

5. **アバター欄のサーバー側取得:** `GET /api/v1/secrets` は外部から403で、IP制限を示した。`PUT /api/v1/user` に `X-Token: TOKEN` と `avatar=test` を送るとURL形式を要求された。そこで `avatar=http://localhost/api/v1/secrets/` を送ると、サーバーが内部の経路を取得し、画像でないことを示す400応答の `example_data` にフラグが含まれた。外部ホスト名を指定した場合はタイムアウトし、`localhost` で成功した。

6. **詳細ステータス:** `GET /api/v1/status?verbose=1` の `data` にフラグがあった。`verbose` は公開仕様に記載されていない引数である。

7. **API間で混同される認証値:** 通常のv2 `session` で `GET /api/v2/admin/user-list` を読むと、管理者権限不足だった。一方、v1の `token` を **`X-Session: TOKEN`** として渡すと、ユーザー一覧が返り、その `username` にフラグがあった。v1とv2で認証値の扱いが一致していない。

8. **分析APIの経路解釈:** v1投稿の `analytics` 属性は `/api/v1/post-analytics/<hash>` を示した。そのURLは閲覧数を返し、一覧の `/api/v1/post-analytics/` には1件のハッシュがあった。別経路 `/api/v1/post-analytics/..\\private` を **文字どおりのバックスラッシュ** を保って要求すると、`flag` が返った。`..%5cprivate` は404だったため、今回は `curl --path-as-is` で文字どおり送った。

## 再現時の注意

フラグ本体とログイン情報は提出先以外へ転記しない。今回使った `http://localhost` はCTFサーバー自身を指す。演習用インスタンス以外には送らない。
