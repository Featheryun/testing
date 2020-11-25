import requests
import json


headers = {'Content-Type': 'application/json', 'x-token': 'XX7pxara29285e87658abe84b6d421145def1017XXXXXXXm1'}


# def refund(datas):
#     month = datas.split(',')[0]
#     regionId = datas.split(',')[1]
#     year = datas.split(',')[2]
#     datas = {'month': month, 'regionId': regionId, 'year': year, 'page': {'pageSize': 200, 'pageNum': 1}}
#     try:
#         response = requests.post(url='http://192.168.3.8:9099/inq/data/refund/paging', headers=headers, data=json.dumps(datas))
#         a = response.json()['result']
#         b = 0
#         for i in a:
#             b = b + i['refundAmount']
#         b = round(b, 2)
#         print(b)
#         return b
#     except requests.exceptions.ConnectionError:
#         print('连接问题')
#     except requests.exceptions.ChunkedEncodingError:
#         print('chunked编码问题')
#     except:
#         print('error')
#
#
# def refund_inquiry(datas):
#     month = datas.split(',')[0]
#     regionId = datas.split(',')[1]
#     year = datas.split(',')[2]
#     datas = {'month': month, 'regionId': regionId, 'year': year}
#     try:
#         response = requests.post(url='http://192.168.3.8:9099/inq/data/refund/inquiry', headers=headers, data=json.dumps(datas))
#         a = response.json()['result']['amount']
#         print(a)
#         return a
#     except requests.exceptions.ConnectionError:
#         print('连接问题')
#     except requests.exceptions.ChunkedEncodingError:
#         print('chunked编码问题')
#     except:
#         print('error')
#
#
# def makeup_amount(datas):
#     month = datas.split(',')[0]
#     regionId = datas.split(',')[1]
#     year = datas.split(',')[2]
#     datas = {'month': month, 'regionId': regionId, 'year': year}
#     try:
#         response = requests.post(url='http://192.168.3.8:9099/inq/data/makeup/inquiry', headers=headers, data=json.dumps(datas))
#         makeupamount = response.json()['result']['amount']
#         print(makeupamount)
#         return makeupamount
#     except requests.exceptions.ConnectionError:
#         print('连接问题')
#     except requests.exceptions.ChunkedEncodingError:
#         print('chuncked编码问题')
#     except:
#         print('error')
#
#
# def makeup_paging(datas):
#     month = datas.split(',')[0]
#     regionId = datas.split(',')[1]
#     year = datas.split(',')[2]
#     datas = {'month': month, 'regionId': regionId, 'year': year, 'page': {'pageSize': 10000, 'pageNum': 1}}
#     try:
#         response = requests.post(url='http://192.168.3.8:9099/inq/data/makeup/paging', headers=headers, data=json.dumps(datas))
#         makeupamount1 = response.json()['result']
#         makeupamount = 0
#         for i in makeupamount1:
#             makeupamount = makeupamount + i['makeupAmount']
#
#         makeupamount = round(makeupamount, 2)
#         print(makeupamount)
#         return makeupamount
#     except requests.exceptions.ConnectionError:
#         print('连接问题')
#     except requests.exceptions.ChunkedEncodingError:
#         print('chuncked编码问题')
#     except:
#         print('error')


def order_paging(datas):
    startAt = datas.split(',')[0]
    endAt = datas.split(',')[1]
    datas = {'startAt': startAt, 'endAt': endAt}
    response = requests.post(url='http://192.168.3.8:9099/usr/order/paging', headers=headers, datas=json.dumps(datas))
    result = response.json()['result']
    print(result)

if __name__ == '__main__':
    # refund_amount = refund('11,511526,2020')
    # refund_amounts = refund_inquiry('11,511526,2020')
    # assert refund_amount == refund_amounts
    # makeup_amounts = makeup_paging('11,511526,2020')
    # makeup_amountss = makeup_amounts('11,511526,2020')
    # assert makeup_amounts == makeup_amountss
    order_paging('2020-11-23 00:00:00,2020-11-23 23:44:11')
