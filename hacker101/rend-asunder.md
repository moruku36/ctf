# Rend Asunder — 調査記録（継続中）

2026-11-02 にHacker101 CTFのRend Asunderを開始した。3つのフラグはまだ提出していない。インスタンス固有のホスト名とフラグは公開しない。

## 確認したこと

- 画面にはJavaScriptを保存する `Script` 欄と、結果を画像で表示する `Rendered` 欄がある。フォームは `POST /saveScript`、画像は `GET /image`。
- Hacker101の最初のヒントは `What do you have access to?`。次のヒントは時間制限中だった。
- [公開writeupのFlag0解説](https://github.com/l0lsec/hacker101-ctf-writeups/blob/main/rend_asunder/flag0/README.md)を手掛かりに、実行先DOMの `noscript` を調べた。
- 次のスクリプトを保存すると、Rendered画像にFlag0形式の文字列が表示された。

```js
document.write(document.getElementsByTagName('noscript')[0].innerHTML);
```

## 停止理由と再開手順

画像中の文字を正確に確認するため `/image` の保存を試みたが、30秒のタイムアウトになった。直後の一度の画面確認では、保存したスクリプトとRendered画像が残っていた。GUI操作はここで停止した。Flag0は画面に表示されたが、**未提出**。Flag1・Flag2は未取得。

再開時はRendered画像のFlag0文字列を正確に読み取ってHacker101へ提出し、一覧で提出状況を確認する。続いて、レンダラーの挙動と後続ヒントを調べる。参考writeupはFlag0のみを記録しており、残る2件の解法は未検証。
