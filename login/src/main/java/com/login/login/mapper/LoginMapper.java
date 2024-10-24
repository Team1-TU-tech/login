package com.login.login.mapper;

import org.apache.ibatis.annotations.Mapper;

import com.login.login.entity.LoginEntity;

import java.util.List;

@Mapper
public interface LoginMapper {
    List<LoginEntity> findAll();

    LoginEntity findByNum(Integer num);

    void createLogin(String firstname, String lastname, String id, String passwd, String email, String gender,
            String birthday, String phonenumber);

    void updateLoginById(LoginEntity loginEntity);

    void deleteLoginById(String id);
}