import requests
import json

headers = {'Content-Type': 'application/json', 'x-token': 'XX7pxara29285e87658abe84b6d421145def1017XXXXXXXm1'}


# 客户余额详情查询
def balance_inquiry(datas):
    beginAt = datas.split(',')[0]
    endAt = datas.split(',')[1]
    regionId = datas.split(',')[2]
    datas = {
        "beginAt": beginAt,
        "endAt": endAt,
        "regionId": regionId
    }
    try:
        response = requests.post(url='http://192.168.3.66:8084/stat/balance/inquiry', headers=headers, data=json.dumps(datas), timeout=60)
        print(response.json()['result'], '\n', response.elapsed.total_seconds())
    except requests.exceptions.ConnectionError:
        print('连接错误')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')


# 客户余额列表查询8天
def balance_list(datas):
    datas = {'regionId': datas}
    try:
        response = requests.post(url='http://192.168.3.66:8084/stat/balance/list', headers=headers, data=json.dumps(datas), timeout=180)
        print(response.json()['result'], '\n', response.elapsed.total_seconds())
    except requests.exceptions.ConnectionError:
        print('连接错误')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')


# 运营收入统计详情查询
def op_income_inquiry(datas):
    beginAt = datas.split(',')[0]
    endAt = datas.split(',')[1]
    regionId = datas.split(',')[2]
    datas = {
    "beginAt": beginAt,
    "endAt": endAt,
    "regionId": regionId
    }
    try:
        response = requests.post(url='http://192.168.3.66:8084/stat/op_income/inquiry', headers=headers, data=json.dumps(datas), timeout=60)
        # print(response.json()['result'], '\n', response.elapsed.total_seconds())
        a = response.json()['result']
        for key in a.keys():
            print(key, a[key])
        print('请求时间：', response.elapsed.total_seconds(), '秒')
    except requests.exceptions.ConnectionError:
        print('连接错误')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')


# 运营收入统计列表查询
def op_income_list(datas):
    datas = {'regionId': datas}
    try:
        response = requests.post(url='http://192.168.3.66:8084/stat/op_income/list', headers=headers,
                                 data=json.dumps(datas), timeout=60)
        # print(response.json()['result'], '\n', response.elapsed.total_seconds())
        a = response.json()['result']
        for key in a:
            for i in key.keys():
                print(key[i])
        print(response.elapsed.total_seconds())
    except requests.exceptions.ConnectionError:
        print('连接错误')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')


# 客户充值统计列表查询
def top_up_list(datas):
    beginAt = datas.split(',')[0]
    endAt = datas.split(',')[1]
    regionId = datas.split(',')[2]
    datas = {
    "beginAt": beginAt,
    "endAt": endAt,
    "regionId": regionId
    }
    try:
        response = requests.post(url='http://192.168.3.66:8084/stat/top_up/list', headers=headers, data=json.dumps(datas), timeout=60)
        print(response.json()['result'], '\n', response.elapsed.total_seconds())
    except requests.exceptions.ConnectionError:
        print('连接错误')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')


# 车辆数据查询
def op_vehicle_inquiry(datas):
    beginAt = datas.split(',')[0]
    endAt = datas.split(',')[1]
    regionId = datas.split(',')[2]
    datas = {
    "beginAt": beginAt,
    "endAt": endAt,
    "regionId": regionId
    }
    try:
        response = requests.post(url='http://192.168.3.66:8084/stat/op_vehicle/inquiry', headers=headers, data=json.dumps(datas), timeout=60)
        print(response.json()['result'], '\n', response.elapsed.total_seconds())
    except requests.exceptions.ConnectionError:
        print('连接错误')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')


# 用户数据查询
def op_user_inquiry(datas):
    beginAt = datas.split(',')[0]
    endAt = datas.split(',')[1]
    regionId = datas.split(',')[2]
    datas = {'beginAt': beginAt, 'endAt': endAt, 'regionId': regionId}

    try:
        response = requests.post(url='http://192.168.3.66:8084/stat/op_user/inquiry', headers=headers,
                                 data=json.dumps(datas))
        print(response.json()['result'], '\n', response.elapsed.total_seconds())
    except requests.exceptions.ConnectionError:
        print('连接问题')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')

if __name__ == '__main__':
    # balance_inquiry('2020-05-01 00:00:00,2020-05-15 23:59:59,511502')
    # balance_list('511902')
    # op_income_inquiry('2020-01-01 00:00:00,2020-12-31 23:59:59,511902')
    op_income_list('511902')
    # op_vehicle_inquiry('2020-07-01 00:00:00,2020-07-27 23:59:59,511502')
    # top_up_list('2020-05-01 00:00:00,2020-05-15 23:59:59,511502 ')
    # launch_paging('511502,1,null')
    # op_user_inquiry('2020-07-01 00:00:00,2020-07-01 23:59:59,511902')

