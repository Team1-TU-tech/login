import streamlit as st
import requests

def kakao_callback(auth_code):
    token_url = "https://kauth.kakao.com/oauth/token"
    client_id = "94f58b0bb01d419714f800fd52e3483c"
    redirect_uri = "http://localhost:8040"
    
    # 토큰 요청
    token_data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'code': auth_code
    }
    
    token_response = requests.post(token_url, data=token_data)
    token_json = token_response.json()
    
    access_token = token_json.get("access_token")
    
    if access_token:
        # 사용자 정보 요청
        user_info_url = "https://kapi.kakao.com/v2/user/me"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        user_info_response = requests.get(user_info_url, headers=headers)
        user_info = user_info_response.json()
        
        # 사용자 정보 표시
        st.write("로그인 성공!")
        st.write(user_info)
    else:
        st.write("로그인 실패")
    
    token_response = requests.post(token_url, data=token_data)
    st.write(f"토큰 요청 응답: {token_response.text}")

# 카카오에서 리디렉션된 후, 제공된 인증 코드를 가져옴
auth_code = st.query_params.get("code")
#auth_code = st.experimental_get_query_params().get("code")


if auth_code:
    kakao_callback(auth_code[0])
else:
    st.write("인증 코드가 없습니다.")

