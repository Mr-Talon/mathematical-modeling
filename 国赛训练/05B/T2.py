import csv

csvFile = open("dataT3F2.csv", 'w', newline='', encoding='utf-8')  # 固定格式
writer = csv.writer(csvFile)  # 固定格式
csvRow = []  # 用来存储csv文件中一行的数据

# 对csvRow通过append()或其它命令添加数据
writer.writerow(csvRow)  # 将csvRow中数据写入csv文件中

f=open("C:/Users/16046/Desktop/T3理想解法b x.txt",encoding="utf=8")
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

csvFile.close()
f.close()