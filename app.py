import streamlit as st
#st라는 변수명으로 스트림릿의 기즌들을 사용하겠다.

st.title('나만의 작은 파이썬 웹페이지')
st.header('8일차')
st.subheader('짜파게티')
st.write('먹고싶다.')
#기능이 실행되는 순서대로 화면에서 표현. 코드상에서 윗줄부터 페이지에 반영
st.video("https://www.youtube.com/watch?v=SaCheA6Njc4")
st.image("https://i.imgur.com/jorp5JH.png")

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSL3WQ-4NkRIKo7liDW5j54KOXeDoFTvRLwzw&usqp=CAU')
st.image('image/img.png')
st.image('image/images.jpeg')
#streamlit run app.py


#마크다운

#https://heropy.blog/2017/09/30/markdown/

#제목 마크다운
st.write('''
# 가장 큰 제목 텍스트 (st.title)
## 그 다음으로 큰 제목(st.header)
### 그 다음 다음으로 큰 제목(st.subheader)
#### 그 다음 다음 다음으로 큰 제목
##### 그 다음 다음 다음 다음으로 큰 제목
######## 이건없음''')

#서식
text="""
기울임은 *별표* 또는 _언더바_

진하게(볼드체) 는 **두개** __두 개__

기울임+진하게 는 ***세 개*** ___세개___

취소선은 ~물결표~

밑줄은 <u>미잍주울</u>

형광펜은 <mark>마크마크</mark>
"""

st.write(text)
st.markdown(text, unsafe_allow_html=True)