import xlrd
import length

def excel_read(file_path, index=0):
    #   打开指定路径的excel
    data = xlrd.open_workbook(file_path)
    #   获取整个sheet对象, 默认获取第一张表
    sheet = data.sheets()[index]
    params = []
    for rownum in range(1, sheet.nrows):  # 从excel中的第一行开始循环读取
        list = sheet.row_values(rownum)  # 获取行数据, 为列表形式
        params.append(list)
    return params

if __name__ == '__main__':
    file_path = 'C:\\Users\\Administrator\\Desktop\\5-15-定位延迟终端.xlsx'
    datas = excel_read(file_path, index=0)
    for i in datas:
        print(round(i[0]))
    print(len(datas))
