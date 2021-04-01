import requests
import json
from datetime import datetime
import time


headers = {'Content-Type': 'application/json', 'x-token': 'XX7tt39ea9a5ab7530b00445973d0a7785c4c0e4XXXXXXm41'}


def order_paging(datas):
    startAt = datas.split(',')[0]
    endAt = datas.split(',')[1]
    regionId = datas.split(',')[2]
    datas = {'startAt': startAt, 'endAt': endAt, 'regionId': regionId, 'page': {'size': 100000, 'current': 1, 'total': 0}}
    try:
        response = requests.post(url='http://boss.nm666.cn/api/v1/usr/order/paging', headers=headers, data=json.dumps(datas))
        result = response.json()['result']
        a = 0
        for i in result:
            a = a + i['amountPaid']
        print(round(a, 2))
        a = round(a, 2)
        return a
    except requests.exceptions.ConnectionError:
        print('连接问题')
    except requests.exceptions.ChunkedEncodingError:
        print('chuncked编码问题')
    except:
        print('error')


def order_loss(datas):
    startAt = datas.split(',')[0]
    endAt = datas.split(',')[1]
    regionId = datas.split(',')[2]
    datas = {'beginAt': startAt, 'endAt': endAt, 'regionId': regionId, 'page': {'size': 100000, 'current': 1, 'total': 0}}
    try:
        response = requests.post(url='http://boss.nm666.cn/api/v1/report/order_loss/paging', headers=headers, data=json.dumps(datas))
        result = response.json()['result']
        # print(result)
        a = 0
        for i in result:
            a = a + i['unlockTimes']
        print(round(a, 2))
        a = round(a, 2)
        return a
    except requests.exceptions.ConnectionError:
        print('连接问题')
    except requests.exceptions.ChunkedEncodingError:
        print('chuncked编码问题')
    except:
        print('error')


def makeup_paging(datas):
    month = datas.split(',')[0]
    regionId = datas.split(',')[1]
    year = datas.split(',')[2]

    datas = {'month': month, 'regionId': regionId, 'year': year, 'page': {'pageSize': 10000, 'pageNum': 1}}
    response = requests.post(url='https://data2020.nm666.cn/inq/data/makeup/paging', headers=headers, data=json.dumps(datas))
    result = response.json()['result']
    a = 0
    for i in result:
        a = a + i['makeupAmount']
        # print(i['customerName'], i['makeupAmount'])
    print(round(a, 2))
    return round(a, 2)

# 挪车效率表
def moving_efficiency(datas):
    beginAt = datas.split(',')[0]
    endAt = datas.split(',')[1]
    regionId = datas.split(',')[2]
    try:
        datas = {'beginAt': beginAt, 'endAt': endAt, 'regionId': regionId, 'page': {'size': 10000, 'current': 1, 'total': 1}}
        response = requests.post(url=' http://localhost:8000/api/v1/report/moving_efficiency/paging', headers=headers, data=json.dumps(datas))
        result = response.json()['result']
        a = 0
        b = 0
        c = 0
        for i in result:
            if beginAt[:10] in i['orderAt']:
                a = a + i['orderDuration']
                b = b + 1
            c = c + i['movingDuration']
        movingnum = len(result)
        movingorder = b
        ordertimes = round(c/len(result), 4)
        movingtimes = round(a/b, 4)
        ordertime = time.strftime('%H:%M:%S', time.gmtime(c/len(result)))
        movingtime = time.strftime('%H:%M:%S', time.gmtime(a/b))
        zhishu = round((b/(a/b))/(len(result)/(c/len(result))), 4)
    except:
        movingnum = 0
        movingorder = 0
        ordertime = 0
        movingtime = 0
        zhishu = 0
        ordertimes = 0
        movingtimes = 0
    return movingnum, movingorder, ordertime, movingtime, zhishu, ordertimes, movingtimes

# 挪车平均里程
def dispatch_log(datas):
    createBeginAt = datas.split(',')[0]
    createStopAt = datas.split(',')[1]
    regionId = datas.split(',')[2]
    try:
        datas = {'createAtOrder': 2, 'createBeginAt': createBeginAt, 'createStopAt': createStopAt, 'regionId':regionId,
                 'creatorName':'', 'endBeginAt':"", 'endStopAt':"",'isItValid':0, 'phone': '','snOrder':0,
                 'vehicleSn':"",'page': {'size': 10000, 'current': 1, 'total': 1}}
        response = requests.post(url=' http://localhost:8000/api/v1/iot/dispatch_log/paging', headers=headers, data=json.dumps(datas))
        result = response.json()['result']
        a = 0
        for i in result:
            a = a + i['distance']
        avgdistance = round(a/len(result), 4)
    except:
        avgdistance = 0
    return avgdistance, avgdistance/23


def monthorder_paging(datas):
    month = datas.split(',')[0]
    regionId = datas.split(',')[1]
    year = datas.split(',')[2]
    datas = {'month': month, 'regionId': regionId, 'year': year, 'page': {'pageSize': 100000, 'pageNum': 1}}
    response = requests.post(url='https://data2020.nm666.cn/inq/data/statement/paging', headers=headers, data=json.dumps(datas))
    print(response.json())
    # result = response.json()['result']
    # actualAmounts = 0
    # basicAmounts = 0
    # receivableAmounts = 0
    # beCollectedAmounts = 0
    # for i in result:
    #     actualAmounts = actualAmounts + i['actualAmount']
    #     basicAmounts = basicAmounts + i['basicAmount']
    #     receivableAmounts = receivableAmounts + i['receivableAmount']
    #     beCollectedAmounts = beCollectedAmounts + i['beCollectedAmount']
    #     print(round(actualAmounts, 2), round(basicAmounts, 2), round(receivableAmounts, 2),
    #           round(beCollectedAmounts, 2))
    # print(round(actualAmounts, 2), round(basicAmounts, 2), round(receivableAmounts, 2), round(beCollectedAmounts, 2))
    # return round(actualAmounts, 2), round(basicAmounts, 2), round(receivableAmounts, 2), round(beCollectedAmounts, 2)


if __name__ == '__main__':
    # refund_amount = refund('11,511526,2020')
    # refund_amounts = refund_inquiry('11,511526,2020')
    # assert refund_amount == refund_amounts
    # makeup_amounts = makeup_paging('11,511526,2020')
    # makeup_amountss = makeup_amounts('11,511526,2020')
    # assert makeup_amounts == makeup_amountss
    # order_paging('2020-12-10 00:00:00,2020-12-12 23:44:11,511526')
    # amount = makeup_paging('12,511526,2020')
    # monthorder_paging('12,522526,2020')
    # print(order_loss('2021-03-15 00:00:00, 2021-03-15 23:59:59, 511526'))
    # print(moving_efficiency('2020-09-02 00:00:00, 2020-09-02 23:59:59, 511526'))
    for i in range(1, 31):
        if i > 9:
            print('2021-03-'+str(i), moving_efficiency('2021-03-'+str(i)+' 00:00:00, 2021-03-'+str(i)+' 23:59:59, 511527'))
        else:
            print('2021-03-0' + str(i), moving_efficiency('2021-03-0' + str(i) + ' 00:00:00, 2021-03-0' + str(i) + ' 23:59:59, 511527'))
    # print(dispatch_log('2021-03-24 00:00:00, 2021-03-24 23:59:59, 511526'))