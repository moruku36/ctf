# Hacker101 CTF 解法記録

2026-10-29 にログイン済みの [Hacker101 CTF](https://ctf.hacker101.com/ctf) で、一覧の上から順に取り組む記録です。フラグはインスタンスごとの値なので、公開リポジトリには全文を載せません。

| 順番 | 課題 | 状態 | 解法 |
| --- | --- | --- | --- |
| 1 | A little something to get you started | 開始時点で 1/1。今回の解法は未再現 | 記録待ち |
| 2 | Micro-CMS v1 | **4/4 提出済み** | [解法](micro-cms-v1.md) |
| 3 | Micro-CMS v2 | **3/3 提出済み** | [解法と調査記録](micro-cms-v2.md) |
| 4 | Encrypted Pastebin | **4/4 提出済み** | [解法](encrypted-pastebin.md) |
| 5 | Photo Gallery | **3/3 提出済み** | [解法](photo-gallery.md) |
| 6 | Cody's First Blog | **3/3 提出済み** | [解法](codys-first-blog.md) |
| 7 | Postbook | **7/7 提出済み** | [解法](postbook.md) |

2026-10-29: Micro-CMS v1 の残る Flag2 と Flag1 を提出し、CTF 一覧で 4/4、合計 9/26 点を確認した。Micro-CMS v2 は起動済み。Changelog とログイン画面を確認した。本人の明示的な承認後、ログインフォームで UNION を使った認証回避に成功した。Private Page のフラグと、未認証 POST で返ったフラグを提出した。Flag2 はログイン応答の真偽差を使ってインスタンス固有の資格情報を特定し、通常ログイン後に提出した。今回の Chrome 操作でタイムアウトは再発せず、CTF 一覧で 3/3、全体 18/26 点を確認した。

2026-10-29: Postbook を開始したが、`/ctf/start/7` に「The level is being set up, one moment please」と表示されたまま待機がタイムアウト。直後の一度の状態確認でも変化なし。Flag は未取得。画面操作はここで停止した。


2026-10-29: Postbook のトップと Sign up 画面を確認した。演習用の仮アカウント入力中にブラウザ操作が切断され、入力・登録の成否は未確認。画面操作を停止し、[調査記録](postbook.md)に状況を保存した。


2026-10-29: Postbook の Flag0、Flag1、Flag2、Flag3、Flag4、Flag6 に該当する6つのフラグを提出した。Flag5 の Cookie を管理者識別値へ変更する操作は自動承認審査が拒否したため実行していない。本人の具体的承認待ち。


2026-10-29: 本人の具体的承認後、Postbook の予測可能なログイン Cookie を検証し、最後の Flag5 を提出した。CTF 一覧で Postbook 7/7、全体 46 点を確認した。解法は [Postbook](postbook.md) に記録した。

2026-10-30: Photo Gallery の SQL 注入で `main.py` を読み、3枚目の保存名と容量表示のコマンド注入から残るフラグを確認した。3つとも提出し、CTF 一覧で 3/3 を確認した。演習中に変更した画像情報は元に戻した。

2026-10-30: Cody's First Blog のコメント投稿、管理ページへの直接アクセス、承認済みコメントを使ったローカルページの再読み込みで3つのフラグを提出した。CTF 一覧で 3/3、全体 79 点を確認した。解法は [Cody's First Blog](codys-first-blog.md) に記録した。

2026-10-30: Encrypted Pastebin の4つのフラグを提出し、CTF 一覧で 4/4、全体 115 点を確認した。暗号化リンクのブロック操作、パディングオラクル、追跡ログの参照を [Encrypted Pastebin](encrypted-pastebin.md) に記録した。
