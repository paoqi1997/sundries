# The manual of MySQL

面向MySQL的基本教程。

## 说明

以下语句均在 MySQL 5.7.21 on Windows 下调试通过。

## 热身

相关SQL语句如下所示：

```sql
-- Return a string that indicates the MySQL server version
mysql> SELECT VERSION();

-- Return the current date
mysql> SELECT CURDATE();
mysql> SELECT CURRENT_DATE;
mysql> SELECT CURRENT_DATE();
-- Return the current time
mysql> SELECT CURTIME();
mysql> SELECT CURRENT_TIME;
mysql> SELECT CURRENT_TIME();
-- Return the current date and time
mysql> SELECT NOW();
mysql> SELECT CURRENT_TIMESTAMP;
mysql> SELECT CURRENT_TIMESTAMP();
mysql> SELECT LOCALTIME;
mysql> SELECT LOCALTIME();
mysql> SELECT LOCALTIMESTAMP;
mysql> SELECT LOCALTIMESTAMP();

-- The user name and host name provided by the client
mysql> SELECT USER();
-- The authenticated user name and host name
mysql> SELECT CURRENT_USER;
mysql> SELECT CURRENT_USER();

-- SHOW STATUS provides server status information
mysql> SHOW STATUS;
```

## 操作数据库

相关SQL语句如下所示：

```sql
-- 返回可用数据库的一个列表
mysql> SHOW DATABASES;

-- 查看MySQL所支持的数据库引擎
mysql> SHOW ENGINES;

-- 创建一个名为mydb的数据库
mysql> CREATE DATABASE mydb CHARACTER SET utf8mb4;
-- 显示创建数据库mydb时所输入的语句
mysql> SHOW CREATE DATABASE mydb;

-- 显示当前选择的数据库
mysql> SELECT DATABASE();

-- 选择数据库mydb
mysql> USE mydb;

-- 删除数据库mydb
mysql> DROP DATABASE mydb;
```

## 操作数据表

相关SQL语句如下所示：

```sql
-- 返回可用数据表的一个列表
mysql> SHOW TABLES;

-- 创建一张名为libs的数据表
mysql> CREATE TABLE libs
    -> (
    -> id       INT         NOT NULL AUTO_INCREMENT,
    -> name     VARCHAR(16) NOT NULL,
    -> language VARCHAR(12) NOT NULL,
    -> windows  BOOLEAN     NOT NULL DEFAULT 0,
    -> linux    BOOLEAN     NOT NULL DEFAULT 0,
    -> macos    BOOLEAN     NOT NULL DEFAULT 0,
    -> PRIMARY KEY (id)
    -> ) ENGINE InnoDB;

-- 显示创建数据表libs时所输入的语句
mysql> SHOW CREATE TABLE libs;

-- 查看数据表libs的状态
mysql> SHOW TABLE STATUS FROM mydb WHERE Name = 'libs';

-- 查看数据表libs所使用的存储引擎
mysql> SELECT ENGINE FROM information_schema.TABLES WHERE TABLE_NAME = 'libs';

-- 查看数据表libs的结构
mysql> SHOW COLUMNS FROM libs;
mysql> DESCRIBE libs;

-- 将数据表libs重命名为libraries
mysql> RENAME TABLE libs TO libraries;

-- 删除数据表libs
mysql> DROP TABLE libs;
```

针对列的操作如下所示：

```sql
-- 给表libs增加一个名为android的列
mysql> ALTER TABLE libs
    -> ADD android BOOLEAN NOT NULL DEFAULT 0;

-- 将名为android的列重命名为ios
mysql> ALTER TABLE libs
    -> CHANGE android ios BOOLEAN NOT NULL DEFAULT 0;

-- 将名为ios的列的数据类型修改为INT
mysql> ALTER TABLE libs
    -> MODIFY ios INT;

-- 删除表coders中名为ios的列
mysql> ALTER TABLE libs
    -> DROP ios;
```

## 增（Create）操作

相关SQL语句如下所示：

