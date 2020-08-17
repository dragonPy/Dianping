# -*- coding:utf-8 -*-

"""
Updated at 10:40 at April 25,2019
@title: 花式反爬之大众点评
@author: Northxw
"""

import requests
import urllib.error
import numpy as np
from scrapy.selector import Selector
from proxy import xdaili_proxy, general_proxy
from config import HEADERS, CSS_URL, SVG_NUM_URL, \
                     SVG_FONT_URL, MONGO_CLIENT,INIT_URL,INIT_URL_1, \
                     INIT_URL_2,INIT_URL_3,INIT_URL_4,INIT_URL_5,INIT_URL_6,INIT_URL_7
from parse import parse
from pymongo import MongoClient
from tqdm import tqdm
import time
import random


class Dianping(object):
    def __init__(self):
        self.headers = HEADERS
        self.proxies = general_proxy()
        self.css_url = CSS_URL
        self.svg_num_url = SVG_NUM_URL
        self.svg_font_url = SVG_FONT_URL
        self.client = MongoClient(MONGO_CLIENT)
        self.db = self.client.dianping
        self.collection = self.db.shop

    def get_store_list_page(self, url):
        try:
            # print(self.proxies)
            response = requests.get(url, headers=self.headers, proxies=self.proxies)
            if response.status_code == 200:
                return response
        except urllib.error.HTTPError as e:
            print(e.reason)

    def parse_data(self, response):
        res = Selector(text=response.text)
        try:
            li_list = res.xpath('//*[contains(@id, "shop-all-list")]/ul/li')
            if li_list:
                for li in li_list:
                    data = parse(li, self.svg_num_url, self.svg_font_url, self.css_url)

                    temp = dict()
                    temp['foot_type'] = data['food_type']
                    print(temp, '<<<<<foot_type')
                    self.save_to_db(data)
                    # break
        except Exception as e:
            print('Error: %s, Please Check it.' % e.args)

    def save_to_db(self, data):
        self.collection.update_one({ 'name': data['name'] }, { "$set": data }, True)

    def main(self):
        """
        主函数
        """
        for i in range(1):
        # for i in tqdm(range(10), desc='Grabbing', ncols=100):
            print("第%d页：" %(i+1), INIT_URL_7.format(str(i+1)))
            response = self.get_store_list_page(INIT_URL_7.format(str(i+1)))
            self.parse_data(response)
            time.sleep(np.random.randint(1,3))
            # 测试仅抓取第一页
            # break

if __name__ == '__main__':
    dianping = Dianping()
    dianping.main()