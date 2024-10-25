package com.login.login.mapper;

import org.apache.ibatis.annotations.Mapper;

import com.login.login.entity.LoginEntity;

import java.util.List;
import java.util.Map;

@Mapper
public interface LoginMapper {
    List<LoginEntity> findAll();

    LoginEntity findById(String id);

    void createLogin(String firstname, String lastname, String id, String passwd, String email, String gender,
            String birthday, String phonenumber);

    void updateLoginById(LoginEntity loginEntity);

    void deleteLoginById(String id);

    LoginEntity findByOptionalParams(Map<String, Object> params); // 새로 추가한 메서드

}