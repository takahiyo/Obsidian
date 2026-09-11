---
notion-id: d0673ab18c554766a4fbf07c0ef7bb52
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - 知識
---
PowerShellの管理者権限で下記コードを実行する

```jsx
([WMI]'').ConvertToDateTime((Get-WmiObject Win32_OperatingSystem).InstallDate)
```