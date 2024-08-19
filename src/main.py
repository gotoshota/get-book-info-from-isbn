import requests
import sys
import time
import tqdm

def get_google_books_info(isbn, api_key):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if "items" in data:
        volume_info = data["items"][0]["volumeInfo"]
        title = volume_info.get("title", "タイトル情報が見つかりません")
        authors = ", ".join(volume_info.get("authors", ["著者情報が見つかりません"]))
        
        # 価格情報の取得
        price = "価格情報が見つかりません"
        sale_info = data["items"][0].get("saleInfo", {})
        if sale_info.get("listPrice"):
            price = f"{sale_info['listPrice']['amount']} {sale_info['listPrice']['currencyCode']}"
        
        return title, authors, price
    else:
        return "情報が見つかりません", "", ""

# sys.argv[1]にはISBNリストのファイルパスが入り、sys.argv[2]にはGoogle Books APIキーが入る
if len(sys.argv) != 2:
    print("ISBNリストのファイルパスを引数に指定してください")
    sys.exit(1)

isbn_file_path = sys.argv[1]
api_key = "AIzaSyD4iMBw2FnjCQ-yHKsqC6mNzmiQ8M78-dk"

# ISBNリストをファイルから読み込む
with open(isbn_file_path, 'r') as file:
    isbn_list = file.read().splitlines()

# ISBNごとにタイトルと価格を取得
total_price = 0
for isbn in tqdm.tqdm(isbn_list):
    title, authors, price = get_google_books_info(isbn, api_key)
    print(f"ISBN: {isbn}, Title: {title}, Authors: {authors}, 価格: {price}")
    if "円" in price:
        total_price += int(price.replace("円", "").replace(" ", ""))  # 価格の合計を計算
    
    # 1リクエストごとに1秒待つ
    #time.sleep(1)

print(f"総額: {total_price}円")

