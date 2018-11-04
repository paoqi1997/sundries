/**
 * MySQL之联结
 */

-- 表plate_number与girls于UNIT-05.sql新建
USE mydb;

CREATE TABLE plate_number
(
id      INT         NOT NULL AUTO_INCREMENT,
city    VARCHAR(12) NOT NULL,
numbers CHAR(4)     NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE girls
(
id      INT         NOT NULL AUTO_INCREMENT,
name    VARCHAR(12) NOT NULL,
numbers CHAR(4)     NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO plate_number
(city, numbers)
VALUES
('guangzhou', 'A'), ('shenzhen', 'B');

INSERT INTO girls
(name, numbers)
VALUES
('timei', 'A'), ('lianru', 'B');

SELECT * FROM plate_number;
SELECT * FROM girls;

SELECT name, city FROM plate_number, girls
WHERE plate_number.numbers = girls.numbers ORDER BY name;

SELECT name, city FROM plate_number
INNER JOIN girls ON plate_number.numbers = girls.numbers ORDER BY name;

DROP TABLE plate_number, girls;
