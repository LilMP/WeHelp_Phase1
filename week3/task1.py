import urllib.request as req, json

def getDataInJson(url):
    request = req.Request(url)
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8") # type: string
    # print(data)
    result = json.loads(data)
    return result

data1 = getDataInJson("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
data2 = getDataInJson("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2")

############## part1 ##############

spot = []
for d1_item in data1['data']['results']:
    title = d1_item.get('stitle')
    long = d1_item.get('longitude')
    lat = d1_item.get('latitude')
    d1_s_no = d1_item.get('SERIAL_NO')
    imgurl = "http://"+d1_item.get('filelist').split("https://")[1]
    for d2_item in data2['data']:
        d2_s_no = d2_item.get('SERIAL_NO')
        if(d1_s_no == d2_s_no):
            district = d2_item.get('address')[5:8]
    # result.append([title, district, long, lat, imgurl])
    spot.append([title+","+district+","+long+","+lat+","+imgurl])
print(spot[:3])

############## part2 ##############

output = {}
for d2_item in data2['data']:
    for d1_item in data1['data']['results']:
        if d1_item.get('SERIAL_NO') == d2_item.get('SERIAL_NO'):
            s_n = d1_item.get('SERIAL_NO')
            mrt = d2_item.get('MRT')
            title = d1_item.get('stitle')
            if mrt in output:
                output[mrt] += ","+title
            else:
                output[mrt] = title

mrt = []
for k,v in output.items():
    # mrt.append([k,v])
    mrt.append([k+","+v])
print(mrt[:3])

#### output
import csv
# header = ["title", "district", "long", "lat", "imgurl"]
with open("spot.csv", "w", encoding="cp950", newline="") as f:
    writer = csv.writer(f)
    # writer.writerow(header) 
    writer.writerows(spot)

with open("mrt.csv", "w", encoding="cp950", newline="") as f:
    writer = csv.writer(f)
    # writer.writerow(header) 
    writer.writerows(mrt)








# for element in data1['data']['results']:
#     if element.get('stitle'):
#         print(element.get('stitle'))   
#     if element.get('longitude'):
#         print(element.get('longitude'))   
#     if element.get('latitude'):
#         print(element.get('latitude'))   
#     if element.get('filelist'):
#         print("http://"+element.get('filelist').split("https://")[1])


######################## playground #######################

# for item in output:
#     output2.append( {} )
#     output[item].update(item.values())
# print(output)
# l2_dict[item].update(l1_dict.get(item, {}))
# l3 = list(l2_dict.values())

# 印出前10項觀察
# count = 0
# for item in data2['data']:
#     print(item)
#     count+=1
#     if(count>9):
#         break

# print("########## before")
# print(data2.get('data')[0].get('avEnd') )
# data3 = data2
# print( data3 == data2)
# print(data3)

# # merge with serial_no
# l1_dict = { e['SERIAL_NO']: e for e in data1['data']['results'] }
# l2_dict = { e['SERIAL_NO']: e for e in data2['data'] }
# # print(l2_dict)

# for item in l2_dict:
#     l2_dict[item].update(l1_dict.get(item, {}))
# l3 = list(l2_dict.values())

# print("########## after")
# print(data2.get('data')[0].get('avEnd'))

# print( data3 == data2)
# # print(data3)

# output = [ [e.get('stitle'),
#             e.get('address')[5:8],
#             e.get('longitude'),
#             e.get('latitude'),
#             "https://"+e.get('filelist').split("https://")[1]
#             ] for e in l3 ]


# for ele in data1.get('data').get('results'):
#     print(ele.get('SERIAL_NO'))

# 從data2中取出行政區
# for e in data2['data']:
#     e.update([{"district",e['address'][5:8]}])
# print(data2)


# ### output
# import csv
# # header = ["title","likeCount","dateTime"]
# with open("spot.csv", "w", encoding="cp950", newline="") as f:
#     writer = csv.writer(f)
#     # writer.writerow(header) 
#     writer.writerows(output)






############



# print(result['data']['results'])
# print(type(result['data']['results'])) # list

# result_list = result['data']['results']

# keys = [ k for k in result_list[0]]
# keys = [ k for k in result_list[0]]
# ['info', 'stitle', 'xpostDate', 'longitude', 'REF_WP', 'avBegin', 'langinfo', 'SERIAL_NO', 'RowNumber', 'CAT1', 'CAT2', 'MEMO_TIME', 'POI', 'filelist', 'idpt', 'latitude', 'xbody', '_id', 'avEnd'] 



# print([d.get('longitude') for d in result['data']['results'] if d.get('longitude')])
# print([d.get('filelist') for d in result['data']['results'] if d.get('filelist')])


# for element in result['data']['results']:
#     if element.get('stitle'):
#         print(element.get('stitle'))   
#     if element.get('longitude'):
#         print(element.get('longitude'))   
#     if element.get('latitude'):
#         print(element.get('latitude'))   
#     if element.get('filelist'):
#         print("http://"+element.get('filelist').split("https://")[1])

         


# test = [d.get('filelist').split('https://') for d in result['data']['results'] if d.get('filelist')]
# print(test[0])

# with open('root.html', 'w', encoding='UTF-8') as f:
#     f.write(data)


# def recursive_items(dictionary):
#     for key, value in dictionary.items():
#         if type(value) is dict:
#             yield (key, value)
#             yield from recursive_items(value)
#         else:
#             yield (key, value[0:5])

# for key, value in recursive_items(result):
#     print(key, value)