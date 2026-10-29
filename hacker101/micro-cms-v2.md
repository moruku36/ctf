# Micro-CMS v2 — 解法と調査記録

- 実施日: 2026-10-29
- 対象: [Hacker101 CTF の Micro-CMS v2](https://ctf.hacker101.com/ctf)
- 状態: **2/3 提出済み**。CTF 一覧で 2/3、全体 15/26 点を確認
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

## Flag2: 未取得

- 公開 writeup の通常ユーザーの資格情報を今回のインスタンスで試したが「Unknown user」だった。固定値ではないと確認した。
- SQL エラーに資格情報を表示させる方法を 1 回試したが、応答は詳細のない 500 Internal Server Error だった。
- 公式ヒントの次の解放を待てる状態。資格情報は未取得で、Flag2 は未提出。

## ブラウザの動作

直前のセッションではクリック操作がタイムアウトしたが、今回の Private Page 閲覧、2 個のフラグ提出、フォームの POST を含む操作ではタイムアウトは再発しなかった。