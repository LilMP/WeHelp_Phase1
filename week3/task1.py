import urllib.request as req, json

############## fetch data ##############

def getDataInJson(url):
    request = req.Request(url)
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8") # type: string
    # print(data)
    result = json.loads(data)
    return result

data1 = getDataInJson("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
data2 = getDataInJson("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2")

############## part1: spot ##############

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
    spot.append([title, district, long, lat, imgurl])
    # spot.append([title+","+district+","+long+","+lat+","+imgurl])
# print(spot[:3])

############## part2: mrt ##############

output = {}
for d2_item in data2['data']:
    for d1_item in data1['data']['results']:
        if d1_item.get('SERIAL_NO') == d2_item.get('SERIAL_NO'):
            s_n = d1_item.get('SERIAL_NO')
            mrt = d2_item.get('MRT')
            title = d1_item.get('stitle')
            if mrt in output:
                output[mrt].append(title)
            else:
                output[mrt] = [mrt,title]

# print(output.values())

# mrt = []
# for k,v in output.items():
#     mrt.append([k,v])
    # mrt.append([k+","+v])
# print(mrt[:3])

############## final step: output ##############
import csv
# header = ["title", "district", "long", "lat", "imgurl"]
with open("spot.csv", "w", encoding="cp950", newline="") as f:
    # 加入 delimiter=' ', escapechar=' ', quoting=csv.QUOTE_NONE 讓"" 消失
    writer = csv.writer(f)
    # writer.writerow(header) 
    writer.writerows(spot)

with open("mrt.csv", "w", encoding="cp950", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output.values())
