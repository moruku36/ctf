# XSS Playground by zseano — 調査記録（継続中）

2026-11-02 にHacker101 CTFのXSS Playgroundを開始した。フラグはまだ取得・提出していない。インスタンス固有のホスト、フラグ、Cookieは公開しない。

## 確認したこと

- 初期の案内には、反射型XSS 5件、保存型XSS 3件、DOM型XSS 2件、CSP回避 1件、何かを漏らすXSS 1件と表示された。
- プロフィール画面にはフィードバック、コメント、ユーザー報告の操作があり、メールは `Error 403 : You are not allowed to view emails.` として隠れていた。
- ページは `/feedback.js`、`/custom.js`、`/helper.php?v=1.0.0` を読み込んでいた。ページ内スクリプトには `tracking.searchterm` と `tracking.redirectUrl` の利用が見えた。
- `/custom.js` をBraveの画面操作で直接開いたところ、`net::ERR_BLOCKED_BY_CLIENT` で遮断された。別の取得経路への切り替えはしていない。

## 再開時の手順

本人がBraveまたはChromeで `/custom.js` を手動で開ける場合、そのタブに表示された内容を確認し、メール表示の保護処理を調べる。操作・応答をこの演習インスタンスで検証してから、フラグをHacker101 CTFに提出する。

現状: **0/1、継続中**。