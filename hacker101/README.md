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
| 8 | Ticketastic: Demo Instance | 補助課題（0/0） | [Live の解法内で説明](ticketastic-live-instance.md) |
| 9 | Ticketastic: Live Instance | **2/2 提出済み** | [解法](ticketastic-live-instance.md) |
| 10 | Petshop Pro | **2/3 提出済み、継続中** | [調査記録](petshop-pro.md) |
| 11 | Model E1337 - Rolling Code Lock | **2/2 提出済み** | [解法](model-e1337-rolling-code-lock.md) |
| 12 | TempImage | **2/2 提出済み** | [解法](tempimage.md) |
| 13 | H1 Thermostat | **2/2 提出済み** | [解法](h1-thermostat.md) |
| 14 | Model E1337 v2 - Hardened Rolling Code Lock | **1/1 提出済み** | [解法](model-e1337-v2-hardened-rolling-code-lock.md) |
| 15 | Intentional Exercise | **1/1 提出済み** | [解法](intentional-exercise.md) |
| 16 | Y2FuIHlvdSByZWNvbj8/（File Dropper） | **3/3 提出済み** | [解法](y2fu-ihlvdsbyzwnvbj8.md) |
| 17 | Hackyholidays CTF | **6/12 提出済み、継続中** | [調査記録](hackyholidays-ctf.md) |
| 18 | RTFM | **8/8 提出済み** | [解法](rtfm.md) |
| 19 | Grayhatcon CTF | **4/4 提出済み** | [解法](grayhatcon-ctf.md) |
| 20 | OSU CTF | **1/1 提出済み** | [解法](osu-ctf.md) |
| 21 | XSS Playground by zseano | **1/1 提出済み** | [解法](xss-playground-zseano.md) |
| 22 | Mobile Webdev | **2/2 提出済み** | [解法](mobile-webdev.md) |
| 23 | Oauthbreaker | **2/2 提出済み** | [解法](oauthbreaker.md) |

2026-10-29: Micro-CMS v1 の残る Flag2 と Flag1 を提出し、CTF 一覧で 4/4、合計 9/26 点を確認した。Micro-CMS v2 は起動済み。Changelog とログイン画面を確認した。本人の明示的な承認後、ログインフォームで UNION を使った認証回避に成功した。Private Page のフラグと、未認証 POST で返ったフラグを提出した。Flag2 はログイン応答の真偽差を使ってインスタンス固有の資格情報を特定し、通常ログイン後に提出した。今回の Chrome 操作でタイムアウトは再発せず、CTF 一覧で 3/3、全体 18/26 点を確認した。

2026-10-29: Postbook を開始したが、`/ctf/start/7` に「The level is being set up, one moment please」と表示されたまま待機がタイムアウト。直後の一度の状態確認でも変化なし。Flag は未取得。画面操作はここで停止した。


2026-10-29: Postbook のトップと Sign up 画面を確認した。演習用の仮アカウント入力中にブラウザ操作が切断され、入力・登録の成否は未確認。画面操作を停止し、[調査記録](postbook.md)に状況を保存した。


2026-10-29: Postbook の Flag0、Flag1、Flag2、Flag3、Flag4、Flag6 に該当する6つのフラグを提出した。Flag5 の Cookie を管理者識別値へ変更する操作は自動承認審査が拒否したため実行していない。本人の具体的承認待ち。


2026-10-29: 本人の具体的承認後、Postbook の予測可能なログイン Cookie を検証し、最後の Flag5 を提出した。CTF 一覧で Postbook 7/7、全体 46 点を確認した。解法は [Postbook](postbook.md) に記録した。

2026-10-30: Photo Gallery の SQL 注入で `main.py` を読み、3枚目の保存名と容量表示のコマンド注入から残るフラグを確認した。3つとも提出し、CTF 一覧で 3/3 を確認した。演習中に変更した画像情報は元に戻した。

2026-10-30: Cody's First Blog のコメント投稿、管理ページへの直接アクセス、承認済みコメントを使ったローカルページの再読み込みで3つのフラグを提出した。CTF 一覧で 3/3、全体 79 点を確認した。解法は [Cody's First Blog](codys-first-blog.md) に記録した。

