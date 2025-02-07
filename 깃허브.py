import streamlit as st

# Streamlit 설정
st.set_page_config(page_title="노후장비 개인구매", layout="wide")

# ✅ 전체적인 배경과 버튼 스타일 적용
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700&display=swap');

    /* 전체 컨텐츠 좌측 정렬 */
    .left-container {
        margin-left: 50px;
        text-align: left;
    }

    /* 버튼 스타일 */
    .custom-btn {
        background-color: #2BC2BD !important;
        color: white !important;
        padding: 5px 24px !important;
        border-radius: 15px !important;
        font-size: 13px !important;
        font-weight: 500;
        border: none;
        font-family: 'Noto Sans KR', sans-serif !important;
        cursor: pointer;
        text-align: center;
        display: inline-block;
        width: auto;
        margin-top: 10px;
    }

    .custom-btn:hover {
        background-color: #0056B3 !important;
    }
    </style>
""", unsafe_allow_html=True)

# GitHub 이미지 URL
GITHUB_IMAGE_URL = "https://raw.githubusercontent.com/kgh-kang/Test/refs/heads/main/assets/image_1.png"

# ✅ 화면을 한 페이지 안에 담기 위해 컨테이너 사용
with st.container():
    # 이미지 중앙 정렬
    st.markdown(
        f"<p style='text-align: center; margin-top: 50px; margin-bottom: 50px;'><img src='{GITHUB_IMAGE_URL}' width='120'></p>",
        unsafe_allow_html=True
    )

    # ✅ 텍스트 및 버튼을 좌측 정렬
    st.markdown('<div class="left-container">', unsafe_allow_html=True)

    # ✅ 제목 및 서브타이틀 (좌측 정렬)
    st.markdown("""
        <p style='font-family: "Noto Sans KR", sans-serif; line-height: 1.5;'>
            <span style="font-size: 35px; font-weight: bold;">노후장비 개인구매.</span><span style="font-size: 35px; color: #66666D;">네꺼에서</span><br>
            <span style="font-size: 35px; color: #66666D;">내꺼로.</span>
        </p>
    """, unsafe_allow_html=True)

    # ✅ 구매 신청 버튼 (좌측 정렬)
    st.markdown("""
        <button class="custom-btn">구매 신청하기</button>
    """, unsafe_allow_html=True)

    # ✅ 안내 문구 (좌측 정렬)
    st.markdown("""
        <p style='font-family: "Noto Sans KR", sans-serif; line-height: 1.5;'>
            <span style="font-size: 15px; font-weight: 400;">시간이 좀 더 필요하신가요?</span><br>
            <span style="font-size: 15px; font-weight: 400;">신규 장비 수령 후 2주가 지나면 구매 기회가 사라집니다</span>
        </p>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # 🔹 좌측 정렬 컨테이너 닫기

# ✅ 상단 툴바 숨기기
st.markdown("""
<style>
.stApp [data-testid="stToolbar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)
