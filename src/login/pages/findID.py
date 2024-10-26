import streamlit as st
import requests as reqs


#회원정보 불러오기
def load_data():
    url = 'http://127.0.0.1:8888/login'
    try:
        r = reqs.get(url)
        get_json = r.json()

        return get_json

    except ConnectionError:
        st.error("서버가 불안정합니다.")


st.title("아이디 찾기")
firstName = st.text_input("이름", key="firstName")
lastName = st.text_input("성", key="lastName")
phoneNumber = st.text_input("전화번호", key="phonenumber")

splitView = [i for i in st.columns([12, 2])]

if splitView[0].button("찾기"):
    status=True
    if firstName and lastName and phoneNumber:
        for user in load_data():
            if user["firstname"]==firstName and user["lastname"]==lastName and user["phonenumber"]==phoneNumber:
                st.success(f"입력하신 정보에 해당하는 ID는 **{user['id']}** 입니다.")
                status=False
        if status:
            st.warning("일치하는 정보가 없습니다. 입력하신 정보를 다시 확인해주세요")
    else:
        st.error("모두 입력!")
if splitView[-1].button("뒤로가기"):
    st.switch_page("login.py")
