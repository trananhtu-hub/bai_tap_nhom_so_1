import requests
from bs4 import BeautifulSoup
import pandas as pd
import time # Thư viện để tạm dừng
# --- 1. Khai báo thông tin ---
URL = "https://homedy.com/ban-nha-dat"
# Giả lập là một trình duyệt để tránh bị chặn
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# --- 2. Gửi yêu cầu và lấy nội dung HTML ---
# --- 2. Gửi yêu cầu và lấy nội dung HTML ---
try:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status() # Báo lỗi nếu request không thành công
except requests.exceptions.RequestException as e:
    print(f"Lỗi khi gửi yêu cầu: {e}")
    exit()

# --- 3. Phân tích HTML ---
soup = BeautifulSoup(response.content, 'html.parser')
# --- 4. Tìm tất cả các tin đăng ---
# *** BẠN PHẢI THAY THẾ 'class_cua_the_cha_chua_tin_dang' ***
# Ví dụ: soup.find_all('div', class_='re__product-item')
list_items = soup.find_all('div', class_='product-content')
print(list_items)