package com.login.login.entity;

import lombok.Setter;
import lombok.Getter;
import lombok.ToString;

@Setter
@Getter
@ToString
public class LoginEntity {
    private Integer id;
    private String subject;
    private String body;
    private Boolean completed;
}