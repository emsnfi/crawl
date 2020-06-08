import requests as rq 
from bs4 import BeautifulSoup
import json
import numpy as np
import os

r = rq.get("https://shopee.tw/") #將此頁面的HTML GET下來
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
print(soup) #印出HTML

sel = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel



#print(json.dumps(api1_data,indent=4))

#print(api1_data['items'][8]['name'])
#print(api1_data['items'][8]['itemid'])
#print(api1_data['items'][8]['shopid'])
#print(api1_data['items'][8]['price_max'])
#抓蝦皮

def crawlshopee(n_item):
    item_name = [] # 存商品資訊
    item_price=[] #存商品價格
    item_img=[] #存商品圖片url
    item_list = {} #商品的dict
    #dict = {}
    #item_name=np.empty(50)
    url = 'https://shopee.tw/api/v2/search_items/?by=relevancy&keyword=掃地機器人&limit=50&newest=0&order=desc&page_type=search&version=2'
#https://shopee.tw/api/v2/search_items/?by=relevancy&keyword=%E8%97%8D%E8%8A%BD%E8%80%B3%E6%A9%9F&limit=50&newest=0&order=desc&page_type=search&version=2
#https://shopee.tw/api/v2/search_items/?by=relevancy&categoryids=8000&keyword=%E9%A3%9F%E7%89%A9&limit=50&newest=0&order=desc&page_type=search&skip_autocorrect=1&version=2
    headers = {
        'User-Agent': 'Googlebot',
    }
    #要抓price 跟 圖片url時
    #Q 為什麼不能直接抓api1裡面的item price 要特別把itemid shopid抓出來 找price
    r = rq.get(url,headers=headers)
    api1_data = json.loads(r.text)#
    #print(json.dumps(api1_data,indent=4))
    for i in range(n_item):
        
        item_name.append(api1_data['items'][i]['name'])
        
        #為了要取商品價格跟圖片url 須額外取itemid 跟 shopid

        itemid=api1_data['items'][i]['itemid']
        shopid=api1_data['items'][i]['shopid']
        url2=f'https://shopee.tw/api/v2/item/get?itemid={itemid}&shopid={shopid}'
        r2 = rq.get(url2,headers=headers)
        api2_data = json.loads(r2.text)
        item_price.append(str(int(api2_data['item']['price']/100000))) #價格
        
        img= str(api2_data['item']['images'][0])
        item_img.append('https://cf.shopee.tw/file/'+img+'_tn')
        c = str(i)
        
        item_list[c] = {"id": i,"ietemName":item_name[i],"itemPrice":item_price[i],"itemImg":item_img[i]}
        

    print(json.dumps(item_list,indent=3,ensure_ascii=False))
    item_json = json.dumps(item_list,indent=3,ensure_ascii=False) #json排版
    
    item_jsonb=[]
    for i in range(50): #為了不要印到dict 的 name
        c=str(i)
        #print(item_list[c])
        item_jsonb.append(item_list[c])
    print(item_jsonb)
    item_json = json.dumps(item_jsonb,indent=3,ensure_ascii=False)
    print(item_json)
    fp = open('item_json.txt', 'w')
    fp.write(item_json)
    #item_list['name'] = item_name
    #item_list['price'] = item_price
    #item_list['img'] = item_img
    #print(json.dumps(item_list,indent=3))
    
    #itemid=api1_data['items'][0]['itemid']
    #shopid=api1_data['items'][0]['shopid']
    #這樣會不對 price1 = api1_data['items'][0]['price']
    
    #這樣不對 img= api1_data['items'][0]['images'][0]
    #print(f'https://shopee.tw/api/v2/item/get?itemid={itemid}&shopid={shopid}')
    #url2=f'https://shopee.tw/api/v2/item/get?itemid={itemid}&shopid={shopid}'
    #r2 = rq.get(url2,headers=headers)
    #api2_data = json.loads(r2.text)
    #output =  str(api2_data['item']['price']/100000)
    #print(output)
   
    #img=str(api2_data['item']['images'][0])
    
    #print('https://cf.shopee.tw/file/'+img+'_tn')
    
    #time.sleep(0.2)
   

crawlshopee(50)


