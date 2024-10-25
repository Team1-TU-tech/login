import streamlit as st
import requests as reqs

import os

if 'klogin_token' not in st.session_state:
    st.session_state['klogin_token'] = None


def logout():
    params = {
        'client_id': os.getenv("KAKAO_TOKEN",""),
        'logout_redirect_uri': "http://localhost:8501/",
    }
    logout_url = f"https://kauth.kakao.com/oauth/logout?client_id={params['client_id']}&logout_redirect_uri={params['logout_redirect_uri']}"

    return logout_url

def kakao_callback(auth_code):
    token_url = "https://kauth.kakao.com/oauth/token"
    client_id = os.getenv("KAKAO_TOKEN","")
    redirect_uri = "http://localhost:8501/callback"
    
    # 토큰 요청
    token_data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'code': auth_code
    }


    token_response = reqs.post(token_url, data=token_data)
    token_json = token_response.json()
    
    access_token = token_json.get("access_token")
    
    if access_token:
        # 사용자 정보 요청
        user_info_url = "https://kapi.kakao.com/v2/user/me"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        user_info_response = reqs.get(user_info_url, headers=headers)
        user_info = user_info_response.json()

        st.session_state['klogin_token'] = access_token
        st.write(access_token)

        # 사용자 정보 표시
        st.write("로그인 성공!")
        st.session_state['id']=user_info["kakao_account"]["profile"]["nickname"]
        st.session_state['logged_in']=True
        st.switch_page("login.py")
        st.switch_page("login.py")
        # st.write(user_info)
        # st.title("Kakao Logout Example")
        # #st.button("logout", on_click=logout)
        # st.write(user_info["kakao_account"]["profile"]["nickname"])
        # st.link_button("logout", url=logout())

    else:
        st.write("로그인 실패")
        #st.switch_page("login.py")



    st.write(token_url)
    st.write(token_data)

# 카카오에서 리디렉션된 후, 제공된 인증 코드를 가져옴
#auth_code = st.query_params["code"]#.get("code")
auth_code = st.query_params.get_all("code")

#auth_code = st.experimental_get_query_params().get("code")


if auth_code:
    kakao_callback(auth_code)
else:
    st.write("인증 코드가 없습니다.")









