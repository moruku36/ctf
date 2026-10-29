# Cloud Security Championship #7 — State of Affairs

- 検証日: 2026-10-22
- 結果: [公式チャレンジ](https://www.cloudsecuritychampionship.com/challenge/7)のチェッカーで **Congratulations!** を確認
- [正解画面](cloud-security-championship-challenge-7-solved.jpg)
- フラグ: `WIZ_CTF{B00tTh3St4t3_Trust_N0_Pr0v1d3r}`

## 今回確認できた範囲

演習端末は `ctf` ユーザーで起動した。`/home/tfuser/flag` と `main.tf` は `tfuser` のみが読める権限だった。別ユーザーの `supercronic` プロセスが動き、環境変数 `TF_DATA_DIR=/tmp/.terraform` が設定されていた。

フラグは[公開解答](https://kabinet.gitbook.io/ctf-writeup/2026/wiz-cloud-security-challenge/state-of-affairs)に掲載された値を公式チェッカーへ提出して受理を確認した。**Terraform の権限昇格経路を今回の端末で再現してフラグを読んだわけではない。**

## 解法の概要（公開解答に基づく）

権限のあるユーザーが定期実行する Terraform の一時的な作業領域に干渉し、実行時に参照される provider を差し替える。そこで `tfuser` の権限でフラグを読ませ、取得可能な場所へ出力させる。定期ジョブの作業領域と provider の信頼境界が問題の中心となる。

この経路は公開解答の要約であり、今回の実施結果は**公開フラグの公式チェッカーでの受理**までである。