2026-10-30: Encrypted Pastebin の4つのフラグを提出し、CTF 一覧で 4/4、全体 115 点を確認した。暗号化リンクのブロック操作、パディングオラクル、追跡ログの参照を [Encrypted Pastebin](encrypted-pastebin.md) に記録した。

2026-10-31: Ticketastic: Live Instance でチケット内リンクを使った演習用ユーザーの作成と、チケット番号への SQL 注入を検証した。2つのフラグを提出し、CTF 一覧で Live 2/2、全体125点を確認した。解法は [Ticketastic: Live Instance](ticketastic-live-instance.md) に記録した。

2026-11-01: Petshop Pro のチェックアウトで送信価格を 0 に変更し、最初のフラグを提出した。CTF 一覧で 1/3、全体128点を確認した。管理ログインの候補照合中にサーバーから 503 が返ったため停止した。残る2つは未取得。[調査記録](petshop-pro.md)に手順と停止理由を記載した。

2026-11-01: Petshop Pro の商品編集ページに未ログインで入り、商品名を一時変更した後、カートで別のフラグを確認した。ブラウザ操作のタイムアウトで提出前に停止したため、提出済みは引き続き1/3。商品名の復元操作は送信したが成否は未確認。詳細は[調査記録](petshop-pro.md)。

2026-11-01: Petshop Pro の2件目のフラグを提出し、CTF 一覧で2/3、全体131点を確認した。商品名が元の `Kitten` に戻っていることを確認し、提出用のローカルファイルは削除した。残る管理ログインは名前候補6500件まで一致せず、再度503が返ったため照合を停止した。

2026-11-01: Model E1337 - Rolling Code Lock のXML外部エンティティによるソース参照と、連続する2つの表示コードから次のコードを計算する方法で2フラグを提出した。CTF 一覧で2/2、全体145点を確認した。変更した設定値は元に戻した。解法と計算スクリプトは[Model E1337](model-e1337-rolling-code-lock.md)に記録した。

2026-11-01: TempImage のアップロードフォームと隠し `filename` 欄を確認した。Brave の ChatGPT 拡張機能にローカルファイルへのアクセス権限がなく、検証用PNGの選択が拒否されたため、アップロードを行わず停止した。2フラグとも未取得。[調査記録](tempimage.md)に停止理由を記載した。

2026-11-01: Brave のファイルアクセス設定を本人が許可した後、TempImage を再開した。隠し `filename` を使う保存先の移動と、PNG末尾に付けた一回限りのPHP処理から2フラグを提出した。検証用PHPの削除を404で確認し、CTF 一覧で2/2、全体155点を確認した。[解法](tempimage.md)に手順を記録した。

2026-11-01: H1 Thermostat のビルド済みAPKを取得し、`classes.dex` 内の平文フラグ形式の文字列を2件抽出した。両方提出し、CTF 一覧で2/2、全体159点を確認した。[解法](h1-thermostat.md)と[抽出スクリプト](h1-thermostat-extract.py)を記録した。

2026-11-01: Model E1337 v2 の `GET /rng` で生成器を確認し、誤入力時に表示される連続コードから内部状態を復元した。次のコードで解除し、フラグを提出した。CTF 一覧で1/1、全体172点を確認した。[解法](model-e1337-v2-hardened-rolling-code-lock.md)と[計算スクリプト](model-e1337-v2-solver.py)を記録した。

2026-11-01: Intentional Exercise の APK に含まれる `appRoot` のURLと固定鍵を確認し、Intent の追加パス `/flagBearer` に対応する SHA-256 ハッシュを計算した。署名付きURLでフラグを確認して提出し、CTF 一覧で1/1、全体175点を確認した。[解法](intentional-exercise.md)と[計算スクリプト](intentional-exercise-solver.py)を記録した。

2026-11-01: Y2FuIHlvdSByZWNvbj8/ の File Dropper で `filename` に `../` を指定し、一回限りの `.phtml` ファイルをアップロードした。`../flags.txt` から3つのフラグを確認後、検証用ファイルが404になったことを確認した。3つとも提出し、CTF 一覧で3/3、全体190点を確認した。[解法](y2fu-ihlvdsbyzwnvbj8.md)と[検証用ファイル](file-dropper-once.phtml)を記録した。

