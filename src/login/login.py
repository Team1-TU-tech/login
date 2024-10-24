import streamlit as st
import requests

#회원정보 불러오기
def load_data():
    url = 'http://127.0.0.1:8888/login'
    try:
        r = requests.get(url)
        get_json = r.json()
        
        return get_json

    except ConnectionError:
        st.write("서버가 불안정합니다.")


# 로그인 함수
def login(id, password):
    users = load_data()
    # 유저 검증
    for user in users:
        if user['id'] == id and user['passwd'] == password:
            st.session_state['logged_in'] = True
            st.session_state['id'] = id
            st.success(f"Welcome {user['firstname']} {user['lastname']}!")
            return
    st.error("아이디 혹은 비밀번호가 일치하지 않습니다.")

def logout():
    st.session_state['logged_in'] = False
    st.session_state['id'] = ""

# 로그인 화면
def login_screen():
    st.title("로그인")
    userid = st.text_input("아이디를 입력해주세요.", key="userid_input_1")
    password = st.text_input("비밀번호를 입력해주세요.", type="password", key="password_input_1")
    
    if st.button("Login"):
        if userid and password:  # 입력된 값이 있는지 확인
            login(userid, password)
        else:
            st.error("아이디와 비밀번호를 입력해주세요.")

# 메인 애플리케이션 화면 (로그인 후 접근 가능)
def main_app():
    st.title("Main Application")
    st.write(f"환영합니다, {st.session_state['id']}님!")
    if st.button("Logout"):
        logout()

# 세션 상태 초기화
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# 메인 로직
if st.session_state['logged_in']:
    main_app()
else:
    login_screen()
    

def kakao_login():
    kakao_auth_url = "https://kauth.kakao.com/oauth/authorize"
    client_id = "10570123f64afae6f4d4e06f75cffced"
    redirect_uri = "http://localhost:8501/callback"
    response_type = "code"

    # 인증 URL 생성
    auth_url = f"{kakao_auth_url}?client_id={client_id}&redirect_uri={redirect_uri}&response_type={response_type}"
    
    # 링크 버튼을 사용하여 Kakao 로그인 페이지로 리디렉션
    st.link_button("카카오 로그인", url=auth_url)


kakao_login()
