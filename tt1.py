import matplotlib.pyplot as plt
import streamlit as st



col1, col2, col3 = st.columns(3)


with col1:
    c1= st.radio('선의 색을 선택하시오',['red', 'green', 'blue','orange'])

with col2:
    s1= st.radio('선의 형태를 선택하시오', ['-', '-.'])

with col3:
    m1= st.radio('마커의 형태를 선택하시오',['p','^','p','s'])
fig, ax = plt.subplots()

x=[]
y=[]
for i in range(-20,21,2):
    x.append(i)
    y.append(-2*i*i+3*i+5)

#plt.plot(x,y,'r:h')
plt.plot(x,y, color=c1, linestyle=s1, marker=m1)

st.pyplot(fig)



import sys
sys.exit()

