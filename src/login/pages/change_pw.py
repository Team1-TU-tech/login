import requests
import streamlit as st  
import bcrypt
import os
import time

def hash_password(new_passwd):
    # bcrypt 해시 생성
    hashed = bcrypt.hashpw(new_passwd.encode(), bcrypt.gensalt())
    return hashed.decode('utf-8')

# 비밀번호 검증 함수
def check_password(new_passwd, hashed):
    # bcrypt 해시 값이 올바른 형식인지 확인하고 비교
    return bcrypt.checkpw(new_passwd.encode(), hashed.encode('utf-8'))

if "is_submitted" not in st.session_state:
    st.session_state.is_submitted = False

# 회원정보 로드
def load_data():
    url = f'http://localhost:8888/login'
    try:
        r = requests.get(url)
        d = r.json()
        return d
    except ConnectionError:
        st.write("서버가 불안정합니다. 다시 접속해주세요!")

def update_user_pw(user_id,updated_pw):
    url = f'http://localhost:8888/login/{user_id}'
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.patch(url, json=updated_pw, headers=headers)
        if response.status_code == 200:
            st.success(f"{user_id}님의 비밀번호가 성공적으로 변경되었습니다.")
            for k, v in st.session_state.items():
                st.session_state[k] = None
                time.sleep(0.7)
                st.switch_page("login.py")
        else:
            st.error("비밀번호 변경에 실패했습니다.")
    except requests.ConnectionError:
        st.error("서버 연결에 문제가 있습니다.")

if 'id' in st.session_state and st.session_state['logged_in']:
    st.title("비밀번호 변경")
    st.write("#### 기존 비밀번호와 새 비밀번호를 입력해주세요!")

    # 로그인한 사용자 정보 불러오기
    user_id = st.session_state['id']

    old_passwd = st.text_input("기존 비밀번호", type="password")
    new_passwd = st.text_input("새 비밀번호", type="password")
    confirm_passwd = st.text_input("비밀번호 확인", type="password")
        
    # 버튼을 위한 열 배치
    splitView = [i for i in st.columns([12,2])] 
    with splitView[0]:
        # 비밀번호 일치여부 확인 후 업데이트
        if st.button("제출하기", key="submit_button"):
            pwdata=load_data()
            for pw in pwdata:
                if check_password(old_passwd, pw['passwd']) and new_passwd == confirm_passwd:
                    hashed_passwd = hash_password(new_passwd)
                    updated_pw = {"passwd":hashed_passwd}
                    update_user_pw(user_id, updated_pw)
                    break
                elif check_password(old_passwd, pw['passwd'])== False:
                    st.write("기존 비밀번호가 일치하지 않습니다. 확인 후 다시 시도해 주세요!")
                    break
                elif new_passwd != confirm_passwd:
                    st.write("새로운 비밀번호와 재입력한 비밀번호가 일치하지 않습니다 !")
                    break

    # 뒤로가기 버튼
    with splitView[1]:  
        if st.button("뒤로가기", key="back_button"):
            st.session_state['page'] = None
            st.session_state['id_check'] = None
            st.switch_page("pages/user_update.py")
