CREATE TABLE LOGIN_TB(
    NUM INT NOT NULL AUTO_INCREMENT,
    FIRSTNAME VARCHAR(50),
    LASTNAME VARCHAR(50),
    ID VARCHAR(50),
    PASSWD VARCHAR(50),
    EMAIL VARCHAR(50),
    GENDER VARCHAR(50),
    BIRTHDAY TIMESTAMP,
    PHONENUMBER VARCHAR(50),
    PRIMARY KEY(NUM)
);