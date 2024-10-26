import streamlit as st
import requests
import time
import bcrypt

#비밀번호 검증 함수
def check_password(new_passwd, hashed):
    return bcrypt.checkpw(new_passwd.encode(), hashed.encode('utf-8'))

# 회원정보 로드
def load_data():
    url = f'http://localhost:8888/login'
    try:
        r = requests.get(url)
        d = r.json()
        return d
    except ConnectionError:
        st.write("서버가 불안정합니다. 다시 접속해주세요!")

# 회원 탈퇴
if 'id' in st.session_state and st.session_state['logged_in']:
    st.title("회원 탈퇴")
    st.write("#### 회원 탈퇴를 위해 비밀번호를 입력해주세요")
    user_passwd = st.text_input("비밀번호 확인",type="password")

# 버튼 나누기
splitView = [i for i in st.columns([12, 2])]  

with splitView[0]:  # 확인 버튼
    if st.button("제출하기", key="submit_button"):
        pwdata=load_data()
        for pw in pwdata:
            if check_password(user_passwd, pw['passwd']):
                try:
                    user_id = st.session_state['id']
                    url = f'http://localhost:8888/login/{user_id}'
                    r = requests.delete(url)
                    if r.status_code == 200:
                        st.write(f"{user_id}님의 탈퇴가 완료되었습니다. 다음에 다시 만나요!😥")
                        time.sleep(1)
                        for k, v in st.session_state.items():
                            st.session_state[k] = None
                            st.switch_page("login.py")
                    else:
                        st.write(f"{user_id}님의 정보가 없습니다. ID를 다시 확인한 후 입력해주세요!")
                except Exception as e:
                    st.write('페이지가 응답하지 않습니다. 다시 접속해 주세요!')
            else:
                st.write("비밀번호가 일치하지 않습니다. 확인 후 다시 시도해주세요")

with splitView[1]:  # back 버튼
    if st.button("뒤로가기"):
        st.switch_page("pages/user_update.py")

