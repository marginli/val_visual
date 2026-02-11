# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 15:47:25 2026

@author: wanju
"""

import streamlit as st
import os
import glob

st.title("ResNet-18 validations")

# 1. 設置選單
layer = st.selectbox("Select Layer", [0,1,2,3,4,5,6,7,8,9])
dataset = st.selectbox('select dataset',['mnist','cifar10'])
epoch = st.selectbox('select epoch',[1,3,4,6,7,8,9,11,15,21,29,30,31,32,35,39])
sub_sampling = st.selectbox('sub sampling',['25_25','36_36','25_50','36_50','50_50'])
#block = st.slider("Select Block", 1, 5, 2)
#channel = st.number_input("Channel", value=2)
classlist = st.text_input("Enter class list", value="0123456789")

# 2. 拼接路徑
#fd='C:/Users/wanju/Desktop/temp20221230/2024 Aug-/AI/validation/figures/'
fd='figures/'
search_pattern =fd+ f"*layer{layer}_{dataset}_class{classlist}_epoch{epoch}_sub{sub_sampling}*.png"
matching_files = glob.glob(search_pattern)
# 3. 顯示圖片 (加入安全檢查)
if matching_files:
    # 取得搜尋到的第一個檔案
    image_path = matching_files[0]
    
    # 顯示檔案名稱（方便除錯，確認抓到的是哪一張）
    st.caption(f"File found: {os.path.basename(image_path)}")
    st.image(image_path, use_column_width=True)
else:
    # 如果 matching_files 是空的，顯示提示
    st.warning(f"File not found! (Checked pattern: *layer{layer}_{dataset}_class{classlist}_epoch{epoch}_sub{sub_sampling}*.png)")
    st.info("File not found")