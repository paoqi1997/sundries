# Part2

关于 MySQL 的第二部分。

## Tools

### mysqldump

通过 mysqldump 备份数据。

```
>mysqldump -uroot -p mydb > /path/to/mydb.sql
```

## Indexes

首先创建好数据表 tbl_bill。

```sql
mysql> USE mydb;

mysql> CREATE TABLE tbl_bill
    -> (
    -> id       INT          NOT NULL AUTO_INCREMENT,
    -> amount   DECIMAL(9,2) NOT NULL,
    -> method   TINYINT      NOT NULL,
    -> category VARCHAR(32)  NOT NULL DEFAULT 'others',
    -> time     DATETIME     NOT NULL,
    -> CONSTRAINT tbl_bill_pk PRIMARY KEY (id, time),
    -> INDEX tbl_bill_idx_category (category(4))
    -> ) ENGINE InnoDB;

mysql> INSERT INTO tbl_bill
    -> (amount, method, category, time)
    -> VALUES
    -> (+12000, 2, 'salary', '2021-05-10 10:00:00'),
    -> (-22.89, 0, 'food and drink', '2021-05-29 11:53:12'),
    -> (-3.5, 0, 'food and drink', '2021-05-29 20:48:35'),
    -> (-328, 0, 'game recharge', '2021-05-30 22:36:07');
```

创建索引。

```sql
mysql> CREATE INDEX tbl_bill_idx_time ON tbl_bill (time);

mysql> ALTER TABLE tbl_bill ADD INDEX tbl_bill_idx_time (time);
```

删除索引。

```sql
mysql> DROP INDEX tbl_bill_idx_time ON tbl_bill;

mysql> ALTER TABLE tbl_bill DROP INDEX tbl_bill_idx_time;
```

查看索引状态。

```sql
mysql> SHOW INDEX FROM tbl_bill;
```
