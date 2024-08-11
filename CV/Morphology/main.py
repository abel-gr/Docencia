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


def basic_morph_gray(im, er_dil, sizeI=4, sizeJ=4):
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
                        
            if er_dil==0:
                newValue = np.min(subImg)
            else:
                newValue = np.max(subImg)
                        
            img[i, j] = newValue
            
    return img



def erode(img, sizeI=4, sizeJ=4):
    return basic_morph_gray(img, 0, sizeI, sizeJ)


def dilate(img, sizeI=4, sizeJ=4):
    return basic_morph_gray(img, 1, sizeI, sizeJ)


def opening(img, sizeI=4, sizeJ=4):
    return dilate(erode(img, sizeI, sizeJ), sizeI, sizeJ)


def openingResidue(img, sizeI=4, sizeJ=4):
    return (img.astype(np.int32) - opening(img, sizeI, sizeJ).astype(np.int32))


def closing(img, sizeI=4, sizeJ=4):
    return erode(dilate(img, sizeI, sizeJ), sizeI, sizeJ)


def closingResidue(img, sizeI=4, sizeJ=4):
    return (img.astype(np.int32) - closing(img, sizeI, sizeJ).astype(np.int32))


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
    
    width_value = document.querySelector("#width_value_text").value
    
    if width_value is None:
        document.querySelector("#output_result").innerHTML = "Write a width"
        return
    
    if type(width_value) == str:
        if width_value == '' or width_value == ' ':
            document.querySelector("#output_result").innerHTML = "Write a width"
            return
    
    width_value = int(width_value)
    
    
    height_value = document.querySelector("#height_value_text").value

    if height_value is None:
        document.querySelector("#output_result").innerHTML = "Write a height"
        return
    
    if type(height_value) == str:
        if height_value == '' or height_value == ' ':
            document.querySelector("#output_result").innerHTML = "Write a height"
            return
    
    height_value = int(height_value)
    
    
    
    if original_img is None:
        document.querySelector("#output_result").innerHTML = "Select an image"
        return
    
    
    
    img = np.copy(np.mean(original_img[:, :, 0:3], axis=2) * 255)

    
    if document.querySelector("#morphological_operation_Dilation").checked:
        o_img = dilate(img, sizeI=height_value, sizeJ=width_value)
        morphological_operation = "Dilation"
        
    elif document.querySelector("#morphological_operation_Erosion").checked:
        o_img = erode(img, sizeI=height_value, sizeJ=width_value)
        morphological_operation = "Erosion"
        
    elif document.querySelector("#morphological_operation_Opening").checked:
        o_img = opening(img, sizeI=height_value, sizeJ=width_value)
        morphological_operation = "Opening"
        
    elif document.querySelector("#morphological_operation_Closing").checked:
        o_img = closing(img, sizeI=height_value, sizeJ=width_value)
        morphological_operation = "Closing"
        
    elif document.querySelector("#morphological_operation_OpeningResidue").checked:
        o_img = openingResidue(img, sizeI=height_value, sizeJ=width_value)
        morphological_operation = "Opening Residue"
        
    elif document.querySelector("#morphological_operation_ClosingResidue").checked:
        o_img = closingResidue(img, sizeI=height_value, sizeJ=width_value)
        morphological_operation = "Closing Residue"
        
    else:
        document.querySelector("#output_result").innerHTML = "Select a morphological operation"
        return
        
    
    fig2, ax2 = plt.subplots(1, 1, figsize=(2,2), dpi=200)
    ax2.imshow(o_img, cmap='gray')
    ax2.axis("off")
    ax2.set_title("Image after " + morphological_operation + "\n" + "(str. el. width = " + str(width_value) + ", str. el. height = " + str(height_value) + ")", size=5)

    document.querySelector("#output_result").innerHTML = ""
    display(fig2, target="output_result")

    