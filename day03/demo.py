import random

# ---------------------- 1. 条件判断示例 ----------------------
print("===== 1. 条件判断示例 =====")
# 多分支成绩评级
score = int(input("请输入考试分数："))
if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"分数：{score}，评级：{grade}")

# 三元表达式
age = 20
status = "成年" if age >= 18 else "未成年"
print(f"年龄{age}：{status}")

# ---------------------- 2. 循环基础示例 ----------------------
print("\n===== 2. 循环基础示例 =====")
# for循环 + range：计算1-100累计和
total = 0
for i in range(1, 101):
    total += i

print(f"1-100累加和：{total}")

# 遍历列表 + continue：只打印偶数
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print("列表中的偶数：", end="")
for num in nums:
    if num % 2 != 0:
        continue  # 跳过奇数
    print(num, end=" ")

print()

# while循环 + break：猜数字基础逻辑
target = 7
count = 0
while True:
    count += 1
    guess = int(input("请一个1-100的数字："))
    if guess == target:
        print(f"猜对了！一共猜了{count}次")
        break  # 猜对就退出循环
    elif guess > target:
        print("大了，再小一点")
    else:
        print("小了，再大一点")

# ---------------------- 3. 函数基础示例 ----------------------
print("\n===== 3. 函数基础示例 =====")


# 无参数无返回值函数
def print_separator():
    """打印分割线"""
    print("-" * 30)


# 必选参数 + 返回值
def add(a, b):
    """计算两个数的和"""
    return a + b


# 默认参数
def greet(name, msg="你好"):
    """打招呼函数，msg有默认值"""
    return f"{msg}，{name}！"


# 多返回值函数
def calc(a, b):
    """同时返回两个数的和与差"""
    return a + b, a - b


# 函数调用测试
print_separator()
print(f"3 + 5  = {add(3, 5)}")
print(greet("张三"))
print(greet("李四", "早上好"))

sum_ab, sub_ab = calc(10, 4)
print(f"和：{sum_ab}，差：{sub_ab}")

# ---------------------- 4. 综合练习1：猜数字游戏 ----------------------
print("\n===== 4. 综合练习：猜数字游戏 =====")


def guess_number_game():
    """猜数字游戏主函数"""
    target_num = random.randint(1, 100)
    guess_count = 0
    print("游戏开始！我想了一个1-100之间的数字，你来猜~")

    while True:
        guess_count += 1
        try:
            user_guess = int(input(f"请输入你猜的数字："))
        except ValueError:
            print("请输入有效的整数！")
            continue

        if user_guess < 1 or user_guess > 100:
            print("数字必须在1-100之间！")
            continue

        if user_guess == target_num:
            print(f"🎉 恭喜你猜对了！答案就是{target_num}")
            print(f"📊 你一共猜了{guess_count}次")
            break
        elif user_guess > target_num:
            print("📉 大了，再小一点")
        else:
            print("📈 小了，再大一点")


# 启动游戏
guess_number_game()

# ---------------------- 5. 综合练习2：简易计算器 ----------------------
print("\n===== 5. 综合练习：简易计算器 =====")


def calculator():
    """简易加减乘除计算器"""
    print("支持运算：+ - * /")
    num1 = float(input("请输入第一个数字："))
    op = input("请输入运算符：")
    num2 = float(input("请输入第二个数字："))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("❌ 错误：除数不能为0")
            return
        result = num1 / num2
    else:
        print("❌ 不支持的运算符")
        return

    print(f"计算结果：{num1} {op} {num2} = {result}")


# 启动计算器
calculator()
