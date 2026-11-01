# Petshop Pro — 解法記録（進行中）

- 実施日: 2026-11-01
- 対象: [Hacker101 CTF の Petshop Pro](https://ctf.hacker101.com/ctf)
- 状態: **1/3 提出済み**。CTF 一覧で全体 **128点**を確認
- 演習インスタンス固有のホスト名、フラグ値、Cookie、資格情報は公開しない

## 初期確認

Brave で本人が起動済みの Petshop Pro を使用した。CTF 一覧は「Go・0/3」で、新しいインスタンスは作っていない。トップには Kitten と Puppy があり、`/add/0` で Kitten をカートへ追加した。通常の `/cart` は $8.95 を表示し、`/checkout` への POST フォームに隠し `cart` 入力がある。通常のチェックアウトは「Payments temporarily disabled」で終わる。

## 受理されたフラグ 1: チェックアウト時の価格改変

公式ヒントはチェックアウトの違和感を示していた。フォームの `cart` には商品情報が含まれ、クライアントから送る価格をサーバーがそのまま使う。演習用のチェックアウト POST に、Kitten の価格を 0 とした次の形の `cart` を送った。

```json
[[0, {"logo":"kitten.jpg","price":0,"name":"Kitten","desc":"8\"x10\" color glossy photograph of a kitten."}]]
```

応答には `$0` の Kitten とフラグが表示された。この値を Hacker101 に提出し、受理を確認した。実際の決済は「Payments temporarily disabled」と表示され、発生していない。

## 残る2フラグの調査状況

`/login` に管理者ログイン画面がある。存在しないユーザー名への応答は `Invalid username` で、ユーザー名とパスワードを区別する応答になっている。公開解説で使われた別インスタンスの資格情報は、このインスタンスでは無効だった。

演習用の名前リストで最初の1000候補を照合したが一致しなかった。並列数を増やした後、サーバーが `503 Service Temporarily Unavailable` を返したため、照合を停止した。残る2フラグは未取得であり、管理ログイン後の画面と商品編集機能は今回まだ確認していない。

## 参考

- [Petshop Pro の公開解説](https://alliumsec.com/hacker-101-ctf-petshop-pro/)
- [SecLists の単語リスト](https://github.com/danielmiessler/SecLists)
