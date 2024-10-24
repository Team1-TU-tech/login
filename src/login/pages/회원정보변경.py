import streamlit as st
import requests

st.write("## 회원 탈퇴를 위해서 ID를 입력해주세요")
user_id = st.text_input("ID","")

url = "http://localhost:8888/login/"

def change_page():
    try:
        r = requests.get(url)
        d = r.json()
        return d
    except:
        st.write("서버 연결이 불안정합니다. 다시 접속해주세요!")
        
        colums = 
        df = pd.DataFrame(d)
        st.write(d)
        return None
def select_column():
    user_firstname = st.text_input("fisrtname","")
    user_lastname = st.text_input("lastname", "")
    user_passwd = st.test_input("password","")
    user_email = st.test_input("email","")
    user_gender = st.test_input("gender","")
    user_birthday = st.test_inpu("birthday", "")
    user_phonenumber = st.test_input("phonenumber","")
    if user_id:
        if user



