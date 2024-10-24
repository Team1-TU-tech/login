package com.login.login.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class ApiController {

    @Autowired
    TodoService todoService;

    @GetMapping("/todos")
    public List<LoginEntity> list() {
        System.out.println("[Controller]");
        List<LoginEntity> r = todoService.getTodos();
        return r;
    }

    @GetMapping("/todos/{id}")
    public LoginEntity find(@PathVariable Integer id) {
        LoginEntity r = todoService.findById(id);
        return r;
    }

    // C - INSERT
    @PostMapping("/todos")
    public void createTodo(@RequestBody LoginEntity todoEntity) {
        System.out.println("[Controller]" + todoEntity.toString());
        todoService.createTodo(todoEntity);
        System.out.println("INSERT SUCCESSED");

    }

    // U - UPDATE
    @PutMapping("/todos/{id}")
    public void updateTodo(@PathVariable Integer id, @RequestBody LoginEntity todoEntity) {
        todoEntity.setId(id);
        todoService.updateTodoById(id, todoEntity);
        System.out.println("UPDATE SUCCESSED");

    }

    // D - DELETE
    @DeleteMapping("/todos/{id}")
    public void deleteTodo(@PathVariable Integer id) {
        todoService.deleteTodoById(id);
        System.out.println(id + "DELETE SUCCESSED");

    }
}
