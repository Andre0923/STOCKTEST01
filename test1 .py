# 导入所需的套件
import requests  # 请求工具
from bs4 import BeautifulSoup  # 解析工具
import time  # 用来暂停程序

# 要爬取的股票列表
stock = ["1101", "2330", "2317"]

# Telegram Bot Token（请替换为您的实际Token）
token = "7916476342:AAHWpntwZiTkojAWOA_804_OomCodEl9MbI"

# 使用者ID（请替换为您的实际Chat ID）
chat_id = "7729879668"

# 添加请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

for stockid in stock:
    # 构建包含股票编号的URL
    url = f"https://tw.stock.yahoo.com/quote/{stockid}.TW"

    try:
        # 发送请求
        r = requests.get(url, headers=headers)
        r.raise_for_status()  # 检查请求是否成功

        # 解析返回的HTML
        soup = BeautifulSoup(r.text, 'html.parser')

        # 定位股价
        price_span = soup.find('span', class_='Fz(32px)')
        if price_span:
            price = price_span.get_text()
        else:
            print(f"无法找到股票 {stockid} 的价格")
            continue  # 跳过当前循环，继续下一个股票

        # 回报的讯息（可自订）
        message = f"股票 {stockid} 即时股价为 {price}"

        # Bot发送讯息
        telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.get(telegram_url, params=params)
        response.raise_for_status()  # 检查请求是否成功

        print(f"已发送股票 {stockid} 的价格：{price}")

    except requests.exceptions.RequestException as e:
        print(f"请求股票 {stockid} 数据时发生错误：{e}")
    except Exception as e:
        print(f"处理股票 {stockid} 时发生未知错误：{e}")

    # 每次暂停3秒
    time.sleep(3)
