data = []
try:
    # 以只读模式打开文件，使用 utf-8 编码
    with open('a.txt', 'r', encoding='utf-8') as file:
        for line in file:
            # 去除每行末尾的换行符
            line = line.strip()
            # 按 ### 分割每行数据
            words = line.split('###')
            # 检查分割后是否刚好有五个词
            if len(words) == 5:
                data.append(words)
            else:
                print(f"警告：行 '{line}' 不包含五个词，已跳过。")
except FileNotFoundError:
    print("文件 'a.txt' 未找到，请检查文件路径。")

# 输出处理后的数据
for row in data:
    print(row)