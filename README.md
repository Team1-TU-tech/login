# TU-tech FINAL PROJECT 
## OVERVIEW
RESTAPI를 java로 구현


Spring Rest 연동 CRUD 사용

## 기술스택
![image](https://github.com/user-attachments/assets/782f95fa-4c30-4c6c-b8ad-1ab62bf2fed4)
![image](https://github.com/user-attachments/assets/9999fdce-b3f0-4e60-9ef3-fddcd4335683)
![image](https://github.com/user-attachments/assets/25f13002-e07e-40e3-a98f-d15d45553b09)
![image](https://github.com/user-attachments/assets/f1c93bcd-fa7e-4115-b88e-5fa3a80ed1cb)

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
$ git clone 
$ docker compose up -d --force-recreate --build
```

### 접속
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
