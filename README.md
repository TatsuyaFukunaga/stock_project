## 	&#9312;制作サイトのタイトル：
### StockApp

## &#9313;制作サイトの説明（40文字程度）：
### バックエンドをdjango、フロントエンドをreactを使って開発しました。フロントエンドのreactでは、株式の証券コードと、株価の表示期間をpostして、バックエンドのdjangoは、yhoo finance APIをたたいて、株価のデータをpandasデーターで引っ張ってきて、jsonで返すAPIサーバーとして動作しています。


## &#9314;工夫した点・こだわった点：
### 無料で株価の情報を引っ張ってこれるのが、pythonのAPIしかなかったので、バックエンドはdjangoを選びました。グラフはreact-chartJs-2を使いました。

## &#9315;難しかった点・次回トライしたこと（または機能）：
### reactのコードは基本typescriptを使っているけど、型エラーでドハマりした点と、APIサーバーからとってきたデーターの非同期処理がうまくいっていなく、hook機能が謎のエラーでデーターがnullになってしまい、悩んだこと。

## &#9316;備考（感想、シェアしたいこと等なんでも）：
### さくらサーバーでssh接続して、pythonの環境構築ができないか？調べたがpermissionが無く、何もできなかった。