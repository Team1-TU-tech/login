package com.login.login.entity;

import lombok.Setter;
import lombok.Getter;
import lombok.ToString;

@Setter
@Getter
@ToString
public class LoginEntity {
    private Integer num;
    private String firstname;
    private String lastname;
    private String id;
    private String passwd;
    private String email;
    private String gender;
    private String birthday;
    private String phonenumber;
}