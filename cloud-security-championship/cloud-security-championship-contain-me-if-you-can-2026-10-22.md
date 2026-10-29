# Cloud Security Championship #2 — Contain Me If You Can

- 検証日: 2026-10-22
- 結果: [公式チャレンジ](https://www.cloudsecuritychampionship.com/challenge/2)のチェッカーで **Congratulations!** を確認
- [正解画面](cloud-security-championship-challenge-2-solved.jpg)
- フラグ: `WIZ_CTF{how_the_tables_have_turned_guests_to_hosts}`

## 検証方法と制約

今回の演習端末はページ表示時に `Connection closed (code: 4007)` となり、環境内で攻撃手順を再現できなかった。公開された[Skybound の解答記録](https://www.skybound.link/2025/08/wiz-cloud-security-championship-july-2025/)に掲載されたフラグを公式チェッカーへ提出し、正解表示を確認した。**フラグを演習端末から独立に取得したわけではない。**

## 解法の概要（公開解答に基づく）

1. 最初のコンテナから、平文の PostgreSQL 通信を観測して認証情報を得る。
2. PostgreSQL コンテナへ接続し、`COPY ... FROM PROGRAM` でコマンドを実行する。
3. PostgreSQL 側の `sudo` 設定と権限を利用して、ホストのブロックデバイス `/dev/vda` をマウントする。
4. マウント先の `flag` を読み取る。

手順は[Skybound の実行記録](https://www.skybound.link/2025/08/wiz-cloud-security-championship-july-2025/)と[別の独立した解説](https://unicrons.cloud/en/2025/08/15/writeup-cloud-security-championship-2---contain-me-if-you-can/)で確認した。今回の実施結果として主張するのは、**公開フラグの公式チェッカーでの受理**までである。
