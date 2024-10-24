package com.login.login.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.login.login.entity.LoginEntity;
import com.login.login.service.LoginService;

import java.util.List;

@RestController
public class ApiController {

    @Autowired
    LoginService loginService;

    @GetMapping("/login")
    public List<LoginEntity> list() {
        System.out.println("[Controller]");
        List<LoginEntity> r = loginService.getLogin();
        return r;
    }

    @GetMapping("/login/{num}")
    public LoginEntity find(@PathVariable Integer num) {
        LoginEntity r = loginService.findByNum(num);
        return r;
    }

    // C - INSERT
    @PostMapping("/login")
    public void createLogin(@RequestBody LoginEntity loginEntity) {
        System.out.println("[Controller]" + loginEntity.toString());
        loginService.createLogin(loginEntity);
        System.out.println("INSERT SUCCESSED");

    }

    // U - UPDATE
    @PutMapping("/login/{num}")
    public void updateLogin(@PathVariable Integer num, @RequestBody LoginEntity loginEntity) {
        loginEntity.setNum(num);
        loginService.updateLoginByNum(num, loginEntity);
        System.out.println("UPDATE SUCCESSED");

    }

    // D - DELETE
    @DeleteMapping("/login/{num}")
    public void deleteLogin(@PathVariable Integer num) {
        loginService.deleteLoginByNum(num);
        System.out.println(num + "DELETE SUCCESSED");

    }
}
