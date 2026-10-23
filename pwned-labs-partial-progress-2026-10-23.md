# Pwned Labs — 無料ラボ進行記録（2026-10-23）

## Exploit SSRF with Gopher for GCP Initial Access

[ラボ](https://app.pwnedlabs.io/labs/exploit-ssrf-with-gopher-for-gcp-initial-access/18) ｜状態: 未解決・未提出

### 今回確認した範囲

- Pwned Labs の既存ログインセッションでラボ画面を開き、`Lab On` が有効であることを確認した。
- ラボ画面に表示された Entry Point は `35.226.245.121` だった。
- 同じ Chrome セッションから `http://35.226.245.121` を新規タブで開こうとしたが、ブラウザにより `net::ERR_BLOCKED_BY_CLIENT` で拒否された。
- 前セッションの in-app browser では同じ対象への接続がタイムアウトしている。今回は AGENTS.md の接続失敗時ルールに従い、別ブラウザ、CLI、プロキシ等への迂回や同一操作の再試行は行っていない。
- フラグの取得・提出、対象アプリケーションへの HTTP リクエスト、SSRF / Gopher ペイロードの送信は行っていない。

### 成功判定とウォークスルー

- Pwned Labs の成功表示は未確認。
- 公式ウォークスルーは利用していない。
- この記録は解法ではなく、到達性確認とブロッカーの証跡である。

### ブロッカー

Chrome 側のクライアント機能が対象 IP への接続を拒否した。次回は、対象 IP へのブラウザ接続を許可できる状態にしたうえでラボを再開する必要がある。認証情報、個人情報、顧客情報は記録していない。
