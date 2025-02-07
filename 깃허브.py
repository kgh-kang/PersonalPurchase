import streamlit as st

# Streamlit 설정
st.set_page_config(page_title="노후장비 개인구매", layout="wide")

# ✅ 전체적인 배경과 버튼 스타일 적용
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700&display=swap');

    /* 버튼 스타일 */
    .center-button {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 15px;
        margin-bottom: 10px;
    }

    .custom-btn {
        background-color: #2bc2bd !important;
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
    }

    .custom-btn:hover {
        background-color: #0056b3 !important;
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

    # ✅ 제목과 서브타이틀에서 폰트를 직접 지정
    st.markdown("""
        <p style='text-align: center; font-family: "Noto Sans KR", sans-serif; line-height: 1.5;'>
            <span style="font-size: 30px; font-weight: bold;">노후장비 개인구매</span><br>
            <span style="font-size: 18px;">네꺼에서 내꺼로 만들 마지막 기회.</span>
        </p>
    """, unsafe_allow_html=True)

    # ✅ 구매 신청 버튼을 화면 정중앙에 배치
    st.markdown("""
        <div class="center-button">
            <button class="custom-btn">구매 신청하기</button>
        </div>
    """, unsafe_allow_html=True)

    # 안내 문구 중앙 정렬
    st.markdown("""
        <p style='text-align: center; font-family: "Noto Sans KR", sans-serif; line-height: 1.5;'>
            <span style="font-size: 15px; font-weight: 400;">시간이 좀 더 필요하신가요?</span><br>
            <span style="font-size: 15px; font-weight: 400;">신규 장비 수령 후 2주가 지나면 구매 기회가 사라집니다</span>
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
