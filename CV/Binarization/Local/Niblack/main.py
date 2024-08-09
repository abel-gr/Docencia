# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:07:39 2024

@author: abelg
"""

import matplotlib.pyplot as plt

import numpy as np

from pyscript import document, display
from pyodide.ffi import create_proxy

from js import FileReader

import io
import base64


def NiblackThreshold(im, sizeI=4, sizeJ=4, k=1.0):
    img = im.copy()
    
    s1 = img.shape[0]
    s2 = img.shape[1]
    
    sizeI = int(sizeI/2)
    sizeJ = int(sizeJ/2)
    
    if(sizeI <= 0):
        sizeI = 1
        
    if(sizeJ <= 0):
        sizeJ = 1
    
    for i in range(0, s1):
        for j in range(0, s2):
            
            posI1 = i-sizeI
            posI2 = i+sizeI
            
            posJ1 = j-sizeJ
            posJ2 = j+sizeJ
            
            if(posI1 < 0):
                posI1 = 0
            
            if(posI2 >= s1):
                posI2 = s1 - 1
                
            if(posJ1 < 0):
                posJ1 = 0
            
            if(posJ2 >= s2):
                posJ2 = s2 - 1
            
            subImg = im[posI1:posI2, posJ1:posJ2]
                        
            t = np.mean(subImg) + k * np.std(subImg)
                        
            img[i, j] = t
            
    return img

def NiblackBinarization(im, sizeI=4, sizeJ=4, k=1.0):
    t = NiblackThreshold(im, sizeI, sizeJ, k)

    img = im.copy()
    img[img <= t] = 0
    img[img > t] = 1
    
    img[:, 0:9] = 0
    img[:, -9:] = 0
    img[0:9, :] = 0
    img[-9:, :] = 0
    
    return img

def load_image(event):
    file = event.target.files.item(0)
    if not file:
        return
    
    reader = FileReader.new()

    def onload(event):
        data_url = event.target.result

        base64_data = data_url.split(',')[1]

        img_data = io.BytesIO(base64.b64decode(base64_data))

        img = plt.imread(img_data, format='png')
        
        global original_img
        original_img = img

        fig1, ax1 = plt.subplots(1, 1, figsize=(2,2), dpi=200)
        ax1.imshow(img, cmap='gray')
        ax1.axis("off")
        ax1.set_title("Original image", size=5)

        document.querySelector("#output_original_image").innerHTML = ""
        display(fig1, target="output_original_image")
        
        # image = document.getElementById("image");
        # image.src = event.target.result

    onload_event = create_proxy(onload)
    reader.onload = onload_event
    reader.readAsDataURL(file)


original_img = None

file_input = document.getElementById('imagefile')
file_input.addEventListener('change', create_proxy(load_image))


def button(event):
    
    window_size = document.querySelector("#window_size_text").value
    
    if window_size is None:
        document.querySelector("#output_binarization_result").innerHTML = "Write a window size"
        return
    
    if type(window_size) == str:
        if window_size == '' or window_size == ' ':
            document.querySelector("#output_binarization_result").innerHTML = "Write a window size"
            return
    
    window_size = int(window_size)
    
    
    k = document.querySelector("#k_value_text").value

    if k is None:
        document.querySelector("#output_binarization_result").innerHTML = "Write a value of parameter k"
        return
    
    if type(k) == str:
        if k == '' or k == ' ':
            document.querySelector("#output_binarization_result").innerHTML = "Write a value of parameter k"
            return
    
    k = float(k)
    
    
    
    if original_img is None:
        document.querySelector("#output_binarization_result").innerHTML = "Select an image"
        return
    
        
    th_img = NiblackBinarization(np.copy(np.mean(original_img[:, :, 0:3], axis=2) * 255),
                                 sizeI=window_size, sizeJ=window_size, k=k)
    
    
    fig2, ax2 = plt.subplots(1, 1, figsize=(2,2), dpi=200)
    ax2.imshow(th_img, cmap='gray')
    ax2.axis("off")
    ax2.set_title("Image after binarization \n" + "(window_size = " + str(window_size) + ", k = " + str(k) + ")", size=5)

    document.querySelector("#output_binarization_result").innerHTML = ""
    display(fig2, target="output_binarization_result")

    