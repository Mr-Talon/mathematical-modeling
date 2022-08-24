import csv

csvFile = open("ans2-3.csv", 'w', newline='', encoding='utf-8')  # 固定格式
writer = csv.writer(csvFile)  # 固定格式
csvRow = []  # 用来存储csv文件中一行的数据

# 对csvRow通过append()或其它命令添加数据
writer.writerow(csvRow)  # 将csvRow中数据写入csv文件中

f=open("C:/Users/16046/Desktop/ans2-3.txt",encoding="utf=8")
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

csvFile.close()
f.close()