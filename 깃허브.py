import streamlit as st

# Streamlit 설정
st.set_page_config(page_title="노후장비 개인구매", layout="wide")

# ✅ 전체적인 배경과 버튼 스타일 적용
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700&display=swap');

    /* 전체 컨테이너 (텍스트와 버튼이 같은 너비를 가짐) */
    .title-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        width: 550px; /* 🔹 "노후장비 개인구매."의 너비와 동일하게 설정 */
        margin: 0 auto;
    }

    /* 버튼 스타일 */
    .custom-btn {
        background-color: #2BC2BD !important;
        color: white !important;
        padding: 15px 0px !important; /* 세로 크기 조정 */
        border-radius: 30px !important;
        font-size: 20px !important;
        font-weight: 400;
        border: none;
        font-family: 'Noto Sans KR', sans-serif !important;
        cursor: pointer;
        text-align: center;
        width: 100%; /* 🔹 부모 컨테이너(title-container)의 너비와 동일하게 설정 */
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
    # 이미지 중앙 정렬 및 크기 조절
    st.markdown(
        f"<p style='text-align: center; margin-top: 60px; margin-bottom: 70px;'><img src='{GITHUB_IMAGE_URL}' width='130'></p>",
        unsafe_allow_html=True
    )

    # ✅ 제목 및 서브타이틀 (버튼과 동일한 너비 유지)
    st.markdown("""
        <div class="title-container">
            <p style='font-family: "Noto Sans KR", sans-serif; line-height: 1.5;'>
                <span style="font-size: 50px; font-weight: bold;">노후장비 개인구매.</span><br>
                <span style="font-size: 40px; color: #66666D;">네꺼에서 내꺼로.</span>
            </p>

            <!-- 구매 신청 버튼 (동일한 너비 적용) -->
            <button class="custom-btn">구매 신청</button>
        </div>
    """, unsafe_allow_html=True)

    # ✅ 안내 문구 중앙 정렬
    st.markdown("""
        <p style='text-align: center; font-family: "Noto Sans KR", sans-serif; line-height: 1.5;'>
            <span style="font-size: 15px; font-weight: bold; font-weight: 400;">시간이 좀 더 필요하신가요?</span><br>
            <span style="font-size: 13px; font-weight: 400; color: #66666D;">신규 장비 수령 후 2주가 지나면 구매 기회가 사라집니다</span>
        </p>
    """, unsafe_allow_html=True)

# ✅ 상단 툴바 숨기기
st.markdown("""
<style>
.stApp [data-testid="stToolbar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)
