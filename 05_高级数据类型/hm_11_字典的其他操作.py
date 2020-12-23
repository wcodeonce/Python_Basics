xiaoming_dict = {"name": "小明",
                 "age": 18}

# 1. 统计键值对的数量
print(len(xiaoming_dict))

# 2. 合并字典
temp_dict = {"height": 1.75,
             "age": 20}
# 注意: 如果被合并的字典中包含已经存在的键值对,会覆盖原来的键值对
xiaoming_dict.update(temp_dict)

# 3. 清空字典
xiaoming_dict.clear()

# 输出
print(xiaoming_dict)