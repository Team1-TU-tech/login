import streamlit as st
import requests as reqs
import smtplib
from email.message import EmailMessage
import random
import string

# 무작위 비밀번호 생성 함수
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# SMTP 연결 및 이메일 전송 함수
def send_email(to_email):
    try:
        # SMTP 세션 생성 및 연결
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()  # 연결 초기화 (optional, 대부분의 서버에서 필요함)
        s.starttls()  # TLS 보안 설정
        s.login("oddsummer56@gmail.com", "oopk dcmo unsg bwdl")  # 본인 이메일과 앱 비밀번호 필요

        # 무작위 비밀번호 생성
        random_password = generate_random_password()

        # 메일 메시지 작성
        message = EmailMessage()
        message['Subject'] = "임시 비밀번호 발급 안내"
        message['From'] = "oddsummer56@gmail.com"
        message['To'] = to_email
        message.set_content(f"요청하신 임시 비밀번호는 다음과 같습니다:\n\n{random_password}")

        # 메일 전송 및 세션 종료
        s.send_message(message)
        s.quit()
        st.success("이메일 전송 완료")

    except smtplib.SMTPException as e:
        st.error(f"이메일 전송 실패: {e}")

# 회원 정보 불러오기
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
    status = True
    if id and email:
        for user in load_data():
            if user["id"] == id and user["email"] == email:
                st.success(f"입력하신 {user['email']}에 임시 비밀번호가 발급되었습니다.")
                # 이메일 전송
                send_email(user["email"])
                status = False
        if status:
            st.warning("일치하는 정보가 없습니다. 입력하신 정보를 다시 확인해주세요")
    else:
        st.error("모두 입력!")
if splitView[-1].button("🔙"):
    st.switch_page("login.py")