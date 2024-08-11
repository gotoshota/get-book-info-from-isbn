# get-book-price-from-isbn
ISNBを指定して本の価格を取得する。
amazonにアクセスして価格を取得しているので、amazonの仕様変更により動作しなくなる可能性があります。
また、amazonの利用規約に違反する可能性があるので、自己責任でご利用ください。

いま、1秒に1回のリクエストを送るようにしているので、amazonに負荷をかけないようにしています。
場合に応じて調整してください。

## 使い方
```python
python main.py ISBNs.txt > prices.txt
```
改行区切りで、ISBNが書かれたファイルを指定してください。
```txt:ISBNs.txt
xxxxxxxxxx
yyyyyyyyyy
zzzzzzzzzz
```
価格が書かれたファイルが出力されます。
```txt:prices.txt
ISBN: xxxxxxxxxx, 価格: ----円
ISBN: yyyyyyyyyy, 価格: ----円
ISBN: zzzzzzzzzz, 価格: ----円
総額: ----円
```


