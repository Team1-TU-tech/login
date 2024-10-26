import streamlit as st
import requests
import time


st.title("회원탈퇴")
st.write("#### 회원 탈퇴를 위해 ID를 입력해주세요")
user_id = st.text_input("ID","")

url =f'http://localhost:8888/login/{user_id}'

def delete_data():
    splitView = [i for i in st.columns([12, 1])]  # 확인 버튼과 back 버튼을 나란히 배치할 열 생성

    with splitView[0]:  # 확인 버튼
        if st.button("확인"):
            params = {'id': f'{user_id}'}
            try:
                r = requests.delete(url=url, json=params)
                if r.status_code == 200:
                    st.write(f"{user_id}님의 탈퇴가 완료되었습니다. 다음에 만나요!😥")
                    time.sleep(1)
                    for k, v in st.session_state.items():
                        st.session_state[k] = None
                    st.switch_page("login.py")
                else:
                    st.write(f"{user_id}님의 정보가 없습니다. ID를 다시 확인한 후 입력해주세요!")
            except Exception as e:
                st.write('페이지가 응답하지 않습니다. 다시 접속해 주세요!')

    with splitView[1]:  # back 버튼
        if st.button("🔙"):
            st.switch_page("pages/user_update.py")

delete_data()
