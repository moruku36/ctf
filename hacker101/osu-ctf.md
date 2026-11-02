# OSU CTF — 調査記録（未完了）

2026-11-02、OSUSEC Student Management Portal のログイン画面から調査を開始した。課題の案内は、Natasha Drew の成績をすべて A にすること。フラグはまだ取得・提出していない。インスタンス固有のホスト名、Cookie、フラグは公開しない。

## 確認したこと

1. `/login` は `username` と `password` をPOSTするフォームだった。
2. 演習用のSQL注入入力 `admin' OR 1=1-- ` を `username` に入れ、任意のパスワードを指定すると、`rhonda.daniels` としてダッシュボードへ進んだ。
3. ダッシュボードにはこの職員の学生一覧が表示された。Natasha Drew は一覧にいなかった。
4. 学生名のセルには `data-id` 属性があり、例として Nancie Brett の値は `TmFuY2llX0JyZXR0` だった。これは `Nancie_Brett` のBase64表現に対応する。学生名セルをクリックしたが、画面は変化しなかった。
5. ページが読み込む `/assets/js/app.min.js` を開こうとしたところ、Brave が `net::ERR_BLOCKED_BY_CLIENT` で遮断した。そのファイルを別経路から取得する操作はしていない。

## 次の手順

Braveでこのインスタンスの `/assets/js/app.min.js` が開ける状態になったら、その中で学生詳細・成績更新の通信先を確認する。Natasha Drew の識別値と権限確認を検証し、フラグ取得後に提出する。

現在の状態: **0/1、継続中**。