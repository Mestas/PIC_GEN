import streamlit as st
import numpy as np
import cv2
from io import BytesIO

st.set_page_config(
    initial_sidebar_state="auto",
    layout="centered"
)

# # # 侧边栏设置
st.sidebar.write("<h4 style='color: blue;'>本工具可以生成bmp图片</h4>", unsafe_allow_html=True)

# # # 工具名称、版本号
st.write("# PIC Generator #")
col1, col2 = st.columns([2, 1])
with col2:
    st.write("<h5 style='color: blue;'>版本号：V1.0</h5>", unsafe_allow_html=True)
    st.write("<h5 style='color: blue;'>发布时间：2024/09/27</h5>", unsafe_allow_html=True)

# # # 设置步骤1
st.write()
st.write("<h6>步骤1: 请输入各区域RGB灰阶数</h6>", unsafe_allow_html=True)

col11, col12, col13, col14, col15, col16 = st.columns((5, 1, 5, 1, 5, 10))
col21, col22, col23 = st.columns((6, 6, 15))
col31, col32, col33, col34, col35, col36 = st.columns((5, 1, 5, 1, 5, 10))

with col11:
    R1 = st.number_input(label='左上位置R灰阶', format='%f', key='R1')
with col11:
    G1 = st.number_input(label='左上位置G灰阶', format='%f', key='G1', label_visibility='collapsed')
with col11:
    B1 = st.number_input(label='左上位置B灰阶', format='%f', key='B1', label_visibility='collapsed')

with col13:
    R2 = st.number_input(label='中上位置R灰阶', format='%f', key='R2')
with col13:
    G2 = st.number_input(label='中上位置G灰阶', format='%f', key='G2', label_visibility='collapsed')
with col13:
    B2 = st.number_input(label='中上位置B灰阶', format='%f', key='B2', label_visibility='collapsed')

with col15:
    R3 = st.number_input(label='右上位置R灰阶', format='%f', key='R3')
with col15:
    G3 = st.number_input(label='右上位置G灰阶', format='%f', key='G3', label_visibility='collapsed')
with col15:
    B3 = st.number_input(label='右上位置B灰阶', format='%f', key='B3', label_visibility='collapsed')

with col22:
    R4 = st.number_input(label='中间位置R灰阶', format='%f', key='R4')
with col22:
    G4 = st.number_input(label='中间位置G灰阶', format='%f', key='G4', label_visibility='collapsed')
with col22:
    B4 = st.number_input(label='中间位置B灰阶', format='%f', key='B4', label_visibility='collapsed')

with col31:
    R5 = st.number_input(label='左下位置R灰阶', format='%f', key='R5')
with col31:
    G5 = st.number_input(label='左下位置G灰阶', format='%f', key='G5', label_visibility='collapsed')
with col31:
    B5 = st.number_input(label='左下位置B灰阶', format='%f', key='B5', label_visibility='collapsed')

with col33:
    R6 = st.number_input(label='中下位置R灰阶', format='%f', key='R6')
with col33:
    G6 = st.number_input(label='中下位置G灰阶', format='%f', key='G6', label_visibility='collapsed')
with col33:
    B6 = st.number_input(label='中下位置B灰阶', format='%f', key='B6', label_visibility='collapsed')

with col35:
    R7 = st.number_input(label='右下位置R灰阶', format='%f', key='R7')
with col35:
    G7 = st.number_input(label='右下位置G灰阶', format='%f', key='G7', label_visibility='collapsed')
with col35:
    B7 = st.number_input(label='右下位置B灰阶', format='%f', key='B7', label_visibility='collapsed')

# # # 设置步骤2
st.write("<h6>步骤2: 点击按钮输出图片</h6>", unsafe_allow_html=True)
h = 2880
l = 1920

img_R = np.ones((h, l))
img_G = np.ones((h, l))
img_B = np.ones((h, l))

reg_h = 960
reg_l = 640

