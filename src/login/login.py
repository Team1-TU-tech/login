import streamlit as st

def kakao_login():
    kakao_auth_url = "https://kauth.kakao.com/oauth/authorize"
    client_id = "YOUR_CLIENT_ID"
    client_id = "94f58b0bb01d419714f800fd52e3483c"
    redirect_uri = "http://localhost:8040"
    response_type = "code"

    # 인증 URL 생성
    auth_url = f"{kakao_auth_url}?client_id={client_id}&redirect_uri={redirect_uri}&response_type={response_type}"
    
    # 링크 버튼을 사용하여 Kakao 로그인 페이지로 리디렉션
    st.link_button("카카오 로그인", url=auth_url)

st.title("Kakao Login Example")
kakao_login()

