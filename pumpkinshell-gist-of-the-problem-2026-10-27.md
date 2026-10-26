# PumpkinShell — Gist of the Problem

- 実施日: 2026-10-27 (JST)
- 対象: [Wiz Haunted House](https://wizhauntedhouse.com/challenge) の Challenge 2
- 結果: **Solved · +15 points**。チャレンジ内の累計得点は 25 点。
- 回答: `AKIA4XQ7ZL2MPNVK9J3R`
- 調査方法: Codex の内蔵ブラウザをコンピュータユースで操作。ヒントは使用していない。
- アカウント: Wiz CTFs の `moruku36` でログインした状態で提出。

## 解き方

1. [前問で特定した `@shellcrafts/colorize` の `index.js`](https://github.wizhauntedhouse.com/shellcrafts/colorize/blob/main/index.js) 末尾を読み、環境変数などを Base64 化して GitHub Gist に送るコードを確認した。コード内の送信先は Gist ID `81e1a5300ff02958f30e82aefadac81f`。
2. [該当 Gist](https://gist.github.com/kevin-strangepush/81e1a5300ff02958f30e82aefadac81f) に複数のホスト別ファイルがあることを確認し、対象の [`vincent-grimm-dev_pumpkinshell.txt`](https://gist.github.com/kevin-strangepush/81e1a5300ff02958f30e82aefadac81f#file-vincent-grimm-dev_pumpkinshell-txt) を選んだ。
3. ファイルの Base64 文字列を復号すると JSON になり、ホスト `vincent-grimm-dev`、プロジェクト `pumpkinshell` と一致した。その `e.AWS_ACCESS_KEY_ID` を読み取った。
4. 上記 ID をチャレンジの「Check flag」に提出し、**Accepted flag** と **+15 points** を確認した。Challenge 3 が解放された。

## 取り扱い

漏えい記録には他の認証情報も含まれるため、この記録には転載しない。調査では悪性パッケージの実行や漏えいした認証情報による外部サービスへのアクセスは行っていない。
