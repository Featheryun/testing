import requests
import json


headers = {'Content-Type': 'application/json', 'x-token': 'XX7pxara29285e87658abe84b6d421145def1017XXXXXXXm1'}


# 设备维修记录详情查询
def repair_log_inquiry(datas):
    id = datas.split(',')[0]
    vehicleId = datas.split(',')[1]
    datas = {'id': id, 'vehicleId': vehicleId}
    try:
        response = requests.post(url='http://192.168.3.66:8084/iot/repair_log/inquiry', headers=headers, data=datas)
        print(response.json()['result'], '\n', response.elapsed.total_seconds())
    except requests.exceptions.ConnectionError:
        print('连接问题')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')

#
# 设备故障分页查询
def fault_paging(current, size, total, datas):
    regionId = datas.split(',')[0]
    terminalId = datas.split(',')[1]
    vehicleSn = datas.split(',')[2]
    datas = {
        'page':{'current': current, 'size': size, 'total': total},
        'regionId': regionId, 'terminalId': terminalId, 'vehichleSn': vehicleSn
    }
    try:
        response = requests.post(url='http://192.168.3.66:8084/iot/fault/paging', headers=headers, data=json.dumps(datas))
        a = response.json()['result']
        for i in a:
            print(i)
        print(response.elapsed.total_seconds())
    except requests.exceptions.ConnectionError:
        print('连接问题')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')


# 设备故障待确认详情查询
def confirm_fault_submit(datas):
    id = datas.split(',')[0]
    vehicleId = datas.split(',')[1]
    datas = {'id': id, 'vehicleId': vehicleId}
    try:
        response = requests.post(url='http://192.168.3.66:8084/iot/confirm_fault/inquiry', headers=headers, data=json.dumps(datas))
        print(response.json(), '\n', response.elapsed.total_seconds())
    except requests.exceptions.ConnectionError:
        print('连接问题')
    except requests.exceptions.ChunkedEncodingError:
        print('chunked编码问题')
    except:
        print('error')

if __name__ == '__main__':
    # fault_paging(1, 20, 20, '511502,null,null')
    confirm_fault_submit('3325,null')