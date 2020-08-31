# Image Segmentation using U-Net

 • Deep learning approach to segment images(foreground and background) using U-Net architecture. 
 
 • Dataset consists of cell images and ground truth labels(foreground, background). Applied various data augmentation techniques such as: 
 
    i) Flip image and labels vertically.
    ii) Flip images and labels horizontally.
    iii) Increase brightness, contrast and saturation of images and labels.
    iv) Rotate images and labels by 90 degrees.
 
 • Trained the model for ~40 epochs on GPU using SGD as the optimizer. Resultant model was used to used to segment the cell images.
 
## U-Net Architecture:

<p align="center">
  <img width=650 height=500 src="/images/arch.JPG">
</p>

## Visualizing the results:

<p align ="center"> Images from left to right (Original -- Ground Truth -- Segmented Image): </p>

<p align="center">
  <img src="/images/seg1.JPG">
</p>

<p align="center">
  <img src="/images/seg2.JPG">
</p>
