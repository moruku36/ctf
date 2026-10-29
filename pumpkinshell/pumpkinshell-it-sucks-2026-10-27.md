# PumpkinShell — It Sucks

- 実施日: 2026-10-27 (JST)
- 対象: [Wiz Haunted House](https://wizhauntedhouse.com/challenge) の Challenge 3
- 結果: **Solved · +30 points**。チャレンジ内の累計得点は 55 点。
- 回答: `hollowdock.cleanbot-cloud.io`
- 調査方法: Codex の内蔵ブラウザで [AWS Logs Explorer](https://logs.wizhauntedhouse.com/) を操作。ヒントは使用していない。
- アカウント: Wiz CTFs の `moruku36` でログインした状態で提出。

## 解き方

1. チャレンジ文は「家の画像を集めるスマートデバイスの公開エンドポイントのホスト名」を要求していた。AWS Logs Explorer の Invocation logs を調べ、関係するエージェントのセッションを追った。
2. 記録 #488 の家のメモには、カメラ付き掃除機 CleanBot とクラウドポータルが記されていた。記録 #489 のシェル履歴では、掃除機のローカルAPI `192.168.87.42:8080` が使われていた。
3. 記録 #497 の `/api/local/info` 応答に、`cloud_zone: hollowdock` と `cloud_domain: cleanbot-cloud.io` があった。
4. 記録 #501 には、その2項目を `.` で結合して `CB_HOST` を作り、`https://$CB_HOST/api/login` へアクセスする操作が残っていた。したがって公開ポータルのホスト名は `hollowdock.cleanbot-cloud.io`。
5. ホスト名をチャレンジの「Check flag」に提出し、**Accepted flag** と **+30 points** を確認した。Challenge 4 が解放された。

## 取り扱い

ログにはアカウント情報や認証情報が含まれる。この記録には転載せず、ログを閲覧してホスト名を特定した。掃除機のポータルへ実際にログインしたり、画像を取得したりはしていない。
