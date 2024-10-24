package com.login.login.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
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

    @GetMapping("/login")
    public LoginEntity find(@RequestParam String id) {
        LoginEntity r = loginService.findById(id);
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
    @PutMapping("/login")
    public void updateLogin(@RequestParam String id, @RequestBody LoginEntity loginEntity) {
        loginEntity.setId(id);
        loginService.updateLoginById(id, loginEntity);
        System.out.println("UPDATE SUCCESSED");

    }

    // D - DELETE
    @DeleteMapping("/login")
    public void deleteLogin(@RequestParam String id) {
        loginService.deleteLoginById(id);
        System.out.println(id + "DELETE SUCCESSED");

    }
}
