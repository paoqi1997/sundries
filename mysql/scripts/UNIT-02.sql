/**
 * MySQL之处理日期
 */

-- 表spending于UNIT-02.sql新建
USE mydb;

CREATE TABLE spending
(
num     INT         NOT NULL AUTO_INCREMENT,
name    VARCHAR(18) NOT NULL,
amount  FLOAT       NOT NULL,
daytime DATETIME    NOT NULL,
payment VARCHAR(24) NOT NULL,
PRIMARY KEY (num)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DESCRIBE spending;

INSERT INTO spending
(name, amount, daytime, payment)
VALUES
('paoqi', 18.88, '2018-09-10 06:00:00', 'alipay'),
('paoqi', 28.88, '2018-10-04 12:00:00', 'wechat'),
('paoqi', 88.88, '2018-11-02 18:00:00', 'alipay');

-- DATE( @param ) 提取年月日
SELECT num, name, amount, payment FROM spending
WHERE DATE(daytime) BETWEEN '2018-10-01' AND '2018-11-01';

DROP TABLE spending;
