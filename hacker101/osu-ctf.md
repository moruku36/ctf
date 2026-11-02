# OSU CTF — 解法（1/1）

2026-11-02 に Natasha Drew の英語・理科・数学をすべて A に変更し、フラグを提出した。Hacker101 CTF 一覧で **1/1、合計248点**を確認した。インスタンス固有のホスト名、フラグ、Cookie は公開しない。

## 1. 職員の画面に入る

`/login` は `username` と `password` をPOSTするフォームだった。演習用のSQL注入入力 `admin' OR 1=1-- ` をユーザー名に入れ、任意のパスワードを指定すると `rhonda.daniels` のダッシュボードへ入った。

この職員の学生一覧に Natasha Drew はいなかった。学生名セルには `data-id` 属性があり、表示名「Brett, Nancie」に対応する値 `TmFuY2llX0JyZXR0` は `Nancie_Brett` のBase64表現だった。

## 2. 学生詳細への導線を調べる

画面が読み込む `/assets/js/app.min.js` を直接開いた。初めはBrave・Chromeの自動操作とも `ERR_BLOCKED_BY_CLIENT` だったが、本人がChromeで手動で開いたタブの内容を確認できた。

JavaScriptの `setupLinks` は `staff.admin` が真のときだけ学生名セルにクリック処理を付け、遷移先を `/update-student/` とセルの `data-id` の結合で作る。今回の職員についてページ内の `staff.admin` は `false` だったため、学生名をクリックしても反応しなかった。

Natasha Drew の識別値は `Natasha_Drew` をBase64化した `TmF0YXNoYV9EcmV3`。この値を使って `/update-student/TmF0YXNoYV9EcmV3` を開くと、一覧にいないNatashaさんの成績編集フォームが表示された。画面側でクリックを隠す条件と、サーバー側のアクセス制御が一致していない。

## 3. 3科目をAにする

成績フォームの初期値は英語F・理科F・数学Eだった。フォームの `english`、`science`、`maths` をすべて `A` にして「Update Record」を押した。更新後、画面には3科目すべてAと、Hacker Campに参加できる旨の成功メッセージ、フラグが表示された。そのフラグをHacker101 CTFに提出し、一覧で1/1を確認した。

## 原因

ログイン入力のSQL注入に加え、学生名セルをクリック可能にする処理がクライアント側の `staff.admin` に依存していた。更新URLを直接開くと、権限と担当範囲の確認が十分でないまま別の学生の成績フォームに到達できた。