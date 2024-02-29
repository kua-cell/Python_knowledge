"""
闭包：
在函数嵌套的前提下，内部函数使用了外部函数的变量，
并且外部函数返回了内部函数，我们把这使用了外部函数变量的内部函数成为闭包
"""

# 原代码：
# account_amount = 0        # 账户余额
# def atm(num,deposit = True):
#    global account_amount
#    if deposit:
#        account_amount += num
#        print(f"存款：+{num}, 账户余额：{account_amount}")
#    else:
#        account_amount -= num
#        print(f"取款:-{num}, 账户余额：{account_amount}")


# atm(300)
# atm(300)
# atm(100, False)

# 闭包后的代码:
def account_create(initial_amount=0):       #默认初始值：initial_amount=0
    def atm(num, deposit=True):
        nonlocal initial_amount       # 使用nonlocal关键字修饰外部函数的变量，才可以在内部变量中修改它
        if deposit:                   #否则，外部函数变量不会变
            initial_amount += num
            print(f"存款：+{num}, 账户余额：{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款:-{num}, 账户余额：{initial_amount}")

    return atm


fn = account_create()
fn(300)
fn(300)
fn(300, False)

# 简单闭包：
