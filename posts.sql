CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

INSERT INTO posts (title,content) VALUES ('Hello, world', 'This is my first blog post!');

SELECT * FROM posts;