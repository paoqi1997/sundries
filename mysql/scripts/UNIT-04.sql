/**
 * MySQL之子查询
 */

-- 表universities与students于UNIT-04.sql新建
USE mydb;

CREATE TABLE universities
(
id     INT         NOT NULL AUTO_INCREMENT,
school VARCHAR(8)  NOT NULL,
city   VARCHAR(12) NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE students
(
id     INT         NOT NULL AUTO_INCREMENT,
name   VARCHAR(12) NOT NULL,
school VARCHAR(8)  NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO universities
(school, city)
VALUES
('scnu', 'guangzhou'), ('zju', 'hangzhou');

INSERT INTO students
(name, school)
VALUES
('paoqi', 'scnu'), ('unknown', 'zju');

SELECT * FROM universities;
SELECT * FROM students;

-- 跨表查询
SELECT name FROM students
WHERE school IN (SELECT school FROM universities WHERE city = 'guangzhou');

DROP TABLE universities, students;
