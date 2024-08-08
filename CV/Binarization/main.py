# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:07:39 2024

@author: abelg
"""

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.datasets import load_breast_cancer, load_digits
import matplotlib.pyplot as plt
import numpy as np
import cv2

from pyscript import document
from pyscript import display

image = np.fromfile('tshirt_grayscale0.txt', dtype=np.uint8)
image = image.reshape(540,540)

fig1, ax1 = plt.subplot(1, 1, figsize=(2,2), dpi=200)
ax1.imshow(image, cmap='gray')
ax1.axis("off")

document.querySelector("#output_original_image").innerHTML = ""
display(fig1, target="output_original_image")

def learning_rate_button(event):


    
    learning_rate = float(document.querySelector("#learning_rate_text").value)