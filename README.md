# Login 기능 구현 (TU-tech JAVA PROJECT)

## 개요
로그인 기능을 위한 REST API를 Java로 구현하고, Spring REST를 연동하여 CRUD 작업을 처리했습니다. 메인 로그인 페이지는 Streamlit으로 제작되었으며, 카카오 로그인 연동을 지원합니다.  
<br></br>

## 목차
- [기술스택](#기술스택)
- [개발기간](#개발기간)
- [주요 기능](#주요-기능)
- [기능 흐름도](#기능-흐름도)
- [데이터베이스 구조](#데이터베이스-구조)
- [사용방법](#사용방법)
- [Streamlit 접속](#Streamlit-접속)
- [시연영상](#시연영상)
- [회고](#회고)
- [Contributors](#Contributors)
- [License](#License)
- [문의](#문의)
<br></br>

## 기술스택
![Java 17](https://img.shields.io/badge/Java-17-007396?logo=java&logoColor=white)
<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=Python&logoColor=F5F7F8"/>   <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=Docker&logoColor=F5F7F8"/> 
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamit&logoColor=F5F7F8"/>   <img src="https://img.shields.io/badge/Spring Boot-6DB33F?style=flat&logo=Spring Boot&logoColor=F5F7F8"/>   <img src="https://img.shields.io/badge/MariaDB-003545?style=flat&logo=MariaDB&logoColor=F5F7F8"/>
<br></br>

## 개발기간
`2024.10.24 ~ 2024.10.25 (총 2일)`
<br></br>

## 주요 기능 
- 로그인
- 카카오톡 연동 로그인
- 아이디 찾기
- 비밀번호 찾기 (임시 비밀번호 발급)
- 회원가입
- 회원 정보 변경
- 비밀번호 변경
- 회원 탈퇴

<br></br>


## 기능 흐름도
![스크린샷 2024-10-26 03 16 15](https://github.com/user-attachments/assets/bf09d28b-b1e6-44be-bd8e-26a145cefca2)
<br></br>


## 데이터베이스 구조
```sql
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
<br></br>

## 사용방법

### DB, API DOKER 설치
```bash
$ git clone git@github.com:Team1-TU-tech/login.git
$ docker compose up -d --force-recreate --build
```

### API 접속
- 엔드포인트: http://localhost:8888/login
<br></br>

### 사용 명령어 예시 - url
- 전체 회원 조회 http://localhost:8888/login
- 특정 회원 조회 http://localhost:8888/login/find?id=<user_id>
- 특정 회원 이메일조회 http://localhost:8888/login/find?passwd=<user_password>
- 특정 회원 전화번호조회 http://localhost:8888/login/find?email=<user_email>
  
<br></br>

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
<br></br>

## 로그인 페이지 구현  
## Streamlit 접속
```bash
$ export KAKAO_TOKEN={TOKEN_ID}
$ export SEND_EMAIL={google email} 
$ export APP_PW="{google app password}"
$ streamlit run src/login/login.py --server.port 8501
```
<br></br>


## 시연영상
### 회원가입
https://github.com/user-attachments/assets/6b42cf60-7caf-4680-a5cc-1795d0253227

### 로그인, 로그아웃
https://github.com/user-attachments/assets/1f4404b4-4e58-49c1-bdda-a6f80e7b22dc

### 카카오 로그인
https://github.com/user-attachments/assets/99804ecd-3c94-487b-9688-8fe9ec30bfc5

### 아이디 찾기
https://github.com/user-attachments/assets/49af9653-c7c7-440b-a831-f926e61dee44

### 비밀번호 찾기
https://github.com/user-attachments/assets/c2181261-6af7-4728-b3d7-c728402f53fb

### 회원정보 수정
https://github.com/user-attachments/assets/5400e109-d1fa-47d5-826f-def736425cbd

### 회원  탈퇴
https://github.com/user-attachments/assets/5b922018-4cc9-42d5-b45a-6d04f9d39bbb

### 비밀번호 변경
https://github.com/user-attachments/assets/d38214d4-a3fd-40e0-a9dc-31c3a08840e3


<br></br>


# 회고

## 좋은점
- 신속한 역할 분배: 팀원 간 빠른 역할 분배를 통해 프로젝트를 효율적으로 진행할 수 있었다.
- 원활한 소통: 팀원 간의 적극적인 소통 덕분에 업무 진행이 매끄러웠다.
- 페어 프로그래밍: 페어 프로그래밍을 통해 코드 문제 해결 속도가 향상되었다.
- 핵심 기능 구현 완료: 시간의 제약이 있었지만 필수 기능을 모두 구현해 프로젝트의 기본 목표를 달성할 수 있었다.
  
## 아쉬운점
- 역할 분배의 미흡: 카카오 로그인과 기본 로그인 구현 역할 배분이 다소 아쉬웠다.
- Streamlit 기능 구현 부족: Streamlit의 다양한 기능을 활용하지 못해 로그인 페이지의 완성도가 낮았다.
- JAVA 오류 해결 시간 소요: JAVA에 익숙하지 않아 예상보다 많은 시간을 오류 해결에 소비하게 되었다.
- Branch 전략 미흡: 사전에 branch 전략을 구체적으로 계획하지 않아 코드 기능 구분이 어려웠다.

## 개선할 점
- 기능 완성도 향상: 로그인 기능의 안정성과 완성도를 더욱 높일 필요가 있다.
- Streamlit 기능 확장: Streamlit의 다양한 기능을 더 적극적으로 활용하여 사용자 경험을 개선할 필요가 있다.
- [이슈 트래킹 활성화](https://github.com/Team1-TU-tech/login/issues): 작업 과정을 체계적으로 관리할 수 있도록 이슈 업데이트 활성화가 필요하다.
- 체계적인 Branch 전략 수립: 프로젝트 시작 전 branch 전략을 세우고 체계적으로 운영하여 협업 효율을 높여야 한다.
- 로그인 기능 구현 시 성능 개선을 위해 redis를 사용해보고 싶다.
<br></br>


## Contributors
- 카카오 로그인 연동: `김태민`, `오지현`
- API 개발: `정미은`, `함선우`
- 로그인 화면 구현: `김태민`, `함선우`, `오지현`
- 회원탈퇴, 회원 정보 변경 및 비밀번호 변경 화면 구현: `정미은`
- 회원가입 화면 구현: `함선우`
- 비밀번호 찾기 구현: `오지현`
- 데이터베이스 설계 및 구축: `정미은`, `함선우`
- 세션 버그 수정: `김태민`, `오지현`
<br></br>


## License
이 애플리케이션은 TU-tech 라이선스에 따라 라이선스가 부과됩니다.
<br></br>


## 문의 
질문이나 제안사항이 있으면 언제든지 연락주세요:
- 이메일: TU-tech@tu-tech.com
- Github: Mingk42, hahahellooo, hamsunwoo, oddsummer56
