# 공공데이터포털 csv파일 읽기
# 부산광역시 시내버스, 마을버스 햐ㅕㄴ황
import csv

fileNmae = 'busanbus.csv'
dirName = 'C:\source\studyPython2023/'
fullpath = dirName + fileNmae

file = open(fullpath,'r', encoding='utf-8')
reader = csv.reader(file, delimiter=',')
next(reader)

for line in reader:
    print(line)

file.close # 반드시 닫아주세요!