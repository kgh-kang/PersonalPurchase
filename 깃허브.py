import streamlit as st

# Streamlit 설정
st.set_page_config(page_title="노후장비 개인구매", layout="wide")

# ✅ 상태 관리 (첫 번째 화면 or 두 번째 화면)
if "page" not in st.session_state:
    st.session_state.page = 1  # 기본값: 첫 번째 화면

# ✅ 화면 전환 함수 (버튼 클릭 시 즉시 적용)
def change_page(page_number):
    st.session_state.page = page_number
    st.rerun()

# ✅ CSS 적용 (Streamlit 버튼을 강제로 스타일 변경)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700&display=swap');

    html, body, .stApp {
        font-family: 'Noto Sans KR', sans-serif !important;
        background-color: #F5F5F7 !important;
        margin: 0;
        padding: 0;
    }

    /* Streamlit 기본 버튼 스타일 강제 변경 */
    div.stButton > button {
        background-color: #2BC2BD !important; /* 민트색 */
        color: white !important;
        padding: 10px 24px !important;
        border-radius: 20px !important;
        font-size: 20px !important;
        font-weight: 400;
        border: none;
        font-family: 'Noto Sans KR', sans-serif !important;
        cursor: pointer;
        text-align: center;
        width: 400px !important;
        display: block;
        margin: auto;
    }

    div.stButton > button:hover {
        background-color: #0056B3 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ 상단 툴바 숨기기 (복구)
st.markdown("""
<style>
.stApp [data-testid="stToolbar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# ✅ 첫 번째 화면
if st.session_state.page == 1:
    with st.container():
        # 이미지 중앙 정렬 및 크기 조절
        st.markdown(
            f"<p style='text-align: center; margin-top: 100px; margin-bottom: 70px;'><img src='https://raw.githubusercontent.com/kgh-kang/Test/refs/heads/main/assets/image_1.png' width='130'></p>",
            unsafe_allow_html=True
        )

        # ✅ 제목과 서브타이틀
        st.markdown("""
            <div>
                <p style='text-align: center; font-family: "Noto Sans KR", sans-serif; line-height: 1.5;'>
                    <span style="font-size: 50px; font-weight: bold;">노후장비 개인구매.</span><br>
                    <span style="font-size: 40px; color: #66666D;">네꺼에서 내꺼로.</span>
                </p>
            </div>
        """, unsafe_allow_html=True)

        # ✅ 구매 신청 버튼 (CSS 스타일이 강제 적용됨)
        if st.button("구매 신청", key="next", use_container_width=False):
            change_page(2)

        # ✅ 안내 문구
        st.markdown("""
            <p style='text-align: center; font-family: "Noto Sans KR", sans-serif; line-height: 1.5;'>
                <span style="font-size: 15px; font-weight: 400;">시간이 좀 더 필요하신가요?</span><br>
                <span style="font-size: 13px; font-weight: 400; color: #66666D;">신규 장비 수령 후 2주가 지나면 구매 기회가 사라집니다</span>
            </p>
        """, unsafe_allow_html=True)

# ✅ 두 번째 화면
elif st.session_state.page == 2:
    with st.container():
        st.markdown("""
            <div>
                <h1 style="text-align: center; font-size: 50px; color: black;">2번째 화면</h1>
                <p style="text-align: center; font-size: 20px; color: #66666D;">이곳에 새로운 내용을 추가할 수 있습니다.</p>
            </div>
        """, unsafe_allow_html=True)

        # ✅ "이전으로" 버튼 (Streamlit 기본 스타일 유지)
        if st.button("이전으로", key="back", use_container_width=False):
            change_page(1)
