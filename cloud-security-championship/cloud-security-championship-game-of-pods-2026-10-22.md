# Cloud Security Championship #5 — Game of Pods

- 検証日: 2026-10-22
- 結果: [公式チャレンジ](https://www.cloudsecuritychampionship.com/challenge/5)のチェッカーで **Congratulations!** を確認
- [正解画面](cloud-security-championship-challenge-5-solved.jpg)
- フラグ: `WIZ_CTF{k8s_is_one_big_proxy}`

## 今回確認できた範囲

演習端末は起動し、フラグが `kube-system` にあるという案内を表示した。`kubectl auth can-i --list` で、初期サービスアカウントが主に現在の名前空間の Pod に対する `get/list/watch` 権限しか持たないことを確認した。

フラグは[Arbaaz の公開解答](https://writeups.arbaazjamadar.com/wiz/wiz-game-of-pods-kubernetes-cve-2022-3294-cluster-admin/)に記載された値を公式チェッカーへ提出して受理を確認した。**今回の演習端末で `kube-system` の Secret を読み取ったわけではない。**

## 解法の概要（公開解答に基づく）

1. staging の Pod を調査して、デバッグ用サービスと到達可能な API を見つける。
2. デバッグサービスのパス処理とリクエスト転送を利用し、別名前空間の Pod に到達する。
3. 権限のあるサービスアカウントのトークンを取得し、サービスアカウントトークン Secret の自動生成を利用して権限を広げる。
4. `nodes/status` と `nodes/proxy` の組み合わせで API サーバーへの転送を悪用し、`kube-system` のフラグ Secret を読む。

この経路は[公開解答](https://writeups.arbaazjamadar.com/wiz/wiz-game-of-pods-kubernetes-cve-2022-3294-cluster-admin/)の要約であり、今回の実施結果は**公開フラグの公式チェッカーでの受理**までである。