```sql
mysql> INSERT INTO libs
    -> (name, language, windows, linux, macos)
    -> VALUES
    -> ('libevent', 'c', TRUE, TRUE, TRUE);

mysql> INSERT INTO libs
    -> (name, language, linux)
    -> VALUES
    -> ('muduo', 'cpp', TRUE), ('pqnet', 'cpp', TRUE);

mysql> INSERT INTO libs
    -> (name, language, linux, macos)
    -> VALUES
    -> ('handy', 'cpp', TRUE, TRUE);
```

## 删（Delete）操作

相关SQL语句如下所示：

```sql
-- 删除name为handy的行
mysql> DELETE FROM libs
    -> WHERE name = 'handy';

-- 删除所有行
mysql> TRUNCATE TABLE libs;
```

## 改（Update）操作

相关SQL语句如下所示：

```sql
mysql> UPDATE libs
    -> SET name = 'libuv'
    -> WHERE name = 'libevent';
```

## 查（Retrieve）操作

### 基础查询

相关SQL语句如下所示：

```sql
mysql> SELECT id, name FROM libs;
-- 通过完全限定的表名和列名查看name列
mysql> SELECT libs.name FROM mydb.libs;

mysql> SELECT * FROM libs WHERE name = 'libevent';
mysql> SELECT windows FROM libs WHERE name = 'libevent';

-- 查看从首行开始的2行数据
mysql> SELECT * FROM libs LIMIT 2;
mysql> SELECT * FROM libs LIMIT 0, 2;
mysql> SELECT * FROM libs LIMIT 2 OFFSET 0;

-- 查看name不重复的name列
mysql> SELECT DISTINCT name FROM libs;

-- 按name升序查看所有行
mysql> SELECT * FROM libs ORDER BY name;
-- 按name降序查看所有行
mysql> SELECT * FROM libs ORDER BY name DESC;
-- 按多个列升序查看所有行
mysql> SELECT * FROM libs ORDER BY windows, linux;

mysql> SELECT * FROM libs WHERE windows = TRUE AND linux = TRUE;
mysql> SELECT * FROM libs WHERE windows = TRUE OR linux = TRUE;
mysql> SELECT * FROM libs WHERE windows != FALSE;
mysql> SELECT * FROM libs WHERE windows <> FALSE;
-- BETWEEN...AND...所形成的区间是闭区间
mysql> SELECT * FROM libs WHERE windows BETWEEN 0 AND 1;
-- IN(...)枚举圆括号中的所有值
mysql> SELECT * FROM libs WHERE windows IN (0, 1);
mysql> SELECT * FROM libs WHERE windows NOT IN (0, 1);
mysql> SELECT * FROM libs WHERE windows IS NOT NULL;

-- 利用通配符对数据进行过滤
mysql> SELECT name FROM libs WHERE name LIKE 'lib%';
mysql> SELECT name FROM libs WHERE name LIKE '%duo';
mysql> SELECT name FROM libs WHERE name LIKE '%d%';
mysql> SELECT name FROM libs WHERE name LIKE '_____';

-- 利用正则表达式对数据进行过滤
mysql> SELECT name FROM libs WHERE name REGEXP '^lib';
mysql> SELECT name FROM libs WHERE name REGEXP 'duo$';
mysql> SELECT name FROM libs WHERE name REGEXP 'd';
mysql> SELECT name FROM libs WHERE name REGEXP 'p.net';
mysql> SELECT name FROM libs WHERE name REGEXP '^.....$';

-- 获取表libs的行数
mysql> SELECT COUNT(*) FROM libs;

-- 对数据进行分组
mysql> SELECT language, COUNT(*) FROM libs GROUP BY language;
mysql> SELECT name, language, COUNT(*) FROM libs GROUP BY name, language;

mysql> SELECT windows, COUNT(*) FROM libs GROUP BY windows;
mysql> SELECT windows, COUNT(*) FROM libs GROUP BY windows HAVING COUNT(*) > 1;
```

创建数据表 player_charge 以学习接下来的查询操作。

