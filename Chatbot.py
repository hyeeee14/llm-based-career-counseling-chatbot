import streamlit as st

st.markdown("실험에 참여해주셔서 감사합니다!📝")
st.caption("챗봇을 골라주세요.")

if st.button("Chatbot-S"):
    st.switch_page("pages/1_Chatbot-S.py")
if st.button("Chatbot-N"):
    st.switch_page("pages/2_Chatbot-N.py")