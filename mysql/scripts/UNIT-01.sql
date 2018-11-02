/**
 * MySQL之计算字段
 */

USE mydb;

-- 相当于NOW()
SELECT CURRENT_TIMESTAMP;

--  TRIM ( @column ) 去除串两边的空格
-- LTRIM ( @column ) 去除串左边的空格
-- RTRIM ( @column ) 去除串右边的空格
SELECT num, CONCAT(name, '(', python, ')') AS pythoner FROM coders ORDER BY name;

-- C++/Java/Python都会的崽种出来挨打！
SELECT num, name, cplusplus & java & python AS lgindex FROM coders ORDER BY name;
