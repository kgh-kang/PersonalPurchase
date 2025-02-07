import requests

# ✅ API 정보
BASE_URL = "http://assets.woowa.in/x1/api/help-desk/assets"
API_KEY = "Bearer help-desk-2e503c87-492f-4665-9a45-9a5517aa2e76"  # 🔹 API 키 입력
USER_NUMBER = "23080058"  # 🔹 조회할 유저 사번

headers = {
    "Authorization": API_KEY,
    "asset-user-number": USER_NUMBER
}

# ✅ 테스트할 유저 사번
test_user_number = "23080058"  # 🔹 테스트할 사번 (임의로 입력)

# ✅ API 호출 테스트
def test_api():
    url = f"{BASE_URL}/user/{test_user_number}"  # 🔹 API URL 구성
    try:
        response = requests.get(url, headers=headers)
        print(f"응답 코드: {response.status_code}")  # 🔹 응답 코드 출력

        if response.status_code == 200:
            print("✅ API 통신 성공!")
            print("응답 데이터:")
            print(response.json())  # 🔹 JSON 응답 출력
        else:
            print(f"⚠️ API 요청 실패: {response.status_code}")
            print(f"응답 본문: {response.text}")  # 🔹 에러 메시지 확인

    except requests.exceptions.RequestException as e:
        print(f"❌ API 요청 중 오류 발생: {e}")

# ✅ 실행
if __name__ == "__main__":
    test_api()
