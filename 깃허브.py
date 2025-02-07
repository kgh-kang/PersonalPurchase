import streamlit as st

# Streamlit 설정
st.set_page_config(page_title="노후장비 개인구매", layout="wide")

# CSS 추가 (텍스트 선택 방지)
st.markdown("""
    <style>
    body {
        -webkit-user-select: none;  /* Chrome, Safari */
        -moz-user-select: none;     /* Firefox */
        -ms-user-select: none;      /* IE, Edge */
        user-select: none;          /* Standard */
    }
    </style>
""", unsafe_allow_html=True)

# GitHub 이미지 URL (사용자명/저장소명 변경)
GITHUB_IMAGE_URL = "GITHUB_IMAGE_URL = "https://raw.githubusercontent.com/kgh-kang/Test/refs/heads/main/assets/image_1.png"

# 이미지 중앙 정렬 및 크기 조절
st.markdown(
    f"<p style='text-align: center;'><img src='{GITHUB_IMAGE_URL}' width='400'></p>",
    unsafe_allow_html=True
)

# 제목 중앙 정렬 (텍스트 선택 방지)
st.markdown("<h1 style='text-align: center; font-size: 70px;'>노후장비 개인구매</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #66666D;'>₩10,000부터</h3>", unsafe_allow_html=True)

# 버튼 생성 (가운데 정렬)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("구매 신청하기", use_container_width=True):
        st.success("구매 신청이 완료되었습니다!")

# 안내 문구 중앙 정렬 (텍스트 선택 방지)
st.markdown("<h4 style='text-align: center; color: black;'>시간이 좀 더 필요하신가요?</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #66666D;'>신규 장비 수령 후 2주가 지나면 구매 기회가 사라집니다.</p>", unsafe_allow_html=True)
