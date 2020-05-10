import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from cv2 import cv2
from PIL import Image
import os

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])*255

if __name__ == '__main__':
    PROCESSED = 'processed'
    SRART=0
    
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename)     
        gray = rgb2gray(img)  
        cv2.imwrite('gray32J/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '41'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '42'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '43'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '44'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '45'
    ddirectory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '46'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '47'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '48'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '49'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '4a'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '4b'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '4c'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1


    key = '4d'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '4e'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '4f'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '50'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '51'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '52'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '53'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '54'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '55'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '56'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '57'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '58'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '59'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1

    key = '5a'
    directory_name = PROCESSED+key+'/'
    i=SRART
    for filename in os.listdir(r"./"+directory_name):
        print(filename)
        img = mpimg.imread(directory_name+filename) 
        gray = rgb2gray(img)  
        cv2.imwrite('gray32_'+key+'/transfer'+'%s' % str(i)+'.png',gray)
        i+=1
