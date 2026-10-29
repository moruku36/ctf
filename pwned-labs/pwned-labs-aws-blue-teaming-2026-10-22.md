# Pwned Labs — AWS Blue Teaming（2026-10-22）

Pwned Labs の [AWS Blue Teaming](https://app.pwnedlabs.io/users/profile) で解いたラボの記録。検証に使った一時認証情報や、S3 オブジェクトに含まれていた認証情報は掲載しない。

## Breach in the Cloud

[ラボ](https://app.pwnedlabs.io/labs/breach-in-the-cloud/19) ｜提出結果: 成功

ラボのウォークスルーを手掛かりに、提供された一時 IAM ユーザーで実環境を確認した。IAM のインラインポリシーを読むと `sts:AssumeRole` で `AdminRole` を引き受けられた。ロール切替後に STS の呼び出し元を確認し、`emergency-data-recovery` バケットに `emergency.txt` があることを確認した。オブジェクト内のフラグだけを提出した。

```sh
aws iam get-user-policy --user-name temp-user --policy-name test-temp-user
aws sts assume-role --role-arn 'arn:aws:iam::<LAB_ACCOUNT_ID>:role/AdminRole' --role-session-name blue-team-review
# 一時ロールの認証情報をローカル環境変数へ設定
aws sts get-caller-identity
aws s3api list-objects-v2 --bucket emergency-data-recovery --query 'Contents[].Key'
aws s3 cp s3://emergency-data-recovery/emergency.txt -
```

フラグ: `3eb222cf55522f0f321f1ed5ed9a3663`

この検証で実行したのは IAM ポリシー、STS、S3 の確認。CloudTrail ログの独立した解析は行っていない。

## Secure S3 with Amazon Macie

[ラボ](https://app.pwnedlabs.io/labs/secure-s3-with-amazon-macie/19) ｜提出結果: 成功

ラボを起動し、提供された一時認証情報で AWS CLI に接続した。STS で `macie-user` として接続していることを確認してから、ロンドンリージョンの Macie バケット一覧を取得した。6 個のバケット名のうち、32 桁の小文字 16 進数という指定形式に一致したのは 1 件だった。そのバケット名を提出すると成功表示になった。

```sh
# ラボで配布された一時認証情報をローカル環境変数へ設定
aws sts get-caller-identity --query Arn --output text
aws macie2 describe-buckets --region eu-west-2 \
  --query 'buckets[].bucketName' --output text
```

フラグ（S3 バケット名）: `4f3fdf4cb5ef0f191ede2a2a00121475`

Macie のバケット一覧を読んで解いた。機密データのオブジェクト内容の取得、設定変更、公開アクセスの修正は行っていない。

## Identify IAM Breaches with CloudTrail and Athena

[ラボ](https://app.pwnedlabs.io/labs/identify-iam-breaches-with-cloudtrail-and-athena/19) ｜提出結果: 成功

ラボを起動し、提供された一時認証情報が `athena-user` のものと STS で確認した。既存の CloudTrail 用 Athena テーブルに対し、`ConsoleLogin` イベントの `useragent` が 32 桁の小文字 16 進数に一致する行を抽出した。クエリは成功し、`195.70.73.130` からの 1 件が返った。その `useragent` を提出すると成功表示になった。対象日を限定せずに検索したため、ラボで説明される 2023-08-30 以外のイベントも対象にできる。

```sql
SELECT DISTINCT sourceipaddress, useragent
FROM cloudtrail_logs_aws_cloudtrail_logs_104506445608_4e45885e
WHERE eventname = 'ConsoleLogin'
  AND regexp_like(useragent, '^[0-9a-f]{32}$');
```

```sh
# ラボで配布された一時認証情報をローカル環境変数へ設定
aws sts get-caller-identity --query Arn --output text
aws athena start-query-execution \
  --query-string "<上記のSQL>" \
  --result-configuration 'OutputLocation=s3://aws-athena-query-results-104506445608-us-east-1/Unsaved/'
aws athena get-query-execution --query-execution-id '<QUERY_EXECUTION_ID>'
aws athena get-query-results --query-execution-id '<QUERY_EXECUTION_ID>'
```

フラグ（`useragent`）: `0646679eca96f84016450fbb18d677d3`

この検証では既存テーブルへのクエリのみ実施した。CloudTrail や Athena テーブルの新規作成、IAM アカウントの封じ込めは行っていない。
