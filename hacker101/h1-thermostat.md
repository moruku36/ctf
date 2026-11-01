# H1 Thermostat — 解法

- 実施日: 2026-11-01
- 対象: [Hacker101 CTF の H1 Thermostat](https://ctf.hacker101.com/ctf)
- 結果: **2/2 提出済み**。CTF 一覧で全体 **159点**を確認
- インスタンス固有のホスト名とフラグ値は公開しない

## APK の取得

本人が Brave で開いていた課題ページには、最初「Your Android APK is building. Please refresh in a few seconds.」と表示された。ビルド後に一度更新すると「Android APK」リンクが現れ、`thermostat.apk` をダウンロードできた。

## 静的解析で2つのフラグを発見

APK は ZIP 形式なので、アプリのバイトコードである `classes.dex` を取り出せる。このファイル内の印字可能な文字列を確認すると、Hacker101 の `^FLAG^...$FLAG$` 形式の値が2件含まれていた。

[抽出スクリプト](h1-thermostat-extract.py)は `classes.dex` だけを読み、64桁の16進数を含むフラグ形式の文字列を重複除去して表示する。

```text
python h1-thermostat-extract.py thermostat.apk
```

今回は2件抽出され、それぞれ Hacker101 に提出して受理された。CTF 一覧で H1 Thermostat **2/2**、全体 **159点**を確認した。アプリの実行やエミュレーターは使っていない。

## 学んだ点

このインスタンスでは、生成されたAPKのバイトコードに2つのフラグが平文で含まれていた。端末上で実行されるコードやデータは配布先で取り出せるため、秘密値をアプリ内に埋め込む設計は保護にならない。今回の取得方法は、実際のAPKとCTFで受理された結果で確認した。
