import requests
import streamlit as st  
import bcrypt

st.title("회원 정보 수정")
st.write("#### 정보를 입력해주세요")

# 회원정보 수정
def update_data():
    user_firstname = st.text_input("이름")
    user_lastname = st.text_input("성")
    user_email = st.text_input("이메일")
    g = ['F', 'M']
    user_gender = st.selectbox("성별", g,index=None)
    user_birthday = st.date_input("생년월일",value=None)
    user_phonenumber = st.text_input("전화번호")

    
    url = f'http://localhost:8888/login'  # 본인의 URL로 수정
    headers = {'Content-Type': 'application/json'}
    params = {
        "firstname": user_firstname, 
        "lastname": user_lastname,
        "email": user_email,
        "gender": user_gender,
        "birthday": user_birthday,
        "phonenumber": user_phonenumber
    }

    # 수정하기 및 back 버튼을 배치할 열 구성
    splitView = [i for i in st.columns([12, 2])]

    # 수정하기 버튼
    with splitView[0]:
        if st.button("수정하기", key="update_button"):
            try:
                r = requests.patch(url=url, headers=headers, json=params)
                if r.status_code == 200:
                    st.write(f"{user_id}님의 정보가 수정되었습니다!")
                else:
                    st.write("서버가 불안정합니다. 다시 시도해주세요.")
            except Exception as e:
                st.write(f"정보를 업데이트 중 오류가 발생하였습니다. 다시 시도해주세요.")

    # back 버튼
    with splitView[1]:
        if st.button("뒤로가기", key="back_button_in_patch"):
            st.session_state['page'] = None
            st.session_state['id_check'] = None
            st.switch_page("login.py")

update_data()
