import requests
import json


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
    print(order_loss('2021-03-15 00:00:00, 2021-03-15 23:59:59, 511526'))
