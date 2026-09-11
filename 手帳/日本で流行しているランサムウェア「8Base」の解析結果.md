---
notion-id: 415be44d91d14703b89915d23fbb2e40
URL: https://techblog.lycorp.co.jp/ja/20241209a
更新されました: Invalid date
作成日時: Invalid date
タグ:
  - セキュリティ
  - 知識
  - 記事
---
[![](https://techblog.lycorp.co.jp/static/39f5be4bf6323c9ac87d6d7212d0111e/7d66e/4d11fdd17ed74d21a87a8806cbaa6554.png)](https://techblog.lycorp.co.jp/static/39f5be4bf6323c9ac87d6d7212d0111e/7d66e/4d11fdd17ed74d21a87a8806cbaa6554.png)

==[LINEヤフー Advent Calendar 2024](https://qiita.com/advent-calendar/2024/lycorp_jp)の記事です。==

==こんにちは。CISO管掌の脅威情報分析対応チームでセキュリティエンジニアとして活動している首浦です。==  
==本記事ではランサムウェアについての解説に加え、8Baseの解析結果を紹介します。==

## ==ランサムウェアとは==

==まず初めにランサムウェアとは、感染端末から内部システムのデータを暗号化・窃取することでそのデータやコンピュータを「人質」として、身代金などを要求するマルウェアの一種です。==

==暗号化前のファイルは完全に端末から削除され、感染端末外部（USBメモリやクラウドストレージ等）にバックアップが存在しない場合、ファイルを復元するためには、暗号化されたファイルを復号する必要があります。==  
==ランサムウェアを用いる攻撃者はこの復号に必要な鍵と引き換えに金銭などを要求します。ただし、身代金を支払った場合においても復号鍵の引き渡しを拒否する場合や、復号鍵での復号が失敗する場合があり、必ずしも身代金を支払えば解決するわけではありません。==  
==また、近年ではランサムウェアを用いる攻撃者はファイル暗号化にとどまらず、内部のデータを窃取し「身代金を支払わなければデータを世に公開する」などと脅す、「二重脅迫」と呼ばれる手法を広く使用します。==

==ランサムウェアにはたくさんの種類・グループが存在していますが、本記事ではその中でも2024年において日本国内で被害事例の多い「8Base」ランサムウェアについて解析を行います。==

## ==8Baseの解析==

==8Baseの解析結果はさまざまなセキュリティベンダーにより公開されています。今回は解析の取っ掛かりとして[Cisco Talosの記事](https://blog.talosintelligence.com/deep-dive-into-phobos-ransomware/)を参考にさせていただきました。今回解析した検体のハッシュ値（SHA-256）は`58626a9bfb48cd30acd0d95debcaefd188ae794e1e0072c5bde8adae9bccafa6`です。なお8BaseはLoader/Dropperなど別の攻撃段階を通じて感染しますが、本記事での解析は8Base本体にとどめています。==

==まずは、Cisco Talosの記事と同様に内部コンフィグデータの復元に取り組みました。この復元のため、検体内部の暗号化されたコンフィグデータを特定し、復号関数を確認、各エントリに基づきコンフィグデータを動的解析で復号し取得しました。==  
==取得した中でも注目すべき復元データを以下に示します。==

- ==MAL_EMBEDDED_RSA_KEY: BD C1 49 1A 73 2E FA 44 D4 3D D1 92 15 D8 EC 5D 0D DB 95 0C 33 68 C0 A0 06 E9 0C 24 44 88 1B 12==
- ==MAL_RANSOM_FILE_EXTENSION: .id[<>-3398].[helprequest@techmail.info].Elbie==
- ==MAL_DEBUG_FILE_NAME: config==

==MAL_EMBEDDED_RSA_KEYは2019年から変わらず観測されている、ファイル暗号化に用いられるkeyを暗号化するための鍵になります。MAL_RANSOM_FILE_EXTENSIONは暗号化後のファイル拡張子です。<>の部分は別関数にてIDが作成されます。これは感染端末のIDになります。MAL_DEBUG_FILE_NAMEは8Baseが実行されている間のデバッグが書き込まれるファイルです。動的解析中に作成されていることを確認しました。==

==ここまではCisco Talosが先述の記事で解説されていることをなぞってきただけなのですが、当該記事では深く触れられていない復号・暗号化関数について説明します。==

==まず、8Baseでは復号・暗号関数にAESが用いられています。解析を困難にするためや検出避けを行うためかWindows APIは使用されず、全てハードコードで実装されています。以下に復号・暗号化関数の実装について、デコンパイルした結果を示します。なお、デコンパイル結果ですので全てが忠実に再現されているわけではないことに留意してください。==

```
bool AES_Decrypt(void *this, int *AES_obj, int *input, int *output){
    int iVar1;
    iVar1 = AES_main(this, AES_obj, 0, input, output)
    ...
}
bool AES_Encrypt(void *this, int *AES_obj, int *input, int *output){
    int iVar1;
    iVar1 = AES_main(this, AES_obj, 1, input, output)
    ...
}
```

==Plain text==

==Copy==

```
int AES_main(void *this, int *AES_obj, int switcher, int *input, int *output){
    ...
    if (switcher == 0) {
        # Decryptの操作
    }
    else {
        # Encryptの操作
    }
    ...
}
```

==Plain text==

==Copy==

==AES_Decrypt関数、AES_Encrypt関数はそれぞれ内部コンフィグデータの復元、ファイル暗号化スレッドで呼び出されますが、これらの関数内部では復号・暗号化処理は行われず、実際にはそれぞれが復号処理か暗号化処理かを決めるswitcherとなるflagを引数に付加し、AES_main関数を呼び出すものになっています。復号・暗号化関数本体はAES_main関数で記述されており、switcherの値に従ってそれぞれの操作を行います。==

==また、本記事に関数は掲載していませんがAES_init関数でもAES_main関数のように条件ごとの処理が記述されています。復号の場合は内部に格納されたAES_keyを利用する操作、ファイル暗号化の場合はランダム生成されたkeyとIVを利用する操作があります。さらに、8Baseにはファイル暗号化で使用したkeyを暗号化する機能を有しており、この場合にはAESではなくRSAを使用します。RSA Keyは内部コンフィグデータに含まれています。==

==次にファイル暗号化フローに着目します。==  
==一般に、ランサムウェアは被害者の環境で大量のファイルを暗号化するので、それらの全てを暗号化するにはかなりの時間を要します。そのため、ランサムウェアの多くはファイル暗号化の高速化手法を採用しています。8Baseにおいても高速化手法が実装されています。==  
==8Baseはサイズの大きなファイルとそうでないファイルに対し、異なる暗号化処理を行います。==

```
int FUN_00408ebe(...){
    ...
    local_1c = lpFileSize.s.LowPart;
    local_18 = lpFileSize.s.HighPart;
    ...
    if (((param_4 & 1) == 0 && ((local_18 != 0 || 0x17ffff < local_1c)))) {
        local_8 = LargeFileEnc(param_2, lpExistingFileName, lpFileName, param_4);
    }
    else {
        local_8 = FileEnc(param_2, lpExistingFileName, lpFileName, param_4)
    }
    ...
}
```

==Plain text==

==Copy==

==上記のコード内の条件分岐で用いられる値はファイルサイズですので、計算すると約1.5MBでふるいにかけられていることが分かります。ファイルが大きいと判断された場合、暗号化処理が異なる点は2つです。==

1. ==ファイル全体を暗号化しない（一部のみ暗号化）==
2. ==暗号化後ファイル末尾に、ファイル暗号化で用いたIVとRSAで暗号化されたkeyが付与されない==

==以下に、大きいファイルの暗号化関数を示します。==

```
int LargeFileEnc(int *param1, LPCWSTR lpExistingFileName, LPCWSTR lpFileName, byte param4){
    ...
    uVar6 = read_file_chunk(hNewFile, (int)(puVar1 + 8), local_18);
    ...
    caller_init()
    AES_Encrypt()
    WriteFile()
    ...
}
```

==Plain text==

==Copy==

==LargeFileEnc関数で呼び出されるread_file_chunk関数の中身は次のようになっています。==

```
uint read_file_chunk(HANDLE param1, int param_2, LPVOID param3){
    ...
    chunk_count = 0;
    while(true){
        if (chunk_count == 2){
            ...
        }
        ...
        bVar3 = ReadFile(param_1, param_3, 0x40000, local_c, 0);
        ...
        param_3 = param_3 + 0x40000;
        chunk_count++;
        if (2 < chunk_count) break;
    }
    ...
}
```

==Plain text==

==Copy==

==0x40000を一つのチャンクとして、3つのチャンクを読み取って元の関数に返します。つまり、大きいと判断されたファイルでは0x120000（約1MB）のみ暗号化されます。==

==参考に大きいと判断されない通常のファイル暗号化関数を記載します。この場合は、ファイル全体を暗号化します。また、暗号化後のファイル末尾には暗号化で利用したkey（RSAで暗号化済み）とIVが付与されます。==

```
int FileEnc(int *param1, LPCWSTR lpExistingFileName, LPCWSTR lpFileName, byte param4){
    ...
    CreateFileW() # ファイル暗号化拡張子がついたファイルを作成
    caller_init()
    ReadFile() # 元のファイルのデータを読み込み
    AES_Encrypt()
    WriteFile() # 暗号化したデータを書き込み
    caller_init()
    AES_Encrypt()
    WriteFile() # ((00 * 20byte) + IV + (00 * 3byte) + Encrypted key)
    ...
}
```

==Plain text==

==Copy==

## ==おわりに==

==本検体の解析環境はこちらです。==

- ==仮想環境: VirtualBox上のWindows==
- ==デコンパイラ: Ghidra==
- ==デバッガ: x64dbg==

==本記事では8Baseの解析結果の一部を紹介しました。==  
==これをお読みの皆様がご自身でマルウェアを解析したい場合は、仮想環境などで適切な解析環境を構築した上で行ってください。普段、個人や業務で利用している端末に直接マルウェアをダウンロードした場合、端末がマルウェア感染して被害にあう可能性があります。くれぐれも、自身の端末で実行されることはないようにお願いします。==

==私たちのチームでは、LINEヤフーのサービスやユーザの皆様を脅威から守るために、日々脅威インテリジェンスに関する取り組みを行っており、今回のランサムウェアの解析はその一部です。==  
==最後までお読みいただきありがとうございました。==