import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

#st.write('DataFrame')

left_col , right_col = st.columns(2)

expander1=st.expander('問合せ')
expander1.text_input('回答は？：')

button=left_col.button('右カラムに文字を表示')
if button:
    right_col.write('ここは右カラム')

if st.checkbox('Show Image'):
#st.write('Display Image')
    img =Image.open('Image20230820090430.jpg')
    st.image(img, caption='GCC logo', use_column_width=True)

text = st.text_input('あなたの趣味は？')
'あなたの趣味：',text

condition=st.slider('あなたの今の調子は？',0,100,50)
'コンディション：' , condition


#df = pd.DataFrame({
#    '1列目':[1,2,3,4],
#    '2列目':[10,20,30,40]
#})

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=['lat','lon']
)

#st.bar_chart(df)
#st.map(df)


#"""
# 章
## 節
### 項
#"""

