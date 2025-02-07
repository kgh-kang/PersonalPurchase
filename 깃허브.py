import streamlit as st
import requests

# ✅ API 정보
BASE_URL = "http://assets.woowa.in/x1/api/help-desk/assets/user"
API_KEY = "Bearer help-desk-2e503c87-492f-4665-9a45-9a5517aa2e76"  # 🔹 실제 API 키 입력
USER_NUMBER = "23080058"  # 🔹 조회하는 유저 사번 (고정)

headers = {
    "Authorization": API_KEY,
    "asset-user-number": USER_NUMBER
}

# ✅ Streamlit UI
st.title("🔹 Woowa API 조회 테스트")

# ✅ 사용자 입력 (조회할 사번)
user_number = st.text_input("조회할 유저 사번 입력:", "")

# ✅ API 요청 버튼
if st.button("조회하기"):
    if user_number.strip():  # 빈 값이 아닐 경우 실행
        with st.spinner("API 요청 중..."):
            api_url = f"{BASE_URL}/{user_number}"  # ✅ 입력한 사번을 URL에 적용
            st.write(f"🔹 요청 URL: {api_url}")  # 🔹 디버깅용 (요청 URL 확인)

            try:
                response = requests.get(api_url, headers=headers, timeout=10)  # ✅ 최대 10초 대기
                st.write(f"응답 코드: {response.status_code}")  # 🔹 응답 코드 출력

                if response.status_code == 200:
                    st.success("✅ API 통신 성공!")
                    st.json(response.json())  # ✅ JSON 응답 출력
                else:
                    st.error(f"⚠️ API 요청 실패: {response.status_code}")
                    st.write(f"응답 본문: {response.text}")  # 🔹 에러 메시지 확인

            except requests.exceptions.Timeout:
                st.error("❌ API 응답 시간이 초과되었습니다. 다시 시도하세요.")
            except requests.exceptions.RequestException as e:
                st.error(f"❌ API 요청 중 오류 발생: {e}")
    else:
        st.warning("⚠️ 조회할 유저 사번을 입력하세요.")
