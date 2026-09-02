# ---------------------- 1. Hello World 入门 ----------------------
print("===== 1. Hello World 测试 =====")
# 第一个Python程序
print("Hello，World！")

# ---------------------- 2. 变量与基本数据类型 ----------------------
print("\n===== 2. 变量与数据类型 =====")
# 定义不同类型的变量
name = "李明"  # 字符串
age = 21  # 整数
height = 1.78  # 浮点数
is_student = True  # 布尔值

# 打印变量和类型
print(f"姓名：{name} | 类型：{type(name)}")
print(f"年龄：{age} | 类型：{type(age)}")
print(f"身高：{height} | 类型：{type(height)}")
print(f"是否学生：{is_student} | 类型：{type(is_student)}")

# 变量动态类型特性
variable = 100
print(f"variable初始值：{variable} | 类型：{type(variable)}")
variable = "现在变成字符串了"
print(f"variable修改后：{variable} | 类型：{type(variable)}")

# ---------------------- 3. print 进阶用法 ----------------------
print("\n===== 3. print 进阶用法 =====")
# sep参数：分隔符
print("Python", "Git", "RAG", "Agent", sep="-")

# end参数：结尾符
print("第一行", end=" → ")
print("第二行")

# ---------------------- 4. input 输入交互 ----------------------
print("\n===== 4. 输入交互测试 =====")
# 注意：input返回的是字符串
user_name = input("请输入你的名字：")
user_age = int(input("请输入你的年龄："))  # 转整数
user_score = float(input("请输入你的编程基础分（0-100）："))  # 转浮点数

print(f"\n你好，{user_name}！")
print(f"你的年龄是：{user_age}岁，明年你就{user_age + 1}岁了。")
print(f"你的基础分为：{user_score}分，继续加油！")

# ---------------------- 5. 综合小练习：个人信息登记卡 ----------------------
print("\n===== 5. 综合练习：个人信息登记卡 =====")
print("------ 学生信息登记系统 ------")
stu_id = input("请输入学号：")
stu_name = input("请输入姓名：")
stu_major = input("请输入专业：")
stu_grade = input("请输入年级：")
gpa = float(input("请输入GPA："))

# 格式化输出
print("\n======================")
print("      学生信息卡      ")
print("======================")
print(f"学号：{stu_id}")
print(f"姓名：{stu_name}")
print(f"专业：{stu_major}")
print(f"年级：{stu_grade}年级")
print(f"GPA：{gpa}")
print("======================")
print("信息登记完成！")
