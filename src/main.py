import requests
from dotenv import load_dotenv
import os
import sys
import tqdm

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数からAPIキーを取得
google_books_api_key = os.getenv("GOOGLE_BOOKS_API_KEY")

def get_google_books_info(isbn, api_key):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if "items" in data:
        volume_info = data["items"][0]["volumeInfo"]
        title = volume_info.get("title", "タイトル情報が見つかりません")
        authors = ", ".join(volume_info.get("authors", ["著者情報が見つかりません"]))
        
        return title, authors
    else:
        return "情報が見つかりません", "", ""

def main():
    # コマンドライン引数からファイルパスを取得
    if len(sys.argv) != 2:
        print("ISBNリストを含むファイルのパスを引数として渡してください")
        sys.exit(1)

    isbn_file_path = sys.argv[1]

    # ISBNリストをファイルから読み込む
    try:
        with open(isbn_file_path, 'r') as file:
            isbn_list = file.read().splitlines()
    except FileNotFoundError:
        print(f"ファイル {isbn_file_path} が見つかりませんでした")
        sys.exit(1)

    # ISBNごとにタイトルなどを取得
    print(f"ISBN\tタイトル\t著者")
    for isbn in tqdm.tqdm(isbn_list):
        title, authors = get_google_books_info(isbn.strip(), google_books_api_key)
        # tab 区切りで出力
        print(f"{isbn}\t{title}\t{authors}")


if __name__ == "__main__":
    main()
