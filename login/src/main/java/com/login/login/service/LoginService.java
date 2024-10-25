package com.login.login.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.login.login.entity.LoginEntity;
import com.login.login.mapper.LoginMapper;

import java.util.List;
import java.util.HashMap;
import java.util.Map;

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

    public LoginEntity findById(String id) {
        return loginMapper.findById(id);
    }

    public LoginEntity findByOptionalParams(String id, String phonenumber, String passwd, String email) {
        Map<String, Object> params = new HashMap<>();
        if (id != null)
            params.put("id", id);
        if (phonenumber != null)
            params.put("phonenumber", phonenumber);
        if (passwd != null)
            params.put("passwd", passwd);
        if (email != null)
            params.put("email", email);

        return loginMapper.findByOptionalParams(params);
    }

    public void createLogin(LoginEntity loginEntity) {
        loginMapper.createLogin(loginEntity.getFirstname(), loginEntity.getLastname(), loginEntity.getId(),
                loginEntity.getPasswd(), loginEntity.getEmail(), loginEntity.getGender(), loginEntity.getBirthday(),
                loginEntity.getPhonenumber());
    }

    public void updateLoginById(String id, LoginEntity loginEntity) {
        loginEntity.setId(id);
        loginMapper.updateLoginById(loginEntity);
    }

    public void deleteLoginById(String id) {
        loginMapper.deleteLoginById(id);
    }

}