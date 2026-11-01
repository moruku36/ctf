# Model E1337 - Rolling Code Lock — 解法

- 実施日: 2026-11-01
- 対象: [Hacker101 CTF](https://ctf.hacker101.com/ctf) の Model E1337 - Rolling Code Lock
- 結果: **2/2 提出済み**。CTF 一覧で全体 **145点**を確認
- フラグ値と演習インスタンス固有のURLは公開しない

## 画面と手がかり

トップにはコード入力欄と「Unlock」ボタンがある。誤ったコードを送ると `Code incorrect. Expected ...` と返り、その回に必要だった26ビットのコードが分かる。公式ヒントの最初の文は「Hidden functionality is good functionality」。

`/admin` を開くとロックの場所が表示された。このページのHTMLコメントに `get-config` への言及があり、`/get-config` は `<config><location>Front door</location></config>` というXMLを返した。

## Flag0: XML外部エンティティによるソース参照

`/set-config` はクエリの `data` をXMLとして解析し、`location` 要素の内容を管理画面に表示する。外部エンティティを定義して課題の `main.py` を参照した。

```xml
<?xml version="1.0"?>
<!DOCTYPE config [<!ENTITY xxe SYSTEM "main.py">]>
<config><location>&xxe;</location></config>
```

このXMLを `/set-config?data=` にURLエンコードして渡すと `/admin` に戻り、`location` 欄に `main.py` の内容が表示された。ソース内のコメントにフラグがあり、提出して受理された。同じ方法で `rng.py` を確認した。調査後、`<config><location>Front door</location></config>` を `/set-config` に渡し、表示が元に戻ったことを確認した。

## Flag1: ローリングコードの予測

`main.py` の `/unlock` はリクエストごとに `rng.next(26)` を呼び、入力が違う場合も生成されたコードを応答に表示する。`rng.py` の初期シードは32ビットで、状態更新と出力はビットごとのXORを中心とするため、シードから連続する出力への写像をGF(2)上のアフィン変換として扱える。

1. `0` を2回送って、応答に表示された連続する26ビットのコードを記録する。
2. [計算スクリプト](model-e1337-solver.py)で、ゼロシードの52ビット出力と各1ビットだけ立てた32個のシードの出力を計算する。
3. 52本の線形方程式をGF(2)で解き、32ビットのシードを復元する。取得した2コードを再現できることも検証する。
4. 同じ生成器を2回進めて次の26ビットコードを計算し、3回目の `/unlock` に入力する。

```text
python model-e1337-solver.py <1回目に表示されたコード> <2回目に表示されたコード>
```

実際の2応答から計算した3回目のコードで `Unlocked successfully` とフラグが表示された。フラグを提出し、一覧で **2/2、全体145点**を確認した。スクリプトは手元の既知シードでも自己検証し、実際のロック解除でも動作を確認した。

## 参考

- [Hacker101 CTF](https://ctf.hacker101.com/ctf)
- [7Rocky の解説](https://7rocky.github.io/en/ctf/hacker101ctf/model-e1337---rolling-code-lock/)