img_R[0:960, 0:640] = int(R1)
img_R[0:960, 640:1280] = int(R2)
img_R[0:960, 1280:1920] = int(R3)
img_R[960:1920, 0:1920] = int(R4)
img_R[1920:2880, 0:640] = int(R5)
img_R[1920:2880, 640:1280] = int(R6)
img_R[1920:2880, 1280:1920] = int(R7)

img_G[0:960, 0:640] = int(G1)
img_G[0:960, 640:1280] = int(G2)
img_G[0:960, 1280:1920] = int(G3)
img_G[960:1920, 0:1920] = int(G4)
img_G[1920:2880, 0:640] = int(G5)
img_G[1920:2880, 640:1280] = int(G6)
img_G[1920:2880, 1280:1920] = int(G7)

img_B[0:960, 0:640] = int(B1)
img_B[0:960, 640:1280] = int(B2)
img_B[0:960, 1280:1920] = int(B3)
img_B[960:1920, 0:1920] = int(B4)
img_B[1920:2880, 0:640] = int(B5)
img_B[1920:2880, 640:1280] = int(B6)
img_B[1920:2880, 1280:1920] = int(B7)

btn_pic = st.button('***生成图片***')
if btn_pic is True:  
    try:
        W_img = cv2.merge([img_B, img_G, img_R])
        
        # 将图像数据保存到内存文件中
        _, buffer = cv2.imencode('.bmp', W_img)
        if buffer is not None:
            byte_data = buffer.tobytes()

        # 使用BytesIO创建一个内存文件对象
        memory_file = BytesIO(byte_data)

        # Streamlit下载按钮
        st.download_button(
            label="Download image", 
            data=memory_file,
            file_name="W_image.bmp",
            mime="image/bmp"
        )
            
    except NameError:
        st.write(':red[DXF文件未解密, 请解密后重新上传]')
    # except TypeError:
    #     st.write(':red[DXF文件未包含正确图层, 请确认后重新上传]')
    # except AttributeError:
    #     st.write(':red[DXF图层不正确, 请确认后重新上传]')  


# 编辑点击计算按钮
st.markdown(
    '''
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div:nth-child(8) > div > button
    {
    background-color: rgb(220, 240, 220);
    height: 70px;
    width: 150px;
    } 
    </style>
    ''',
    unsafe_allow_html=True
)

# 通过markdown设置textarea区域的字体和input字体
st.markdown(
    """
    <style>
    textarea {
        font-size: 0.9rem !important;
    }
    input {
        font-size: 0.9rem !important; /*设置字体大小，加上!important是避免被 Markdown 样式覆盖*/
        color: rgb(0, 0, 0) !important; /*设置字体颜色*/
        background-color: rgb(220, 240, 220) !important; /*设置背景颜色*/
        /background-color: rgb(220, 240, 220, 50%) !important; /*设置背景颜色*/
        justify-content: center !important;
        text-align: center !important; /*设置字体水平居中*/
        vertical-align: middle !important; /*设置字体垂直居中*/
        height: 39px !important;/ /*设置input的高度*/
    }
    label {
        color: rgb(0, 0, 0) !important; /*设置字体颜色*/
        background-color: rgb(255, 255, 255) !important; /*设置背景颜色*/
        text-align: center !important; /*设置字体水平居中*/
        vertical-align: middle !important; /*设置字体垂直居中*/
        justify-content: center !important; /*设置label居中*/
        /outline: 5px solid rgb(15,15,15) !important;/ /*大小不变，设置边框*/
        /border: 5px solid rgb(15,15,15) !important;/ /*外形变大，增加边框并设置*/
        /*letter-spacing: 30px !important;*/ /*设置字体间距*/
        /*text-transform: uppercase !important;*/ /*强制大写*/
        /align-items: center !important;
        /height: 1vh !important;/ /*调节label垂直间距*/
    }
    </style>
    """,
    unsafe_allow_html=True,
)
