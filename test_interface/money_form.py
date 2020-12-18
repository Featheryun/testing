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


if __name__ == '__main__':
    # refund_amount = refund('11,511526,2020')
    # refund_amounts = refund_inquiry('11,511526,2020')
    # assert refund_amount == refund_amounts
    # makeup_amounts = makeup_paging('11,511526,2020')
    # makeup_amountss = makeup_amounts('11,511526,2020')
    # assert makeup_amounts == makeup_amountss
    order_paging('2020-12-10 00:00:00,2020-12-12 23:44:11,511526')
