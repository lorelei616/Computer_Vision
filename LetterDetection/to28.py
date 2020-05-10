from PIL import Image
import matplotlib.pylab as plt
import numpy as np
import os


def picTo01(filename,subname,num):
    """
    将图片转化为28*28像素的文件，
    """
    # 打开图片
    img = Image.open(filename).convert('L')

    # 设置为32*32的大小
    img = img.resize((28,28), Image.LANCZOS)

    # 进行保存，方便查看
    img.save(r'C:/Users/Lorelei/Desktop/手写字体数据/28/'+subname+'/test'+ '%s' % str(num) + '.png')

if __name__ == '__main__':
    # picTo01('hsf_0_00000.png',0)
    SRART = 0
    DIR = 'gray32_'


    key = '41'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '42'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '43'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '44'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '45'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '46'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '47'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '48'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '49'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '4a'
    directory_name =DIR+ key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '4b'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '4c'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)


    key = '4d'
    directory_name =DIR+ key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '4e'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '4f'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '50'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '51'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '52'
    directory_name =DIR+ key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '53'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '54'
    directory_name =DIR+ key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '55'
    directory_name =DIR+ key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '56'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '57'
    directory_name =DIR+ key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '58'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '59'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

    key = '5a'
    directory_name = DIR+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        i+=1
        picTo01(directory_name+filename,key,i)

   


