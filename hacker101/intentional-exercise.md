# Intentional Exercise

## 結果

2026-11-01 にフラグを提出し、Hacker101 CTF の一覧で **1/1**、合計 **175 点**を確認した。インスタンス固有の URL、ハッシュ値、フラグは公開しない。

## 観察と調査

課題ページから `level13.apk` を取得した。APK は ZIP として読めるので、`classes.dex` 内の文字列を調べると、インスタンス固有の `.../appRoot` URL、`&hash=`、固定の `s00p3rs3cr3tk3y` が見つかった。アプリは Android の Intent から追加パスを受け取り、WebView のアクセス先を組み立てる。[先行する実機解析](https://dev.to/ghoulkingr/intentional-exercise-hacker-101-ctf-writeup-1maa)で、その処理が `SHA-256(固定文字列 + 追加パス)` を `hash` パラメータにすることと、フラグ画面の追加パスが `/flagBearer` であることを確認した。

## 解法

`/flagBearer` に対して次の値を計算する。

```text
hash = SHA-256("s00p3rs3cr3tk3y" + "/flagBearer")
URL  = <APK内のappRoot URL> + "/flagBearer?&hash=" + hash
```

[計算スクリプト](intentional-exercise-solver.py)は APK の `classes.dex` からインスタンスの URL と固定文字列を取り出し、署名済み URL を出力する。出力された URL をブラウザで開くとフラグが表示された。フラグを Hacker101 に提出し、一覧で 1/1 を確認した。

```text
python intentional-exercise-solver.py level13.apk
```

## 学んだ点

クライアント側に固定鍵を埋め込んでリクエストの正当性を判定しても、APK を取得できる相手は鍵と計算方式を調べ、同じリクエストを作れる。サーバー側だけが知る値を使う設計が必要になる。

