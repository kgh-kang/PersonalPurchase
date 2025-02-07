import streamlit as st
import requests

# ✅ 테스트할 공공 API (무료 API)
TEST_API_URL = "https://jsonplaceholder.typicode.com/todos/1"  # 샘플 JSON 데이터 제공 API

st.title("🔹 공공 API 테스트")

# ✅ API 요청 실행
if st.button("API 요청 테스트"):
    with st.spinner("API 요청 중..."):
        try:
            response = requests.get(TEST_API_URL, timeout=10)  # ✅ 최대 10초 대기
            st.write(f"응답 코드: {response.status_code}")  # 🔹 응답 코드 출력

            if response.status_code == 200:
                st.success("✅ API 요청 성공!")
                st.json(response.json())  # ✅ JSON 응답 출력
            else:
                st.error(f"⚠️ API 요청 실패: {response.status_code}")
                st.write(f"응답 본문: {response.text}")  # 🔹 에러 메시지 확인

        except requests.exceptions.Timeout:
            st.error("❌ API 응답 시간이 초과되었습니다. 다시 시도하세요.")
        except requests.exceptions.RequestException as e:
            st.error(f"❌ API 요청 중 오류 발생: {e}")
