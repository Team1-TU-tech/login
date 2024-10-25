import streamlit as st
import requests
st.title("회원탈퇴")
st.write("## 회원 탈퇴를 위해 ID를 입력해주세요")
user_id = st.text_input("ID","")

url =f'http://localhost:8888/login/{user_id}'

def delete_data():
    if st.button("Submit"):
        params = {'id':f'{user_id}'}
        try:
            r = requests.delete(url=url, json = params)
            if r.status_code == 200:
                st.write(f"{user_id}님의 탈퇴가 완료되었습니다. 다음에 만나요!😥")
                st.switch_page("login.py")
            else:
                st.write(f"{user_id}님의 정보가 없습니다. ID를 다시 확인한 후 입력해주세요 !")
        except Exception as e:
            st.write('페이지가 응답하지 않습니다. 다시 접속해 주세요!')
    else:
        st.write("ID를 입력후 버튼을 눌러주세요!")

delete_data()
