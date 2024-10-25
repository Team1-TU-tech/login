import streamlit as st
import requests

def patch_data(user_id):
    # 동적 파라미터를 위한 입력 필드
    user_firstname = st.text_input("Firstname")
    user_lastname = st.text_input("Lastname")
    user_passwd = st.text_input("Password")
    user_email = st.text_input("Email")
    user_gender = st.text_input("Gender")
    user_birthday = st.text_input("Birthday")
    user_phonenumber = st.text_input("Phonenumber")

    # API URL (user_id를 포함)
    url = f'http://localhost:8888/login/{user_id}'  # 본인의 URL로 수정
    headers = {'Content-Type': 'application/json'}

    # 빈 값을 제외하고 동적으로 params 딕셔너리 구성
    params = {}
    if user_firstname:
        params["firstname"] = user_firstname
    if user_lastname:
        params["lastname"] = user_lastname
    if user_passwd:
        params["passwd"] = user_passwd
    if user_email:
        params["email"] = user_email
    if user_gender:
        params["gender"] = user_gender
    if user_birthday:
        params["birthday"] = user_birthday
    if user_phonenumber:
        params["phonenumber"] = user_phonenumber

    # PATCH 요청 실행
    if st.button("Submit") and user_id:  # 버튼 클릭 후 유효한 user_id가 있는 경우
        try:
            # PATCH 요청
            r = requests.patch(url=url, headers=headers, json=params)
            # 응답 상태 코드 확인
            if r.status_code == 200:
                st.write(f"{user_id}님의 정보가 수정되었습니다!")
            else:
                st.write(f"서버 오류 발생: {r.status_code}. 다시 시도해주세요.")
        except Exception as e:
            st.write(f"오류 발생: {e}")
    else:
        st.write("정보를 입력 후 Submit 버튼을 눌러주세요.")

# 수정할 사용자 ID를 입력 받는 함수
def show_update():
    user_id = st.text_input("수정할 사용자 ID를 입력하세요")
    if user_id and st.button("Load User"):
        patch_data(user_id)

# 메인 함수 호출
show_update()

