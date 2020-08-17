# -*- coding:utf-8 -*-

from fake_useragent import UserAgent
import random

API = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=cavnkfabvajfhv12fa1v4fv12g1ba2b1gsgb&orderno=vanfjvadfb1sg5b4s4bf4b1s2n&returnType=2&count=1'

INIT_URL = 'http://www.dianping.com/zhenjiang/ch10/p{}'

INIT_URL_1 = 'http://www.dianping.com/zhenjiang/ch10/r9350p{}'
INIT_URL_2 = 'http://www.dianping.com/zhenjiang/ch10/r3913p{}'
INIT_URL_3 = 'http://www.dianping.com/zhenjiang/ch10/r3914p{}'
INIT_URL_4 = 'http://www.dianping.com/zhenjiang/ch10/r3915p{}'
INIT_URL_5 = 'http://www.dianping.com/zhenjiang/ch10/c864p{}'
INIT_URL_6 = 'http://www.dianping.com/zhenjiang/ch10/c865p{}'
INIT_URL_7 = 'http://www.dianping.com/zhenjiang/ch10/c863p{}'

CSS_URL = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/bdddc0d632d43c9c3a9d46a1363c22a5.css'
SVG_NUM_URL = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/20b501902c483d49e1e66d2159f1d2b8.svg'
SVG_FONT_URL = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/37b6ad50c87b9ec0e1744f4291efb622.svg'

MAX_PAGES = 20

# 获取随机UA
with open('./utils/ua.log', 'r', encoding='utf-8') as f:
    random_ua = random.choice(f.read().split('\n'))

print(random_ua)

HEADERS = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7',
            'Cache-Control': 'max-age=0',
            'Host': 'www.dianping.com',
            'Referer': 'http://www.dianping.com/beijing/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': random_ua,
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
            "Proxy-Tunnel": str(random.randint(1,10000))  # 使用亿牛云代理时需设置
}

# 亿牛云
NIU_PROXY_HOST = 'u5395.b5.t.16yun.cn'
NIU_PROXY_PORT = 6460
NIU_PROXY_USER = '16JVFLKJ'
NIU_PROXY_PASS = '050500'

DEFAULT_STAR = '三星级商户'
DEFAULT_NAME = 'Unnamed'
DEFAULT_NUM = 10

MONGO_CLIENT = 'mongodb://localhost:27017'