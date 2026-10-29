# Cloud Security Championship — 未解決問題の調査記録

- 調査日: 2026-10-22（UTC）
- 対象: [Cloud Security Championship](https://www.cloudsecuritychampionship.com/) の #2–#5、#7–#12
- 結果: **全件未解決**。今回の調査で正解として確認できた問題、チェッカー成功、新しい証書はない
- 調査範囲: 公式問題ページと、各問題で指定された演習環境・教材

#1 [Perimeter Leak](RESULTS.md#cloud-security-championship--perimeter-leak) と #6 [Malware Busters!](cloud-security-championship-malware-busters-2026-10-18.md) は以前の解答済み記録であり、今回の調査結果には含めない。以下の観測は正解やフラグ取得を意味しない。

| 問題 | 確認した範囲 | 未解決の理由・未実施事項 |
| --- | --- | --- |
| [#2 Contain Me If You Can](https://www.cloudsecuritychampionship.com/challenge/2) | 公式ページの演習端末への接続を再確認した。 | 端末の接続が閉じられ、演習内の調査を進められなかった。チェッカー未提出。 |
| [#3 Breaking The Barriers](https://www.cloudsecuritychampionship.com/challenge/3) | 公式ページに課題が inactive と表示された。 | 演習環境・提出が利用できず、未解決。 |
| [#4 Needle in a Haystack](https://www.cloudsecuritychampionship.com/challenge/4) | 指定 DNS 演習環境で提供された候補群を調べたが、目的の到達可能な A レコードを確認できなかった。 | 対象サイトに到達できず、候補の正否やフラグは未確認。チェッカー未提出。 |
| [#5 Game of Pods](https://www.cloudsecuritychampionship.com/challenge/5) | 演習内の初期権限と診断機能を調査し、想定外の Pod メタデータ参照と、指定された演習 Pod 内での無害な `id` 実行を確認した。 | これは目的のフラグ取得・他の名前空間での実行を示さない。チェッカー未提出。 |
| [#7 State of Affairs](https://www.cloudsecuritychampionship.com/challenge/7) | 制限付きファイルと、別ユーザーによる定期的な Terraform 実行、生成された state の権限を確認した。 | 必要なファイルの読取経路は未確認。大量の競合試行や provider の追加実行は行っていない。 |
| [#8 Confession Booth](https://www.cloudsecuritychampionship.com/challenge/8) | 公式ソース ZIP の取得を試みた。 | 利用環境のダウンロード制限で取得できず、別経路による回避はしていない。ソース解析・チェッカー提出は未実施。 |
| [#9 Trust Issues](https://www.cloudsecuritychampionship.com/challenge/9) | 指定公開リポジトリの暗号化教材を取得し、指定 runner 内の不審なモジュールを静的に調べ、収集・暗号化・アップロード処理の構造を確認した。 | モジュールは実行・import していない。長文入力後の演習端末の最終状態は不確実で、教材の完全転送・復号・フラグ取得・チェッカー提出は確認できていない。 |
| [#10 Happy Birthday](https://www.cloudsecuritychampionship.com/challenge/10) | 公式ページで指定サイトと policy ZIP の所在を確認した。 | 教材の取得・解析、対象サイトの検証、チェッカー提出は未実施。 |
| [#11 Split Horizon](https://www.cloudsecuritychampionship.com/challenge/11) | 公式ページで指定演習環境と課題範囲を確認した。 | 演習環境内の調査とチェッカー提出は未実施。 |
| [#12 Glass House](https://www.cloudsecuritychampionship.com/challenge/12) | 公式ページで指定リポジトリの所在を確認した。 | リポジトリの内容は取得・検証できておらず、チェッカー提出も未実施。 |

## 演習環境に関する安全メモ

#5 の演習中に一時的な演習用 Secret を作成したが、接続中断後に削除を確認できていない。現在の存否は不明であり、後続の調査では安全な方法で状態を確認する必要がある。値や認証情報はこのリポジトリに記録しない。

このページは途中経過の記録であり、未解決問題の解法や完了報告ではない。
