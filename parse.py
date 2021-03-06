# -*- coding:utf-8 -*-

import re
from config import *
import requests
from utils.common import get_md5

def parse(li, svg_num_url, svg_font_url, css_url):
    """
    解析数据
    """
    data = dict()
    # 店铺名称
    data['name'] = li.css('.txt .tit > a > h4::text').extract_first(DEFAULT_NAME)
    # 店铺封面
    data['img'] = li.css('.pic > a > img::attr(src)').extract_first('').split('%')[0]
    # 店铺链接
    data['shop_detail_url'] = li.css('.txt .tit > a:nth-child(1)::attr(href)').extract_first('')
    # ID
    data['id'] = get_md5(data['shop_detail_url'])
    # 星级
    data['star'] = li.css('.txt .comment > span::attr(title)').extract_first(DEFAULT_STAR)
    # print(data, '星级')

    # 评论数
    comment_class_list = li.css("div.txt div.comment> a.review-num > b ").extract() 
    data['comments'] = get_count(comment_class_list)
    # 人均价
    price_inner_number = li.css('.txt .comment > a.mean-price > b').extract()
    data['price'] = get_count(price_inner_number)
    # 口味
    taste_class_list = li.css('.txt .comment-list > span:first-child > b').extract()
    data['taste'] = get_count(taste_class_list)
    # 环境
    environment_class_list = li.css('.txt .comment-list > span:nth-child(2) > b').extract()
    data['environment'] = get_count(environment_class_list)
    # 服务
    quality_class_list = li.css('.txt .comment-list > span:last-child > b').extract()
    data['quality'] = get_count(quality_class_list)


    # # 美食分类
    type_class_list = li.css('.txt .tag-addr > a:nth-child(1) > span').extract()
    data['food_type'] = get_foot_type(type_class_list)
    # # 地址
    # address_class_list = re.findall(r'class="(.*?)">', li.css('.txt .tag-addr > a:nth-child(3) > span').extract_first(), re.S)[1:]
    # data['fuzzy_address'] = get_completed_font_424(svg_font_url, css_url, address_class_list)
    # print(data['fuzzy_address'])
    # # 详细地址
    # detail_address_class_list = re.findall(r'class="(.*?)">', li.css('.txt > div.tag-addr > span').extract_first(), re.S)[1:]
    # data['detail_address'] = get_completed_font_424(svg_font_url, css_url, detail_address_class_list)
    # print(data['detail_address'])
    #推荐菜
    data['recommend'] = '|'.join(re.findall('blank.*?>(.*?)</a>', li.css('.txt .recommend').extract()[0], re.S))

    # print(data, 'daa')

    return data

def get_count(uncode_list):  
    try:  
        count = ""
        woff = {  
            "\ue4fa": "0",  
            # "": "1",  
            "\ue903": "2",  
            "\uf105": "3",  
            "\uf531": "4",  
            "\ueeee": "5",  
            "\uf7b8": "6",  
            "\uf7cf": "7",  
            "\ue45e": "8",  
            "\ue576": "9",  
        }
        for uncode in uncode_list:  
            uncodes = uncode.replace('<svgmtsi class="shopNum"', "").replace("</svgmtsi", "").replace("</b>", "").replace("<b>", "").split('>')  
            for uncs in uncodes:
                if uncs in woff.keys():  
                    cc = woff[uncs]
                else:  
                    cc = uncs
                # print(cc, 'cccc')
                count = count + cc 
        return count
    except Exception as e:
        print("数字解析出现错误")  
        return uncode_list[0]

def get_foot_type(uncode_list):  
    try:  
        count = ""
        woff = {  
            "\ue428": "菜",  
            "\uf2e9": "合",  
            "\ue112": "烤",  
            "\ue277": "肉",  
            "\uf5db": "快",  
            "\ue545": "餐",  
            "\uecf2": "自",  
            "\ue0dd": "助",  
            "\ue112": "串",
            "\ued09": "意",
            "\ued22": "特",
            "\uf755": "色", 
            "\ue92a": "其", 
            "\ue5cf": "他",
            "\ue18f": "中",
            "\ueb22": "串",
            "\ue19e": "香",
            "\ue58e": "川",
            "\ue428": "菜",
            "\ue018": "馆",
            "\ueeb4": "西",
            "\ued9f": "国",
            "\ue7ad": "料",
            "\ue3b3": "理",
            "\uef45": "茶",
            "\uf0ba": "果",

            "\uef59": "四",
            "\uf08e": "火",
            "\uec3c": "锅",
            "\uec72": "云",
            "\uf537": "南",
            "\ue390": "日",

            "\uec7d": "式",
            "\ue0da": "烧",
            "\ue66e": "本",
            "\uee9f": "小",
            "\uee7d": "吃",
            "\ue6a1": "面",
            "\ue0fd": "食",
            "\ue405": "鸡",

            "\ue115": "农",
            "\uf103": "家",
            "\ue474": "铁",
            "\uf213": "板",
            "\uf777": "牛",
            "\ue8bf": "东",
            "\ue669": "重",
            "\ue453": "庆",

            "\uf303": "房",
            "\ue8bf": "东",
            "\uf38a": "北",
            "\ue9bb": "包",
            "\uf5ee": "甜",
            "\uf443": "品",
            "\ue252": "鱼",
            "\uf8d9": "厅",

            "\uf22f": "老",
            "\uf02e": "京",
            "\uead5": "司",
            "\uf817": "手",
            "\ue0a0": "海",
            "\ue314": "鲜",
            "\uf79a": "酸",
            "\uf6b9": "水",

            "\ue508": "新",
            "\ue514": "奶",
            "\ue5c3": "常",
            "\uebd3": "江",
            "\ue5e2": "地",
            "\uedfb": "子",
            "\uf6ae": "干",
            "\uec71": "虾",

            "\ue7fa": "羊",
            "\ue2d7": "龙",
            "\ue5c3": "常",
            "\uf704": "生",
            "\uee6a": "鸭",
            "\ue1d0": "店",
            "\uf7a8": "味",
            "\uf89f": "美",

            "\ue6ea": "民",
            "\ue744": "间",
            "\uf2c3": "酱",
            "\ue2fe": "更",
            "\uef54": "多",
            "\uf0f8": "保",
            "\ue236": "健",
            "\ue719": "黄",

            "\ue92e": "河",
            "\ue693": "湖",
            "\ueb75": "大",
            "\uf6fb": "州",
            "\ue2ef": "汤",
            "\ue55f": "花",
            "\uf52d": "甲",
            "\ue1a9": "门",

            "\uf4ad": "豆",
            "\ue79a": "客",
            "\ueb75": "大",
            "\uf6fb": "州",
            "\ue2ef": "汤",
            "\ue55f": "花",
            "\uf52d": "甲",
            "\ue1a9": "门"
        }
        for uncode in uncode_list:  
            uncodes = uncode.replace('<svgmtsi class="tagName"', "").replace("</svgmtsi", "").replace("</span>", "").replace('<span class="tag"', "").split('>')  
            # print(uncodes, 'uncodes array')
            for uncs in uncodes:
                if uncs in woff.keys():  
                    cc = woff[uncs]
                else:  
                    cc = uncs
                count = count + cc 
        # print('cccccoooouuuut', 'type') 
        return count
    except Exception as e:
        print("数字解析出现错误")  
        return uncode_list[0]  

if __name__ == '__main__':
    pass
    # get_completed_font(CSS_URL, SVG_FONT_URL, ['jv3j8', 'jvu8v', 'jvp6e', 'jv8vh'])