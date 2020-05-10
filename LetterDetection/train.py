# -*- coding: utf-8 -*-
import generateInput
import tensorflow as tf
try:
    import tensorflow.python.keras as keras
except:
    import tensorflow.keras as keras
from tensorflow.python.keras import layers

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from tensorflow.keras.utils import to_categorical
import numpy as np
#读取图片的np.array列表以及标签列表
#分别存储到x,y中
x_train,y_train,x_test,y_test= generateInput.get_files('28/',0.2)

#训练集末尾增加维度，转化成（b,h,w,c)的格式
X_train4D = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32')
X_test4D = x_test.reshape(x_test.shape[0], 28, 28, 1).astype('float32')

X_train4D_Normalize = X_train4D / 255 # 除以 255 是为了归一化。
X_test4D_Normalize = X_test4D / 255

y_trainOnehot = to_categorical(y_train) #one-hot编码
y_testOnehot = to_categorical(y_test)
#顺序模型：多个网络的线性堆叠
model = Sequential() #Sequential用于建立序列模型

#使用add()方法将各层添加到模型中
# 一层卷积
#输入：(b,28,28,1);输出：(b,28,28,16)
model.add(
    Conv2D(
        filters=16, #滤波器的数量
        kernel_size=(5, 5),  #卷积核大小5*5
        padding='same',  #保证卷积核大小
        input_shape=(28, 28, 1),  #输入
        activation='relu')) #激活函数选择relu
# 池化层1、
#输入(b,28,28,16)，输出(b,14,14,16)
model.add(MaxPool2D(pool_size=(2, 2)))
#在训练过程中每次更新时将输入单元按比例随机设置为0，防止过拟合
model.add(Dropout(0.25))

# 二层卷积
#输入(b,14,14,16)，输出(b,14,14,32)
model.add(
    Conv2D(filters=32, kernel_size=(5, 5), padding='same', activation='relu'))
# 池化层2
#输入(b,14,14,32)，输出(b,7,7,32)
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(  #输入(b,7,7,32)，输出(b,7,7,64)
    Conv2D(filters=64, kernel_size=(5, 5), padding='same', activation='relu'))
model.add(  #输入(b,7,7,32)，输出(b,7,7,128)
    Conv2D(filters=128, kernel_size=(5, 5), padding='same', activation='relu'))
#输入(b,7,7,32)，输出(b,3,3,128)
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())  # 平坦层
model.add(Dense(128, activation='relu'))  # 全连接层
model.add(Dropout(0.25)) 
model.add(Dense(91, activation='softmax')) # 激活函数

# 优化器选择 Adam 优化器。
# 损失函数使用 categorical_crossentropy，
#metrics=['accuracy']指的是训练和测试期间的模型评估标准
# 训练模型
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
# 以给定数量的轮次训练模型
# y=y_trainOnehot,x=X_train4D_Normalize：训练数据的numpy数组
# validation_split：用作验证集的训练数据比例（这里用的是课上讲的train、test、validation）
# batch_size设为300：防止underfitting或者内存容量无法满足需求
# verbose设为2，每迭代一轮显示一行
train_history = model.fit(x=X_train4D_Normalize,
                          y=y_trainOnehot,
                          validation_split=0.2,
                          batch_size=300,
                          epochs=10,
                          verbose=2)


# evaluate 用于评估模型，返回的数值分别是损失和指标。
#model.fit(x_train,y_train,epochs=10)
# 将整个模型保存为HDF5文件
model.save('my_model.h5')
model.evaluate(X_test4D_Normalize,y_testOnehot)