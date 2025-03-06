import xlwt

# 示例数据
data = [
    ['AA1', 'BB1', 'CC1', 'DD1', 'EE1'],
    ['AA2', 'BB2', 'CC2', 'DD2', 'EE2'],
    ['AA3', 'BB3', 'CC3', 'DD3', 'EE3']
]

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
workbook.save('hada.xlsx')

print("数据已成功写入 hada.xlsx 文件。")