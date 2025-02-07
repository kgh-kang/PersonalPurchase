import streamlit as st

st.title("안녕하세요! 🚀")
st.write("이 앱은 GitHub Private Repo + Streamlit Cloud에서 실행됩니다.")

user_input = st.text_input("이름을 입력하세요:")
if user_input:
    st.write(f"반갑습니다, {user_input}님!")
