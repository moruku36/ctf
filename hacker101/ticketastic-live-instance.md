# Ticketastic: Live Instance — 解法記録

- 実施日: 2026-10-31
- 対象: [Hacker101 CTF](https://ctf.hacker101.com/ctf) の Ticketastic: Live Instance
- 状態: **2/2 提出済み**。CTF 一覧で全体 **125点**を確認
- 公開リポジトリにはフラグ値、演習インスタンス固有のホスト名、実際に使った資格情報や Cookie を載せない

## 対象の確認

CTF 一覧で Demo Instance は 0/0、Live Instance は 0/2。Live が「Go」になった後、別の演習ホストに移動し、トップの表示が `Support Home` であることを確認した。Demo のトップには `Demo Instance` と表示され、管理者向けの公開された演習用ログイン情報が案内されている。

## フラグ 1: チケット内リンクを経由した演習内ユーザーの作成

Demo に案内された演習用アカウントでログインし、`/newUser` のフォームを確認した。このフォームは **GET** 方式で `username`、`password`、`password2` を受け取り、リクエストの正当性を確認するトークンがない。

Live では Demo の公開ログイン情報は使えなかった。そこで Live の `/newTicket` から、次の形のリンクを本文に入れたチケットを送った。値は一時的な演習用のものにする。

```html
<a href="http://localhost/newUser?username=<演習用ユーザー>&password=<演習用パスワード>&password2=<同じパスワード>">support details</a>
```

送信後、その演習用ユーザーで Live にログインできた。チケットを読む側が自身のローカルアドレスでリンクを開くと、管理者のログイン状態でユーザー作成が実行されると考えられる。これは GET による状態変更と CSRF 対策の欠如を組み合わせた手順である。

管理画面の `Flag Won't Work` というチケットには、投稿者が誤って使ったフラグ形の値と、サポートの返信にある訂正後の値が並んでいた。**返信側の値**を提出し、受理を確認した。

## フラグ 2: チケット番号の SQL 注入

ログイン後、`/ticket?id=1'` を開くと詳細エラーが表示され、チケット検索が概ね次の SQL を文字列補間で組み立てていることを確認した。

```python
cur.execute('SELECT title, body, reply FROM tickets WHERE id=%s' % request.args['id'])
```

検索結果は3列なので、存在しないチケット番号に `UNION SELECT` を続け、演習用 DB の `users` テーブルにある `admin` 行の `password` 列を本文に表示させた。

```sql
0 UNION SELECT 'probe',password,'reply' FROM users WHERE username='admin'-- 
```

表示されたフラグ形の値を提出し、受理を確認した。CTF 一覧で Live Instance **2/2**、全体 **125点**となった。

## 参考

- [Ticketastic: Live Instance の公開解説](https://hacker101.testerting.science/ticketastic_live_instance/)を参照し、上記の挙動を今回の演習インスタンスで確認した。
