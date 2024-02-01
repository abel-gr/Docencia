# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:07:39 2024

@author: abelg
"""

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import numpy as np

from pyscript import document
from pyscript import display

def learning_rate_button(event):
    
    learning_rate = document.querySelector("#learning_rate_text")
    
    dataset = load_breast_cancer()

    x = dataset.data
    y = dataset.target

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = MLPClassifier(learning_rate_init=learning_rate, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)


    fig, ax = plt.subplots(1, 1, figsize=(5,5), dpi=350)
    ax.set_title("Confusion matrix\n with learning\n rate = " + str(learning_rate))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=dataset.target_names)
    disp.plot(ax=ax, cmap="Blues", values_format="d")
    plt.show()
    
    display(fig, target="output_confusion_matrix")
    
    document.querySelector("#accuracy").innerText = accuracy