import streamlit as st
from pathlib import Path

# Streamlit 설정
st.set_page_config(page_title="노후장비 개인구매", layout="wide")

# 이미지 상대 경로 설정 (현재 실행 파일 기준)
ASSETS_PATH = Path(__file__).parent / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# 이미지 표시
image_path = relative_to_assets("image_1.png")

# Streamlit 실행
st.markdown("<h1 style='text-align: center; font-size: 70px;'>노후장비 개인구매</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #66666D;'>₩10,000부터</h3>", unsafe_allow_html=True)

# 이미지 표시 (파일이 존재하는 경우만)
if image_path.exists():
    st.image(image_path, use_column_width=True)
else:
    st.warning("이미지 파일을 찾을 수 없습니다. GitHub에서 직접 불러오는 방식을 사용할 수도 있습니다.")

# 버튼 생성
if st.button("구매 신청하기", use_container_width=True):
    st.success("구매 신청이 완료되었습니다!")

# 안내 문구
st.markdown("<h4 style='text-align: center; color: black;'>시간이 좀 더 필요하신가요?</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #66666D;'>신규 장비 수령 후 2주가 지나면 구매 기회가 사라집니다.</p>", unsafe_allow_html=True)
