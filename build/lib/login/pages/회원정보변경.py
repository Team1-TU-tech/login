import streamlit as st
import requests
st.title("회원 정보 변경")
st.write("## 회원 정보 변경을 위해 ID를 입력해주세요")
user_id = st.text_input("ID","")

url = 'http://172.21.0.2:8888/login'
def load_data():
    try:
        r = requests.get(url)
        d= r.json()

        return d

    except ConnectionError:
        st.write("서버가 불안정합니다. 다시 접속해주세요 !")

def delete_data():
    logindata = load_data()
    if st.button("Submit"):
        if logindata['id']==user_id:
            params = {'id':f'{user_id}'}
            try:
                r = requests.delete(url=url,params = params)
                if r.status_code == 200:
                    st.write(f"{user_id}님의 탈퇴가 완료되었습니다. 다음에 만나요!😥")
                else:
                    st.write(f"{user_id}님의 정보가 없습니다. ID를 다시 확인한 후 입력해주세요 !")
            except Exception as e:
                st.write('페이지가 응답하지 않습니다. 다시 접속해 주세요!')
        else:
            st.wirte("ID를 입력해주세요")

delete_data()
