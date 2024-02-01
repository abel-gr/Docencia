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

from pyscript import document
from pyscript import display

def learning_rate_button(event):
    
    learning_rate = float(document.querySelector("#learning_rate_text").value)
    
    # dataset = load_breast_cancer()
    dataset = load_digits()
    
    
    x = dataset.data
    y = dataset.target
    
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=42)
    
    model = MLPClassifier(learning_rate_init=learning_rate, hidden_layer_sizes=(4), random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    
    fig, ax = plt.subplots(1, 1, figsize=(5,5), dpi=150)
    ax.set_title("Confusion matrix\n with learning\n rate = " + str(learning_rate))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=dataset.target_names)
    disp.plot(ax=ax, cmap="Blues", values_format="d")
        
    document.querySelector("#output_confusion_matrix").innerHTML = ""
    display(fig, target="output_confusion_matrix")
    
    document.querySelector("#accuracy").innerText = round(accuracy, 6)
    
    
    fig2, ax2 = plt.subplots(1, 1, figsize=(5,5), dpi=150)
    ax2.plot(model.loss_curve_)
    ax2.set_xlabel("Iteration")
    ax2.set_ylabel("Loss")
    ax2.set_title("Loss curve")
    
    document.querySelector("#output_loss_curve").innerHTML = ""
    display(fig2, target="output_loss_curve")