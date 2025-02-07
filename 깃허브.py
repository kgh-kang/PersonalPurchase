import streamlit as st

# Streamlit 설정
st.set_page_config(page_title="노후장비 개인구매", layout="wide")

# ✅ 배경색을 회색(#F0F0F0)으로 변경
st.markdown("""
    <style>
    body {
        background-color: #F0F0F0;
    }
    .stApp {
        background-color: #F0F0F0;
    }
    .stButton>button {
        background-color: #007BFF !important; /* 파란색 */
        color: white !important;
        padding: 10px 20px !important;
        border-radius: 8px !important;
        font-size: 18px !important;
    }
    .stButton>button:hover {
        background-color: #0056b3 !important; /* 더 진한 파란색 */
    }
    </style>
""", unsafe_allow_html=True)

# GitHub 이미지 URL (사용자명/저장소명 변경)
GITHUB_IMAGE_URL = "https://raw.githubusercontent.com/kgh-kang/Test/refs/heads/main/assets/image_1.png"

# ✅ 화면을 한 페이지 안에 담기 위해 컨테이너 사용
with st.container():
    # 이미지 중앙 정렬 및 크기 조절
    st.markdown(
        f"<p style='text-align: center;'><img src='{GITHUB_IMAGE_URL}' width='150'></p>",
        unsafe_allow_html=True
    )

    # 제목 중앙 정렬
    st.markdown("<h1 style='text-align: center; font-size: 50px;'>노후장비 개인구매</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #66666D;'>₩10,000부터</h3>", unsafe_allow_html=True)

    # ✅ 구매 신청 버튼 (가운데 정렬 + 크기 자동 조정)
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("구매 신청하기", use_container_width=False):  # 텍스트에 맞춰 크기 조정
            st.success("구매 신청이 완료되었습니다!")

    # 안내 문구 중앙 정렬
    st.markdown("<h4 style='text-align: center; color: black;'>시간이 좀 더 필요하신가요?</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #66666D;'>신규 장비 수령 후 2주가 지나면 구매 기회가 사라집니다.</p>", unsafe_allow_html=True)

# ✅ 상단 툴바 숨기기 (예: Streamlit 메뉴)
st.markdown("""
<style>
.stApp [data-testid="stToolbar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)
