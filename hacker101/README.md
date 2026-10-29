# Hacker101 CTF 解法記録

2026-10-29 にログイン済みの [Hacker101 CTF](https://ctf.hacker101.com/ctf) で、一覧の上から順に取り組む記録です。フラグはインスタンスごとの値なので、公開リポジトリには全文を載せません。

| 順番 | 課題 | 状態 | 解法 |
| --- | --- | --- | --- |
| 1 | A little something to get you started | 開始時点で 1/1。今回の解法は未再現 | 記録待ち |
| 2 | Micro-CMS v1 | **4/4 提出済み** | [解法](micro-cms-v1.md) |
| 3 | Micro-CMS v2 | **3/3 提出済み** | [解法と調査記録](micro-cms-v2.md) |
| 7 | Postbook | **6/7 提出済み**。Cookie 検証は承認待ち | [解法と調査記録](postbook.md) |

2026-10-29: Micro-CMS v1 の残る Flag2 と Flag1 を提出し、CTF 一覧で 4/4、合計 9/26 点を確認した。Micro-CMS v2 は起動済み。Changelog とログイン画面を確認した。本人の明示的な承認後、ログインフォームで UNION を使った認証回避に成功した。Private Page のフラグと、未認証 POST で返ったフラグを提出した。Flag2 はログイン応答の真偽差を使ってインスタンス固有の資格情報を特定し、通常ログイン後に提出した。今回の Chrome 操作でタイムアウトは再発せず、CTF 一覧で 3/3、全体 18/26 点を確認した。

2026-10-29: Postbook を開始したが、`/ctf/start/7` に「The level is being set up, one moment please」と表示されたまま待機がタイムアウト。直後の一度の状態確認でも変化なし。Flag は未取得。画面操作はここで停止した。


2026-10-29: Postbook のトップと Sign up 画面を確認した。演習用の仮アカウント入力中にブラウザ操作が切断され、入力・登録の成否は未確認。画面操作を停止し、[調査記録](postbook.md)に状況を保存した。


2026-10-29: Postbook の Flag0、Flag1、Flag2、Flag3、Flag4、Flag6 に該当する6つのフラグを提出した。Flag5 の Cookie を管理者識別値へ変更する操作は自動承認審査が拒否したため実行していない。本人の具体的承認待ち。
