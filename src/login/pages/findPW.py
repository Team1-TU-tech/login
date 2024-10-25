import streamlit as st
import requests as reqs
import smtplib
from email.message import EmailMessage
import random
import string
import bcrypt
import os

# 무작위 비밀번호 생성 함수
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# 비밀번호 해시화 함수
def hash_password(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=5))  # bcrypt 해시 생성
    return hashed.decode('utf-8')  # 문자열 변환 후 반환

# 환경 변수에서 이메일과 비밀번호 가져오기
send_email = os.getenv("SEND_EMAIL")
app_pw = os.getenv("APP_PW")

# 잘 EXPORT 되었는지 콘솔에서 확인용
print(f"SEND_EMAIL: {send_email}")      
print(f"APP_PW: {app_pw}")  

# SMTP 연결 및 이메일 전송 함수
def send_temp_password_email(to_email, random_password):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(send_email, app_pw)

        message = EmailMessage()
        message['Subject'] = "임시 비밀번호 발급 안내"
        message['From'] = send_email
        message['To'] = to_email
        message.set_content(f"{user['id']}님이 요청하신 임시 비밀번호는 다음과 같습니다:\n\n{random_password}")

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
    except reqs.ConnectionError:
        st.error("서버가 불안정합니다.")

st.title("패스워드 찾기")
id = st.text_input("아이디", key="id")
email = st.text_input("이메일", key="email")

splitView = [i for i in st.columns([12, 1])]

# 찾기 버튼 클릭 시
if splitView[0].button("찾기"):
    status = True
    if id and email:
        for user in load_data():
            if user["id"] == id and user["email"] == email:
                st.success(f"입력하신 {user['email']}에 임시 비밀번호가 발급되었습니다.")

                # 임시 비밀번호 생성 및 암호화 저장
                random_password = generate_random_password()
                hashed_password = hash_password(random_password)  # 생성된 임시 비밀번호를 해시화

                # 이메일 전송
                send_temp_password_email(user["email"], random_password)

                # 해시화된 비밀번호로 DB 업데이트
                url = f'http://localhost:8888/login/{id}'  # PATCH 요청 URL
                headers = {'Content-Type': 'application/json'}
                params = {"passwd": hashed_password}  # 해시화된 비밀번호로 업데이트

                try:
                    r = reqs.patch(url=url, headers=headers, json=params)
                    if r.status_code == 200:
                        st.success(f"{id}님의 비밀번호가 임시 비밀번호로 업데이트되었습니다!")
                    else:
                        st.warning("서버가 불안정합니다. 다시 시도해주세요.")
                except reqs.RequestException:
                    st.warning("비밀번호 업데이트에 실패했습니다. 다시 시도해주세요.")

                status = False
        if status:
            st.warning("일치하는 정보가 없습니다. 입력하신 정보를 다시 확인해주세요")
    else:
        st.error("모두 입력!")

# 뒤로가기 버튼
if splitView[-1].button("🔙"):
    st.switch_page("login.py")
