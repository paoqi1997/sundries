# 简述

面向MySQL的基本教程。

# 说明

以下语句均在MySQL 5.7.21 on Windows下调试通过。

# 语句

那么，就让我们开始吧！祝你好运！

## 1. MySQL是什么来的？

若要查看MySQL的版本，可以使用以下语句：

```sql
mysql> SELECT VERSION();
```

你可使用以下语句查看当前日期：

```sql
mysql> SELECT CURRENT_DATE;
```

接上文，以下语句可以得到更加精确的结果：

```sql
mysql> SELECT NOW();
```

以下语句可以帮助你查看当前用户名：

```sql
mysql> SELECT USER();
```

以下语句用于显示服务器的状态信息：

```sql
mysql> SHOW STATUS;
```

## 2. 什么？数据库里面还有数据库？

以下语句用于查看MySQL Server下所有已经建立好的数据库：

```sql
mysql> SHOW DATABASES;
```

以下语句用于查看MySQL所支持的数据库引擎：

```sql
mysql> SHOW ENGINES;
```

若要创建一个数据库，可以使用以下语句：

```sql
mysql> CREATE DATABASE mydb;
```

这条语句复现了你创建这个数据库的过程：

```sql
mysql> SHOW CREATE DATABASE mydb;
```

要删除它，可以这么做：

```sql
mysql> DROP DATABASE mydb;
```

## 3. 让我看看你的数据表！

为了进行后续的操作，我们需要选定一个数据库：

```sql
mysql> USE mydb;
```

你可以查看你所选定的数据库：

```sql
mysql> SELECT DATABASE();
```

以下语句用于查看某个数据库所持有的数据表：

```sql
mysql> SHOW TABLES;
```

接下来就可以创建一张数据表了：

```sql
mysql> CREATE TABLE coders
    -> (
    -> num       INT         NOT NULL AUTO_INCREMENT,
    -> name      VARCHAR(12) NOT NULL,
    -> clang     BOOLEAN     NOT NULL DEFAULT 0,
    -> cplusplus BOOLEAN     NOT NULL DEFAULT 0,
    -> csharp    BOOLEAN     NOT NULL DEFAULT 0,
    -> java      BOOLEAN     NOT NULL DEFAULT 0,
    -> python    BOOLEAN     NOT NULL DEFAULT 0,
    -> PRIMARY KEY (num)
    -> ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

这条语句复现了你创建这个数据表的过程：

```sql
mysql> SHOW CREATE TABLE coders;
```

如果你想知道表的结构，可以这么做：

```sql
mysql> SHOW COLUMNS FROM coders;
```

下面这条语句更加简便，效果也是一样的：

```sql
mysql> DESCRIBE coders;
```

现在让我们尝试插入一行数据：

```sql
mysql> INSERT INTO coders
    -> (name, clang, cplusplus, python)
    -> VALUES
    -> ('laidaoqi', TRUE, TRUE, TRUE);
```

## 4. 查询是门大学问！ 

该怎么查看它呢？你可以这么做：

```sql
mysql> SELECT * FROM coders WHERE name = 'laidaoqi';
```

如果只想查看它的某些属性，这条语句可以帮到你：

```sql
mysql> SELECT cplusplus FROM coders WHERE name = 'laidaoqi';
```

实际上，我们可以查看整张表的数据，在此之前我们先插入另外一行数据：

```sql
mysql> INSERT INTO coders
    -> (name)
    -> VALUES
    -> ('chenxiaoting');

mysql> SELECT * FROM coders;
```

同样地，你可以只查看整张表的某些字段：

```sql
mysql> SELECT num, name FROM coders;
```

有时候你可能会使用完全限定的表名和列名来查询：

```sql
mysql> SELECT coders.name FROM mydb.coders;
```

查看从首行开始的两行数据可以这么做：

```sql
mysql> SELECT * FROM coders LIMIT 2;
```

以下语句的效果是一样的：

```sql
mysql> SELECT * FROM coders LIMIT 0, 2;

mysql> SELECT * FROM coders LIMIT 2 OFFSET 0;
```

让我们再次插入一行数据，如果不想看到重复的数据，这么做是可行的：

```sql
mysql> INSERT INTO coders
    -> (name, clang, java, python)
    -> VALUES
    -> ('leihaibo', TRUE, TRUE, TRUE);

mysql> SELECT DISTINCT name FROM coders;
```

按序查看整张表也是可以的：

```sql
mysql> SELECT * FROM coders ORDER BY name;
```

如果想反过来看呢？对不起，这个同样可以做到：

```sql
mysql> SELECT * FROM coders ORDER BY name DESC;
```

按多个列进行排序也是可以做到的：

```sql
mysql> SELECT * FROM coders ORDER BY clang, cplusplus;
```

## 5. 更加高明的查询！

我需要一名C/C++开发工程师！

```sql
mysql> SELECT * FROM coders WHERE clang = TRUE AND cplusplus = TRUE;
```

Java和.NET是两种不同的Web开发技术栈。

```sql
mysql> SELECT * FROM coders WHERE java = TRUE OR csharp = TRUE;
```

掌握Python就更好了！

```sql
mysql> SELECT * FROM coders WHERE python != FALSE;

mysql> SELECT * FROM coders WHERE python <> FALSE;
```

你的C++学到什么地步了？闭区间[0, 1]代表我的评判标准。

```sql
mysql> SELECT * FROM coders WHERE cplusplus BETWEEN 0 AND 1;
```

C++是门难以捉摸的语言，你要么会，要么不会。

```sql
mysql> SELECT * FROM coders WHERE cplusplus IN (0, 1);
```

再怎么样我也是编译通过的男人啊！

```sql
mysql> SELECT * FROM coders WHERE cplusplus NOT IN (0, 1);
```

一切的一切都是如此的真实。

```sql
mysql> SELECT * FROM coders WHERE cplusplus IS NOT NULL;
```

## 6. 匹配模式开启！

如果你想查询开头为'lai'的名字，可以这么做：

```sql
mysql> SELECT name FROM coders WHERE name LIKE 'lai%';
```

如果是结尾为'qi'的名字呢？那就这样：

```sql
mysql> SELECT name FROM coders WHERE name LIKE '%qi';
```

不行！我就是要站在中间！

```sql
mysql> SELECT name FROM coders WHERE name LIKE '%ao%';
```

能找到长度为8的名字吗？当然可以！不过你得有8个下划线！

```sql
mysql> SELECT name FROM coders WHERE name LIKE '________';
```

你可在MySQL中使用正则表达式这一工具，先来查询开头为'lai'的名字吧！

```sql
mysql> SELECT name FROM coders WHERE name REGEXP '^lai';
```

其他类似的查询操作同样可以用正则表达式来完成：

```sql
mysql> SELECT name FROM coders WHERE name REGEXP 'qi$';

mysql> SELECT name FROM coders WHERE name REGEXP 'ao';

mysql> SELECT name FROM coders WHERE name REGEXP '^........$';
```

## 7. 一些有用的数值

如果你想查看表里有多少行数据可以这么做：

```sql
mysql> SELECT COUNT(*) FROM coders;
```

那么，这里到底有多少人掌握Python呢？现在就可以看到：

```sql
mysql> SELECT python, COUNT(*) FROM coders GROUP BY python;
```

如果是C和C++呢？也是一样的：

```sql
mysql> SELECT clang, cplusplus, COUNT(*) FROM coders GROUP BY clang, cplusplus;
```

## 8. 后续

后续操作就交给脚本们吧！

```sql
mysql> \q
```
