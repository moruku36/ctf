# BugDB v1 — 解法

2026-11-02 にHacker101 CTFでフラグを提出し、一覧の **1/1** と全体 **274点** を確認した。インスタンス固有のホスト名とフラグは公開しない。

## GraphQLスキーマの確認

`/graphql` のGraphiQLにあるDocsを開いた。Queryの `allBugs` は `BugsConnection` を返すが、その `Bugs` 型には本文を示す `text` がない。一方、`allUsers` の各 `Users` から辿れる `bugs` は `Bugs_Connection` を返し、その `Bugs_` 型には `text` がある。

## フラグの取得

次の読み取り専用クエリで、ユーザーから関連Bugの本文へ辿った。

```graphql
{
  allUsers {
    edges {
      node {
        username
        bugs {
          edges {
            node {
              text
              private
              reporterId
            }
          }
        }
      }
    }
  }
}
```

応答には `admin` の例示用Bugと、`victim` の `private: true` のBugが含まれた。後者の `text` にフラグがあり、Hacker101へ提出すると成功表示が出た。CTF一覧でも **BugDB v1 1/1** を確認した。

## 原因

ルートのBug一覧では本文フィールドを隠しているが、ユーザーとの関連から得られる別の型 `Bugs_` では本文を公開している。さらに、その経路では `private: true` のBugも返る。GraphQLの型や取得経路ごとに一貫した閲覧制限が適用されていない。
