# 简述

面向MySQL的基本教程。

# 说明

以下语句均在MySQL 5.7.21 on Windows下调试通过。

# 语句

那么，就让我们开始吧！祝你好运！

## 1. 开胃小菜

查看MySQL的版本：

```sql
mysql> SELECT VERSION();
```

查看当前日期：

```sql
mysql> SELECT CURRENT_DATE;
```

查看当前时间：

```sql
mysql> SELECT NOW();
```

查看当前用户：

```sql
mysql> SELECT USER();
```

查看MySQL服务器的状态信息：

```sql
mysql> SHOW STATUS;
```

## 2. 操作数据库

获得可用数据库的一个列表：

```sql
mysql> SHOW DATABASES;
```

查看MySQL所支持的数据库引擎：

```sql
mysql> SHOW ENGINES;
```

创建一个名为mydb的数据库：

```sql
mysql> CREATE DATABASE mydb;
```

显示创建数据库mydb时输入的语句：

```sql
mysql> SHOW CREATE DATABASE mydb;
```

删除数据库mydb：

```sql
mysql> DROP DATABASE mydb;
```

选定数据库mydb：

```sql
mysql> USE mydb;
```

查看当前选定的数据库：

```sql
mysql> SELECT DATABASE();
```

## 3. 操作数据表

获得可用数据表的一个列表：

```sql
mysql> SHOW TABLES;
```

创建一张名为coders的数据表：

```sql
mysql> CREATE TABLE coders
    -> (
    -> num       INT         NOT NULL AUTO_INCREMENT,
    -> name      VARCHAR(12) NOT NULL,
    -> golang    BOOLEAN     NOT NULL DEFAULT 0,
    -> cplusplus BOOLEAN     NOT NULL DEFAULT 0,
    -> java      BOOLEAN     NOT NULL DEFAULT 0,
    -> python    BOOLEAN     NOT NULL DEFAULT 0,
    -> PRIMARY KEY (num)
    -> ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

显示创建数据表coders时输入的语句：

```sql
mysql> SHOW CREATE TABLE coders;
```

删除数据表coders：

```sql
mysql> DROP TABLE coders;
```

查看表的结构：

```sql
mysql> SHOW COLUMNS FROM coders;
mysql> DESCRIBE coders;
```

将表coders重命名为programmers：

```sql
mysql> RENAME TABLE coders TO programmers;
```

给表coders增加一个名为javascript的列：

```sql
mysql> ALTER TABLE coders
    -> ADD javascript BOOLEAN;
```

将名为javascript的列重命名为js：

```sql
mysql> ALTER TABLE coders
    -> CHANGE javascript js BOOLEAN;
```

将js列的数据类型修改为INT：

```sql
mysql> ALTER TABLE coders
    -> MODIFY COLUMN js INT;
```

删去表coders中名为js的列：

```sql
mysql> ALTER TABLE coders
    -> DROP COLUMN js;
```

## 4. 增（Create）操作

插入第一行数据：

```sql
mysql> INSERT INTO coders
    -> (name, golang, cplusplus, python)
    -> VALUES
    -> ('paoqi', TRUE, TRUE, TRUE);
```

插入第二行数据：

```sql
mysql> INSERT INTO coders
    -> (name, java, python)
    -> VALUES
    -> ('hypo', TRUE, TRUE);
```

插入第三行数据：

```sql
mysql> INSERT INTO coders
    -> (name)
    -> VALUES
    -> ('xiaoting');
```

## 5. 删（Delete）操作

删去name为paoqi的行：

```sql
mysql> DELETE FROM coders
    -> WHERE name = 'paoqi';
```

删除所有数据：

```sql
mysql> TRUNCATE TABLE coders;
```

## 6. 改（Update）操作

将name为paoqi的行的golang字段置为FALSE：

```sql
mysql> UPDATE coders
    -> SET golang = FALSE
    -> WHERE name = 'paoqi';
```

## 7. 查（Retrieve）操作

查看name为paoqi的行的所有列：

```sql
mysql> SELECT * FROM coders WHERE name = 'paoqi';
```

查看name为paoqi的行的cplusplus列：

```sql
mysql> SELECT cplusplus FROM coders WHERE name = 'paoqi';
```

查看所有行的num和name列：

```sql
mysql> SELECT num, name FROM coders;
```

通过完全限定的表名和列名查看name列：

```sql
mysql> SELECT coders.name FROM mydb.coders;
```

查看从首行开始的两行数据：

```sql
mysql> SELECT * FROM coders LIMIT 2;
mysql> SELECT * FROM coders LIMIT 0, 2;
mysql> SELECT * FROM coders LIMIT 2 OFFSET 0;
```

查看name不重复的name列：

```sql
mysql> SELECT DISTINCT name FROM coders;
```

按name升序查看数据：

```sql
mysql> SELECT * FROM coders ORDER BY name;
```

按name降序查看数据：

```sql
mysql> SELECT * FROM coders ORDER BY name DESC;
```

按多个列升序查看数据：

```sql
mysql> SELECT * FROM coders ORDER BY cplusplus, python;
```

BETWEEN...AND...所形成的区间是闭区间，IN(...)枚举圆括号中的所有值。

```sql
mysql> SELECT * FROM coders WHERE cplusplus = TRUE AND python = TRUE;
mysql> SELECT * FROM coders WHERE java = TRUE OR golang = TRUE;
mysql> SELECT * FROM coders WHERE python != FALSE;
mysql> SELECT * FROM coders WHERE python <> FALSE;
mysql> SELECT * FROM coders WHERE cplusplus BETWEEN 0 AND 1;
mysql> SELECT * FROM coders WHERE cplusplus IN (0, 1);
mysql> SELECT * FROM coders WHERE cplusplus NOT IN (0, 1);
mysql> SELECT * FROM coders WHERE cplusplus IS NOT NULL;
```

利用通配符对数据进行过滤：

```sql
mysql> SELECT name FROM coders WHERE name LIKE 'lai%';
mysql> SELECT name FROM coders WHERE name LIKE '%qi';
mysql> SELECT name FROM coders WHERE name LIKE '%ao%';
mysql> SELECT name FROM coders WHERE name LIKE '________';
```

利用正则表达式对数据进行过滤：

```sql
mysql> SELECT name FROM coders WHERE name REGEXP '^lai';
mysql> SELECT name FROM coders WHERE name REGEXP 'qi$';
mysql> SELECT name FROM coders WHERE name REGEXP 'ao';
mysql> SELECT name FROM coders WHERE name REGEXP '.ing';
mysql> SELECT name FROM coders WHERE name REGEXP '^........$';
```

获取表coders的行数：

```sql
mysql> SELECT COUNT(*) FROM coders;
```

对数据进行分组：

```sql
mysql> SELECT python, COUNT(*) FROM coders GROUP BY python;
mysql> SELECT cplusplus, python, COUNT(*) FROM coders GROUP BY cplusplus, python;
```
