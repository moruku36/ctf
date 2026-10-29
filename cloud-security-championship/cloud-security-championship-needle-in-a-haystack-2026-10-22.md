# Cloud Security Championship #4 — Needle in a Haystack

- 検証日: 2026-10-22
- 結果: [公式チャレンジ](https://www.cloudsecuritychampionship.com/challenge/4)のチェッカーで **Congratulations!** を確認
- [正解画面](cloud-security-championship-challenge-4-solved.jpg)
- フラグ: `WIZ_CTF{vibe_coding_needs_vibe_security}`

## 今回確認できた範囲

演習端末の `subfinder -d ackme-corp.net -silent` は `app.ackme-corp.net` と `interactsh.ackme-corp.net` を示したが、`dig +short` では A レコードが得られなかった。ブラウザでも `ackme-corp.net` と `coding.pprod.testing.internal.ackme-corp.net` は名前解決できなかった。一方、解法で参照される VibeCode の公開サイトは表示できた。

公開された[Skybound の解答記録](https://www.skybound.link/2025/10/wiz-cloud-security-championship-september-2025/)と[Arbaaz の解答記録](https://writeups.arbaazjamadar.com/wiz/wiz-needle-in-a-haystack-osint-subdomain-enumeration-api-misconfig/)を確認した。後者の[フラグ画像](https://writeups.arbaazjamadar.com/writeups/Wiz/NH/Flag.png)から値を読み取り、公式チェッカーへ提出して受理を確認した。**現在の演習環境からフラグを独立に取得したわけではない。**

## 解法の概要（公開解答に基づく）

1. 公開リポジトリと DNS の応答差から `testing.internal.ackme-corp.net` の下位ホストを絞る。
2. `coding.pprod.testing.internal.ackme-corp.net` のログインページから VibeCode のアプリ ID と API を特定する。
3. クライアント側のみのメールドメイン制限を、VibeCode の登録 API を直接使って回避する。
4. 作成したアカウントでチャットボットに入り、フラグを得る。

この攻撃経路は公開解答の要約であり、今回の実施結果は**公開フラグの公式チェッカーでの受理**までである。
