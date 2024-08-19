# get-book-info-from-isbn
ISBNを指定して本の情報を取得するPythonスクリプト。
出力はタブ区切りなので、ExcelやGoogleスプレッドシートにimportすることもできる。
必要ライブラリはrequirements.txtに記載しているので、以下のコマンドでインストールしてください。
```bash
# 一応、仮想環境を作成してインストールすることをおすすめします。
python3 -n venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## main.py
ISNBを指定して本の情報を取得する。
ただし、google book apiを利用しているので、google book apiの利用規約に従ってご利用ください。
### 使い方
まずは、google book apiのAPIキーを取得する必要がある。
[Google developers console](https://console.developers.google.com/)にアクセスして、プロジェクトを作成し、APIキーを取得する。
その後、`.env`ファイルにAPI_KEYに取得したAPIキーを設定する。
```.env
GOOGLE_BOOKS_API_KEY="your_api_key"
```
次に、ISBNを指定して実行する。
`test`ディレクトリにテスト用のISBNが書かれたファイルがあるので、それを利用すると良い。
一応説明しておくと、改行区切りで、ISBNが書かれたファイルを指定する。
```txt:ISBNs.txt
xxxxxxxxxx
yyyyyyyyyy
zzzzzzzzzz
```
それを用いて、
```python
python main.py test/ISBNs.txt > test/bookinfo.txt
```

## get-price.py
ISNBを指定して本の価格を取得する。
amazonにアクセスして価格を取得しているので、amazonの仕様変更により動作しなくなる可能性があります。
また、amazonの利用規約に違反する可能性があるので、**自己責任**でご利用ください。

1秒に1回のリクエストを送るようにして、amazonに負荷をかけないようにしています。
場合に応じて調整してください。

## 使い方
```python
python main.py test/ISBNs.txt > test/prices.txt
```
価格が書かれたファイルが出力されます。
```txt:prices.txt
ISBN: xxxxxxxxxx, 価格: ----円
ISBN: yyyyyyyyyy, 価格: ----円
ISBN: zzzzzzzzzz, 価格: ----円
総額: ----円
```


