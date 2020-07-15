from util.excel_read import excel_read

class Driven:
    def drive_it(self):
        file_path = "test_data_driven.xlsx"
        datas = excel_read(file_path)
        for data in datas:
            print('==========='+data[0]+'=============\n')
            # 动态导入包
            module = __import__("cases."+data[1], fromlist=True)
            # 反射类并实例化
            cla = getattr(module, data[2])()
            # 反射方法
            method = getattr(cla, data[3])
            # 放入参数，执行方法
            method(data[0], data[4], data[5])

if __name__ == '__main__':
    driven = Driven()
    driven.drive_it()