```sql
mysql> CREATE TABLE player_charge
    -> (
    -> id     INT             NOT NULL AUTO_INCREMENT,
    -> uid    INT(6) ZEROFILL NOT NULL,
    -> name   VARCHAR(32)     NOT NULL,
    -> method TINYINT         NOT NULL,
    -> num    INT UNSIGNED    NOT NULL,
    -> stime  DATETIME        NOT NULL,
    -> utime  INT UNSIGNED    NOT NULL,
    -> PRIMARY KEY (id)
    -> ) ENGINE InnoDB;

mysql> INSERT INTO player_charge
    -> (uid, name, method, num, stime, utime)
    -> VALUES
    -> (2468, 'paoqi', 0, 128, NOW(), UNIX_TIMESTAMP()),
    -> (2468, 'paoqi', 0, 328,
    -> DATE_ADD(NOW(), INTERVAL 1 MINUTE),
    -> UNIX_TIMESTAMP(DATE_ADD(NOW(), INTERVAL 1 MINUTE)));

mysql> INSERT INTO player_charge
    -> (uid, name, method, num, stime, utime)
    -> VALUES
    -> (4096, 'honolulu', 0, 648, NOW(), UNIX_TIMESTAMP());

-- 拼接 name(uid) 字段
mysql> SELECT CONCAT(name, '(', uid, ')') AS name_uid FROM player_charge;
-- 八折充值
mysql> SELECT name, num, num * 0.8 AS new_num FROM player_charge;
-- 获取充值情况
mysql> SELECT COUNT(num), MIN(num), MAX(num), SUM(num), AVG(num)
    -> FROM player_charge WHERE name = 'paoqi';
```

### 子查询

创建数据表 player 以学习接下来的查询操作。

```sql
mysql> CREATE TABLE player
    -> (
    -> id      INT             NOT NULL AUTO_INCREMENT,
    -> uid     INT(6) ZEROFILL NOT NULL,
    -> name    VARCHAR(32)     NOT NULL,
    -> level   INT UNSIGNED    NOT NULL,
    -> regtime DATETIME        NOT NULL,
    -> PRIMARY KEY (id)
    -> ) ENGINE InnoDB;

mysql> INSERT INTO player
    -> (uid, name, level, regtime)
    -> VALUES
    -> (2468, 'paoqi', 32, '2020-09-16 20:32:03'),
    -> (4096, 'honolulu', 28, '2020-10-12 13:56:18');
```

相关SQL语句如下所示：

```sql
-- 查询等级在30级及以上的玩家的充值记录
mysql> SELECT uid, name, num, stime FROM player_charge
    -> WHERE uid IN (SELECT uid FROM player WHERE level >= 30);

-- 查询玩家的uid、名字、等级及充值总额
mysql> SELECT uid, name, level,
    -> (SELECT SUM(num) FROM player_charge WHERE player.uid = player_charge.uid) AS sum
    -> FROM player;
```

### 联结

以内联结的方式查询玩家的uid、名字及充值记录。

```sql
mysql> SELECT player.uid, player.name, num, stime FROM player, player_charge
    -> WHERE player.uid = player_charge.uid ORDER BY player.uid, player.name, num;

mysql> SELECT player.uid, player.name, num, stime FROM player INNER JOIN player_charge
    -> ON player.uid = player_charge.uid;
```

接下来准备要用到的数据：

```sql
mysql> INSERT INTO player_charge
    -> (uid, name, method, num, stime, utime)
    -> VALUES
    -> (4096, 'honolulu', 1, 68,
    -> DATE_ADD(NOW(), INTERVAL 3 HOUR),
    -> UNIX_TIMESTAMP(DATE_ADD(NOW(), INTERVAL 3 HOUR)));

mysql> INSERT INTO player
    -> (uid, name, level, regtime)
    -> VALUES
    -> (6779, 'souryuu', 26, '2020-11-03 08:22:47');

mysql> INSERT INTO player_charge
    -> (uid, name, method, num, stime, utime)
    -> VALUES
    -> (6779, 'souryuu', 1, 6, NOW(), UNIX_TIMESTAMP()),
    -> (6779, 'souryuu', 2, 30,
    -> DATE_ADD(NOW(), INTERVAL 1 DAY),
    -> UNIX_TIMESTAMP(DATE_ADD(NOW(), INTERVAL 1 DAY)));
```

