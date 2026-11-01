# Petshop Pro — 解法記録（進行中）

- 実施日: 2026-11-01
- 対象: [Hacker101 CTF の Petshop Pro](https://ctf.hacker101.com/ctf)
- 状態: **1/3 提出済み**。別の1件は画面で発見したが未提出。CTF 一覧で全体 **128点**を確認
- 演習インスタンス固有のホスト名、フラグ値、Cookie、資格情報は公開しない

## 初期確認

Brave で本人が起動済みの Petshop Pro を使用した。CTF 一覧は「Go・0/3」で、新しいインスタンスは作っていない。トップには Kitten と Puppy があり、`/add/0` で Kitten をカートへ追加した。通常の `/cart` は $8.95 を表示し、`/checkout` への POST フォームに隠し `cart` 入力がある。通常のチェックアウトは「Payments temporarily disabled」で終わる。

## 受理されたフラグ 1: チェックアウト時の価格改変

公式ヒントはチェックアウトの違和感を示していた。フォームの `cart` には商品情報が含まれ、クライアントから送る価格をサーバーがそのまま使う。演習用のチェックアウト POST に、Kitten の価格を 0 とした次の形の `cart` を送った。

```json
[[0, {"logo":"kitten.jpg","price":0,"name":"Kitten","desc":"8\"x10\" color glossy photograph of a kitten."}]]
```

応答には `$0` の Kitten とフラグが表示された。この値を Hacker101 に提出し、受理を確認した。実際の決済は「Payments temporarily disabled」と表示され、発生していない。

## 発見したフラグ 2: 商品編集からの XSS（提出待ち）

公開解説の補足を参考に、ログインしていない状態で `/edit?id=0` を開いたところ、Kitten の編集フォームが表示された。商品名を一時的に変更して保存できることを確認した。商品名に `<script>console.log(1);</script>` を設定し、ホームから Kitten をカートへ追加すると、`/cart` の商品名欄に新しいフラグが表示された。フラグ値は公開しない。

提出前にブラウザ操作がタイムアウトした。指示に従い状態を1回確認したが、その確認もタイムアウトしたため操作を停止した。**このフラグは未提出**。商品名を元の `Kitten` に戻す保存操作は送ったが、その直後に接続が切れたため、復元の成否は未確認である。値は GitHub 外のローカルファイルに一時保存している。

## 残るフラグ 3: 管理ログイン

`/login` に管理者ログイン画面がある。存在しないユーザー名への応答は `Invalid username` で、ユーザー名とパスワードを区別する応答になっている。公開解説で使われた別インスタンスの資格情報は、このインスタンスでは無効だった。

演習用の名前リストで最初の1000候補を照合したが一致しなかった。並列数を増やした後、サーバーが `503 Service Temporarily Unavailable` を返したため、照合を停止した。後にログイン画面は再読み込みできたが、単発の認証入力も `Invalid username` だった。資格情報とログイン後のフラグは未取得である。

## 参考

- [Petshop Pro の公開解説](https://alliumsec.com/hacker-101-ctf-petshop-pro/)
- [SecLists の単語リスト](https://github.com/danielmiessler/SecLists)
