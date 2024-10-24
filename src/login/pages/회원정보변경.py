import streamlit as st
import requests

st.write("## 회원 정보 변경 또는 회원 탈퇴를 원하시면 ID를 입력해주세요")
user_id = st.test_input("ID","")
user_id
url = "http://localhost:8888/login/"
def delete_data():
    if st.button("Submit"):
        if user_id:
            params = {'id':f'{user_id}'}
            try:
                r = requests.delete(url=url,params = params)
                if r.status_code == 200:
                    st.write(f"{user_id}님의 탈퇴가 완료되었습니다. 다음에 만나요!>
😥")
                else:
                    st.write(f"{user_id}님의 정보가 없습니다. ID를 다시 확인한 후 >
입력해주세요 !")
            except Exception as e:
                st.write('페이지가 응답하지 않습니다. 다시 접속해 주세요!')
        else:
            st.wirte("ID를 입력해주세요")

delete_data() 
