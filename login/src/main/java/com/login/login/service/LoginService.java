package com.login.login.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.login.login.entity.LoginEntity;
import com.login.login.mapper.LoginMapper;

import java.util.List;

@Service
public class LoginService {

    @Autowired
    LoginMapper loginMapper;

    public List<LoginEntity> getLogin() {
        System.out.println("[service] findAll");
        List<LoginEntity> login = loginMapper.findAll();
        System.out.println("[login]:" + login.size());
        return login;
    }

    public LoginEntity findByNum(Integer num) {
        return loginMapper.findByNum(num);
    }

    public void createLogin(LoginEntity loginEntity) {
        loginMapper.createLogin(loginEntity.getFirstname(), loginEntity.getLastname(), loginEntity.getId(),
                loginEntity.getPasswd(), loginEntity.getEmail(), loginEntity.getGender(), loginEntity.getBirthday(),
                loginEntity.getPhonenumber());
    }

    public void updateLoginByNum(Integer num, LoginEntity loginEntity) {
        loginEntity.setNum(num);
        loginMapper.updateLoginByNum(loginEntity);
    }

    public void deleteLoginByNum(Integer num) {
        loginMapper.deleteLoginByNum(num);
    }

}