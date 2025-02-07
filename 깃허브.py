import streamlit as st

# Streamlit 설정
st.set_page_config(page_title="노후장비 개인구매", layout="wide")

# GitHub에 업로드한 이미지 URL (사용자명/저장소명을 실제 값으로 변경)
GITHUB_IMAGE_URL = "https://raw.githubusercontent.com/사용자명/저장소명/main/assets/image_1.png"

# Streamlit 실행
st.markdown("<h1 style='text-align: center; font-size: 70px;'>노후장비 개인구매</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #66666D;'>₩10,000부터</h3>", unsafe_allow_html=True)

# GitHub에서 직접 이미지 로드
st.image(GITHUB_IMAGE_URL, use_container_width=True)  # 변경된 부분

# 버튼 생성
if st.button("구매 신청하기", use_container_width=True):  # 버튼도 화면 크기에 맞게 조정
    st.success("구매 신청이 완료되었습니다!")

# 안내 문구
st.markdown("<h4 style='text-align: center; color: black;'>시간이 좀 더 필요하신가요?</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #66666D;'>신규 장비 수령 후 2주가 지나면 구매 기회가 사라집니다.</p>", unsafe_allow_html=True)
