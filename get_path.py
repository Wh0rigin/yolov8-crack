"""
划分训练集\验证集\测试集的文件的路径
存入train.txt valid.txt test.txt
比例推荐8:1:1
"""
 
from pathlib import Path
import random
 
path_train = Path('./datasets/crack/images')#--图片数据集目录
path_dataset = Path('./datasets/crack/dataSet')#--存放数据集的划分文件
 
f_train = open(path_dataset/'train.txt', 'w')
f_valid = open(path_dataset/'valid.txt', 'w')
f_test = open(path_dataset/'test.txt', 'w')
 
for path in path_train.glob('*.*'):
    i = random.random()
    if i<0.1:
        f_test.write(str(path)+'\n')
    elif i<0.2:
        f_valid.write(str(path)+'\n')
    else:
        f_train.write(str(path)+'\n')
# print(str(path))
 