import streamlit as st
import requests

# ✅ API 정보
BASE_URL = "http://assets.woowa.in/x1/api/help-desk/assets/user"
API_KEY = "Bearer help-desk-2e503c87-492f-4665-9a45-9a5517aa2e76"  # 🔹 API 키 입력
USER_NUMBER = "23080058"  # 🔹 기본 사용자 번호

headers = {
    "Authorization": API_KEY,
    "asset-user-number": USER_NUMBER
}

# ✅ Streamlit UI
st.title("API 통신 테스트")

# ✅ 상태 저장 변수 초기화 (첫 실행 시)
if "api_response" not in st.session_state:
    st.session_state.api_response = None  # API 응답 저장

# ✅ 사용자 입력 필드 (사번 입력)
user_number = st.text_input("사번을 입력하세요:", "23080058")  # 기본값 포함

# ✅ 조회 버튼 클릭 시 API 요청 실행
if st.button("조회하기"):
    with st.spinner("API 요청 중..."):
        api_url = f"{BASE_URL}/{user_number}"  # ✅ 입력한 사번을 URL에 적용
        st.write(f"🔹 요청 URL: {api_url}")  # 🔹 디버깅용 (요청 URL 확인)

        try:
            response = requests.get(api_url, headers=headers)
            st.write(f"응답 코드: {response.status_code}")  # 🔹 응답 코드 출력

            if response.status_code == 200:
                st.success("✅ API 통신 성공!")
                st.session_state.api_response = response.json()  # API 응답 저장
            else:
                st.error(f"⚠️ API 요청 실패: {response.status_code}")
                st.write(f"응답 본문: {response.text}")  # 🔹 에러 메시지 확인

        except requests.exceptions.RequestException as e:
            st.error(f"❌ API 요청 중 오류 발생: {e}")

# ✅ API 결과 출력 (이전 조회 결과 유지)
if st.session_state.api_response:
    st.json(st.session_state.api_response)
