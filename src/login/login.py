import streamlit as st
import requests as reqs
import bcrypt
import base64
import os

st.session_state['page'] = None

####### 카카오 토큰 설정 + 로그아웃 #############################
if 'klogin_token' not in st.session_state:
    st.session_state['klogin_token'] = None

def logout_kakao():
    params = {
        'client_id': os.getenv("KAKAO_TOKEN",""),
        'logout_redirect_uri': "http://localhost:8501/",
    }
    logout_url = f"https://kauth.kakao.com/oauth/logout?client_id={params['client_id']}&logout_redirect_uri={params['logout_redirect_uri']}"

    return logout_url
####### 카카오 토큰 설정 + 로그아웃 끝 ##########################

#회원정보 불러오기
def load_data():
    url = 'http://127.0.0.1:8888/login'
    try:
        r = reqs.get(url)
        get_json = r.json()
        
        return get_json

    except ConnectionError:
        st.write("서버가 불안정합니다.")

###### 카카오 로그인 버튼 만들기 ###########################################################################
def kakao_login():
    kakao_auth_url = "https://kauth.kakao.com/oauth/authorize"
    client_id = os.getenv("KAKAO_TOKEN","")
    redirect_uri = "http://localhost:8501/callback"
    response_type = "code"

    # 인증 URL 생성
    auth_url = f"{kakao_auth_url}?client_id={client_id}&redirect_uri={redirect_uri}&response_type={response_type}"

    # 링크 버튼을 사용하여 Kakao 로그인 페이지로 리디렉션
    # st.link_button("카카오 로그인", url=auth_url)

    html = f"<a href='{auth_url}'><img src='./app/static/kakao.png'></a>"
    st.markdown(html, unsafe_allow_html=True)
###### 카카오 로그인 버튼 만들기  끝 #######################################################################

# 비밀번호 검증 함수
def check_password(passwd, hashed):
    return bcrypt.checkpw(passwd.encode(), hashed.encode())

# 로그인 함수
def login(id, password):
    users = load_data()

    # 유저 검증
    for user in users:
        if user['id'] == id and check_password(password, user['passwd']):
            st.session_state['logged_in'] = True
            st.session_state['id'] = id
            st.success(f"Welcome {user['firstname']} {user['lastname']}!")
            st.rerun()      # 버튼 누르면 바로 새로고침
            return
    st.error("아이디 혹은 비밀번호가 일치하지 않습니다.")

def logout():
    st.session_state['logged_in'] = False
    st.session_state['id'] = ""
    st.rerun()

# 로그인 화면
def login_screen():
    st.title("로그인")
    userid = st.text_input("아이디를 입력해주세요.", key="userid_input_1")
    password = st.text_input("비밀번호를 입력해주세요.", type="password", key="password_input_1")
    columns = [i for i in st.columns(5)]
    kakao_login()     # 카카오 로그인 버튼
    
    if columns[0].button("Login"):
        if userid and password:  # 입력된 값이 있는지 확인
            login(userid, password)
        else:
            st.error("아이디와 비밀번호를 입력해주세요.")
    if columns[2].button("아이디 찾기"):
        st.switch_page("pages/find.py")

    if columns[1].button("회원 가입"):
        st.switch_page("pages/signup.py")
    


# 메인 애플리케이션 화면 (로그인 후 접근 가능)
def main_app():
    st.title("TU-Universe-Tech")
    st.write(f"환영합니다, {st.session_state['id']}님!")
    #st.write(st.session_state)
    columns=[i for i in st.columns(5)]
    if st.session_state['klogin_token']:
        columns[0].link_button("Logout", url=logout_kakao())
    else:
        if columns[0].button("Logout"):
            logout()

    if st.session_state['klogin_token']==None:
        if columns[-1].button("회원정보 수정"):
            st.switch_page("pages/user_update.py")

# 세션 상태 초기화
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# 메인 로직
if st.session_state['logged_in']:
    main_app()
else:
    login_screen()



