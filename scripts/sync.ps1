# PowerShell Backup Script for Obsidian Vault
# C:\Local_Storage\Obsidian_Vault の最新ファイルを Gitリポジトリへ同期（削除反映含む）して Push します。

$ErrorActionPreference = "Stop"
$VaultPath = Split-Path -Path $PSScriptRoot -Parent
$SourcePath = "C:\Local_Storage\Obsidian_Vault"

Set-Location -Path $VaultPath

Write-Host "=== Starting Obsidian Vault Sync & Backup ===" -ForegroundColor Cyan

# 1. Local_Storage からリポジトリディレクトリへのミラーリング同期
if (Test-Path -Path $SourcePath) {
    Write-Host "Syncing and mirroring files from $SourcePath..." -ForegroundColor Yellow
    robocopy $SourcePath $VaultPath /MIR /XD .git .obsidian/plugins/remotely-save .opencode /XF sync.ps1 | Out-Null
}

# 2. 全変更のステージング
Write-Host "Staging all updated files..." -ForegroundColor Cyan
git add -A

# 3. ステージングされた変更があるか確認
$hasStagedChanges = (git status --porcelain)
if (-not $hasStagedChanges) {
    Write-Host "No changes detected. Local vault is up-to-date with GitHub." -ForegroundColor Green
    exit 0
}

Write-Host "Detected changes:" -ForegroundColor Yellow
git status --short

# 4. コミット & プッシュ
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$commitMessage = "Sync and backup vault: $timestamp"
Write-Host "Creating commit: $commitMessage" -ForegroundColor Cyan
git commit -m $commitMessage

Write-Host "Pushing to GitHub (origin/main)..." -ForegroundColor Cyan
git push origin main

Write-Host "=== Backup completed successfully! ===" -ForegroundColor Green
