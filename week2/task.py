# task1

# 原始訊息的dict
messages={
    "Leslie":"I'm at home near Xiaobitan station.",
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Vivian":"I'm at Xindian station waiting for you."
}
# 捷運站名的list
green_line_stations = ["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing","Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xindian City Hall","Xindian","Xiaobitan"];

# 找出朋友所在的index
# 把message中有比對到跟站名list一樣的字串找出來
# 並製作 朋友名字: 站名: 捷運站index: 的dict
friend_station_list = [ {"name":name,"station":i,"station_idx":green_line_stations.index(i)} for i in green_line_stations for name in messages if messages[name].find(i) > -1 ]
# print(friend_station_list)
# [{'name': 'Copper', 'station': 'Taipei Arena', 'station_idx': 2}, 
#  {'name': 'Bob', 'station': 'Ximen', 'station_idx': 7}, 
#  {'name': 'Mary', 'station': 'Jingmei', 'station_idx': 14}, 
#  {'name': 'Vivian', 'station': 'Xindian', 'station_idx': 18}, 
#  {'name': 'Leslie', 'station': 'Xiaobitan', 'station_idx': 19}]

########## 下面3行簡化成上面1行 ##########
# friend_idx = [ i for i in green_line_stations for name in messages if messages[name].find(i) > -1 ]
# friend_station = [ name for i in green_line_stations for name in messages if messages[name].find(i) > -1 ]
# friend_station_index = [ green_line_stations.index(key) for key in friend_idx  ]
########################################

# 取出站名對應idx
friend_station_index = [ i['station_idx'] for i in friend_station_list]
# print(friend_station_index) # ex: [2, 7, 14, 18, 19]

# 取出朋友名字列表
friend_station = [ i['name'] for i in friend_station_list]
# print(friend_station) # ex: ['Copper', 'Bob', 'Mary', 'Vivian', 'Leslie']

# 計算相距站數
def calculate_stops(friend, current):
    # 狀況1: 朋友在小碧潭、自己不在小碧潭: 計算從自己到七張的站數,再+1
    # Friend at Xiaobitan, current not at Xiaobitan
    if friend == 19 and current != 19:
        # Calculate the number of stations from Qizhang to current location + 1
        stop_count = abs(16 - current) + 1
    
    # 狀況2: 朋友不在小碧潭、自己在小碧潭: 計算從朋友到七張的站數,再+1
    # Friend not at Xiaobitan, current at Xiaobitan
    elif friend != 19 and current == 19:
        stop_count = abs(friend - 16) + 1
    
    # 其他狀況: 朋友跟自己都不在小碧潭、or 朋友跟自己都在小碧潭: 計算從朋友到自己的站數
    # Friend not at Xiaobitan, current not at Xiaobitan OR Friend at Xiaobitan, current at Xiaobitan
    else:
        stop_count = abs(friend - current)
    
    # 回傳站數
    return stop_count

def find_and_print(messages, current_station):
    # your code here
    # 取出自己目前所在位置的捷運站index
    current_index = green_line_stations.index(current_station)

    # 計算每個朋友到自己所在位置的站數,存成list
    distance_list = [ calculate_stops(i, current_index) for i in friend_station_index ]
    # print(distance_list) # ex: [11, 6, 1, 5, 4]

    # 找出最少站數的index 並對應到朋友名字列表, 得出距離最近的朋友
    print(friend_station[distance_list.index(min(distance_list))])
    

print("=== task1 ===")
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

# task2


consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
]

# 建立一個初始時間表(list), 有24個element(24小時)每個element都有三個顧問的名字，表示每個顧問都可以預約
# time_table = [ consultants for i in range(24) ]
# 修正: consultants資料會變動, 所以不能寫死
time_table = [ [ i['name'] for i in consultants ] for i in range(24) ]
# print(time_table)



# 傳入有空的顧問list,以及比對的標準(criteria)
def compare(available_consultants_name, criteria):
    # print(available_consultants_name) # ex: ["John","Bob"]

    # 從顧問的dict中取出有空的顧問,以及其 rating/price 資料
    candidates = [ i for i in consultants for j in available_consultants_name if i['name'].find(j)!=-1  ]
    # print(candidates) # ex: [{'name': 'John', 'rate': 4.5, 'price': 1000}, {'name': 'Bob', 'rate': 3, 'price': 1200}]

    # 沒有顧問有空時: 無法服務
    if(len(available_consultants_name)==0):
        return "no service"
    
    if(criteria=="rate"):
        # 從candidates中取出有空顧問的rating
        rate_list = [ i['rate'] for i in candidates ]
        # 從candidates中取出有有最高rating的顧問
        max_rate_name = [ i['name'] for i in candidates if i['rate'] == max(rate_list) ]
        # 回傳顧問名字
        return max_rate_name[0]
     
    if(criteria=="price"):
        # 從candidates中取出有空顧問的price
        price_list = [ i['price'] for i in candidates ]
        # 從candidates中取出有有最低price的顧問
        min_price_name = [ i['name'] for i in candidates if i['price'] == min(price_list) ]
        # 回傳顧問名字
        return min_price_name[0]

