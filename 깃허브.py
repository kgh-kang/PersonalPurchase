import streamlit as st

# Streamlit 설정
st.set_page_config(page_title="노후장비 개인구매", layout="wide")

# ✅ 전체적인 배경과 버튼 스타일 적용
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700&display=swap');

    body, .stApp {
        background-color: #F5F5F7;
    }

    /* 버튼을 더 곡선형으로 변경 */
    .stButton>button {
        background-color: #0071E3 !important; /* 기본 버튼 색상 */
        color: white !important;
        padding: 10px 24px !important;
        border-radius: 30px !important; /* 더 둥글게 */
        font-size: 18px !important;
        font-weight: 500;
        border: none;
        font-family: 'Noto Sans KR', sans-serif !important;
        margin-top: 10px !important;  /* 버튼 위 간격 줄이기 */
        margin-bottom: 10px !important; /* 버튼 아래 간격 줄이기 */
        display: flex;
        justify-content: center;
        align-items: center;
        width: 200px; /* 버튼 크기 고정 */
        margin-left: auto;
        margin-right: auto;
    }
    
    .stButton>button:hover {
        background-color: #0056b3 !important; /* 더 진한 파란색 */
    }

    /* 제목 스타일 */
    h1 {
        font-size: 35px !important; /* "노후장비 개인구매" 폰트 크기 */
        text-align: center;
        font-family: 'Noto Sans KR', sans-serif;
        font-weight: 700;
        margin-bottom: 5px;
    }

    /* 서브 타이틀 스타일 */
    .subtitle {
        font-size: 18px !important;
        text-align: center;
        font-family: 'Noto Sans KR', sans-serif;
        color: #66666D;
        margin-top: -5px;
        margin-bottom: 5px;
    }

    /* "마지막 기회" 스타일 */
    .last-chance {
        font-size: 18px !important;
        text-align: center;
        font-family: 'Noto Sans KR', sans-serif;
        color: #66666D;
        font-weight: bold;
    }

    /* 안내 문구 마진 줄이기 */
    h4 {
        margin-bottom: 5px !important;
    }

    p {
        margin-bottom: 5px !important;
    }
    
    </style>
""", unsafe_allow_html=True)

# GitHub 이미지 URL
GITHUB_IMAGE_URL = "https://raw.githubusercontent.com/kgh-kang/Test/refs/heads/main/assets/image_1.png"

# ✅ 화면을 한 페이지 안에 담기 위해 컨테이너 사용
with st.container():
    # 이미지 중앙 정렬 및 크기 조절
    st.markdown(
        f"<p style='text-align: center;'><img src='{GITHUB_IMAGE_URL}' width='130'></p>",
        unsafe_allow_html=True
    )

    # ✅ 제목과 서브타이틀에서 폰트를 직접 지정 & 간격 더 줄이기
    st.markdown("<h1>노후장비 개인구매</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>네꺼에서 내꺼로 만들</p>", unsafe_allow_html=True)
    st.markdown("<p class='last-chance'>마지막 기회</p>", unsafe_allow_html=True)

    # ✅ 구매 신청 버튼 (정중앙 배치)
    st.markdown("<div style='text-align: center;'><button class='stButton'>구매 신청하기</button></div>", unsafe_allow_html=True)

    # 안내 문구 중앙 정렬 (간격 줄이기 적용)
    st.markdown("<h4 style='text-align: center; font-size: 15px; font-family: \"Noto Sans KR\", sans-serif;'>시간이 좀 더 필요하신가요?</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 12px; font-family: \"Noto Sans KR\", sans-serif; color: #66666D;'>신규 장비 수령 후 2주가 지나면 구매 기회가 사라집니다.</p>", unsafe_allow_html=True)

# ✅ 상단 툴바 숨기기
st.markdown("""
<style>
.stApp [data-testid="stToolbar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)
