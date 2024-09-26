# 导入所需的套件
import requests  # 请求工具
from bs4 import BeautifulSoup  # 解析工具
import time  # 用来暂停程序

# 要爬取的股票列表
stock = ["1101", "2330", "2317"]

for i in range(len(stock)):  # 迴圈依序爬取股价
    # 现在处理的股票
    stockid = stock[i]

    # 构建包含股票编号的URL
    url = "https://tw.stock.yahoo.com/quote/" + stockid + ".TW"

    # 发送请求
    r = requests.get(url)

    # 解析返回的HTML
    soup = BeautifulSoup(r.text, 'html.parser')

    # 定位股价
    price = soup.find('span', class_=[
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"
    ]).getText()

    # 回报的讯息（可自订）
    message = "股票 " + stockid + " 即时股价为 " + price

    # 用 Telegram Bot 回报股价

    # Bot Token（请替换为您的实际Token）
    token = "7916476342:AAHWpntwZiTkojAWOA_804_OomCodEl9MbI"

    # 使用者ID（请替换为您的实际Chat ID）
    chat_id = "7729879668"

    # Bot发送讯息
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

    # 每次暂停3秒
    time.sleep(3)