def book(consultants, hour, duration, criteria):
    
    # // get who is available with the hour/duration
    # // 從預約表(time_table)中取出指定時段(hour/duration)有空的顧問
    available_consultants = []
    for i in range(hour, hour+duration):
        available_consultants.append(time_table[i])
    # print(available_consultants) # ex: [['John', 'Bob', 'Jenny'], ['John', 'Bob']]

    # // 取交集,得到可預約的顧問名單
    available_consultants_set = set(available_consultants[0]) # 型別轉換,把list改成set,不然無法取交集
    for i in available_consultants:
        available_consultants_set &= set(i) # 取交集
    # print(available_consultants_set) # {'Bob', 'John'}
    # print(list(available_consultants_set)) # 如果想改回list: ['Bob', 'John']

    # 根據有空的名單以及條件找出推薦顧問
    recommendation = compare(available_consultants_set, criteria)
    print(recommendation)

    # 更新預約表 把推薦的顧問從預約的時段中刪除
    # update time_table
    for i in range(hour, hour+duration):
        if(recommendation!="no service"):
            time_table[i].remove(recommendation)
    


print("=== task2 ===")
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John


# task3
# 取中間字的方法
def getMiddleName(name):
    length = len(name)
    match length:
        case 2:
            return name[1]
        case 4:
            return name[2]
        case _: # 其他狀況: 除2無條件捨去
            return name[length//2]

def func(*data):
    str = []
    count = []
    for x in data:
        middle = getMiddleName(x)
        # 判斷取出來的字是不是已經存在str中了,如果是則設為該名字list的index ;否則設為-1
        middle_index = str.index(middle) if middle in str else -1
        
        # 沒有存過, 把取出來的字存到str中, 並在count list中放1
        if(middle_index==-1):
            str.append(middle)
            count.append(1)
        # 有存過, 把取出來的字存到str中, 並新增一個-1, 表示該位置不需要計算總數,並把前面對應的count加1
        else:
            # print("已有存過middle")
            # print(middle_index)
            str.append(middle)
            count.append(-1) # 表示該位置前面已經加總過了
            count[middle_index] += 1
    # print(str) # ex: ['靜', '立', '靜', '立', '花']
    # print(count) # ex: [2, 2, -1, -1, 1]
    
    # python 的index方法 如果沒找到會出現error 不會回傳-1 (跟javascript不一樣)
    # 解決辦法:
    # unique: 找count為1的index; 如果找不到則設為-1
    # 注意: 這裡會有一個情況: 如果count中有多個出現一次的中間名,則只會回傳第一個找到的
    unique = count.index(1) if 1 in count else -1
    unique_middlename = data[unique] if(unique!=-1) else "沒有" 
    print(unique_middlename)


print("=== task3 ===")
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安
# // func("郭宣雅", "夏曼藍波安"); // print 夏曼藍波安


# task4

# 0,4,8,7,11,15,14,18,22,21,25....
# 取3餘數:
# 餘0: 前項-1
# 餘1: 前項+4
# 餘2: 前項+4

def get_sequence(index):
    if(index == 0):
        return 0
    idx = index % 3
    if(idx == 1):
        return get_sequence(index-1)+4
    elif(idx == 2):
        return get_sequence(index-1)+4
    return get_sequence(index-1)-1

def get_number(index):
    print(get_sequence(index))

print("=== task4 ===")
get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70


# task5

def find(spaces, stat, n):
    # your code here
    
    # stat為0表示該車廂不開放, 把相對應的spaces list 設為-1
    for index, item in enumerate(stat):
        if(stat[index]==0):
            spaces[index] = -1
    
    # 如果spaces中所有位置總數都比需求(n)小, 表示無車可搭 回傳-1
    if(max(spaces) < n):
        print(-1)
    # 找出比n大的space中,最小的那個車廂Index並回傳
    else:
        smallest_i = 0
        for index, item in enumerate(spaces):
            if(spaces[index]>=n):
                if(spaces[smallest_i]>=spaces[index]):
                    smallest_i = index
            else:
                smallest_i += 1
        print(spaces.index(min([x for x in spaces if x>=n])))

print("=== task5 ===")
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2
