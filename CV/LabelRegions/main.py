# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:07:39 2024

@author: abelg
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap

import numpy as np

from pyscript import document, display
from pyodide.ffi import create_proxy

from js import FileReader

import io
import base64

def LabelingRegions(img, min_region_area=2):
    K = 1
    im_out = np.zeros((img.shape), dtype=np.uint32)

    equivalences = {}

    # Iterate over image to set labels
    for i,r in enumerate(img):
        for j,p in enumerate(r):
            if(p!=0):
                Xu = i-1
                Xl = j-1

                if (Xu >= 0 and Xl >= 0):

                    im_out_xu = im_out[Xu, j]
                    im_out_xl = im_out[i, Xl]

                    if(im_out_xu != 0 and im_out_xl == 0):
                        im_out[i, j] = im_out_xu

                    elif(im_out_xu == 0 and im_out_xl != 0):
                        im_out[i, j] = im_out_xl

                    elif(im_out_xu != 0 and im_out_xl != 0):
                        im_out[i, j] = im_out_xl

                        if(im_out_xu != im_out_xl):
                            if im_out_xl in equivalences:
                                if im_out_xu not in equivalences[im_out_xl]:
                                    equivalences[im_out_xl].append(im_out_xu)
                            else:
                                equivalences[im_out_xl] = [im_out_xu]

                    elif(im_out_xu == 0 and im_out_xl == 0):
                        im_out[i, j] = K
                        K = K + 1


    # Replace the labels of the dictionary of equivalences.                
    for k,v in equivalences.items():
        for equiv in v:
            im_out[im_out==equiv] = k
            
            
    u = np.unique(im_out, return_counts=True)      
    u2 = np.hstack((u[0].reshape(-1, 1), u[1].reshape(-1, 1)))
    u2_small_regions = u2[u2[:, 1] < min_region_area][:, 0]

    for small_region_val in u2_small_regions:
        im_out = np.where(im_out == small_region_val, 0, im_out)
        
    
    im_out_seq = np.copy(im_out)
        
    u2_regions = u2[u2[:, 1] >= min_region_area][:, 0]

    regions_count_def = 0
    for region_val in u2_regions:
        im_out_seq[im_out == region_val] = regions_count_def
        regions_count_def = regions_count_def + 1
            
    im_out_seq = im_out_seq.astype(np.uint8)
    return [im_out_seq, equivalences]


