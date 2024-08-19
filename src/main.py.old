import requests
from bs4 import BeautifulSoup
import time
import sys
import tqdm

def get_amazon_title_and_price(isbn):
    url = f"https://www.amazon.co.jp/dp/{isbn}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # タイトルを取得
    title = soup.find("span", {"id": "productTitle"})
    if title:
        title_text = title.text.strip()
    else:
        title_text = "タイトル情報が見つかりません"
    
    # 価格を取得
    price = soup.find("span", {"class": "a-price-whole"})
    if price:
        price_text = price.text.replace(",", "") + "円"
    else:
        price_text = "価格情報が見つかりません"

    return title_text, price_text

# sys.argv[1]にはISBNリストのファイルパスが入る
if len(sys.argv) != 2:
    print("ISBNリストのファイルパスを引数に指定してください")
    sys.exit(1)
isbn_file_path = sys.argv[1]
# ISBNリストをファイルから読み込む
with open(isbn_file_path, 'r') as file:
    isbn_list = file.read().splitlines()

# ISBNごとに価格を取得
total_price = 0
for isbn in tqdm.tqdm(isbn_list):
    title, price = get_amazon_title_and_price(isbn)
    print(f"ISBN: {isbn}, Title: {title}, 価格: {price}")
    if "円" in price:
        total_price += int(price.replace("円", ""))
    
    # 1リクエストごとに1秒待つ
    time.sleep(1)

print(f"総額: {total_price}円")

