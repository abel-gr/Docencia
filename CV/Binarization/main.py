# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:07:39 2024

@author: abelg
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np

from pyscript import document, display, URL
from pyodide.ffi import create_proxy

def load_image(event):
    file = event.target.files[0]
    if not file:
        return

    file_url = URL.createObjectURL(file)

    img = mpimg.imread(file_url)

        
    fig1, ax1 = plt.subplot(1, 1, figsize=(2,2), dpi=200)
    ax1.imshow(img, cmap='gray')
    ax1.axis("off")

    document.querySelector("#output_original_image").innerHTML = ""
    display(fig1, target="output_original_image")


file_input = document.getElementById('imagefile')
file_input.addEventListener('change', create_proxy(load_image))




def learning_rate_button(event):
    
    
    learning_rate = float(document.querySelector("#learning_rate_text").value)