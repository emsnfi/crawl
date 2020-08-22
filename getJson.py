import json
import os

def setos(): #設定路徑
    os.chdir("/Users/emily/Desktop")
    print(os.getcwd())

def getTarget(target,data,temp): #針對dict尋找
        if target not in data.keys(): #如果不是所經過的key，則往此key裡面的value找
            for val in data.values():
                if (isinstance(val, dict)): #如果是dict型式則呼叫本function
                    getTarget(target,val,temp)

                elif isinstance(val, (list, tuple)):
                    get_value(target, val)  # 傳入數據的value值是列表或者元組，則調用get_value
        else: #找到了，就將其底下的value存在temp內
            temp.append(data[target])

        return temp

def get_value(key, val):
    for val_ in val:
        if isinstance(val_, dict):
            getTarget(key, val_,temp)  # 傳入數據的value值是字典，則調用getTarget
        elif isinstance(val_, (list, tuple)):
            get_value(key, val_)   # 傳入數據的value值是列表或者元組，則調用自己


if __name__ == '__main__':
    setos()
    with open("weather_predict.json", mode="r", encoding="utf-8") as file:
        data = json.load(file)
    temp_dict = {}
    temp = []  # 放所要key值的value
    # 目標要取出某一天的天氣資訊、溫度
    plist = ["weatherForecasts", "locationName", "location", "daily"]  # 所要取的資訊最金的階層key
    time = "2020-08-25"  # 所要資訊的日期
    area = "北部地區"  # 所要的地區

    index = 1  # 用來存所要地區的index

    tc = 0  # 溫度有最高跟最低，但其名稱都叫temperature，故用取的順序判定，若是第一次取則為最高溫
    for i in plist:
        temp_dict = {}
        temp = []
        y = getTarget(i, data, temp)
        temp_dict[i] = y
        for j in range(len(y)):
            if (y[j] == area and i == "locationName"):
                index = j
        if (i == "location"):
            k = list(temp_dict.values())[0][0][index]
            temp_dict[i] = k
        if (i != "locationName"):
            data = temp_dict
        if (i == "daily"):
            dateindex = 0
            a = list(temp_dict.values())[0][0]  # [c]
            for c in range(len(a)):
                a = list(temp_dict.values())[0][0][c]
                if ((list(a.values())[0]) == time):
                    dateindex = c
                    for t in range(3):
                        a = list(temp_dict.values())[0][t][dateindex]
                        for k in a.keys():
                            if (k == "weather"):
                                print("地區：",area)
                                print("時間：", time)
                                print("天氣為：", a['weather'])
                            elif (k == "temperature"):
                                if (tc == 0):
                                    print("最高氣溫：", a['temperature'])
                                else:
                                    print("最低氣溫：", a['temperature'])
                                tc += 1



