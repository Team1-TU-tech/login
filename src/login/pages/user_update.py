import requests
import streamlit as st  
import bcrypt

st.title("회원 정보 수정")
st.write("#### 회원 정보를 수정하려면 ID를 입력 후 `ENTER`를 눌러주세요!")
user_id = st.text_input("아이디", "")
url = f'http://localhost:8888/login'

# 비밀번호 해시화 함수
def hash_password(password):
    # bcrypt 해시 생성
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed.decode('utf-8')  # 문자열로 변환 후 반환

if "is_submitted" not in st.session_state:
    st.session_state.is_submitted = False

def load_data():
    try:
        r = requests.get(url)
        d = r.json()
        return d
    except ConnectionError:
        st.write("서버가 불안정합니다. 다시 접속해주세요!")

# 버튼을 위한 열 배치
splitView = [i for i in st.columns([12, 1])] 

# 탈퇴하기 버튼
with splitView[0]:
    if st.button("탈퇴하기", key="delete_button"):
        st.switch_page("pages/user_deletion.py")

# back 버튼
with splitView[1]:  
    if st.button("🔙", key="back_button"):
        st.session_state['page'] = None
        st.session_state['id_check'] = None
        st.switch_page("login.py")

# 동적 파라미터를 위한 초기 딕셔너리
def show_update():
    logindata = load_data()
    for i in range(len(logindata)):
        if logindata[i]['id'] == user_id:
            patch_data()

def patch_data():
    # 동적 파라미터를 위한 초기 딕셔너리
    user_firstname = st.text_input("이름")
    user_lastname = st.text_input("성")
    user_passwd = st.text_input("비밀번호", type='password')
    user_email = st.text_input("이메일")
    g = ['F', 'M']
    user_gender = st.selectbox("성별", g)
    user_birthday = st.date_input("생년월일").strftime('%Y-%m-%d')
    user_phonenumber = st.text_input("전화번호")

    # 비밀번호를 해시화
    hashed_password = hash_password(user_passwd)  # 입력받은 비밀번호를 해시화
    
    url = f'http://localhost:8888/login/{user_id}'  # 본인의 URL로 수정
    headers = {'Content-Type': 'application/json'}
    params = {
        "firstname": user_firstname, 
        "lastname": user_lastname,
        "id": user_id,
        "passwd": hashed_password,
        "email": user_email,
        "gender": user_gender,
        "birthday": user_birthday,
        "phonenumber": user_phonenumber
    }

    # 수정하기 및 back 버튼을 배치할 열 구성
    splitView = [i for i in st.columns([12, 1])]

    # 수정하기 버튼
    with splitView[0]:
        if st.button("수정하기", key="update_button"):
            try:
                r = requests.patch(url=url, headers=headers, json=params)
                if r.status_code == 200:
                    st.write(f"{user_id}님의 정보가 수정되었습니다!")
                else:
                    st.write("서버가 불안정합니다. 다시 시도해주세요.")
            except Exception as e:
                st.write(f"오류 발생: {str(e)}")

    # back 버튼
    with splitView[1]:
        if st.button("🔙", key="back_button_in_patch"):
            st.session_state['page'] = None
            st.session_state['id_check'] = None
            st.switch_page("login.py")

show_update()
