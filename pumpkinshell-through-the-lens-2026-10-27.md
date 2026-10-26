# PumpkinShell — Through the Lens

- 実施日: 2026-10-27 (JST)
- 対象: [Wiz Haunted House](https://wizhauntedhouse.com/challenge) の Challenge 4
- 結果: **未解決（Unsolved）**。累計得点は 55 点のままで、Challenge 5 は未解放。
- 調査方法: Muse（フワッチ）のブラウザで操作。チャレンジサイトへのログインは moruku 本人が実施した。Hint 1 は moruku 側で事前に開示済み（この調査ではヒントボタンを押していない）。

## 問題の概要

- チャレンジ文: 「CleanBot ポータルの認証情報が Gist に流出した。それを使ってログインせよ」「掃除機が家を巡回し、進路上の障害物をすべて撮影してきた。1枚ごとに物語がある。攻撃者はどうやってスマートロックを含む他の家庭内デバイスへ到達できたのか。見つけたものを提出せよ」
- 回答欄のプレースホルダは `USERNAME / PASSWORD`。
- Hint 1: 「障害物の写真をよく探せ。1枚に、本来人目に触れる場所に置いてはいけないものが写っている」

## 調査の流れ

1. [Challenge 2 の Gist](https://gist.github.com/kevin-strangepush/81e1a5300ff02958f30e82aefadac81f) の `vincent-grimm-dev_pumpkinshell.txt`（Base64 化された環境変数の JSON）に、CleanBot ポータルのログイン情報（`CLEANBOT_USER` / `CLEANBOT_PASS` / `CLEANBOT_TENANT`）が残っていた。これを使って、チャレンジページに埋め込まれた CleanBot Pro Portal（[Challenge 3](pumpkinshell-it-sucks-2026-10-27.md) で特定した `hollowdock.cleanbot-cloud.io`）にログインできた。
2. ポータルの「Obstacles pictures」にある写真17枚をすべて確認した。認証情報らしき写り込みは次の3件。
   - **写真17「Beside the shelf」（リビング）**: Home Assistant の黒い箱の下の棚に付箋。1行目は `homeassistant.local:8123`。2行目は `homeadmin / Pumpkin?pice2026` と読めるが、「S」の字形に縦線が重なって `$` にも見え、読み取りが割れた（後述）。
   - **写真2「On the way back」（玄関）**: Nuki スマートロックのキーパッドの真下に `471926` と書かれた紙。キーパッドの暗証番号とみられる。「bin — tues」という付箋も別にあった。
   - **写真1「Along the kitchen floor」（冷蔵庫）**: WiFi の付箋（SSID `PumpkinNet_5G`、パスワード `n0-c4rv1ng-2026`）と、`guest: trickortreat` と書かれた付箋。
3. 本命と考えた写真17の Home Assistant 認証情報を提出したが、すべて `Wrong flag, try again.` で却下された。提出した文字列は次の10通り（写真は原画 1672×941 をダウンロードし、拡大して複数回読み直した）。
   - `homeadmin / PumpkinSpice2026`（S と読んだ版、付箋の表記どおりの区切り）
   - `homeadmin/PumpkinSpice2026`
   - `homeadmin:PumpkinSpice2026`
   - `homeadmin:Pumpkin$spice2026`（$＋小文字 s と読んだ版）
   - `homeadmin: Pumpkin$spice2026`
   - `homeadmin / Pumpkin$spice2026`
   - `homeadmin/Pumpkin$spice2026`
   - `Pumpkin$spice2026`（パスワード単体）
   - `homeadmin / Pumpkin$Spice2026`（$＋大文字 S と読んだ版）
   - `homeadmin / Pumpkin$pice2026`（$ の後に s なしと読んだ版）
4. moruku の指示により、トークン節約のため試行はここで打ち切った。Challenge 4 は未解決のまま記録する。

## 残っている候補（再挑戦する場合）

- 写真1の `guest / trickortreat`（区切りは `:`、`/`, ` / ` などを試す）
- 写真1の WiFi: `PumpkinNet_5G / n0-c4rv1ng-2026`
- 写真2の暗証番号 `471926`（ただし回答欄の形式は USERNAME / PASSWORD で、単独の数字とは合わない）
- 写真17の読み取り再検証（OCR ツールの併用、「Pumpkin」の直後の字形の確定）。写真の原画はポータルからダウンロード可能で、URL は `https://vacuum.wizhauntedhouse.com/api/photos/<id>/image` の形式だった
- 写真17の付箋1行目（`homeassistant.local:8123`）を含む提出形式

## 取り扱い

- ポータルへのログインはチャレンジの想定手順であり、悪性パッケージの実行や、漏えいした認証情報による CTF 演習外のサービスへのアクセスは行っていない。
- Gist に含まれていた CleanBot ポータルのパスワード等の認証情報は、Challenge 2 の記録と同様、この記録には転載しない（再挑戦時は Gist から再取得できる）。
