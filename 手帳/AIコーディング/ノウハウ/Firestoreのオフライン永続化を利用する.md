---
notion-id: 2ec37ce6287180f980f7e9bc1f085e4c
テキスト: "Firestoreのオフライン永続化（js/config.js）Firestore SDKの標準機能を有効化することで、一度取得したデータをブラウザのローカルストレージ（IndexedDB）に保存しています。• 実装箇所: js/config.js 内の initFirebase 関数• コード:JavaScript// ★追加: オフライン永続化（キャッシュ）を有効にするfirebase.firestore().enablePersistence({ synchronizeTabs: true })• 効果:    ◦ コスト削減: 再読み込み時、サーバーに変更がなければローカルのキャッシュデータを使用するため、Firestoreの「読み取り回数（課金対象）」を節約できます。    ◦ オフライン動作: ネットワークが切断されても、キャッシュされたデータを元にアプリを閲覧・操作できます。    ◦ タブ間同期: synchronizeTabs: true により、複数のタブでアプリを開いていても、あるタブでの変更が即座に他のタブ（のキャッシュ）にも反映されます。"
選択:
  - Firestore
---
