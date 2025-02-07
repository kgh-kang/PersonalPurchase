import streamlit as st
import requests
import pandas as pd

# Streamlit 설정
st.set_page_config(page_title="노후장비 개인구매", layout="wide")

# ✅ API 호출 함수
def fetch_assets(user_number):
    url = f"http://assets.woowa.in/x1/api/help-desk/assets/user/{user_number}"
    headers = {
        "Authorization": "실제토큰",
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

# ✅ 두 번째 화면
elif st.session_state.page == 2:
    with st.container():
        # 이미지 추가
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

        # ✅ CSS 적용 (입력 필드 크기 및 여백 조정)
        st.markdown("""
            <style>
            div.stTextInput > div > input {
                width: 400px !important;
                padding: 10px !important;
                border-radius: 8px !important;
            }
            
            /* 조회하기 버튼 스타일 */
            .disabled-btn {
                background-color: #D3D3D3 !important; /* 회색 (비활성화) */
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
                background-color: #2BC2BD !important; /* 민트색 (활성화) */
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
