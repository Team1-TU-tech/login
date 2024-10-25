import streamlit as st
import requests as reqs

import smtplib
from email.message import EmailMessage

# SMTP 세션생성
s = smtplib.SMTP('smtp.gmail.com', 587)
# 보안 TLS 시작
s.starttls()
# 로그인 & 인증
s.login("oddsummer56@gmail.com", "readysetshine56*")
# 보낼 메시지 지정
message = EmailMessage()
message['Subject'] = f"제목"
message['From'] = "oddsummer56@gmail.com"
message['To'] = "jihyuno0730@naver.com"
message.set_content("본문")
# 메일전송
s.send_message(message)
# 메일전송세션 종료
s.quit()

#회원정보 불러오기
def load_data():
    url = 'http://127.0.0.1:8888/login'
    try:
        r = reqs.get(url)
        get_json = r.json()

        return get_json

    except ConnectionError:
        st.write("서버가 불안정합니다.")


st.title("패스워드 찾기")
id = st.text_input("ID.", key="id")
email = st.text_input("email.", key="email")

splitView = [i for i in st.columns(7)]

if splitView[0].button("찾기"):
    status=True
    if id and email:
        for user in load_data():
            if user["id"]==id and user["email"]==email:
                st.success(f"입력하신 정보에 해당하는 ID는 **{user['id']}** 입니다.")
                status=False
        if status:
            st.warning("일치하는 정보가 없습니다. 입력하신 정보를 다시 확인해주세요")
    else:
        st.error("모두 입력!")
if splitView[-1].button("🔙"):
    st.switch_page("login.py")


