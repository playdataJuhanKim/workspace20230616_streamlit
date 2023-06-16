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
st.divider()
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

st.divider()

#레이아웃
st.subheader("레이아웃")
st.write('''
    ### 순서가 없는 리스트
    *별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트.
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트.
        * 들여쓰기 1
            * 들여들여쓰기
    (-)도 됨
        - 쓰기쓰기
    ### 순서가 있는 리스트
    1. 순서가
    2. 있는
    3. 리스트 
        4.들여
            9.쓰기 (숫자를 건너뛰어도 순서를 따름)
    1. 들여쓰기는
        1. 1로시작해야됨
    1. 1부터 증가함

    ---
    가로줄로 나눔
    ---
    ###테이블(표) 만들기
    |이름|직업|
    |---|---|
    |파이썬|백수|
''')

#링크
# st.divider()
# st.subheader('링크')
# st.write('''
#     * [표시할 텍스트](주소)
#     * [연습문제](https://solved.ac/)
#     * ![이미지에 대한 설명](jetbrains://pycharm/navigate/reference?project=workspace20230616_streamlit&path=image/images.jpeg)
#     * 이미지에 링크를 넣으려면
#     * [image/img.png](https://github.com/playdataJuhanKim/workspace20230616_streamlit/blob/106e06338b5c78bfbc4e4e633e772c113302b7fb/image/img.png)
# ''')
#
# st.write(f"""
#     * [표시할 텍스트](https://naver.com)
#     * [표시할 텍스트]({l1})
#     * ![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)
#     * ![이미지에 대한 설명]({l2})
#     * [![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)](https://naver.com))
# """)

#인용
st.divider()
st.subheader('인용')
st.write('''
    > 무언가 멋진 말 - 유명한 사람
    
    > 대충 흑백사진에 글쓰면 명언이다 - 침착맨
    
    > 인용 첫줄
        > > 인용문 안에 인용
    #### 코드
    `(1옆에 이거)`
    ```
    이걸로 여러줄 코드를 나타내고
    줄바꿈도?
    print("짜장면")
    ```
    ```python
    print("파이썬!")
    ''')