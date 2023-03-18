from processing_tables.dto import DTO
import re
import numpy as np 
from processing_tables.variant_controller import VariantController
import os


def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            print(os.path.join(dir, f))
            os.remove(os.path.join(dir, f))

purge('test_dir/1/', f'state_{0}')


# pathToEncry = os.path.abspath(os.curdir) + '/report_answer'
# files = os.listdir(pathToEncry)
# photoFiles = [file for file in files if ".txt" in file]
# print(photoFiles)

# vc = VariantController()

# vc.getAllNumberOfVariant()



# dto = DTO()
# dto.cipherOfWorks = [1, 2, 3, 4]
# dto.duration = [2, 4, 5, 6]
# dto.performers = [2, 3, 8, 9]
# dto.numberOfPerformers = [3, 4, 5, 6]
# dto.numberOfDivision = [8, 6]
# dto.numberOfPeople = [5, 5]
# dictionaryParametrs = dto.__dict__

# listData = []

# for key in dictionaryParametrs:
#     if type(dictionaryParametrs[key]) == list:
#         listData.append(dictionaryParametrs[key]) 



# length = len(listData[0])

# for i in listData:
#     while len(i) < length:
#         i.append(-1)

# print(listData)
# l = [] 
# l = list(map(list, zip(*listData)))
# for i in l:
#     try:
#         while True:
#             i.remove(-1)
#     except:
#         pass
# print(l)

# fileName = 'variant_table_data.txt'
# lis = [['1', '2', '3'], ['4', '3'], ['9', '7', '6', '5', '4'], ['1'], ['2'], ['3'], ['4'], ['5']]

# f = open(fileName,'a+')
# try:
#     # работа с файлом
#     f.write('1' + '\n')
#     print("OK write")
# finally:
#     f.close()

# f = open(fileName,'a+')
# try:
#     # работа с файлом
#     listData = lis

#     for row in listData:
#         f.write(' '.join([a for a in row]) + '\n')
#     print("OK write")
# finally:
#     f.close()

# f = open(fileName,'r+')
# try:
#     # работа с файлом
#     listData = []
#     lines = f.readlines()
#     for line in lines:
#         l = re.split(' |\n', line)
#         try:
#             l.remove('')
#         except:
#             pass
#         print(l)
#         listData.append(l)
    
#     print(listData)

    
#     i = 0
#     for key in dictionaryParametrs:
#         if type(dictionaryParametrs[key]) == str:
#             dictionaryParametrs[key] = listData[i][0]
#         elif type(dictionaryParametrs[key]) == list:
#             dictionaryParametrs[key] = listData[i]
#         print(i)
#         i = i + 1
    
#     print(dto.cipherOfWorks)
#     print(dto.duration)
#     print(dto.variant)

# finally:
#     f.close()