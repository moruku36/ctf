# Rend Asunder — 調査記録（継続中）

2026-11-02 にHacker101 CTFのRend Asunderを検証した。CTF一覧で **1/3 提出済み**。インスタンス固有のホスト名とフラグは公開しない。

## Flag0 — DOM内のnoscript

画面の `Script` 欄は `POST /saveScript` で保存され、実行結果が `GET /image` のPNG画像として表示される。最初のヒントは `What do you have access to?`。

[公開writeupのFlag0解説](https://github.com/l0lsec/hacker101-ctf-writeups/blob/main/rend_asunder/flag0/README.md)を参考に、次のJavaScriptを保存した。

```js
document.write(document.getElementsByTagName('noscript')[0].innerHTML);
```

Rendered画像にフラグが現れた。画像を取得して文字列を正確に読み、Hacker101へ提出したところ `Congratulations, you found a flag!` が表示され、CTF一覧でもRend Asunder **1/3**を確認した。

## 残る2件の調査

実行先の `document.documentElement.outerHTML` では、`head` 内に `noscript` と自分の `script` があることを確認した。実行環境のUser-AgentはHeadlessChrome 67.0.3396.79。Cookieは空で、表示された文書URLはレンダラー内部のローカルURLだった。

[公開された詳しい解析](https://www.3lyly0.dev/research/rend-asunder-explained/)は、親iframeにあるFlag1をブラウザー内部のメモリから読み、Flag2を実行環境のファイルから得る方法を述べている。ただし、記事には今回の環境で実行できる完全なコードや必要な内部オフセットがない。この記事のFlag1・Flag2の手順は、こちらでは**未検証**である。


### 再現できたブラウザーの問題

公開解析の `Math.expm1(-0)` を使うコードを実行すると、長さ3の配列が異常に大きな長さとして扱われた。近くに確保したオブジェクト配列を介してDOMオブジェクトの内部参照値を観測し、`ArrayBuffer` の参照先を自分のバッファ内で8バイト移動させると、`DataView` の読み取り値が移動先の既知の値へ変わることも確認した。これは任意メモリー読み取りにつながる足掛かりだが、親文書のフラグがある場所はまだ特定していない。広い範囲を直接走査した試行では描画失敗の画像が返ったため、以後は範囲を限定した。

技術的背景は[元のV8脆弱性を使ったKrautflareの解説](https://www.jaybosamiya.com/blog/2019/01/02/krautflare/)にも詳しい。この解説は別のCTF向けなので、Rend Asunder固有のメモリー配置やFlag1・Flag2の位置を保証しない。

次は時間制限後のHacker101ヒントを確認し、実際の描画環境と照合する。Flag1・Flag2は未取得・未提出。
