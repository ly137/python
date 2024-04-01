def addition(x, y):  # 实现加法功能
    count = x + y  # 计算两个数的和
    print(f'结果: {count}')  # 输出结果

def subtraction(x, y):  # 实现减法功能
    count = x - y  # 计算两个数的差
    print(f'结果: {count}')  # 输出结果

def multiplication(x, y):  # 实现乘法功能
    count = x * y  # 计算两个数的乘积
    print(f'结果: {count}')  # 输出结果

def division(x, y):  # 实现除法功能
    if y == 0:  # 判断除数是否为零
        print('非法操作，除数不能为零。')  # 如果除数为零，则输出错误提示
    else:
        count = x / y  # 计算两个数的商
        print(f'结果: {count}')  # 输出结果

def calculator():  # 定义计算器函数
    while True:  # 进入循环，持续接收用户输入
        n = int(input("请选择操作：\n1. 加法\n2. 减法\n3. 乘法\n4. 除法\n5. 退出\n"))  # 提示用户选择操作
        if n == 1:  # 如果用户选择加法
            x = int(input("请输入第一个数字："))  # 接收用户输入的第一个数字
            y = int(input("请输入第二个数字："))  # 接收用户输入的第二个数字
            addition(x, y)  # 调用加法函数
        elif n == 2:  # 如果用户选择减法
            x = int(input("请输入第一个数字："))  # 接收用户输入的第一个数字
            y = int(input("请输入第二个数字："))  # 接收用户输入的第二个数字
            subtraction(x, y)  # 调用减法函数
        elif n == 3:  # 如果用户选择乘法
            x = int(input("请输入第一个数字："))  # 接收用户输入的第一个数字
            y = int(input("请输入第二个数字："))  # 接收用户输入的第二个数字
            multiplication(x, y)  # 调用乘法函数
        elif n == 4:  # 如果用户选择除法
            x = int(input("请输入被除数："))  # 接收用户输入的被除数
            y = int(input("请输入除数："))  # 接收用户输入的除数
            division(x, y)  # 调用除法函数
        elif n == 5:  # 如果用户选择退出
            print("再见！")  # 输出退出提示
            break  # 退出循环，结束程序
        else:  # 如果用户输入非法选项
            print("非法操作，请重新选择。")  # 输出错误提示
#调用函数实现计算机功能
calculator()