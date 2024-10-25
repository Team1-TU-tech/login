import requests
import streamlit as st  
st.title("회원 정보 수정")
st.write("### 회원 정보 수정을 원하시면 ID를 입력해주세요!")
user_id = st.text_input("id","")
url =f'http://localhost:8888/login'
#url =f'http://localhost:8888/login/{user_id}'ID
st.write("회원정보가 없으면 상세 정보 입력란이 보이지 않습니다. 회원가입 후 다시 시도해주세요!")
if "is_submitted" not in st.session_state:
    st.session_state.is_submitted = False
def load_data():
    try:
        r = requests.get(url)
        d= r.json()

        return d

    except ConnectionError:
        st.write("서버가 불안정합니다. 다시 접속해주세요 !")


# 동적 파라미터를 위한 초기 딕셔너리
def show_update():
    logindata = load_data()
    for i in range(len(logindata)):
        if logindata[i]['id']==user_id:
            patch_data()
    
def patch_data():

    # 동적 파라미터를 위한 초기 딕셔너리
    user_firstname = st.text_input("Firstname")
    user_lastname = st.text_input("Lastname")
    user_passwd = st.text_input("Password")
    user_email = st.text_input("Email")
    user_gender = st.text_input("Gender")
    user_birthday = st.text_input("Birthday")
    user_phonenumber = st.text_input("Phonenumber")
    
    url = f'http://localhost:8888/login/{user_id}'  # 본인의 URL로 수정
    headers = {'Content-Type': 'application/json'}
    params = {"firstname":user_firstname, "lastname":user_lastname,"id":user_id, "passwd":user_passwd, "email":user_email,  "gender":user_gender, "birthday":user_birthday, "phonenumber":user_phonenumber}
    if st.button("Submit"):
        try:
            r = requests.patch(url=url, headers=headers, json=params)
            if r.status_code==200:
                st.write(f"{user_id}님의 정보가 수정되었습니다!")
            else:
                st.write("서버가 불안정합니다. 다시 시도해주세요")
        except:
            st.write(f"다시 시도해주세요")
    else:
        st.write("정보를 입력 후 summit 버튼을 눌러주세요")


show_update()  