查询充值过648块的玩家的充值记录。

```sql
-- 子查询
mysql> SELECT uid, name, method, num, stime FROM player_charge
    -> WHERE uid = (SELECT uid FROM player_charge WHERE num = 648);

-- 自联结
mysql> SELECT p1.uid, p1.name, p1.method, p1.num, p1.stime
    -> FROM player_charge AS p1, player_charge AS p2
    -> WHERE p1.uid = p2.uid AND p2.num = 648;
```

以外联结的方式查询玩家的uid、名字及充值记录。

```sql
-- 左外联结
mysql> SELECT player.uid, player.name, num, stime FROM player LEFT OUTER JOIN player_charge
    -> ON player.uid = player_charge.uid;

-- 右外联结
mysql> SELECT player.uid, player.name, num, stime FROM player RIGHT OUTER JOIN player_charge
    -> ON player.uid = player_charge.uid;
```

### 组合查询

相关SQL语句如下所示：

```sql
mysql> SELECT uid, name FROM player WHERE level >= 30
    -> UNION
    -> SELECT uid, name FROM player_charge WHERE num <= 30;

mysql> SELECT uid, name FROM player WHERE level >= 30
    -> UNION ALL
    -> SELECT uid, name FROM player_charge WHERE num <= 30;
```

### 全文本搜索

创建数据表 intros 以学习接下来的查询操作。

```sql
-- 无论是 MyISAM 还是 InnoDB 全文本搜索都有点问题，可能是别的原因所致
mysql> CREATE TABLE intros
    -> (
    -> id         INT         NOT NULL AUTO_INCREMENT,
    -> name       VARCHAR(16) NOT NULL,
    -> content    TEXT        NOT NULL,
    -> intro_time DATETIME    NOT NULL,
    -> PRIMARY KEY (id),
    -> FULLTEXT (content)
    -> ) ENGINE MyISAM;

mysql> INSERT INTO intros
    -> (name, content, intro_time)
    -> VALUES
    -> ('paoqi', 'Be the best.', NOW()),
    -> ('VAN', 'My name is VAN.', DATE_SUB(NOW(), INTERVAL 5 MINUTE)),
    -> ('Jimmy', 'I think I am the best one for this position.',
    -> DATE_SUB(NOW(), INTERVAL '0:30' HOUR_MINUTE));
```

相关SQL语句如下所示：

```sql
mysql> SELECT content FROM intros WHERE Match(content) Against('best');

mysql> SELECT content, Match(content) Against('best') AS rank FROM intros;

-- 使用查询扩展
mysql> SELECT content FROM intros WHERE Match(content) Against('best' WITH QUERY EXPANSION);

-- 匹配短语'best one'
mysql> SELECT content FROM intros WHERE Match(content) Against('"best one"' IN BOOLEAN MODE);
```

## 视图

相关SQL语句如下所示：

```sql
mysql> CREATE VIEW iview AS
    -> SELECT player.uid, player.name, num, stime, utime FROM player, player_charge
    -> WHERE player.uid = player_charge.uid;

mysql> SHOW TABLE STATUS FROM mydb WHERE Comment = 'VIEW';

mysql> DESCRIBE iview;
mysql> DESC iview;

mysql> SELECT * FROM iview WHERE num >= 100;

-- 修改视图结构但不影响基表
mysql> ALTER VIEW iview AS
    -> SELECT player.uid, player.name FROM player, player_charge
    -> WHERE player.uid = player_charge.uid;

mysql> UPDATE iview SET stime = NOW(), utime = UNIX_TIMESTAMP()
    -> WHERE name = 'souryuu' AND num = 30;

mysql> DROP VIEW iview;
```

