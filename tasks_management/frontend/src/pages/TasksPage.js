import React from 'react';
import TaskList from '../components/TaskList';
import TaskForm from '../components/TaskForm';

const TasksPage = () => {
  return (
    <div>
      <h1>Tasks Page</h1>
      <TaskList />
      <TaskForm />
    </div>
  );
};

export default TasksPage;
