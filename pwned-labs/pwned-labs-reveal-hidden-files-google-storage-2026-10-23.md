# Pwned Labs — Reveal Hidden Files in Google Storage（2026-10-23）

[元のラボ](https://app.pwnedlabs.io/labs/reveal-hidden-files-in-google-storage/18) ｜提出結果: 成功

## 確認した手順

1. ラボのウォークスルーにある Google Cloud Storage バケット `it-storage-bucket` を手掛かりに、`backup.7z` への匿名 HTTP HEAD リクエストを送った。`200 OK` と約 22 KB のサイズを確認した。
2. 公開アーカイブを取得し、ファイル名一覧から `flag.txt` と顧客データの CSV が含まれることを確認した。CSV は展開しなかった。
3. ラボのキャリアページの本文から単語を抽出し、大文字小文字を変えた候補を作成した。7-Zip の `t` コマンドで候補を順に検証し、アーカイブを開けるパスワードを特定した。
4. 7-Zip の標準出力に `flag.txt` だけを取り出し、得た値を提出した。

```sh
curl -I https://storage.googleapis.com/it-storage-bucket/backup.7z
curl -o backup.7z https://storage.googleapis.com/it-storage-bucket/backup.7z
7z l backup.7z
# キャリアページ由来の候補を 7z t -p'<候補>' backup.7z で検証
7z x -so -p'<見つけたパスワード>' backup.7z flag.txt
```

フラグ: `ea0aebbb6d68571f668e18c8fc03589d`

## 防御上の要点

公開サイトに使うバケットにバックアップを置き、オブジェクト名を知るだけで取得できたことが問題だった。アーカイブのパスワードもサイト本文から推測できた。公開コンテンツと非公開バックアップを分離し、非公開側のアクセス制御と強い暗号化を適用する。

アーカイブのパスワード、CSV に含まれる顧客情報、取得したファイル自体は公開しない。バケット全体の一覧取得や `ffuf` による網羅的な探索は今回実行していない。
