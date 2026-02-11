# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 15:47:25 2026

@author: wanju
"""

import streamlit as st
import os
import glob

# 1. 設置寬螢幕模式，這是讓圖撐大的關鍵
st.set_page_config(layout="wide")

# 2. 定義容器順序：上面放圖，下面放參數
image_placeholder = st.container()
control_placeholder = st.container()

# 3. 在下方的控制區塊設置「一橫列」的選單
with control_placeholder:
    st.divider()
    # 建立 5 個欄位，對應你的 5 個參數
    c1, c2, c3, c4, c5 = st.columns(5)
    
    with c1:
        layer = st.selectbox("Layer", [0,1,2,3,4,5,6,7,8,9], index=9)
    with c2:
        dataset = st.selectbox('Dataset', ['mnist', 'cifar10'], index=1)
    with c3:
        epoch = st.selectbox('Epoch', [1,3,4,6,7,8,9,11,15,21,29,30,31,32,35,39], index=15)
    with c4:
        sub_sampling = st.selectbox('Sub Sampling', ['25_25','36_36','25_50','36_50','50_50'], index=4)
    with c5:
        classlist = st.text_input("Class List", value="0123456789")

# 4. 圖片檢索邏輯 (使用相對路徑，方便上傳 GitHub)
# 建議將圖片放在專案資料夾下的 figures 子資料夾
fd = 'figures/' 
search_pattern = fd + f"*layer{layer}_{dataset}_class{classlist}_epoch{epoch}_sub{sub_sampling}*.png"
matching_files = glob.glob(search_pattern)

# 5. 在上方區塊顯示大圖
with image_placeholder:
    st.title("ResNet-18 Validations")
    if matching_files:
        image_path = matching_files[0]
        # 顯示搜尋到的完整檔名，方便確認
        st.write(f"📂 `{os.path.basename(image_path)}`")
        # use_container_width=True 會讓圖片寬度自動適應你的螢幕寬度
        st.image(image_path, use_container_width=True)
    else:
        st.error("❌ 無法找到匹配的圖片，請檢查下方參數組合。")
