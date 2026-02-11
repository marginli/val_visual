# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 15:47:25 2026

@author: wanju
"""

import streamlit as st
import os
import glob

# 1. 設置寬螢幕模式，讓圖可以撐到最大
st.set_page_config(layout="wide")

# 2. 為了讓選單在圖下面，我們可以用 st.container() 來控製顯示順序
# 先建立兩個區塊：上面放圖，下面放選單
image_placeholder = st.container()
control_placeholder = st.container()

# 3. 在下方的控制區塊設置選單
with control_placeholder:
    st.divider() # 加一條分割線
    col1, col2, col3 = st.columns(3) # 使用 columns 讓選單並排，節省空間
    
    with col1:
        layer = st.selectbox("Select Layer", [0,1,2,3,4,5,6,7,8,9], index=9)
        dataset = st.selectbox('select dataset', ['mnist', 'cifar10'], index=1)
    with col2:
        epoch = st.selectbox('select epoch', [1,3,4,6,7,8,9,11,15,21,29,30,31,32,35,39], index=15)
        sub_sampling = st.selectbox('sub sampling', ['25_25','36_36','25_50','36_50','50_50'], index=4)
    with col3:
        classlist = st.text_input("Enter class list", value="0123456789")

# 4. 圖片檢索邏輯 (保持不變，但使用相對路徑建議)
fd = 'figures/' # 記得改為相對路徑以便上傳 GitHub
search_pattern = fd + f"*layer{layer}_{dataset}_class{classlist}_epoch{epoch}_sub{sub_sampling}*.png"
matching_files = glob.glob(search_pattern)

# 5. 在上方的圖片區塊顯示結果
with image_placeholder:
    st.title("ResNet-18 Validations")
    if matching_files:
        image_path = matching_files[0]
        st.caption(f"File found: {os.path.basename(image_path)}")
        # use_container_width=True 會讓圖寬度撐滿
        st.image(image_path, use_container_width=True)
    else:
        st.error("File not found! Please check the parameters below.")