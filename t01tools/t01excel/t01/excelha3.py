data = []
try:
    # 以只读模式打开文件，使用 utf-8 编码
    with open('d.txt', 'r', encoding='utf-8') as file:
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

import xlwt



# 创建一个新的工作簿
workbook = xlwt.Workbook(encoding='utf-8')

# 创建一个工作表
worksheet = workbook.add_sheet('Sheet1')

# 定义列名
column_names = ['AA', 'BB', 'CC', 'DD', 'EE']

# 写入列名
for col_index, col_name in enumerate(column_names):
    worksheet.write(0, col_index, col_name)

# 写入数据
for row_index, row_data in enumerate(data, start=1):
    for col_index, cell_data in enumerate(row_data):
        worksheet.write(row_index, col_index, cell_data)

# 保存工作簿
workbook.save('electric4.xlsx')

print("数据已成功写入 electric3.xlsx 文件。")