def LabelingRegionsC8(img, min_region_area=2):
    K = 1
    im_out = np.zeros((img.shape), dtype=np.uint32)

    equivalences = {}

    # Iterate over image to set labels
    for i,r in enumerate(img):
        for j,p in enumerate(r):
            if(p!=0):
                Xu = i-1
                Xl = j-1
                Xr = j+1

                if (Xu >= 0 and Xl >= 0 and Xr < im_out.shape[1]):

                    im_out_xu = im_out[Xu, j]
                    im_out_xl = im_out[i, Xl]
                    im_out_xul = im_out[Xu, Xl]
                    im_out_xur = im_out[Xu, Xr]

                    if(im_out_xu != 0 and im_out_xul == 0 and im_out_xl == 0 and im_out_xur == 0):
                        im_out[i, j] = im_out_xu

                    elif(im_out_xu == 0 and im_out_xul != 0 and im_out_xl == 0 and im_out_xur == 0):
                        im_out[i, j] = im_out_xul
                        
                    elif(im_out_xu == 0 and im_out_xul == 0 and im_out_xl != 0 and im_out_xur == 0):
                        im_out[i, j] = im_out_xl
                        
                    elif(im_out_xu == 0 and im_out_xul == 0 and im_out_xl == 0 and im_out_xur != 0):
                        im_out[i, j] = im_out_xur

                    elif(im_out_xu != 0 and im_out_xul == 0 and im_out_xl != 0 and im_out_xur == 0):
                        im_out[i, j] = im_out_xl

                        if(im_out_xu != im_out_xl):
                            if im_out_xu in equivalences:
                                if im_out_xl not in equivalences[im_out_xu]:
                                    equivalences[im_out_xu].append(im_out_xl)
                            else:
                                equivalences[im_out_xu] = [im_out_xl]
                                
                    elif(im_out_xu == 0 and im_out_xul != 0 and im_out_xl != 0 and im_out_xur == 0):
                        im_out[i, j] = im_out_xl

                        if(im_out_xul != im_out_xl):
                            if im_out_xul in equivalences:
                                if im_out_xl not in equivalences[im_out_xul]:
                                    equivalences[im_out_xul].append(im_out_xl)
                            else:
                                equivalences[im_out_xul] = [im_out_xl]
                                
                    elif(im_out_xu != 0 and im_out_xul != 0 and im_out_xl == 0 and im_out_xur == 0):
                        im_out[i, j] = im_out_xul

                        if(im_out_xu != im_out_xul):
                            if im_out_xu in equivalences:
                                if im_out_xul not in equivalences[im_out_xu]:
                                    equivalences[im_out_xu].append(im_out_xul)
                            else:
                                equivalences[im_out_xu] = [im_out_xul]
                                
                                
                    elif(im_out_xu != 0 and im_out_xul == 0 and im_out_xl == 0 and im_out_xur != 0):
                        im_out[i, j] = im_out_xu

                        if(im_out_xur != im_out_xu):
                            if im_out_xur in equivalences:
                                if im_out_xu not in equivalences[im_out_xur]:
                                    equivalences[im_out_xur].append(im_out_xu)
                            else:
                                equivalences[im_out_xur] = [im_out_xu]    
                                
                    elif(im_out_xu == 0 and im_out_xul != 0 and im_out_xl == 0 and im_out_xur != 0):
                        im_out[i, j] = im_out_xul

                        if(im_out_xur != im_out_xul):
                            if im_out_xur in equivalences:
                                if im_out_xul not in equivalences[im_out_xur]:
                                    equivalences[im_out_xur].append(im_out_xul)
                            else:
                                equivalences[im_out_xur] = [im_out_xul]   
                   
                    elif(im_out_xu == 0 and im_out_xul == 0 and im_out_xl != 0 and im_out_xur != 0):
                        im_out[i, j] = im_out_xl

                        if(im_out_xur != im_out_xl):
                            if im_out_xur in equivalences:
                                if im_out_xl not in equivalences[im_out_xur]:
                                    equivalences[im_out_xur].append(im_out_xl)
                            else:
                                equivalences[im_out_xur] = [im_out_xl]
                                
                    elif(im_out_xu == 0 and im_out_xul == 0 and im_out_xl == 0 and im_out_xur == 0):
                        im_out[i, j] = K
                        K = K + 1
                                
                    else:
                        
                        if(im_out_xl != 0):
                            save = im_out_xl
                        else:
                            save = im_out_xul
                            
                        im_out[i, j] = save

                        if(im_out_xu != save and im_out_xu != 0):
                            if im_out_xu in equivalences:
                                if save not in equivalences[im_out_xu]:
                                    equivalences[im_out_xu].append(save)
                            else:
                                equivalences[im_out_xu] = [save]
                                
                        if(im_out_xul != save and im_out_xul != 0):
                            if im_out_xul in equivalences:
                                if save not in equivalences[im_out_xul]:
                                    equivalences[im_out_xul].append(save)
                            else:
                                equivalences[im_out_xul] = [save]
                                
                                
                        if(im_out_xur != save and im_out_xur != 0):
                            if im_out_xur in equivalences:
                                if save not in equivalences[im_out_xur]:
                                    equivalences[im_out_xur].append(save)
                            else:
                                equivalences[im_out_xur] = [save]
                          
                        
                        if(im_out_xl != save and im_out_xl != 0):
                            if im_out_xl in equivalences:
                                if save not in equivalences[im_out_xl]:
                                    equivalences[im_out_xl].append(save)
                            else:
                                equivalences[im_out_xl] = [save]            
                    

                
    # Replace the labels of the dictionary of equivalences.
    for k,v in equivalences.items():
        for equiv in v:
            if(k in equivalences):
                im_out[im_out==k] = equiv
                 

    u = np.unique(im_out, return_counts=True)      
    u2 = np.hstack((u[0].reshape(-1, 1), u[1].reshape(-1, 1)))
    u2_small_regions = u2[u2[:, 1] < min_region_area][:, 0]

    for small_region_val in u2_small_regions:
        im_out = np.where(im_out == small_region_val, 0, im_out)
        
    
    im_out_seq = np.copy(im_out)
        
    u2_regions = u2[u2[:, 1] >= min_region_area][:, 0]

    regions_count_def = 0
    for region_val in u2_regions:
        im_out_seq[im_out == region_val] = regions_count_def
        regions_count_def = regions_count_def + 1
            
    im_out_seq = im_out_seq.astype(np.uint8)
    return [im_out_seq, equivalences]


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
    
    min_region_area = document.querySelector("#min_region_area_text").value
    
    if min_region_area is None:
        document.querySelector("#output_result").innerHTML = "Write a minimum area"
        return
    
    if type(min_region_area) == str:
        if min_region_area == '' or min_region_area == ' ':
            document.querySelector("#output_result").innerHTML = "Write a minimum area"
            return
    
    min_region_area = int(min_region_area)
    
    
    if original_img is None:
        document.querySelector("#output_result").innerHTML = "Select an image"
        return
    
    img = np.copy(np.mean(original_img[:, :, 0:3], axis=2) * 255)

    
    if document.querySelector("#connectivity4").checked:
        o_img, _ = LabelingRegions(img, min_region_area=min_region_area)
        connectivity = "C4"
        
    elif document.querySelector("#connectivity8").checked:
        o_img, _ = LabelingRegionsC8(img, min_region_area=min_region_area)
        connectivity = "C8"
        
    else:
        document.querySelector("#output_result").innerHTML = "Select a connectivity"
        return
    
    u = np.unique(o_img, return_counts=True)
    regions_found = u[0].shape[0] - 1
    
    tab20b = mpl.colormaps['tab20b']
    tab20c = mpl.colormaps['tab20c']

    newcolors = np.vstack((tab20b(np.linspace(0, 1, 20)), tab20c(np.linspace(0, 1, 20))))

    rng = np.random.default_rng(12345)
    rng.shuffle(newcolors)
    
    newcolors = np.concatenate(([[0, 0, 0, 1]], newcolors), axis=0)

    newcmp = ListedColormap(newcolors, name='tab20b_tab20c')
        
    fig2, ax2 = plt.subplots(1, 1, figsize=(2,2), dpi=200)
    ax2.imshow(o_img, cmap=newcmp)
    ax2.axis("off")
    ax2.set_title("Image after region labelling (" + connectivity + ")\n (min area: " + str(min_region_area) + ", regions found: " + str(regions_found) + ")", size=5)
    psm = ax2.pcolormesh(o_img, cmap=newcmp, rasterized=True, vmin=0, vmax=regions_found)

    document.querySelector("#output_result").innerHTML = ""
    display(fig2, target="output_result")

    