# Petshop Pro — 解法記録（進行中）

- 実施日: 2026-11-01
- 対象: [Hacker101 CTF の Petshop Pro](https://ctf.hacker101.com/ctf)
- 状態: **2/3 提出済み**。CTF 一覧で全体 **131点**を確認
- 演習インスタンス固有のホスト名、フラグ値、Cookie、資格情報は公開しない

## 初期確認

Brave で本人が起動済みの Petshop Pro を使用した。CTF 一覧は「Go・0/3」で、新しいインスタンスは作っていない。トップには Kitten と Puppy があり、`/add/0` で Kitten をカートへ追加した。通常の `/cart` は $8.95 を表示し、`/checkout` への POST フォームに隠し `cart` 入力がある。通常のチェックアウトは「Payments temporarily disabled」で終わる。

## 受理されたフラグ 1: チェックアウト時の価格改変

公式ヒントはチェックアウトの違和感を示していた。フォームの `cart` には商品情報が含まれ、クライアントから送る価格をサーバーがそのまま使う。演習用のチェックアウト POST に、Kitten の価格を 0 とした次の形の `cart` を送った。

```json
[[0, {"logo":"kitten.jpg","price":0,"name":"Kitten","desc":"8\"x10\" color glossy photograph of a kitten."}]]
```

応答には `$0` の Kitten とフラグが表示された。この値を Hacker101 に提出し、受理を確認した。実際の決済は「Payments temporarily disabled」と表示され、発生していない。

## 受理されたフラグ 2: 商品編集からの XSS

公開解説の補足を参考に、ログインしていない状態で `/edit?id=0` を開いたところ、Kitten の編集フォームが表示された。商品名を一時的に変更して保存できることを確認した。商品名に `<script>console.log(1);</script>` を設定し、ホームから Kitten をカートへ追加すると、`/cart` の商品名欄に新しいフラグが表示された。フラグ値は公開しない。

最初の提出前にブラウザ操作がタイムアウトしたため、フラグをローカルに一時保存した。後に Brave の既存タブで編集フォームの名前が元の `Kitten` であることを確認した。保存していたフラグを Hacker101 に提出すると受理され、CTF 一覧で Petshop Pro **2/3**、全体 **131点**を確認した。ローカルのフラグファイルは削除した。

## 残るフラグ 3: 管理ログイン

`/login` に管理者ログイン画面がある。存在しないユーザー名への応答は `Invalid username` で、ユーザー名とパスワードを区別する応答になっている。公開解説で使われた別インスタンスの資格情報は、このインスタンスでは無効だった。

演習用の名前リストで候補を照合した。最初の1000件に一致せず、並列数を増やしたときサーバーが `503 Service Temporarily Unavailable` を返したため停止した。後にログイン画面は再読み込みできたが、単発の認証入力も `Invalid username` だった。少数並列で再開し、合計6500件まで名前候補を照合したが一致しなかった。再び503が返った時点で自動停止し、追加の照合は行っていない。資格情報とログイン後のフラグは未取得である。

## 参考

- [Petshop Pro の公開解説](https://alliumsec.com/hacker-101-ctf-petshop-pro/)
- [SecLists の単語リスト](https://github.com/danielmiessler/SecLists)
