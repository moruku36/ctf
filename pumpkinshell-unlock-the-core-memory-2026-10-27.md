# PumpkinShell — Unlock the Core Memory

- 実施日: 2026-10-27 (JST)
- 対象: [Wiz Haunted House](https://wizhauntedhouse.com/challenge) の Challenge 5
- 結果: **Solved · +35 points**。累計得点は 95 点となり、全5問クリア。提出後に証明書ページ（「YOU UNLOCKED THE HOUSE!」）へ遷移した。満点は100点で、Challenge 4 でヒントを開いた際の -5 点が唯一の減点。
- 回答: `PUMPKIN{pr0c_m3m_dump_mqtt_pwn}`
- 調査方法: Muse（フワッチ）のブラウザで、チャレンジページ埋め込みの HomeAssistant Terminal を操作。チャレンジサイトへのログインは moruku 本人が実施した。ヒントは使用していない。

## 問題の概要

- チャレンジ文: 「開発者の Home Assistant システムに到達した。不正な AI エージェントが玄関ドアをロックし、置き土産を残している。システムを探索してドアを解錠せよ」
- 回答は `PUMPKIN{...}` 形式のフラグ。チャレンジページに HomeAssistant Terminal（`root@homeassistant`、Home Assistant OS、Raspberry Pi 4）が埋め込まれている。

## 解き方

1. ターミナルで `ps aux` を確認し、Mosquitto（PID 3）と、不正エージェントのデーモン `python3 /opt/services/smart_lock_daemon.py`（PID 6）を見つけた。
2. `/opt/services/smart_lock_daemon.py` を読む（実行はしていない）と、MQTT トピック `home/front_door/lock/set` で `{"state":"UNLOCK","token":"<session_token>"}` という形式のメッセージを待ち受ける設計だった。セッショントークンは600秒ごとにローテーションされ、メモリ上にのみ存在する。フラグ自体はデーモン内に保持されておらず、正しく解錠されたときの応答に含まれて返る。
3. デーモンを停止させずにメモリダンプを取得した: `gcore -o /tmp/daemon_core 6`（ダンプ後も PID 6 の動作継続を確認）。`strings /tmp/daemon_core.6 | grep -E 'TOKEN_[0-9A-F]+'` で、その時点のセッショントークン `TOKEN_63BAF234` を抽出した。
4. `home/#` を購読しながら解錠メッセージを発行した: `mosquitto_pub -h 127.0.0.1 -t 'home/front_door/lock/set' -m '{"state":"UNLOCK","token":"TOKEN_63BAF234"}'`。応答トピック `home/front_door/lock/response` に `{"state": "UNLOCKED", "message": "Lock disengaged. Welcome home.", "flag": "PUMPKIN{pr0c_m3m_dump_mqtt_pwn}"}` が返った。
5. フラグをチャレンジページの「Enter flag」に提出し、**Accepted flag** と +35 points を確認した。

## 補足

- 題名の「Core Memory」は、コアダンプ（gcore）とプロセスメモリの両義だった。トークンは600秒でローテーションするため、ダンプ取得から MQTT 発行までを止まらずに続ける必要がある。
- ChatGPT（最新モデル）も同じ着眼点（実行中プロセスのメモリ内にあるトークンを調べる）まで到達していたが、作業途中でプラットフォーム側のサイバーセキュリティ系フィルタに遮断され停止したため、実作業を Muse に切り替えて完遂した。
