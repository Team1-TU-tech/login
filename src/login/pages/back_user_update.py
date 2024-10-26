import streamlit as st
import requests as reqs

def load_user_info(user_id):
    """로그인된 사용자의 정보를 가져오는 함수"""
    url = f'http://127.0.0.1:8888/login/find?id={user_id}'  # 예: 특정 사용자 정보를 불러오는 엔드포인트
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

def update_user_info(user_id, updated_info):
    """사용자 정보를 업데이트하는 함수"""
    url = f'http://127.0.0.1:8888/login/find?id={user_id}'  # 예: 사용자 정보 업데이트 엔드포인트
    try:
        response = reqs.put(url, json=updated_info)
        if response.status_code == 200:
            st.success("회원 정보가 성공적으로 업데이트되었습니다.")
        else:
            st.error("정보 업데이트에 실패했습니다.")
    except reqs.ConnectionError:
        st.error("서버 연결에 문제가 있습니다.")

# 세션 상태에서 아이디 확인
if 'id' in st.session_state and st.session_state['logged_in']:
    # 로그인한 사용자 정보 불러오기
    user_id = st.session_state['id']
    user_info = load_user_info(user_id)
    
    if user_info:
        # 기존 정보로 폼 필드 채우기
        user_firstname = st.text_input("이름", value=user_info.get("firstname", ""))
        user_lastname = st.text_input("성", value=user_info.get("lastname", ""))
        user_email = st.text_input("이메일", value=user_info.get("email", ""))
        user_gender = st.selectbox("성별", ['','F', 'M'], index=0 if user_info.get("gender") == 'F' else 1)
        user_birthday = st.date_input("생년월일", value=user_info.get(str("birthday")))
        user_phonenumber = st.text_input("전화번호", value=user_info.get("phonenumber", ""))
        
        # 수정된 정보 제출하기
        if st.button("정보 수정 제출"):
            updated_info = {
                "firstname": user_firstname,
                "lastname": user_lastname,
                "email": user_email,
                "gender": user_gender,
                "birthday": user_birthday.strftime('%Y-%m-%d'),
                "phonenumber": user_phonenumber,
            }
            update_user_info(user_id, updated_info)
else:
    st.warning("로그인 후에 이용할 수 있습니다.")

