package com.login.login.mapper;

import org.apache.ibatis.annotations.Mapper;
import java.util.List;

@Mapper
public interface TodoMapper {
    List<TodoEntity> findAll();

    TodoEntity findById(Integer id);

    void insertTodo(String subject, String body, Boolean completed);

    void updateTodoById(TodoEntity todoEntity);

    void deleteTodoById(Integer id);
}