import os
from os.path import isdir, exists, abspath, join

import random

import numpy as np
from PIL import Image, ImageEnhance

import torchvision.transforms.functional as TF
import torchvision.transforms

class DataLoader():
    
    def __init__(self, root_dir='data', batch_size=2, test_percent=0.1):
        
        img_filepath=[]
        label_filepath = []
        
        self.batch_size = batch_size
        self.test_percent = test_percent

        self.root_dir = abspath(root_dir)
        self.data_dir = join(self.root_dir,'scans')
        self.labels_dir = join(self.root_dir, 'labels')

        self.files = os.listdir(self.data_dir)

        self.data_files = [join(self.data_dir, f) for f in self.files]
        self.label_files = [join(self.labels_dir, f) for f in self.files]
        
       
        #print (self.files)
        
        #img_filepath = [join(self.data_dir, f) for f in self.files]
        #label_filepath = [join(self.labels_dir, f) for f in self.files]
        
        #print (self.label_files)
    
    def __iter__(self):
        n_train = self.n_train()
        img_file_path = self.data_files
        label_file_path = self.label_files
        
        #print (img_file_path)
        print ('Dataloader')
        
        if self.mode == 'train':
            current = 0
            endId = n_train
        elif self.mode == 'test':
            current = n_train
            endId = len(self.data_files)
    
        while current < endId:
              
            data_image = Image.open(self.data_files[current]) #img_file_path[i]
            label_image = Image.open(self.label_files[current]) #label_file_path[j]

            value = np.random.randint(1,7)
            print ('Value : ', value)
            
            applyDataAugmentation(data_image, label_image, value)
            
            #resizing image and label to 388, 388
            data_image=data_image.resize((388,388))
            label_image=label_image.resize((388,388))                    
                    
            data_image= np.asarray(data_image)
            label_image= np.asarray(label_image)
            
            data_image = np.pad(data_image, (94,94), 'symmetric')
    
            data_image = (data_image/255.0)
      
            #label_image = label_image-1
            #label_image = (label_image/255.0)
            # todo: load images and labels
            # hint: scale images between 0 and 1
            # hint: if training takes too long or memory overflow, reduce image size!

            current += 1
            
            yield (data_image, label_image)
        

    def setMode(self, mode):
        self.mode = mode
        
    def n_train(self):
        data_length = len(self.data_files)
        return np.int_(data_length - np.floor(data_length * self.test_percent))
        

class applyDataAugmentation():

     def __init__(self, data_image, label_image , value): 
        
        print ('Data Augmentation')
        self.image = data_image
        self.label = label_image
        self.value = value
        
        if (self.value==1):
            
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.label = self.label.transpose(Image.FLIP_LEFT_RIGHT)
                
        elif (self.value==2):
            
            self.image = torchvision.transforms.ColorJitter(brightness =0.5, contrast =0.5, saturation = 0.5, hue=0)
            self.label = torchvision.transforms.ColorJitter(brightness =0.5, contrast =0.5, saturation = 0.5, hue=0)
            # enhancer_img = ImageEnhance.Brightness(self.image)
            # enhancer_img = enhancer_img.enhance(2)
            # self.image = enhancer_img
            
            # enhancer_lb = ImageEnhance.Brightness(self.label)
            # enhancer_lb = enhancer_lb.enhance(2)
            # self.label = enhancer_lb
            
        elif (self.value==3):
            self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
            self.label = self.label.transpose(Image.FLIP_TOP_BOTTOM)
            
        elif (self.value == 4):
            self.image = self.image.transpose(Image.ROTATE_90)
            self.label = self.label.transpose(Image.ROTATE_90)
            
        elif (self.value == 5):
        
            self.image= TF.adjust_gamma(self.image, 1.5 , gain=1)
            self.label = TF.adjust_gamma(self.label, 1.5 , gain=1)

        else:
            self.image = data_image
            self.label = label_image

    
