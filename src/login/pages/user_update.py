import requests
import streamlit as st  

st.title("회원 정보 수정")
st.write("### ID를 입력 후 `ENTER`를 눌러주세요!")
user_id = st.text_input("아이디","")
url =f'http://localhost:8888/login'
#url =f'http://localhost:8888/login/{user_id}'ID

if "is_submitted" not in st.session_state:
    st.session_state.is_submitted = False

if st.button("탈퇴하기"):
    st.switch_page("pages/user_deletion.py")


def load_data():
    try:
        r = requests.get(url)
        d= r.json()

        return d

    except ConnectionError:
        st.write("서버가 불안정합니다. 다시 접속해주세요 !")
    if st.button("탈퇴하기"):
        st.switch_page("pages/user_deletion.py")

# 동적 파라미터를 위한 초기 딕셔너리
def show_update():
    logindata = load_data()
    for i in range(len(logindata)):
        if logindata[i]['id']==user_id:
            patch_data()

def patch_data():

    # 동적 파라미터를 위한 초기 딕셔너리
    user_firstname = st.text_input("이름")
    user_lastname = st.text_input("성")
    user_passwd = st.text_input("비밀번호",type='password')
    user_email = st.text_input("이메일")
    g=['F','M']
    user_gender = st.multiselect("성별",g)
    user_birthday = st.date_input("생년월일")
    user_phonenumber = st.text_input("전화번호")
    
    url = f'http://localhost:8888/login/{user_id}'  # 본인의 URL로 수정
    headers = {'Content-Type': 'application/json'}
    params = {"firstname":user_firstname, "lastname":user_lastname,"id":user_id, "passwd":user_passwd, "email":user_email,  "gender":user_gender, "birthday":user_birthday, "phonenumber":user_phonenumber}
    if st.button("변경하기"):
        try:
            r = requests.patch(url=url, headers=headers, json=params)
            if r.status_code==200:
                st.write(f"{user_id}님의 정보가 수정되었습니다!")
            else:
                st.write("서버가 불안정합니다. 다시 시도해주세요")
        except:
            st.write(f"다시 시도해주세요")
    # else:
    #     st.write("정보를 입력 후 summit 버튼을 눌러주세요")


show_update()  
