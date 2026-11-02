# BugDB v2 — 解法

2026-11-02 にHacker101 CTFでフラグを提出し、一覧の **1/1** と全体 **272点** を確認した。インスタンス固有のホスト名とフラグは公開しない。

## スキーマと公開データ

`/graphql` のGraphiQLでスキーマを確認した。Queryには `allBugs`、`findUser`、`node(id: ID!)`、Mutationには `modifyBug(id: Int, private: Boolean, text: String)` がある。

```graphql
{ allBugs { id text private reporterId reporter { username } } }
```

初期状態の `allBugs` は、`private: false` の例示用Bugを1件だけ返した。IDは `QnVnczox` で、Base64として復号すると `Bugs:1` になる。また、`findUser(username: "victim")` はID `VXNlcnM6Mg==`（`Users:2`）を返した。

## 非公開Bugの直接参照

公開Bugと同じID形式で `Bugs:2` をBase64化すると `QnVnczoy` になる。これを `node` に指定した。

```graphql
{
  node(id: "QnVnczoy") {
    ... on Bugs {
      id
      text
      private
      reporterId
    }
  }
}
```

応答は `private: true`、`reporterId: 2` のBugを返し、`text` にフラグが含まれていた。フラグを提出し、CTF一覧で **BugDB v2 1/1** を確認した。

## 原因と検証範囲

`allBugs` では非公開レコードを除外していたが、`node(id: …)` は同じ非公開レコードを返した。列挙処理だけに公開範囲の制限を置き、単一ID参照で同じ制限を適用していないことが原因と考えられる。今回 `modifyBug` は実行しておらず、レコードの公開設定や本文は変更していない。

参考として、[HackerOne公式のGraphQL Week紹介](https://www.hackerone.com/blog/graphql-week-hacker101-capture-flag-challenges)にはBugDB v2でmutationが導入されたことが説明されている。公開writeupにもmutationを使う別解があるが、今回のフラグは読み取り専用の `node` 照会で取得した。
