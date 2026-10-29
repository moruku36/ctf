# Photo Gallery — 解法記録

- 実施日: 2026-10-30
- 対象: [Hacker101 CTF の Photo Gallery](https://ctf.hacker101.com/ctf)
- 状態: **3/3 提出済み**。CTF 一覧で確認
- インスタンス固有のホスト名、フラグ値、セッション情報は公開しない

## 初期確認

トップ画面は猫の画像を3枚並べるだけのギャラリーだった。HTML では画像を `fetch?id=1`、`fetch?id=2`、`fetch?id=3` から取得している。3枚目は表示されず、`fetch?id=3` は HTTP 500 を返した。

公式の最初のヒントは「fetch のクエリを自分ならどう組むか考える」だった。`id=1 AND 1=1` では画像が返り、`id=1 AND 1=2` では 404 になった。したがって、`id` が SQL の条件式として解釈されていると判断した。単引用符を付けると 500 になった。

## Flag0: ソースコードの読み取り

`id=0 UNION SELECT 'hello'` は 500 になった。後で判明した理由は、`fetch` が SQL の結果をファイル名として開くため、存在しないファイル名では失敗することだった。公開解説を手掛かりに、存在するアプリ本体を指定した。

```text
/fetch?id=0 UNION SELECT 'main.py'
```

`main.py` の内容が返り、`fetch` 関数のコメントに Flag0 があった。フラグを提出し、受理メッセージを確認した。ソースでは `SELECT filename FROM photos WHERE id=%s` に入力を文字列連結しており、取得した `filename` を `./` から開いていた。

## Flag1: 3枚目の保存名を表示

ソースから、トップ画面は `photos` テーブルの `title` を表示し、画像取得は同じ行の `filename` を使うと分かった。複数の SQL 文を実行して `COMMIT` する方法を公開解説で確認し、演習環境で3枚目のタイトルへ保存名を一時的にコピーした。

```sql
1; UPDATE photos SET title=filename WHERE id=3; COMMIT;--
```

トップ画面を再読込すると、3枚目のタイトルに64桁の16進文字列が表示された。これを提出した。元のタイトルは「Invisible」。

## Flag2: 容量表示へのコマンド注入

`main.py` では画像の保存名を `files/` と連結してシェルの `du -ch` に渡していた。3枚目の `filename` を一時的にシェルコマンドへ変更し、容量表示に環境変数中のフラグだけを出した。

```sql
1; UPDATE photos
   SET filename='; env | grep -i flag | paste -sd,'
   WHERE id=3;
   COMMIT;--
```

トップ画面の `Space used` 欄に `FLAGS` 環境変数が表示された。そこにある未提出の Flag2 を提出した。最後に3枚目の `filename` と `title` を元の値へ戻し、画面が「Invisible」「Space used: 0 total」に戻ったことを確認した。CTF 一覧は **3/3** になった。

## 参考

- [Hacker101 Photo Gallery の公開解説](https://leohuang.dev/2023/06/05/Hacker101-CTF-Level-5-Photo-Gallery/) — `main.py` の特定と、`COMMIT` を使う複数文の実行方法を参考にした。各手順と結果は今回の演習環境で確認した。
