/**
 * MySQL之计算字段
 */

USE mydb;

-- 相当于NOW()
SELECT CURRENT_TIMESTAMP;

--  Trim ( @column ) 去除串两边的空格
-- LTrim ( @column ) 去除串左边的空格
-- RTrim ( @column ) 去除串右边的空格
SELECT num, Concat(name, '(', python, ')') AS pythoner FROM coders ORDER BY name;

-- C++/Java/Python都会的崽种出来挨打！
SELECT num, name, cplusplus & java & python AS lgindex FROM coders ORDER BY name;
