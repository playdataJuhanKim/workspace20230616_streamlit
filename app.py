import streamlit as st
#st라는 변수명으로 스트림릿의 기즌들을 사용하겠다.

st.title('나만의 작은 파이썬 웹페이지')
st.header('8일차')
st.subheader('짜파게티')
st.write('먹고싶다.')
#기능이 실행되는 순서대로 화면에서 표현. 코드상에서 윗줄부터 페이지에 반영
st.video("https://www.youtube.com/watch?v=SaCheA6Njc4")
st.image("https://i.imgur.com/jorp5JH.png")
#streamlit run app.py
