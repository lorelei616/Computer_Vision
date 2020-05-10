import tensorflow as tf
try:
    import tensorflow.python.keras as keras
except:
    import tensorflow.keras as keras
from tensorflow.python.keras import layers

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from tensorflow.keras.utils import to_categorical
import os
import math
import numpy as np
import matplotlib.image as mpimg
from PIL import Image

def char2int(char):  #用于将16进制转化为10进制
    if char=='a':
        return 10
    if char=='b':
        return 11
    if char=='c':
        return 12
    if char=='d':
        return 13
    if char=='e':
        return 14
    if char=='f':
        return 15

#image、label分别传入图片和标签的空List，从相应文件夹中读取图片，label保存相应的标签
def get_append(file_dir,key,image,label): 
    for file in os.listdir(file_dir+key):
        image.append(file_dir +key+'/'+ file) 
        if(key[1]!='a' and key[1]!='b' and key[1]!='c' and key[1]!='d' and key[1]!='e' and key[1]!='f'):
            label.append((int(key)%10)+(int(key)//10)*16)
        else:
            unit = char2int(key[1])
            decade = int(key[0])
            label.append(unit+decade*16)
        

def get_files(file_dir, ratio):
    image_list = [] #保存图像存储路径的list
    label_list = [] #保存label的list
    get_append(file_dir,'41',image_list,label_list)#A
    get_append(file_dir,'42',image_list,label_list)#B
    get_append(file_dir,'43',image_list,label_list)#C
    get_append(file_dir,'44',image_list,label_list)
    get_append(file_dir,'45',image_list,label_list)
    get_append(file_dir,'46',image_list,label_list)
    get_append(file_dir,'47',image_list,label_list)
    get_append(file_dir,'48',image_list,label_list)
    get_append(file_dir,'49',image_list,label_list)
    get_append(file_dir,'4a',image_list,label_list)
    get_append(file_dir,'4b',image_list,label_list)
    get_append(file_dir,'4c',image_list,label_list)
    get_append(file_dir,'4d',image_list,label_list)
    get_append(file_dir,'4e',image_list,label_list)
    get_append(file_dir,'4f',image_list,label_list)
    get_append(file_dir,'50',image_list,label_list)
    get_append(file_dir,'51',image_list,label_list)
    get_append(file_dir,'52',image_list,label_list)
    get_append(file_dir,'53',image_list,label_list)
    get_append(file_dir,'54',image_list,label_list)
    get_append(file_dir,'55',image_list,label_list)
    get_append(file_dir,'56',image_list,label_list)
    get_append(file_dir,'57',image_list,label_list)
    get_append(file_dir,'58',image_list,label_list)
    get_append(file_dir,'59',image_list,label_list)
    get_append(file_dir,'5a',image_list,label_list)#Z

    print('image_list length:'+'%s'%len(image_list))#输出image list的长度
    print('label_list length'+'%s'%len(label_list))#输出label list的长度

    #将image_list与label_list合并为二维矩阵
    temp = np.array([image_list, label_list])  

    #设置 Dataset 对象随机打散数据之间的顺序，防止每次训练时数据按固定顺序产生，从而使得模型尝试“记忆”住标签信息
    temp = temp.T
    np.random.shuffle(temp) 

    shuffled_image_list = list(temp[:,0]) #从打乱的list中取出image
    shuffled_label_list = list(temp[:,1]) #取出label

    total_length = len(shuffled_image_list)  #总长度
    validate_length = (int)(math.ceil(ratio*total_length)) #验证集长度
    train_length = total_length - validate_length #训练集长度

    #将图片转化成二维array，范围0~255，
    shuffled_array_image_list = np.zeros([total_length,28,28])
    for i in range(total_length):
        shuffled_array_image_list[i] = 255-255*mpimg.imread(shuffled_image_list[i])

    train_image = shuffled_array_image_list[0:train_length]
    train_label = shuffled_label_list[0:train_length]
    train_label = np.array(train_label)
    validate_image = shuffled_array_image_list[train_length:-1]
    validate_label = shuffled_label_list[train_length:-1]
    validate_label = np.array(validate_label)

    return train_image,train_label,validate_image,validate_label


# x_train,y_train,x_test,y_test= get_files('28/',0.2)
# print(x_train[0])
# print(x_train.shape)
# print(y_train[0])
# print(y_train.shape)

   