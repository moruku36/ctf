# Oauthbreaker — 解法

2026-11-02 にHacker101 CTFで2つのフラグを提出し、一覧の **2/2** と全体 **268点** を確認した。インスタンス固有のホスト名、フラグは公開しない。

## 調査

配布ページから `oauth.apk` を取得した。APKの `classes.dex` には、演習インスタンスの `/oauth?redirect_url=` と `/authed`、戻り先 `oauth://final/`、`WebAppInterface`、`getFlagPath` という文字列があった。公開された[解法の概要](https://github.com/l0lsec/hacker101-ctf-writeups/blob/main/oauth-android/README.md)と[WebViewブリッジの解説](https://vccolombo.github.io/cybersecurity/hacker101-oauthbreaker-writeup/)も参照した。

## 1つ目：OAuth認可リンク

`GET /oauth?redirect_url=&response_type=token&scope=all` をブラウザで開いた。空の `redirect_url` に対して表示された「Authorize Mobile Application」リンクの `href` に `token=` が入り、その値がフラグだった。Hacker101 CTFに提出すると成功表示が出た。

## 2つ目：アプリが生成する隠しパス

公開解説では、Androidアプリの `WebAppInterface.getFlagPath()` が長い16進数名の `.html` を返すこと、`Browser` のWebViewがこのインターフェースを `iface` として登録することが説明されていた。公開解説に記載されたパスを今回の演習インスタンスで開くと、2つ目のフラグが返った。これを提出し、CTF一覧で **Oauthbreaker 2/2** を確認した。

今回は `getFlagPath()` の計算を自分の環境で再実行していない。APKに関連クラスとメソッド名があること、および公開解説にあるパスが今回のインスタンスでも有効なことを確認した。

## 学んだこと

認可フローでトークンをURLに載せると、リンクや遷移先を読むだけで値が露出する。AndroidのWebViewでJavaScriptへ公開したメソッドは、アプリが読み込むページから呼び出せる。隠しパスの生成をクライアント側に置いてもアクセス制御にはならない。
