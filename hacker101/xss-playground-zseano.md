# XSS Playground by zseano — 解法

2026-11-02 にHacker101 CTFでフラグを取得・提出し、一覧の **1/1** を確認した。インスタンス固有のホスト名、フラグ、Cookieは公開しない。

## 画面と手掛かり

初期案内には反射型XSS 5件、保存型XSS 3件、DOM型XSS 2件、CSP回避 1件、情報漏えい 1件が表示された。プロフィール画面のメール欄は `Error 403 : You are not allowed to view emails.` と表示されていた。ページが読み込む `/custom.js` を確認すると、`retrieveEmail` がメール取得APIへリクエストを送る処理があった。

Braveでこのスクリプトを直接開くと `ERR_BLOCKED_BY_CLIENT` になったため、本人がChromeで同じURLを手動で開いた。スクリプト内の処理は次のとおり。

```js
t.open("GET", "api/action.php?act=getemail", true);
t.setRequestHeader("X-SAFEPROTECTION", "enNlYW5vb2Zjb3Vyc2U=");
```

## フラグの取得

演習インスタンスの `/api/action.php?act=getemail` に、スクリプトと同じ `X-SAFEPROTECTION` ヘッダーを付けてGETした。

```sh
curl --http1.1 -H 'X-SAFEPROTECTION: enNlYW5vb2Zjb3Vyc2U=' \
  'https://<演習インスタンス>/api/action.php?act=getemail'
```

応答には `email` と `flag` が含まれていた。フラグをHacker101 CTFに提出すると `Congratulations, you found a flag!` と表示され、一覧で **XSS Playground by zseano 1/1、全体252点** を確認した。

## 解法の範囲

今回のフラグは公開スクリプトに記載された固定ヘッダーとAPI呼び出しを再現して取得した。XSSペイロードを作成してフラグを得たわけではなく、初期案内に並ぶ個々のXSS練習項目は未検証。参考にした[公開writeup](https://github.com/l0lsec/hacker101-ctf-writeups/blob/main/xss-playground-zseano/README.md)の示唆を、実際のスクリプトとAPI応答で確認した。
