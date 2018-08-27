# -*- coding: utf-8 -*-
import os

# 获得复制文件的大小
fileTotalSize = os.stat('photo.jpg').st_size
print("fileTotalSize={0}".format(fileTotalSize))
# 读取文件大小
readSize = 0

# 以二进制格式打开一个文件用于读写
file = open('photo.jpg', 'rb' )
# 以二进制格式打开一个文件只用于写入
file2 = open("photo2.jpg", "wb")

while readSize < fileTotalSize:
    #每次读取50K的文件内容
    content = file.read(1024 * 50)
    readSize = readSize + len(content)
    file2.write(content)

# 关闭文件资源
file.close()
file2.close()

