# X API AI Automation Sample

AI自動化のためのX API (v2) サンプルスクリプトです。

## 概要
- 公式 Python XDK を使用
- 最近の投稿を検索し、AIで要約を生成（プレースホルダー）

## セットアップ
1. X Developer Portal でアプリを作成: https://console.x.com
2. Bearer Token を取得（検索用）
3. 環境変数を設定:
   ```bash
   export BEARER_TOKEN='your_bearer_token_here'
   ```
4. 依存関係をインストール:
   ```bash
   pip install xdk
   ```
5. 実行:
   ```bash
   python ai_automation_example.py
   ```

## 注意事項
- Xのオートメーションルールを遵守してください（公式API使用、スパム禁止）
- 投稿には OAuth 2.0 PKCE が必要です
- 詳細: https://docs.x.com/tools/ai

このサンプルは確認用です。必要に応じて拡張してください。
