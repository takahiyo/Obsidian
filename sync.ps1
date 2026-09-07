# PowerShell Backup Script for Obsidian Vault
$ErrorActionPreference = "Stop"
$VaultPath = $PSScriptRoot

Set-Location -Path $VaultPath

Write-Host "=== Starting Obsidian Vault Backup ===" -ForegroundColor Cyan

$status = git status --porcelain
if ([string]::IsNullOrWhiteSpace($status)) {
    Write-Host "No changes detected. Local vault is up-to-date with GitHub." -ForegroundColor Green
    exit 0
}

Write-Host "Detected changes:" -ForegroundColor Yellow
git status --short

Write-Host "Staging changes..." -ForegroundColor Cyan
git add -A

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$commitMessage = "Backup vault: $timestamp"
Write-Host "Creating commit: $commitMessage" -ForegroundColor Cyan
git commit -m $commitMessage

Write-Host "Pushing to GitHub (origin/main)..." -ForegroundColor Cyan
git push origin main

Write-Host "=== Backup completed successfully! ===" -ForegroundColor Green
