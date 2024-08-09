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

from skimage.filters import threshold_niblack

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
        document.querySelector("#output_binarization_result").innerHTML = "Write a window size"
        return
    
    if type(k) == str:
        if k == '' or k == ' ':
            document.querySelector("#output_binarization_result").innerHTML = "Write a window size"
            return
    
    k = float(k)
    
    
    
    if original_img is None:
        document.querySelector("#output_binarization_result").innerHTML = "Select an image"
        return
    
    
    thresh_niblack = threshold_niblack(np.mean(original_img[:, :, 0:3], axis=2) * 255, window_size=window_size, k=k)
    
    th_img = original_img > thresh_niblack
    
    
    fig2, ax2 = plt.subplots(1, 1, figsize=(2,2), dpi=200)
    ax2.imshow(th_img, cmap='gray')
    ax2.axis("off")
    ax2.set_title("Image after binarization \n" + "(window_size = " + str(window_size) + "k = " + str(k) + ")", size=5)

    document.querySelector("#output_binarization_result").innerHTML = ""
    display(fig2, target="output_binarization_result")

    