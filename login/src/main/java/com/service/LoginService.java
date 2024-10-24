package com.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import shop.samdule.demo.entity.TodoEntity;
import shop.samdule.demo.mapper.TodoMapper;
import java.util.List;

@Service
public class LoginService {

    @Autowired
    TodoMapper todoMapper;

    public List<TodoEntity> getTodos() {
        System.out.println("[service] findAll");
        List<TodoEntity> todos = todoMapper.findAll();
        System.out.println("[todos]:" + todos.size());
        return todos;
    }

    public TodoEntity findById(Integer id) {
        return todoMapper.findById(id);
    }

    public void createTodo(TodoEntity todoEntity) {
        todoMapper.insertTodo(todoEntity.getSubject(), todoEntity.getBody(), todoEntity.getCompleted());
    }

    public void updateTodoById(Integer id, TodoEntity todoEntity) {
        todoEntity.setId(id);
        todoMapper.updateTodoById(todoEntity);
    }

    public void deleteTodoById(Integer id) {
        todoMapper.deleteTodoById(id);
    }

}