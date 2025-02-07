import streamlit as st
import requests

# ✅ API 정보
BASE_URL = "http://assets.woowa.in/x1/api/help-desk/assets"
API_KEY = "Bearer help-desk-2e503c87-492f-4665-9a45-9a5517aa2e76"  # 🔹 API 키 입력
USER_NUMBER = "23080058"  # 🔹 조회할 유저 사번

headers = {
    "Authorization": API_KEY,
    "asset-user-number": USER_NUMBER
}

# ✅ Streamlit UI
st.title("API 통신 테스트")

# 사용자 입력 필드 (사번 입력)
user_number = st.text_input("사번을 입력하세요:", "20020049")

# 조회 버튼
if st.button("API 조회"):
    with st.spinner("API 요청 중..."):
        url = f"{BASE_URL}/user/{user_number}"  # 🔹 API URL 구성

        try:
            response = requests.get(url, headers=headers)
            st.write(f"응답 코드: {response.status_code}")  # 🔹 응답 코드 출력

            if response.status_code == 200:
                st.success("✅ API 통신 성공!")
                st.json(response.json())  # 🔹 JSON 응답 출력
            else:
                st.error(f"⚠️ API 요청 실패: {response.status_code}")
                st.write(f"응답 본문: {response.text}")  # 🔹 에러 메시지 확인

        except requests.exceptions.RequestException as e:
            st.error(f"❌ API 요청 중 오류 발생: {e}")
