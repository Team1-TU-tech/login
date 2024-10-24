import requests
import streamlit as st  
st.title("회원 탈퇴")
st.write("회원 탈퇴를 위해 ID를 입력해주세요!")
user_id = st.text_input("id","")

url = 'http://localhost:8888/login'
def load_data():
    try:
        r = requests.get(url)
        d= r.json()

        return d

    except ConnectionError:
        st.write("서버가 불안정합니다. 다시 접속해주세요 !")

# 동적 파라미터를 위한 초기 딕셔너리
def show_update_data():
    logindata = load_data()
    if st.button("submit"):
        if logindata['id']==user_id:
            st.write("업데이트하고 싶은 회원 정보를 입력해 주세요")
            return update_data()
        else:
            st.write("회원 정보가 없습니다.ID를 확인해 주세요")

def update_data():

    params = {}

    # 예시로 Streamlit input을 사용하여 값을 입력받음
    user_firstname = st.text_input("Firstname","")
    user_lastname = st.text_input("Lastname","")
    user_passwd = st.text_input("Password","")
    user_email = st.text_input("Email","")
    user_gender = st.text_input("Gender","")
    user_birthday = st.text_input("Birthday","")
    user_phonenumber = st.text_input("Phonenumber","")

    headers = {
        'Content-Type': 'application/json',
    }

    if user_firstname:
        params['firstname'] = user_firstname
    if user_lastname:
        params['lastname'] = user_lastname
    if user_passwd:
        params['password'] = user_passwd
    if user_email:
        params['email'] = user_email
    if user_gender:
        params['gender'] = user_gender
    if user_birthday:
        params['birthday'] = user_birthday
    if user_phonenumber:
        params['phonenumber'] = user_phonenumber

    # 유저 ID가 있을 때 업데이트 진행
    if st.button("Submit"):
        if params:  # params가 비어있지 않다면 요청
            try:
                r = requests.patch(url=url, headers=headers, json=params)
                if r.status_code == 200:
                    st.write(f"{user_id}님의 회원 정보가 업데이트가 되었습니다.")
                else:
                    st.write(f"{user_id}님의 회원 정보 업데이트가 실패하였습니다. 다시 시도해 주세요!")
            except Exception as e:
                st.write(f"페이지가 응답하지 않습니다. 다시 접속해 주세요!")
        else:
            st.write("업데이트하고 싶은 정보를 입력해주세요!")
show_database()
