
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['axes.unicode_minus'] = False  

url = 'https://opendata.epa.gov.tw/ws/Data/CFPCarbon/?$format=json'
response = requests.get(url, verify=False)
data_df = pd.DataFrame(response.json())
print(data_df.head())

data = []
data_lis = []

def get_name (CFPL_Code):

    CFPL_Code = str(CFPL_Code)

    for i in range (0, len(response.json())):
        if response.json()[i]['CFPL_Code'] == CFPL_Code:
            data = [response.json()[i]['Product_Name'], response.json()[i]['Product_Carbon_Footprint_Data']]
            data_lis.append(data)
    return data_lis

get_name(1800714004)
get_name(1802202001)
data_lis[0][1] = '650'
data_lis[1][1] = '380'
print('早上八點吃早餐', data_lis[0], data_lis[1])

get_name(1604931002)
get_name(1716412002)
data_lis[2][1] = '80'
data_lis[3][1] = '2000'
print('早上九點搭公車去銀行辦事', data_lis[2], data_lis[3])

get_name(1800203002)
get_name(1800203010)
get_name(1800203011)
data_lis[4][1] = '4500'
data_lis[5][1] = '7500'
data_lis[6][1] = '7000'
print('早上十點市場買肉', data_lis[4], data_lis[5], data_lis[6])

get_name('R1701905001')
print('中午簡單吃兩個鳳梨酥', data_lis[7])
data_lis[7][1] = '340'
print('中午簡單吃兩個鳳梨酥', data_lis[7])

get_name(1716312002)
print('下午待在家看影片', data_lis[8])
data_lis[8][1] = '3680'
print('下午待在家看影片', data_lis[8])

get_name(1803305002)
data_lis[9][1] = '80'
print('晚上洗頭', data_lis[9])

get_name(1716312002)
data_lis[10][1] = '1200'
print('繼續看影片', data_lis[10])

total = 0
for i in range (0, 11):
    total = total + int(data_lis[i][1])
print(total)

df = pd.DataFrame(data_lis, columns = ['事件', '碳足跡(g)'])
labels = list(df['事件'])
sizes = [int(list(df['碳足跡(g)'])[int(i)]) for i in range(11)]

explode = (0,0,0.2,0,0.1,0.1,0.1,0,0,0.2,0)
fig1, ax1 = plt.subplots()

ax1.pie(sizes, labels=labels, explode=explode, autopct='%1.0f%%', shadow=False, startangle=180, textprops = {'fontsize':8})
ax1.axis('equal')
plt.title('Carbon_Foot per day = 27.41(kg)', loc='right')
plt.show()