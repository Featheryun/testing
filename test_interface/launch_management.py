import requests
import json


headers = {'Content-Type': 'application/json', 'x-token': 'XX7pxara29285e87658abe84b6d421145def1017XXXXXXXm1'}


# 投放回收分页查询
def launch_paging(current, size, total, datas):
    # 库存状态 1=投放 2=回收
    flag = datas.split(',')[0]
    # 区域ID
    regionId = datas.split(',')[1]
    # 车辆ID
    vehicleId = datas.split(',')[2]
    datas = {
        'page': {'current': current, 'size': size, 'total': total},
        'regionId': regionId, 'flag': flag, 'vehicleId': vehicleId
    }
    try:
        response = requests.post(url='http://192.168.3.66:8084/iot/launch/paging', headers=headers, data=json.dumps(datas))
        # print(response.json()['result'], '\n', response.elapsed.total_seconds())
        a = response.json()['result']
        if response.status_code == requests.codes.ok:
            print('ok')
        else:
            print('error')
        for i in a:
            for key in i.keys():
                print(key, i[key])
            print('\n')
        print(response.elapsed.total_seconds())
    except requests.exceptions.ConnectionError:
        print('连接问题')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')


# 车辆投放回收详情查询
def launch_inquiry(datas):
    # 记录ID
    id = datas.split(',')[0]
    # 车辆ID（与记录ID 2选1）
    vehicleId = datas.split(',')[1]
    datas = {'id': id, 'vehicleId': vehicleId}
    try:
        response = requests.post(url='http://192.168.3.66:8084/iot/launch/inquiry', headers=headers, data=json.dumps(datas))
        print(response.json()['result'], '\n', response.elapsed.total_seconds())
    except requests.exceptions.ConnectionError:
        print('连接问题')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')


if __name__ == '__main__':
    launch_paging(1, 10, 20, '1,511902,null')