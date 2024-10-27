import streamlit as st
import requests as reqs
from datetime import datetime

# 로그인된 사용자 정보를 가져오는 함수
def load_user_info(user_id):
    url = f'http://localhost:8888/login/find?id={user_id}'  
    try:
        response = reqs.get(url)
        if response.status_code == 200:
            return response.json()  # 사용자 정보 반환
        else:
            st.error("사용자 정보를 불러오는 데 실패했습니다.")
            return None
    except reqs.ConnectionError:
        st.error("서버 연결에 문제가 있습니다.")
        return None

# 사용자 정보를 업데이트 하는 함수
def update_user_info(user_id, updated_info):
    url = f'http://localhost:8888/login/{user_id}'
    headers = {'Content-Type': 'application/json'}
    try:
        response = reqs.patch(url, json=updated_info, headers=headers)
        if response.status_code == 200:
            st.success(f"{user_id}님의 회원 정보가 성공적으로 업데이트되었습니다.")
        else:
            st.error("정보 업데이트에 실패했습니다.")
    except reqs.ConnectionError:
        st.error("서버 연결에 문제가 있습니다.")

# 세션 상태에서 아이디 확인
if 'id' in st.session_state and st.session_state['logged_in']:
    st.title("회원 정보 변경")
    st.write("##### 변경을 원하시는 정보를 입력 후 제출하기 버튼을 눌러주세요")
    
    # 로그인한 사용자 정보 불러오기
    user_id = st.session_state['id']
    user_info = load_user_info(user_id)
    
    if user_info:
        # 기존 정보로 폼 필드 채우기
        user_firstname = st.text_input("이름", value=user_info.get("firstname", ""))
        user_lastname = st.text_input("성", value=user_info.get("lastname", ""))
        user_email = st.text_input("이메일", value=user_info.get("email", ""))
        user_gender = st.selectbox("성별", ['F', 'M'], index=0 if user_info.get("gender") == 'F' else 1)

        birthday_str = user_info.get("birthday")
        birthday_value=datetime.strptime(birthday_str,"%Y-%m-%d")
        user_birthday = st.date_input("생년월일",value=birthday_value)
        user_phonenumber = st.text_input("전화번호", value=user_info.get("phonenumber", ""))
        
        # 수정하기 및 뒤로가기 버튼 배치할 열 
        splitView = [i for i in st.columns([5.7,2.5,2,1.8])]
        
        # 수정하기 버튼
        with splitView[0]:
            # 수정된 정보 제출하기
            if st.button("제출하기"):
                updated_info = {
                    "firstname": user_firstname,
                    "lastname": user_lastname,
                    "email": user_email,
                    "gender": user_gender,
                    "birthday": user_birthday.strftime("%Y-%m-%d"),
                    "phonenumber": user_phonenumber,
                }
                update_user_info(user_id, updated_info)

        # 비밀번호 변경하기
        with splitView[1]:
            if st.button("비밀번호 변경"):
                st.session_state['page'] =None
                st.session_state['id_check']=None
                st.switch_page("pages/change_pw.py")


        with splitView[2]:
            if st.button("회원 탈퇴"):
                st.session_state['page'] =None
                st.session_state['id_check']=None
                st.switch_page("pages/user_deletion.py")

        # 뒤로가기
        with splitView[3]:
            if st.button("뒤로가기", key="back_button_in_patch"):
                st.session_state['page'] = None
                st.session_state['id_check'] = None
                st.switch_page("login.py")
        
