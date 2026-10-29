# CTF

[English](README.md) | [日本語](README.ja.md)

このリポジトリは、私のCTFおよびセキュリティチャレンジの結果、writeup、証跡を、プラットフォーム・イベント別に整理して収録しています。

## 結果サマリー

最も古い記録結果（2026-10-16）と手法については、[RESULTS.md](RESULTS.md)を参照してください。

## 目次

### PumpkinShell

PumpkinShell (Wiz)。全チャレンジクリア、95/100（2026-10-27）。

- [Dependency Issues](pumpkinshell/pumpkinshell-dependency-issues-2026-10-27.md)
- [Gist of the Problem](pumpkinshell/pumpkinshell-gist-of-the-problem-2026-10-27.md)
- [It Sucks](pumpkinshell/pumpkinshell-it-sucks-2026-10-27.md)
- [Through the Lens](pumpkinshell/pumpkinshell-through-the-lens-2026-10-27.md)
- [Unlock the Core Memory](pumpkinshell/pumpkinshell-unlock-the-core-memory-2026-10-27.md)
- [証明書](pumpkinshell/pumpkinshell-certificate.png)

### Cloud Security Championship

Cloud Security Championship。チャレンジ #2、#4、#5、#6、#7 の writeup と、未解決分の調査ログ。

- [#2 — Contain Me If You Can](cloud-security-championship/cloud-security-championship-contain-me-if-you-can-2026-10-22.md)
- [#4 — Needle in a Haystack](cloud-security-championship/cloud-security-championship-needle-in-a-haystack-2026-10-22.md)
- [#5 — Game of Pods](cloud-security-championship/cloud-security-championship-game-of-pods-2026-10-22.md)
- [#6 — Malware Busters!](cloud-security-championship/cloud-security-championship-malware-busters-2026-10-18.md)
- [#7 — State of Affairs](cloud-security-championship/cloud-security-championship-state-of-affairs-2026-10-22.md)
- [未解決チャレンジの調査ログ](cloud-security-championship/cloud-security-championship-partial-progress-2026-10-22.md)
- [証明書](cloud-security-championship/cloud-security-championship-malware-busters-certificate.png)

### The Cloud Hunting Games

The Cloud Hunting Games。全5チャレンジクリア、40ポイント（2026-10-18）。

- [Writeup](cloud-hunting-games/cloud-hunting-games-2026-10-18.md)
- [証明書](cloud-hunting-games/cloud-hunting-games-certificate.png)

### Prompt Airlines

Prompt Airlines。5/5チャレンジクリア、およびライブリプレイ。

- [5/5チャレンジ](prompt-airlines/prompt-airlines-2026-10-18.md)
- [ライブ5/5リプレイ](prompt-airlines/prompt-airlines-2026-10-22.md)
- [証明書](prompt-airlines/prompt-airlines-certificate.png)
- [チャレンジ4で使用したメンバーカード生成スクリプト](prompt-airlines/make-member-card.ps1)

### K8s LAN Party

K8s LAN Party。5問中2問クリア。詳細はRESULTS.mdに記載。

- [証明書](k8s-lan-party/k8s-lan-party-certificate.png)

### Pwned Labs

Pwned Labs。無料ラボのwriteup。

- [AWS Blue Teaming、3問クリア](pwned-labs/pwned-labs-aws-blue-teaming-2026-10-22.md)
- [Reveal Hidden Files in Google Storage](pwned-labs/pwned-labs-reveal-hidden-files-google-storage-2026-10-23.md)
- [無料ラボの進捗ログ](pwned-labs/pwned-labs-partial-progress-2026-10-23.md)

### Hacker101 CTF

- [Hacker101 CTF の writeup](hacker101/README.md)

### HackerOne

- [日本語の学習・練習ロードマップ](hackerone/hackerone-learning-roadmap.md)

## 規約

- プラットフォームまたはイベントごとに1つのフォルダー。writeupのファイル名は`<event>-<challenge>-<date>.md`とします。
- Writeupには手法と証跡を記録します。クリア済みの公開チャレンジのフラグはRESULTS.mdおよび各writeupに保管しています。
- 実際の認証情報、パスワード、トークン、個人データはここには一切記載しません。これらを使用した手順がある場合も、参照するのみで、値を直接記載しません。

## 参考資料

- [HackerOne](https://www.hackerone.com/)
- [HackerOne ドキュメント](https://docs.hackerone.com/en/)
- [X の HackerOne](https://x.com/Hacker0x01)