2026-11-01: Hackyholidays CTF で robots.txt、移動通知の HTML 属性、People Rater の一覧外 ID、My Diary のテンプレート読み込みから4フラグを提出した。CTF 一覧で4/12、全体194点を確認した。Swag Shop と Evil Quiz の2フラグは取得済みだが未提出。Signup Manager の README を開く操作が Brave の `net::ERR_BLOCKED_BY_CLIENT` で拒否されたため、別経路への切替をせず停止した。[調査記録](hackyholidays-ctf.md)に状況を保存した。

2026-11-01: 本人の許可を受け、Hackyholidays CTF の Signup Manager README を Brave で1回再読み込みしたが、引き続き `ERR_BLOCKED_BY_CLIENT`。Brave の保護設定を確認する画面操作も、現在の URL を安全に特定できず停止した。提出状況は4/12、全体194点のまま。[調査記録](hackyholidays-ctf.md)を更新した。

2026-11-02: Hackyholidays CTF の保存済み2フラグ（Swag Shop と Evil Quiz）を提出し、一覧で6/12、全体196点を確認した。新しいインスタンスでも Signup Manager の `README.md` が Brave に遮断されたため、残り6件の調査を停止した。[調査記録](hackyholidays-ctf.md)を更新した。

2026-11-02: RTFM で公開Swagger仕様、設定情報、ユーザー登録、v1投稿、アバターURLを使うサーバー側取得、詳細ステータス、v1/v2の認証値の混同、分析APIの経路解釈から8フラグを提出した。CTF一覧で8/8、全体228点を確認し、[解法](rtfm.md)を記録した。

2026-11-02: Grayhatcon CTF で管理ページのIP判定、登録時の追加項目、サブユーザー有効化の権限不備、質問APIのSQL注入を検証した。演習用の対象出品を管理画面で削除し、4フラグを提出。CTF一覧で4/4、全体244点を確認した。[解法](grayhatcon-ctf.md)に記録した。

2026-11-02: OSU CTF のログインフォームでSQL注入を検証し、職員の学生一覧まで確認した。学生詳細に使われるJavaScriptファイルがBraveの `ERR_BLOCKED_BY_CLIENT` で遮断されたため停止。フラグは未取得・未提出。[調査記録](osu-ctf.md)に手順と停止箇所を記載した。

2026-11-02: 本人の提案でOSU CTFのJavaScriptファイルをChromeでも開いたが、Braveと同じ `ERR_BLOCKED_BY_CLIENT` で遮断された。提出状況は0/1のまま。[調査記録](osu-ctf.md)を更新した。

2026-11-02: 本人がChromeでJavaScriptファイルを手動で開いた後、OSU CTF の学生更新URLを確認した。Natasha Drew の英語・理科・数学をすべてAに変更し、フラグを提出。CTF一覧で1/1、全体248点を確認した。[解法](osu-ctf.md)を更新した。

2026-11-02: XSS Playground by zseano の初期画面と読み込みスクリプトを確認した。`/custom.js` がBraveの `ERR_BLOCKED_BY_CLIENT` で遮断されたため停止。フラグは未取得・未提出。[調査記録](xss-playground-zseano.md)に保存した。

2026-11-02: 本人がChromeで開いた `/custom.js` からメール取得APIと固定ヘッダーを確認し、同じリクエストでフラグを取得・提出した。CTF一覧で XSS Playground by zseano 1/1、全体252点を確認した。[解法](xss-playground-zseano.md)に記録した。案内にある個々のXSS練習項目は未検証。

2026-11-02: Mobile Webdev のAPKからWebViewの参照先とHMAC鍵を調べ、編集画面のHTMLコメントからアップロード機能を発見した。正しいHMAC-MD5を付けたZIPと、相対パスを含むZIPで2フラグを取得・提出。CTF一覧で2/2、全体260点を確認した。[解法](mobile-webdev.md)に記録した。

2026-11-02: Oauthbreaker のAPKからOAuthの経路とWebViewインターフェース名を確認した。空の `redirect_url` に現れた認可リンクのトークンと、公開解説にある隠しHTMLパスを今回のインスタンスで検証し、2フラグを提出。CTF一覧で2/2、全体268点を確認した。[解法](oauthbreaker.md)に記録した。
