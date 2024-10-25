import streamlit as st
import requests
import datetime

# 페이지 상태를 초기화 (페이지 상태를 세션에서 관리)
if 'page' not in st.session_state:
    st.session_state['page'] = 'signup'
if 'id_check' not in st.session_state:
    st.session_state['id_check'] = None  # 아이디 중복 확인 결과 상태


# 서버에 POST 요청을 보내는 함수
def load_data(firstname, lastname, id, passwd, email, gender, birthday, phonenumber):
    if firstname and lastname and id and passwd and email and gender and birthday and phonenumber:
        headers = {'Content-Type': 'application/json'}
        params = {
            'firstname': firstname,
            'lastname': lastname,
            'id': id,
            'passwd': passwd,
            'email': email,
            'gender': gender,
            'birthday': birthday.strftime('%Y-%m-%d'),  # date 객체를 문자열로 변환
            'phonenumber': phonenumber
        }

        try:
            response = requests.post('http://127.0.0.1:8888/login', json=params, headers=headers, timeout=15)
            if response.status_code == 200:
                st.session_state['page'] = 'success'  # 성공 시 페이지 상태 변경
            else:
                st.write("가입에 실패했습니다. 다시 시도해주세요.")
        except Exception as e:
            st.write("서버가 불안정하오니 나중에 다시 시도해주세요.")
            st.write(f"오류: {str(e)}")
    else:
        st.write("모든 항목을 입력해 주세요.")

# 서버에 GET 요청을 보내는 함수 (아이디 중복 확인)
def check_userid(userid):
    url = f'http://127.0.0.1:8888/login/find?id={userid}'
    try:
        r = requests.get(url)
        if r.status_code == 200:  # 아이디가 존재할 때
            st.session_state['id_check'] = '이미 존재하는 아이디입니다.'
        elif r.status_code == 404:  # 아이디가 존재하지 않을 때
            st.session_state['id_check'] = '사용 가능한 아이디입니다.'
        else:
            st.session_state['id_check'] = '아이디 확인 중 문제가 발생했습니다.'
    except requests.ConnectionError:
        st.write("서버가 불안정합니다.")
        st.session_state['id_check'] = '서버 연결 실패'

# 페이지 이동 함수
def redirect_page():
    if st.session_state['page'] == 'signup':
        show_signup_form()
    elif st.session_state['page'] == 'success':
        show_success_page()

# 회원가입 폼
def show_signup_form():
    st.title("회원가입")

    firstname = st.text_input("이름")
    lastname = st.text_input("성")
    userid = st.text_input("아이디")

    if st.button("아이디 중복 확인"):
        if check_userid(userid): # 아이디 중복 확인 요청
            st.write(st.session_state['id_check'])
    if st.session_state['id_check']:
        st.write(st.session_state['id_check'])  # 중복 확인 결과 출력

    passwd = st.text_input("비밀번호", type="password")
    email = st.text_input("이메일")
    gender = st.selectbox("성별", ("M", "F"),index=None)
    birthday = st.date_input("생년월일", value=None)
    phonenumber = st.text_input("전화번호")

    if st.button("가입하기"):
        if st.session_state['id_check'] == '사용 가능한 아이디입니다.':  # 아이디 사용 가능 여부 확인
            load_data(firstname, lastname, userid, passwd, email, gender, birthday, phonenumber)
            st.rerun()
        else:
            st.write("아이디 중복 확인을 해주세요.")

# 가입 성공 페이지
def show_success_page():
    st.title("가입이 완료되었습니다!")
    st.write("환영합니다!")
    #if st.button("로그인 하기"):
    #    st.session_state['page'] = 'main'  # 다시 메인 페이지로 이동
        #st.rerun() #바로 리다이렉트

# 메인 로직 (페이지 이동 처리)
redirect_page()

