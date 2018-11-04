/**
 * MySQL之高级连接
 */

-- 表plate_number与girls于UNIT-05.sql新建
USE mydb;

SELECT name, city
FROM plate_number AS p, girls AS g
WHERE p.numbers = g.numbers ORDER BY name;

SELECT name, numbers
FROM girls WHERE id = (SELECT id FROM girls WHERE numbers = 'B');

SELECT g1.name, g1.numbers
FROM girls AS g1, girls AS g2 WHERE g1.id = g2.id AND g1.numbers = 'B';

SELECT g.* FROM girls AS g, girls AS gg WHERE g.id = gg.id AND g.numbers = 'B';

-- 左外连接 <-> 包括左表的所有行及右表符合匹配条件的行
SELECT name, city FROM plate_number
LEFT OUTER JOIN girls ON plate_number.numbers = girls.numbers ORDER BY name;

-- 右外连接 <-> 包括右表的所有行及左表符合匹配条件的行
SELECT name, city FROM plate_number
RIGHT OUTER JOIN girls ON plate_number.numbers = girls.numbers ORDER BY name;
