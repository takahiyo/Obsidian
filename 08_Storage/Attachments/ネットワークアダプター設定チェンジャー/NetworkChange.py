import sys
import os
import ctypes
import wmi
import tkinter as tk
from tkinter import simpledialog, messagebox

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_all_network_adapters():
    c = wmi.WMI()
    adapters = []
    for nic in c.Win32_NetworkAdapter():
        if nic.NetConnectionID:
            adapters.append({'Name': nic.NetConnectionID, 'Index': nic.InterfaceIndex})
    return adapters

def set_dhcp(adapter_index):
    c = wmi.WMI()
    nic_configs = c.Win32_NetworkAdapterConfiguration(InterfaceIndex=adapter_index)
    for nic in nic_configs:
        return_value = nic.EnableDHCP()
        if return_value[0] == 0 or return_value[0] == 1:
            messagebox.showinfo("結果", f"{nic.Description} の DHCP 設定が完了しました。")
        else:
            messagebox.showerror("エラー", f"DHCP の設定に失敗しました。エラーコード: {return_value[0]}")

        return_value = nic.SetDNSServerSearchOrder()
        if return_value[0] == 0 or return_value[0] == 1:
            messagebox.showinfo("結果", "DNS サーバー設定をリセットしました。")
        else:
            messagebox.showerror("エラー", f"DNS サーバー設定のリセットに失敗しました。エラーコード: {return_value[0]}")

def set_static_ip(adapter_index, ip_list):
    c = wmi.WMI()
    nic_configs = c.Win32_NetworkAdapterConfiguration(InterfaceIndex=adapter_index)
    for nic in nic_configs:
        nic.EnableDHCP()
        nic.SetDNSServerSearchOrder()

        ip_addresses = [ip_info['ip'] for ip_info in ip_list]
        subnet_masks = [ip_info['mask'] for ip_info in ip_list]

        return_value = nic.EnableStatic(IPAddress=ip_addresses, SubnetMask=subnet_masks)
        if return_value[0] == 0 or return_value[0] == 1:
            messagebox.showinfo("結果", f"{nic.Description} に固定 IP アドレスを設定しました。")
        else:
            messagebox.showerror("エラー", f"IP アドレスの設定に失敗しました。エラーコード: {return_value[0]}")

def main_cui():
    adapters = get_all_network_adapters()
    if not adapters:
        print("ネットワークアダプターが見つかりませんでした。")
        sys.exit(1)

    print("ネットワークアダプターの一覧：")
    for idx, adapter in enumerate(adapters):
        print(f"{idx}: {adapter['Name']}")

    choice = input("設定するネットワークアダプターの番号を入力してください: ")
    try:
        choice = int(choice)
        if choice < 0 or choice >= len(adapters):
            raise ValueError
    except ValueError:
        print("無効な選択です。")
        sys.exit(1)

    adapter_index = adapters[choice]['Index']

    print("\n1: 固定IPアドレスを設定する")
    print("2: DHCPに戻す")
    action = input("操作を選択してください（1または2）: ")

    if action == '1':
        ip_list = [
            {'ip': '10.0.0.234', 'mask': '255.255.0.0'},
            {'ip': '192.168.0.234', 'mask': '255.255.255.0'},
            {'ip': '192.168.1.234', 'mask': '255.255.255.0'},
            {'ip': '192.168.2.234', 'mask': '255.255.255.0'},
            {'ip': '192.168.10.234', 'mask': '255.255.255.0'},
            {'ip': '192.168.11.234', 'mask': '255.255.255.0'},
            {'ip': '192.168.24.234', 'mask': '255.255.255.0'},
            {'ip': '192.168.100.234', 'mask': '255.255.255.0'},
            {'ip': '169.254.0.234', 'mask': '255.255.255.248'}
        ]
        set_static_ip(adapter_index, ip_list)
    elif action == '2':
        set_dhcp(adapter_index)
    else:
        print("無効な選択です。")
        sys.exit(1)

def main_gui():
    root = tk.Tk()
    root.withdraw()

    adapters = get_all_network_adapters()
    if not adapters:
        messagebox.showerror("エラー", "ネットワークアダプターが見つかりませんでした。")
        sys.exit(1)

    adapter_names = "\n".join([f"{idx}: {adapter['Name']}" for idx, adapter in enumerate(adapters)])
    choice = simpledialog.askinteger("ネットワークアダプター選択", f"ネットワークアダプターの一覧：\n{adapter_names}\n設定するネットワークアダプターの番号を入力してください:")

    if choice is None or choice < 0 or choice >= len(adapters):
        messagebox.showerror("エラー", "無効な選択です。")
        sys.exit(1)

    adapter_index = adapters[choice]['Index']

    action = simpledialog.askinteger("操作選択", "1: 固定IPアドレスを設定する\n2: DHCPに戻す\n操作を選択してください（1または2）:")

    if action == 1:
        ip_list = [
            {'ip': '10.0.0.234', 'mask': '255.255.0.0'},
            {'ip': '192.168.0.234', 'mask': '255.255.255.0'},
            {'ip': '192.168.1.234', 'mask': '255.255.255.0'},
            {'ip': '192.168.2.234', 'mask': '255.255.255.0'},
            {'ip': '192.168.10.234', 'mask': '255.255.255.0'},
            {'ip': '192.168.11.234', 'mask': '255.255.255.0'},
            {'ip': '192.168.24.234', 'mask': '255.255.255.0'},
            {'ip': '192.168.100.234', 'mask': '255.255.255.0'},
            {'ip': '169.254.0.234', 'mask': '255.255.255.248'}
        ]
        set_static_ip(adapter_index, ip_list)
    elif action == 2:
        set_dhcp(adapter_index)
    else:
        messagebox.showerror("エラー", "無効な選択です。")
        sys.exit(1)

if __name__ == "__main__":
    if not is_admin():
        messagebox.showerror("エラー", "このスクリプトを管理者として実行してください。")
        sys.exit(1)

    # EXE として実行されている場合、自動的に GUI モードにする
    if getattr(sys, 'frozen', False):
        main_gui()
    elif len(sys.argv) > 1 and sys.argv[1] == "--gui":
        main_gui()
    else:
        main_cui()
