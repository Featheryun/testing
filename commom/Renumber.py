import xlrd
import xlwt

# 读文件
def excel_read(file_path, index=0):
    #   打开指定路径的excel
    data = xlrd.open_workbook(file_path)
    #   获取整个sheet对象, 默认获取第一张表
    sheet = data.sheets()[index]
    params = []
    for rownum in range(0, sheet.nrows):  # 从excel中的第一行开始循环读取
        list = sheet.row_values(rownum)  # 获取行数据, 为列表形式
        params.append(list)
    return params

# 写入文件
def excel_write(file_path, datas):
    workbook = xlwt.Workbook()
    table = workbook.add_sheet('sheet 1', cell_overwrite_ok=True)
    j = 0
    for i in datas:
        table.write(j, 0, i[0])
        j = j + 1
    workbook.save(file_path)

# file1去除file2中同样的数据（file1-file2），并写入new_file
def excel_a_b(file1, file2, new_file):
    datas1 = excel_read(file1, index=0)
    datas2 = excel_read(file2, index=0)
    for i in datas2:
        for j in datas1:
            if i == j:
                datas1.remove(i)
    print(len(datas1))
    excel_write(new_file, datas1)


if __name__ == '__main__':
    # file_path1 = 'C:\\Users\\Administrator\\Desktop\\5-15-定位延迟终端.xlsx'
    # file_path2 = 'C:\\Users\\Administrator\\Desktop\\未升级设备.xlsx'
    # datas1 = excel_read(file_path1, index=0)
    # print(len(datas1))
    # datas2 = excel_read(file_path2, index=0)
    # print(len(datas2))
    # for i in datas2:
    #     for j in datas1:
    #         if i == j:
    #             datas1.remove(j)
    # print(datas1)
    # print(len(datas1))
    # excel_write('已升级终端.xls', datas1)
    file_path1 = 'C:\\Users\\Administrator\\Desktop\\work\\所有终端号.xlsx'
    file_path2 = 'C:\\Users\\Administrator\\Desktop\\终端以及语音升级成功的编号.xlsx'
    excel_a_b(file_path1, file_path2, '未升级终端号.xls')




