import requests
import json


headers = {'Content-Type': 'application/json', 'x-token': 'XX7pxara29285e87658abe84b6d421145def1017XXXXXXXm1'}


# opStatus	integer($int32) 运维状态 1=挪车中 2=换电中 3=维修中 4=现场排障中
# regionId*	integer($int32) 区域ID
# vehicleStatus	integer($int32)
# 车辆状态 0=正常 1=失联 2=离线 3=收车 4=故障不可用 5=缺电 6=服务区外 7=禁停区内 8=待排查故障 9=低电 10=闲置 11=故障可用 12待保养
def device_list(datas):
    opStatus = datas.split(',')[0]
    regionId = datas.split(',')[1]
    vehicleStatus = datas.split(',')[2]
    datas = {'opStatus': opStatus, 'regionId': regionId, 'vehicleStatus': vehicleStatus}
    try:
        response = requests.post(url='http://192.168.3.66:8084/monitor/device/list', headers=headers, data=json.dumps(datas))
        a = response.json()['result']
        b = 0
        for i in a:
            b+=1
            print(i)
        print(b, response.elapsed.total_seconds())
    except requests.exceptions.ConnectionError:
        print('连接问题')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')


# 设备监控列表查询
# regionId*	integer($int32)  区域ID
# status	integer($int32)  员工状态 0=空闲 1=挪车中 2=换电中 3=排查中 4=维修中 5=保养中
def staff_list(datas):
    regionId = datas.split(',')[0]
    status = datas.split(',')[1]
    datas = {'regionId': regionId, 'status': status}
    try:
        response = requests.post(url='http://192.168.3.66:8084/monitor/staff/list', headers=headers, data=json.dumps(datas))
        a = response.json()['result']
        b = 0
        for i in a:
            print(i)
            b += 1
        print(b, response.elapsed.total_seconds())
    except requests.exceptions.ConnectionError:
        print('连接问题')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')


def refund(datas):
    month = datas.split(',')[0]
    regionId = datas.split(',')[1]
    year = datas.split(',')[2]
    datas = {'month': month, 'regionId': regionId, 'year': year, 'page':{'pageSize': 200, 'pageNum': 1}}
    try:
        response = requests.post(url='http://192.168.3.66:9099/inq/data/refund/paging', headers=headers, data=json.dumps(datas))
        a = response.json()['result']
        b = 0
        for i in a:
            b = b + i['refundAmount']
        b = round(b, 2)
        print(b)
        return b
    except requests.exceptions.ConnectionError:
        print('连接问题')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')


def refund_inquiry(datas):
    month = datas.split(',')[0]
    regionId = datas.split(',')[1]
    year = datas.split(',')[2]
    datas = {'month': month, 'regionId': regionId, 'year': year}
    try:
        response = requests.post(url='http://192.168.3.66:9099/inq/data/refund/inquiry', headers=headers, data=json.dumps(datas))
        a = response.json()['result']['amount']
        print(a)
        return a
    except requests.exceptions.ConnectionError:
        print('连接问题')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')


def makeup_amount(datas):
    month = datas.split(',')[0]
    regionId = datas.split(',')[1]
    year = datas.split(',')[2]
    datas = {'month': month, 'regionId': regionId, 'year': year}
    try:
        response = requests.post(url='http://192.168.3.66:9099/inq/data/makeup/inquiry', headers=headers, data=json.dumps(datas))
        makeupamount = response.json()['result']['amount']
        print(makeupamount)
        return makeupamount
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
    try:
        response = requests.post(url='http://192.168.3.66:9099/inq/data/makeup/paging', headers=headers, data=json.dumps(datas))
        makeupamount1 = response.json()['result']
        makeupamount = 0
        for i in makeupamount1:
            makeupamount = makeupamount + i['makeupAmount']

        makeupamount = round(makeupamount, 2)
        print(makeupamount)
        return makeupamount
    except requests.exceptions.ConnectionError:
        print('连接问题')
    except requests.exceptions.ChunkedEncodingError:
        print('chuncked编码问题')
    except:
        print('error')



if __name__ == '__main__':
    # device_list('null,511902,null')
    # staff_list('511902,0')
    a = refund('10,511526,2020')
    b = refund_inquiry('10,511526,2020')
    assert a == b
    print(type(a), type(b))
    # c = makeup_amount('10,511526,2020')
    # d = makeup_paging('10,511526,2020')
    # assert c == d