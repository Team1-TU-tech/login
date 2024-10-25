package com.login.login.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.login.login.entity.LoginEntity;
import com.login.login.service.LoginService;

import java.util.List;

@RestController
@RequestMapping("/login")
public class ApiController {

    @Autowired
    LoginService loginService;

    // 모든 로그인 정보 조회
    @GetMapping
    public List<LoginEntity> list() {
        System.out.println("[Controller] get all logins");
        return loginService.getLogin();
    }

    // 특정 ID의 로그인 정보 조회 (RequestParam 사용)
    @GetMapping("/find")
    public LoginEntity find(@RequestParam(required = false) String id,
            @RequestParam(required = false) String phonenumber,
            @RequestParam(required = false) String passwd,
            @RequestParam(required = false) String email) {
        if (id != null && phonenumber == null && passwd == null && email == null) {
            return loginService.findById(id);
        }
        return loginService.findByOptionalParams(id, phonenumber, passwd, email);
    }

    // C - INSERT
    @PostMapping
    public void createLogin(@RequestBody LoginEntity loginEntity) {
        System.out.println("[Controller] Create login: " + loginEntity);
        loginService.createLogin(loginEntity);
        System.out.println("INSERT SUCCESSFUL");
    }

    // U - UPDATE
    @PatchMapping("/{id}")
    public void updateLogin(@PathVariable String id, @RequestBody LoginEntity loginEntity) {
        System.out.println("[Controller] Update login with id: " + id);
        loginEntity.setId(id);
        loginService.updateLoginById(id, loginEntity);
        System.out.println("UPDATE SUCCESSFUL");
    }

    // D - DELETE
    @DeleteMapping("/{id}")
    public void deleteLogin(@PathVariable String id) {
        System.out.println("[Controller] Delete login with id: " + id);
        loginService.deleteLoginById(id);
        System.out.println("DELETE SUCCESSFUL");
    }
}
