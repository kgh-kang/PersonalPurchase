import streamlit as st

# Streamlit 설정
st.set_page_config(page_title="노후장비 개인구매", layout="wide")

# ✅ CSS 적용 (폰트 및 레이아웃 조정)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700&display=swap');

    html, body, .stApp {
        font-family: 'Noto Sans KR', sans-serif !important;
        background-color: #F5F5F7 !important;
        margin: 0;
        padding: 0;
    }

    /* 컨테이너 스타일 */
    .content-container {
        margin-top: 200px; /* 상단 여백 */
        margin-left: 50px; /* 좌측 정렬 */
    }

    /* 제목 스타일 */
    .title-text {
        font-size: 30px;
        font-weight: bold;
        color: black;
        text-align: left;
        margin-bottom: 5px;
    }

    /* 서브 텍스트 (회색) */
    .subtitle-text {
        font-size: 18px;
        color: #66666D;
        text-align: left;
        margin-bottom: 30px; /* 버튼과의 여백 */
    }

    /* 버튼 스타일 */
    .buy-button {
        background-color: #007BFF; /* 파란색 */
        color: white;
        font-size: 16px;
        font-weight: 500;
        padding: 12px 24px;
        border-radius: 8px;
        border: none;
        font-family: 'Noto Sans KR', sans-serif;
        cursor: pointer;
        text-align: center;
        display: inline-block;
    }

    .buy-button:hover {
        background-color: #0056b3; /* 더 진한 파란색 */
    }
    </style>
""", unsafe_allow_html=True)

# ✅ 레이아웃 구성
st.markdown('<div class="content-container">', unsafe_allow_html=True)

# **노후장비 개인구매 (검은색) / 네꺼에서 (회색)**
st.markdown("""
    <p class="title-text">노후장비 개인구매.</p>
    <p class="subtitle-text">네꺼에서 내꺼로 만들 마지막 기회.</p>
""", unsafe_allow_html=True)

# **구매하기 버튼**
st.markdown("""
    <button class="buy-button">구매하기</button>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # 🔹 레이아웃 컨테이너 닫기