## 存储过程

相关SQL语句如下所示：

```sql
mysql> DELIMITER #
    -> CREATE PROCEDURE showAll()
    -> BEGIN
    ->     SELECT * FROM player_charge;
    -> END; #
    -> DELIMITER ;

mysql> SHOW PROCEDURE STATUS LIKE 'showAll';

mysql> SELECT ROUTINE_NAME FROM information_schema.ROUTINES
    -> WHERE ROUTINE_SCHEMA = 'mydb' AND ROUTINE_TYPE = 'PROCEDURE';

mysql> CALL showAll();

mysql> DELIMITER #
    -> CREATE PROCEDURE analyseNum(
    ->     OUT nl DECIMAL(8, 2),
    ->     OUT nh DECIMAL(8, 2),
    ->     OUT na DECIMAL(8, 2)
    -> )
    -> BEGIN
    ->     SELECT MIN(num) INTO nl FROM player_charge;
    ->     SELECT MAX(num) INTO nh FROM player_charge;
    ->     SELECT AVG(num) INTO na FROM player_charge;
    -> END; #
    -> DELIMITER ;

mysql> CALL analyseNum(@nl, @nh, @na);
mysql> SELECT @nl, @nh, @na;

mysql> DELIMITER #
    -> CREATE PROCEDURE calNetIncome(
    ->     IN  take_a_cut BOOLEAN,
    ->     IN  rate       DECIMAL(8, 2),
    ->     OUT net_income DECIMAL(8, 2)
    -> ) COMMENT 'Calculate the net income.'
    -> BEGIN
    ->     DECLARE total DECIMAL(8, 2);
    ->     SELECT SUM(num) INTO total FROM player_charge;
    ->     IF take_a_cut THEN
    ->         SELECT total * (1 - rate) INTO net_income;
    ->     ELSE
    ->         SELECT total INTO net_income;
    ->     END IF;
    -> END; #
    -> DELIMITER ;

mysql> SHOW CREATE PROCEDURE calNetIncome;

mysql> CALL calNetIncome(TRUE, 0.3, @income);
mysql> SELECT @income;

mysql> DROP PROCEDURE calNetIncome;
```

### 游标

相关SQL语句如下所示：

```sql
mysql> DELIMITER #
    -> CREATE PROCEDURE discount(
    ->     IN  num     INT UNSIGNED,
    ->     IN  rate    DECIMAL(8, 2),
    ->     OUT new_num DECIMAL(8, 2)
    -> )
    -> BEGIN
    ->     SELECT num * rate INTO new_num;
    -> END; #
    -> DELIMITER ;

mysql> DELIMITER #
    -> CREATE PROCEDURE showDiscountedNums(
    ->     IN rate DECIMAL(8, 2)
    -> )
    -> BEGIN
    ->     DECLARE done BOOLEAN DEFAULT 0;
    ->     DECLARE n INT UNSIGNED;
    ->     DECLARE new_n DECIMAL(8, 2);
    ->     --
    ->     DECLARE numcur CURSOR
    ->     FOR SELECT num FROM player_charge;
    ->     --
    ->     DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET done=1;
    ->     --
    ->     CREATE TABLE IF NOT EXISTS tbl_new_nums(
    ->         num     INT UNSIGNED,
    ->         new_num DECIMAL(8, 2)
    ->     );
    ->     --
    ->     OPEN numcur;
    ->     REPEAT
    ->         FETCH numcur INTO n;
    ->         IF done != 1 THEN
    ->             CALL discount(n, rate, new_n);
    ->             INSERT INTO tbl_new_nums (num, new_num) VALUES (n, new_n);
    ->         END IF;
    ->     UNTIL done END REPEAT;
    ->     CLOSE numcur;
    ->     --
    ->     SELECT * FROM tbl_new_nums;
    ->     DROP TABLE IF EXISTS tbl_new_nums;
    -> END; #
    -> DELIMITER ;

mysql> CALL showDiscountedNums(0.8);
```
