# The Cloud Hunting Games — ExfilCola (全5問)

- 実施日: 2026-10-18
- 結果: 全問クリア、40点（ヒントによる減点なし）
- 証書名義: Kentaro Mori
- [チャレンジ](https://www.cloudhuntinggames.com/challenge) / [発行された証書](https://www.cloudhuntinggames.com/certificate/exfilcola/a2d4ee2a-f091-445b-b24b-21e392a75d6e)
- [証書画像](cloud-hunting-games-certificate.png)

## 攻撃の流れ

S3 のレシピ取得を起点に、`S3Reader` ロールを引き受けた IAM ユーザー、Lambda コードを更新した EC2 インスタンス、SSH の侵入元、PostgreSQL 上の cron による永続化を順に追った。最後に演習環境内の攻撃者 API に対して、奪われたファイルを削除した。

## 1. Ain't no data when she's gone

`s3_data_events` で `soda-vault` の `GetObject` を調査した。通常のアクセスに比べて、2025-05-05 12:47 頃に `37.19.199.135` / Boto3 から連続してレシピを取得したセッションが異常だった。約20件、合計約51 MB。呼び出し元 ARN をフラグとして提出し、受理された。

```sql
SELECT *
FROM s3_data_events
WHERE requestParameters LIKE '%soda-vault%'
  AND EventName = 'GetObject';
```

**解答:** `arn:aws:sts::509843726190:assumed-role/S3Reader/drinks`

## 2. Follow, follow the trail

`cloudtrail` の `AssumeRole` を調べると、2025-05-05 12:43:21Z に `Moe.Jito` が `S3Reader` を `drinks` セッション名で引き受けていた。送信元は `109.236.81.188`。第1問のロールセッションを IAM ユーザーまで遡った。

```sql
SELECT * FROM cloudtrail WHERE EventName = 'AssumeRole';
```

**解答:** `Moe.Jito`

## 3. Deeper into the trail

CloudTrail の Lambda 関連イベントから、12:28:23 の `ListFunctions20150331` と 12:32:42 の `UpdateFunctionCode20150331v2` を確認した。`credsrotator` のコードを更新した主体は `lambdaWorker` ロールを持つ EC2 インスタンスで、送信元は `54.227.18.169`。直後に同 Lambda が `IAMAccessKeys` に対して `PutSecretValue` を繰り返しており、資格情報の操作へつながっていた。

```sql
SELECT * FROM cloudtrail WHERE EventName LIKE 'UpdateFunctionCode%';
```

**解答:** `i-0a44002eec2f16c25`

## 4. Ain't no mountain high enough to keep me away from my logs

`ssh-fetcher` 上で `/var/log` は空に見え、隠しファイル `.gK8du9` に攻撃者の落書きが残っていた。`findmnt` で `/var/log` への重ねたマウントを確認し、ひとつアンマウントすると元の `auth.log` が現れた。SSH の成功ログを集計すると、`102.54.197.238` からの接続が2,000件あった。

```sh
findmnt /var/log
umount /var/log
grep 'Accepted' /var/log/auth.log |
  awk '{for(i=1;i<=NF;i++) if ($i=="from") print $(i+1)}' |
  sort | uniq -c
```

**解答:** `102.54.197.238`

## 5. Now you're just somebody that I used to log

PostgreSQL サービスで root の `crontab -l` は空だったが、`/var/spool/cron/crontabs/postgres` に毎日0時実行のジョブがあった。ジョブは `/var/lib/postgresql/data/pg_sched` を実行する。スクリプトは Base64 化された Bash で、攻撃者の HTTP API への接続情報が含まれていた。

この環境のブラウザー端末では長い復号パイプラインが応答しなかったため、[公開解説](https://medium.com/@aniketsp0/the-cloud-hunting-games-ctf-exfilcola-66424c40e3b1)で API のアドレスと認証情報を照合した。認証情報はレポジトリに転載しない。演習環境の `GET /` で API の操作一覧を、認証付き `GET /files` で `ExfilCola-Top-Secret.txt` の存在を確認した。ユーザーの確認を得てから、同ファイルに認証付き `DELETE /files/ExfilCola-Top-Secret.txt` を送信した。端末は削除成功とフラグを返し、サイトへのフラグ提出も受理された。

```sh
cat /var/spool/cron/crontabs/postgres
cat /var/lib/postgresql/data/pg_sched
curl -u 'USER:PASS' http://34.118.239.100/files
curl -X DELETE -u 'USER:PASS' \
  http://34.118.239.100/files/ExfilCola-Top-Secret.txt
```

**フラグ:** `{I know it when I see it}`

## 検証

5問すべてサイトが受理し、最終スコアは40点。証書発行ページで `Kentaro Mori` を入力し、表示された PNG の元画像を保存した。証書の印字日付「MAY 2025」はサイト側のデザイン表記であり、実施日は上記のとおり。

## 参考

- [Wiz: The Cloud Hunting Games](https://www.cloudhuntinggames.com/challenge)
- [Aniket Pattanshetti による解説](https://medium.com/@aniketsp0/the-cloud-hunting-games-ctf-exfilcola-66424c40e3b1) — 第5問の API 接続情報の照合に使用
- [r/netsec の第4問のヒント](https://www.reddit.com/r/netsec/comments/1kgcq32) — `/var/log` のマウントを調べる手がかり
