DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS habits;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS item_tags;
DROP TABLE IF EXISTS user_sessions;
DROP TABLE IF EXISTS habit_logs;


CREATE TABLE users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  email TEXT
);

CREATE TABLE tasks (
  task_id INTEGER PRIMARY KEY AUTOINCREMENT,
  owner_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  due_date DATETIME,
  task_name TEXT NOT NULL,
  task_description TEXT,
  task_priority INTEGER,
  task_complete BOOLEAN NOT NULL DEFAULT 0,
  FOREIGN KEY (owner_id) REFERENCES users (user_id)
);

CREATE TABLE habits (
  habit_id INTEGER PRIMARY KEY AUTOINCREMENT,
  owner_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  habit_name TEXT UNIQUE NOT NULL,
  habit_description TEXT,
  habit_history JSON
);

CREATE TABLE habit_logs (
  log_id INTEGER PRIMARY KEY AUTOINCREMENT,
  habit_id INTEGER NOT NULL,
  log_date DATE NOT NULL,
  completed BOOLEAN NOT NULL,
  FOREIGN KEY (habit_id) REFERENCES habits (habit_id)
);

CREATE TABLE tags (
  tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
  tag_name TEXT UNIQUE NOT NULL,
  tag_color TEXT
);

CREATE TABLE item_tags (
  task_id INTEGER NOT NULL,
  tag_id INTEGER NOT NULL,
  FOREIGN KEY (task_id) REFERENCES tasks (task_id),
  FOREIGN KEY (tag_id) REFERENCES tags (tag_id)
);

CREATE TABLE user_sessions (
  session_id INTEGER PRIMARY KEY AUTOINCREMENT,
  start_time DATETIME NOT NULL,
  end_time DATETIME,
  user_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES users (user_id)
);