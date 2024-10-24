import streamlit as st


st.title('회원가입')

def input_data():
    firstname = st.text_input("이름", "")
    lastname = st.text_input("성", "")
    id = st.text_input("아이디", "")
    passwd = st.text_input("패스워드", "")
    email = st.text_input("E-mail", "")
    gender = st.selectbox("성별",("M", "F"),)
    birthday = 


def post_data():
    headers = {
    'Content-Type': 'application/json',}

    json_data = {
        'num': 1,
        'firstname': 'universe',
        'lastname': 'tu',
        'id': 'ham',
        'passwd': '1234',
        'email': 'universe.tu@tut.com',
        'gender': 'F',
        'birthday': '2024.10.24',
        'phonenumber': '01020241024',
    }

    response = requests.post('http://localhost:8888/login', headers=headers, json=json_data)
    
