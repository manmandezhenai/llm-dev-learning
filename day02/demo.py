# ---------------------- 1. 列表基础操作 ----------------------
print("===== 1. 列表基础操作 =====")
# 创建列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print(f"初始列表：{fruits}")

# 增删改操作
fruits.append("芒果")  # 末尾添加
print(f"append后：{fruits}")

fruits.insert(1, "西瓜")  # 指定位置插入
print(f"insert后：{fruits}")

fruits[0] = "红富士苹果"
print(f"修改后：{fruits}")  # 修改元素

fruits.remove("橙子")  # 删除指定元素
print(f"remove后：{fruits}")

pop_item = fruits.pop()
print(f"pop删除的元素：{pop_item}，剩余列表：{fruits}")

# 切片操作
print(f"索引1-3元素：{fruits[1:4]}")
print(f"反转列表：{fruits[::-1]}")

# 排序与长度
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()
print(f"升序排序：{nums}")
print(f"列表长度：{len(nums)}")

# ---------------------- 2. 字典基础操作 ----------------------
print("\n===== 2. 字典基础操作 =====")
# 创建字典
student = {
    "name": "张三",
    "age": 21,
    "major": "软件工程"
}
print(f"初始字典：{student}")

# 增改操作
student["phone"] = "19126489556"
student["age"] = 22
print(f"增改后：{student}")

# 查询操作
print(f"直接访问姓名：{student['name']}")
print(f"get访问不存在的key：{student.get('gender', '未知')}")

# 遍历键值对
print("\n遍历所有键值对：")
for key, value in student.items():
    print(f"    {key}：{value}")

# 删除操作
student.pop("major")
print(f"\n删除major后：{student}")

# ---------------------- 3. 元组与集合 ----------------------
print("\n===== 3. 元组与集合 =====")
# 元组与解包
info = ("李四", 20, "软件工程")
name, age, major = info
print(f"元组解包：姓名 - {name}，年龄 - {age}，专业 - {major}")
print(f"元组索引0：{info[0]}")

# 集合：自动去重 + 集合运算
nums = [1, 2, 2, 3, 3, 3, 4, 5]
unique_nums = list(set(nums))
print(f"去重后列表：{unique_nums}")

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(f"交集：{s1.intersection(s2)}")
print(f"并集：{s1.union(s2)}")
print(f"差集（s1-s2）：{s1.intersection(s2)}")

# ---------------------- 4. 综合练习：简易通讯录管理 ----------------------
print("\n===== 4. 综合练习：简易通讯录管理 =====")
# 数据结构：列表存储所有联系人，每个联系人是一个字典
contact_book = []


def add_contact(name, phone, email):
    """添加联系人"""
    contact = {"name": name, "phone": phone, "email": email}
    contact_book.append(contact)
    print(f"✅ 已添加联系人：{name}")


def search_contact(name):
    """按姓名查找联系人，找到返回字典，找不到返回None"""
    for contact in contact_book:
        if contact["name"] == name:
            return contact

    return None


def show_all_contacts():
    """显示所有联系人"""
    print("\n===== 通讯录列表 =====")
    if not contact_book:
        print("通讯录为空！")
        return

    for index, contact in enumerate(contact_book, 1):
        email = contact.get("email", "未填写")
        print(f"{index}. 姓名：{contact['name']} | 电话：{contact['phone']} | 邮箱：{email}")


# 功能测试
add_contact("张三", "19126489556", "1758994523@qq.com")
add_contact("李四", "15362979257", "lisi@example.com")

show_all_contacts()

# 查找联系人
result = search_contact("李四")
if result:
    print(f"\n🔍 【查找结果】姓名：{result['name']}，电话：{result['phone']}，邮箱：{result['email']}")
else:
    print(f"\n🔍 未找到该联系人")

# 删除联系人
target = search_contact("张三")
if target:
    contact_book.remove(target)
    print("\n🗑️ 已删除联系人张三")

show_all_contacts()