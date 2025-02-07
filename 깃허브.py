import streamlit as st
import requests
import pandas as pd

# Streamlit 설정
st.set_page_config(page_title="노후장비 개인구매", layout="wide")

# ✅ API 호출 함수
def fetch_assets(user_number):
    url = f"http://assets.woowa.in/x1/api/help-desk/assets/user/23080058"
    headers = {
        "Authorization": "Bearer help-desk-2e503c87-492f-4665-9a45-9a5517aa2e76",
        "asset-user-number": "23080058"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json().get("data", [])
        # '노트북' 카테고리 필터링
        laptops = [
            {
                "카테고리": item["categoryParentName"],
                "모델명": item["categoryName"],
                "자산ID": item["assetId"],
                "배정일": item["assignedDateTime"],
                "예상가격": item["sapEstimatedPrice"] if item["sapEstimatedPrice"] else "정보 없음"
            }
            for item in data if item["categoryGrandParentName"] == "노트북"
        ]
        return laptops
    else:
        return None

# ✅ 상태 관리
if "page" not in st.session_state:
    st.session_state.page = 1  # 기본값: 첫 번째 화면
if "laptop_data" not in st.session_state:
    st.session_state.laptop_data = None  # 조회 결과 저장

# ✅ 화면 전환 함수
def change_page(page_number):
    st.session_state.page = page_number
    st.rerun()

# ✅ CSS 적용 (공통 스타일)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700&display=swap');

    html, body, .stApp {
        font-family: 'Noto Sans KR', sans-serif !important;
        background-color: #F5F5F7 !important;
        margin: 0;
        padding: 0;
    }

    /* 버튼 스타일 */
    div.stButton > button {
        background-color: #2BC2BD !important;
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

    /* 조회하기 버튼 스타일 */
    .disabled-btn {
        background-color: #D3D3D3 !important;
        color: white !important;
        padding: 10px 24px !important;
        border-radius: 20px !important;
        font-size: 20px !important;
        font-weight: 400;
        border: none;
        font-family: 'Noto Sans KR', sans-serif !important;
        cursor: not-allowed;
        text-align: center;
        width: 400px !important;
        display: block;
        margin: auto;
    }

    .enabled-btn {
        background-color: #2BC2BD !important;
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
    </style>
""", unsafe_allow_html=True)

# ✅ 상단 툴바 숨기기
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

        # ✅ 구매 신청 버튼
        if st.button("구매 신청", key="next", use_container_width=False):
            change_page(2)

        # ✅ 안내 문구
        st.markdown("""
            <p style='text-align: center; font-family: "Noto Sans KR", sans-serif; line-height: 1.5;'>
                <span style="font-size: 15px; font-weight: 400;">시간이 좀 더 필요하신가요?</span><br>
                <span style="font-size: 13px; font-weight: 400; color: #66666D;">신규 장비 수령 후 2주가 지나면 구매 기회가 사라집니다</span>
            </p>
        """, unsafe_allow_html=True)

# ✅ 두 번째 화면 (노트북 조회)
elif st.session_state.page == 2:
    with st.container():
        st.markdown(
            f"<p style='margin-top: 20px; margin-bottom: 10px;'>"
            f"<img src='https://raw.githubusercontent.com/kgh-kang/Test/refs/heads/main/assets/chatbot.png' width='30'></p>",
            unsafe_allow_html=True
        )

        # ✅ 안내 문구
        st.markdown("""
            <p style='font-family: "Noto Sans KR", sans-serif;'>
                <span style="font-size: 25px; font-weight: 400; font-weight: bold;">사번 입력.</span>
                <span style="font-size: 25px; font-weight: 400; color: #66666D;">구매 신청하시는 당신은 누군가요?</span>
            </p>
        """, unsafe_allow_html=True)

        # ✅ 입력 필드
        employee_id = st.text_input("사번", placeholder="모를 경우 사번 검색하기")

        # ✅ 조회하기 버튼 (입력값이 있어야 활성화)
        if employee_id.strip():
            if st.button("조회하기"):
                st.session_state.laptop_data = fetch_assets(employee_id)

        # ✅ 데이터 출력 (조회 결과가 있을 경우)
        if st.session_state.laptop_data:
            df = pd.DataFrame(st.session_state.laptop_data)
            st.table(df)

        # ✅ "이전으로" 버튼
        if st.button("이전으로", key="back"):
            change_page(1)
