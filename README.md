# TU-tech FINAL PROJECT 
# Login 기능 구현
## OVERVIEW
RESTAPI를 java로 구현


Spring Rest 연동 CRUD 사용


메인 로그인 페이지 Streamlit으로 구현


로그인 페이지 카카오톡과 연동




## 기술스택
<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=Python&logoColor=F5F7F8"/>
![image](https://github.com/user-attachments/assets/8d765cb3-f3c2-4e5f-92fd-457a5472387c)
![image](https://github.com/user-attachments/assets/9999fdce-b3f0-4e60-9ef3-fddcd4335683)
![image](https://github.com/user-attachments/assets/25f13002-e07e-40e3-a98f-d15d45553b09)
![image](https://github.com/user-attachments/assets/f1c93bcd-fa7e-4115-b88e-5fa3a80ed1cb)
![image](https://github.com/user-attachments/assets/87428359-20f5-439d-ad6b-7a08e25e40b0)




## 주요 기능 
- 전체 회원 정보 조회`GET`
- 특정 회원 정보 조회`GET`
- 회원가입`POST`
- 회원 정보 변경`PATCH`
- 회원 탈퇴`DELETE`

## DB 구조
```java
CREATE TABLE LOGIN_TB(
    NUM INT NOT NULL AUTO_INCREMENT,
    FIRSTNAME VARCHAR(50),
    LASTNAME VARCHAR(50),
    ID VARCHAR(50),
    PASSWD VARCHAR(50),
    EMAIL VARCHAR(50),
    GENDER VARCHAR(50),
    BIRTHDAY VARCHAR(50),
    PHONENUMBER VARCHAR(50),
    PRIMARY KEY(NUM)
);
```
## 사용방법

### DOKER 설치
```bash
$ git clone git@github.com:Team1-TU-tech/login.git
$ docker compose up -d --force-recreate --build
```

### API 접속
http:localhost:8888/login

### 사용 명령어 예시 - url
- 전체 회원 조회 http://localhost:8888/login
- 특정 회원 조회 http://localhost:8888/login/find?id=tut

### 사용 명령어 예시 - 프롬프트
```bash
# 전체 회원 조회
$ curl -X GET http://localhost:8888/login
# 회원가입
$ curl -X POST -H "Content-Type:application/json" -d '{"firstname":"mieun", "lastname":"jeong", "id":"hh", "passwd":"122345", "email":"hahahah@gmail.com",  "gender":"F", "birthday":"2024.10.11", "phonenumber":"01012341234"}' http://localhost:8888/login
# 회원정보 수정
$ curl -X PATCH -H "Content-Type:application/json" -d '{"firstname":"sunwoo", "lastname":"ham"}' http://localhost:8888/login/hh
# 회원 탈퇴
$ curl -X DELETE "http://localhost:8888/login/hh"
```

# 로그인 페이지 구현  
## Streamlit 접속
```bash
$ export KAKAO_TOKEN={TOKEN_ID}
$ streamlit run src/login/login.py --server.port 8501
```

## 시연영상
### 회원가입
https://github.com/user-attachments/assets/234f6914-1d24-4d23-88d5-552d2f98cc65

### 로그인, 로그아웃
https://github.com/user-attachments/assets/49148f7d-8856-49c2-baf5-4f8a488defc8

### 카카오 로그인
https://github.com/user-attachments/assets/1cb11a56-3f46-4fd6-a9e6-04cbb11d6708

### 회원정보 수정
https://github.com/user-attachments/assets/821fd40b-1ca9-4936-9fb4-7ceb93ad3be4

### 탈퇴
https://github.com/user-attachments/assets/2178658e-91bc-4764-b05d-3af81de834e1

# 회고

## 좋은점
- 역할 분배가 빠르게 됨  
- 원활한 커뮤니케이션  
- 페어 프로그래밍으로 진행
- 부족한 시간에도 필수 기능 개발 완성
  
## 아쉬운점
- 역할분배가 아쉬웠음 (카카오/기본 로그인) 
- Streamlit 기능 구현이 부족 
- JAVA에 익숙치 않아 오류해결에 많은 시간을 소비
- branch 전략을 미리 구상하지 않아 기능 식별이 어려움

## 개선할 점
- 기능 완성도 개선
- Streamlit 기능 개선
- 이슈 업데이트 활성화
- branch 전략을 구상 후 프로젝트 진행

## Contributors
김태민, 정미은, 함선우, 오지현
