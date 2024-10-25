import streamlit as st
import requests
import datetime
import bcrypt
import base64

# 페이지 상태를 초기화 (페이지 상태를 세션에서 관리)
if 'page' not in st.session_state:
    st.session_state['page'] = None
if 'id_check' not in st.session_state:
    st.session_state['id_check'] = None  # 아이디 중복 확인 결과 상태


# 서버에 POST 요청을 보내는 함수
def load_data(firstname, lastname, id, hashed_passwd, email, gender, birthday, phonenumber):
    if firstname and lastname and id and hashed_passwd and email and gender and birthday and phonenumber:
        headers = {'Content-Type': 'application/json'}
        params = {
            'firstname': firstname,
            'lastname': lastname,
            'id': id,
            'passwd': hashed_passwd,
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
                st.error("가입에 실패했습니다. 다시 시도해주세요.")
        except Exception as e:
            st.werror("서버가 불안정하오니 나중에 다시 시도해주세요.")
            st.error(f"오류: {str(e)}")
    else:
        st.error("모든 항목을 입력해 주세요.")

# 서버에 GET 요청을 보내는 함수 (아이디 중복 확인)
def check_userid(userid):
    url = f'http://127.0.0.1:8888/login/find?id={userid}'
    try:
        r = requests.get(url)
        data = r.json()  # 서버에서 반환된 JSON 데이터
        if isinstance(data, list) and len(data) > 0 and 'id' in data[0]:
            return True  # 아이디가 존재하는 경우
        else:
            return False  # 아이디가 존재하지 않는 경우
    except requests.ConnectionError:
        st.write("서버가 불안정합니다. 다시 접속해주세요!")
        return None
    except ValueError:
        st.write("서버에서 올바르지 않은 데이터를 받았습니다.")
        return None

# 페이지 이동 함수
def redirect_page():
    if st.session_state['page'] == 'success':
        show_success_page()
    else:
        show_signup_form()

def hash_password(passwd):
    # bcrypt 해시를 생성하고 문자열로 변환
    hashed = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt(rounds=5)) #해시화 5번
    return hashed.decode('utf-8')  # 문자열로 변환 후 리턴

# 비밀번호 검증 함수
def check_password(passwd, hashed):
    decoded_hashed = base64.b64decode(hashed)
    return bcrypt.checkpw(passwd.encode(), decoded_hashed)


# 회원가입 폼
def show_signup_form():
    st.title("회원가입")


    firstname = st.text_input("이름")
    lastname = st.text_input("성")
    userid = st.text_input("아이디")

    if st.button("아이디 중복 확인"):
        is_existing = check_userid(userid)
        if is_existing is False:  # 중복된 아이디일 경우
            st.session_state['id_check'] = '이미 존재하는 아이디입니다.'
        else:
            st.session_state['id_check'] = '사용 가능한 아이디입니다.'
        st.rerun()  # 상태 업데이트 후 페이지 다시 렌더링

    # 중복 확인 결과 출력
    if 'id_check' in st.session_state:
        st.write(st.session_state['id_check'])

    passwd = st.text_input("비밀번호", type="password")
    email = st.text_input("이메일")
    gender = st.selectbox("성별", ("M", "F"),index=None)
    birthday = st.date_input("생년월일", value=None)
    phonenumber = st.text_input("전화번호")

    # 가입하기 및 back 버튼을 배치할 열 구성
    splitView = [i for i in st.columns([12, 1])]  

    with splitView[0]:
        if st.button("가입하기"):
            if st.session_state['id_check'] == '사용 가능한 아이디입니다.':  # 아이디 사용 가능 여부 확인
                hashed_passwd = hash_password(passwd)  # 비밀번호 해시화
                load_data(firstname, lastname, userid, hashed_passwd, email, gender, birthday, phonenumber)
                st.rerun()
            else:
                st.error("아이디 중복 확인을 해주세요.")

    with splitView[1]:
        if st.button("🔙"):
            st.session_state['page'] = None
            st.session_state['id_check'] = None
            st.switch_page("login.py")


# 가입 성공 페이지
def show_success_page():
    st.title("가입이 완료되었습니다!")
    st.success("환영합니다!")
    st.page_link("login.py", label="로그인")


# 메인 로직 (페이지 이동 처리)
redirect_page()