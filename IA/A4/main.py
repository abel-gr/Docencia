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

def draw(n_layer0, hiddenL, textSize=9, customRadius=0, showLegend=True, showInputLayer=True):
    fig = plt.figure(figsize=(10,8), dpi=250)

    ax = fig.subplots()
    
    ax.set_title("Layers and neurons of the multilayer perceptron")
    ax.set_xlim(xmin=0, xmax=1)
    ax.set_ylim(ymin=0, ymax=1)

    xmin, xmax, ymin, ymax = ax.axis()

    xdim = xmax - xmin
    ydim = ymax - ymin

    space_per_layer = xdim / (len(hiddenL) + 1)

    x0 = xmin
    x1 = xmin + space_per_layer

    medio_intervalo = space_per_layer / 2

    if customRadius <= 0:
        radio = 1 / ((sum(hiddenL) + (n_layer0 if showInputLayer == True else 0)) * 5)
    else:
        radio = customRadius

    lista_lineas_xy = []
    
    lasth = n_layer0
    
    num_FC_layers = len(hiddenL) + 1

    # For each layer
    for capa, h in enumerate([n_layer0] + hiddenL):
        
        if capa == 0 and showInputLayer == False:
            continue
        
        space_per_neuron = ydim / h
        y0 = ymin
        y1 = ymin + space_per_neuron
        medio_intervalo_n = space_per_neuron / 2
        lista_lineas_xy_pre = []
        ne = (lasth * h) - 1
        neY = h - 1
        
        if showLegend:
            if capa == 0:
                plot_label = "Input layer"
                neuron_color = 'r'
            elif capa + 1 == num_FC_layers:
                plot_label = "Output layer"
                neuron_color = 'b'
            else:
                plot_label = "Hidden layer"
                neuron_color = 'g'

                if capa > 1:
                    plot_label = "_" + plot_label # Avoid displaying the same label in the legend for each hidden layer
        else:
            plot_label = ""
            neuron_color = 'r'
                
        # For each neuron in this layer
        for j in range(0, h):
            plot_label = plot_label if j == 0 else ("_" + plot_label) # Avoid displaying the same label in the legend for each neuron in that layer
            
            ax.add_patch(plt.Circle(((medio_intervalo + x0), (medio_intervalo_n + y0)), radio, color=neuron_color, label=plot_label, zorder=1))
            
            neX = lasth - 1

            # For each input to this neuron
            for xy in lista_lineas_xy:
                ax.plot([xy[0],(medio_intervalo + x0)],[xy[1], (medio_intervalo_n + y0)], zorder=0)

                my = ((medio_intervalo_n + y0) - xy[1])
                mx = ((medio_intervalo + x0) - xy[0])
                pendiente = my / mx
                ordenada_origen = xy[1] - pendiente * xy[0]
                margen_ord = 0.015
                if pendiente < 0:
                    margen_ord = -0.045 # compensate text rotation
                ordenada_origen = ordenada_origen + margen_ord # add the text above the line
                                                                
                ne = ne - 1
                neX = neX - 1 # Index of the neuron of the previous layer

            lista_lineas_xy_pre.append([(medio_intervalo + x0), (medio_intervalo_n + y0)])
            
            neY = neY - 1 # Index of the neuron of the current layer

            y0 = y0 + space_per_neuron
            y1 = y1 + space_per_neuron
            
        lasth = h

        x0 = x0 + space_per_layer
        x1 = x1 + space_per_layer

        lista_lineas_xy = lista_lineas_xy_pre

    if showLegend:
        ax.legend(loc='best')
        
    return fig

def learning_rate_button(event):
    
    learning_rate = float(document.querySelector("#learning_rate_text").value)
    hidden_layer_sizes_str = str(document.querySelector("#hidden_layer_sizes_text").value)
    
    hidden_layer_sizes = tuple([int(h) for h in hidden_layer_sizes_str.split(",")])
    
    # dataset = load_breast_cancer()
    dataset = load_digits()
    
    
    x = dataset.data
    y = dataset.target
    
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=42)
    
    model = MLPClassifier(learning_rate_init=learning_rate, hidden_layer_sizes=hidden_layer_sizes, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    
    fig, ax = plt.subplots(1, 1, figsize=(5,5), dpi=250)
    ax.set_title("Confusion matrix with\n learning rate = " + str(learning_rate))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=dataset.target_names)
    disp.plot(ax=ax, cmap="Blues", values_format="d")
        
    document.querySelector("#output_confusion_matrix").innerHTML = ""
    display(fig, target="output_confusion_matrix")
    
    document.querySelector("#accuracy").innerText = round(accuracy, 6)
    
    
    fig2, ax2 = plt.subplots(1, 1, figsize=(5,5), dpi=250)
    ax2.plot(model.loss_curve_)
    ax2.set_xlabel("Iteration")
    ax2.set_ylabel("Loss")
    ax2.set_title("Loss curve with\n learning rate = " + str(learning_rate))
    
    document.querySelector("#output_loss_curve").innerHTML = ""
    display(fig2, target="output_loss_curve")
    
    num_classes = dataset.target_names.shape[0]
    
    fig_draw1 = draw(x.shape[1], list(hidden_layer_sizes) + [num_classes], textSize=9, customRadius=0, showLegend=True, showInputLayer=True)
    fig_draw2 = draw(x.shape[1], list(hidden_layer_sizes) + [num_classes], textSize=9, customRadius=0, showLegend=True, showInputLayer=False)
    
    document.querySelector("#output_hidden_layer_sizes").innerHTML = ""
    display(fig_draw1, target="output_hidden_layer_sizes")
    
    document.querySelector("#output_hidden_layer_sizes_no_input_layer").innerHTML = ""
    display(fig_draw2, target="output_hidden_layer_sizes_no_input_layer")