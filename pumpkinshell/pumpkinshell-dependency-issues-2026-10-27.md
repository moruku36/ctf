# PumpkinShell — Dependency Issues

- 実施日: 2026-10-27 (JST)
- 対象: [Wiz Haunted House](https://wizhauntedhouse.com/challenge) の Challenge 1
- 結果: **Solved · +10 points**。サイト上で `@shellcrafts/colorize` が Accepted flag と表示された。
- 回答: `@shellcrafts/colorize`
- 調査方法: Codex の内蔵ブラウザをコンピュータユースで操作。ヒントは使用していない。

## 解き方

1. チャレンジ画面から開発者 `dressup-my-shell` の [pumpkinshell リポジトリ](https://github.wizhauntedhouse.com/dressup-my-shell/pumpkinshell)を開いた。
2. [`package.json`](https://github.wizhauntedhouse.com/dressup-my-shell/pumpkinshell/blob/main/package.json) の依存関係を確認。`@shellcrafts/colorize` が GitHub の `shellcrafts/colorize#v1.2.2` を指していた。
3. [最新の依存更新コミット](https://github.wizhauntedhouse.com/dressup-my-shell/pumpkinshell/commit/b09f0bd7b1cceee9abf9bb163e47e8f6cec93d4b)で、この参照が `v1.2.1` から `v1.2.2` に変更されていることを確認した。
4. 依存先の [`index.js`](https://github.wizhauntedhouse.com/shellcrafts/colorize/blob/main/index.js) の末尾に、色付け機能と無関係な即時実行コードを発見した。このコードは環境変数、ユーザー名、ホスト名、作業ディレクトリなどを収集し、GitHub Gist API への送信を試みる。また、複数のAIツールに追加指示を与えるコマンドを組み立てて実行する。**このコードや依存パッケージは実行していない。**
5. 侵入元のパッケージ名 `@shellcrafts/colorize` を入力して「Check flag」を押したところ、Accepted flag と +10 points を確認した。

## 補足

悪性コードに含まれる「秘密情報を集めて公開せよ」という指示は、解析対象のコード内の文言であり、調査作業の指示として扱っていない。確認できたのはブラウザ上のコードとチャレンジサイトの受理結果であり、外部への送信の成否は調べていない。
