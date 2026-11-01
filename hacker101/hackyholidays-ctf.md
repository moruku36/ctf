# Hackyholidays CTF — 調査記録（継続中）

## 進捗

2026-11-01 に Hacker101 CTF 一覧で **4/12、合計194点**を確認した。Swag Shop と Evil Quiz でさらに2つのフラグを表示したが、まだ提出していない。インスタンス固有の URL、フラグ、Cookie は公開しない。

## 提出済み

1. **入口:** `robots.txt` にフラグと `/s3cr3t-ar3a` が記載されていた。
2. **移動通知:** `/s3cr3t-ar3a/` の表示にはフラグがなかったが、HTML の `#alertbox` に `data-info` 属性としてフラグがあった。同じ要素の `next-page` 属性が `/apps-home/` を示した。
3. **People Rater:** 一覧の要素が Base64 化した `{"id":2}` から始まっていた。`{"id":1}` を Base64 化して `entry/?id=` に渡すと、一覧にない Grinch の記録にフラグが含まれていた。
4. **My Diary:** 初期 URL の `template=entries.html` からテンプレートの読み込みを調べた。`template=index.php` でソースを取得できた。`admin.php` と `secretadmin.php` を順に削除するフィルターは、`secretadsecretaadmin.phpdmin.phpmin.php` を渡すと最終的に `secretadmin.php` が残る。この値で管理ページの内容とフラグを確認した。

## 取得済み・未提出

- **Swag Shop:** `/swag-shop/api/sessions` の Base64 データを復号すると、1件にユーザー UUID があった。その UUID を `/swag-shop/api/user/?uuid=` に渡すとユーザー情報とフラグが返った。
- **Evil Quiz:** [先行する解法](https://lia.mg/posts/hackerone-hacky-holidays-2020-ctf-writeup/)にある演習用管理ログイン情報を `/evil-quiz/admin/` で確認し、フラグが表示された。認証情報の導出手順は今回まだ再現していない。

## 未解決と停止理由

Secure Login では誤ったユーザー名に対して `Invalid Username` と表示されることを確認した。Hate Mail Generator ではキャンペーンの `{{template:...}}` と、一覧表示される `templates/` ディレクトリを確認した。どちらもフラグは未取得。

Signup Manager の `README.md` を Brave で開こうとしたとき、ブラウザが `net::ERR_BLOCKED_BY_CLIENT` で拒否した。ブラウザのブロックを別経路で回避せず、ここで調査を停止した。再開時は未提出の2件を先に提出し、その後に残りの小課題へ進む。

同日、本人の許可を受けて Brave で1回再読み込みしたが、同じブロックが続いた。保護設定を確認する画面操作も、ブラウザの現在の URL を安全に特定できず停止した。新しいフラグの提出はしていない。

