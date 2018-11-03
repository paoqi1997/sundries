/**
 * MySQL之分组数据
 */

USE mydb;

SELECT COUNT(*) AS item_cnt,
       MIN(amount) AS amount_min,
       MAX(amount) AS amount_max,
       AVG(amount) AS amount_avg
FROM spending;

-- 按payment分组
SELECT name, payment, COUNT(*) AS item_cnt
FROM spending GROUP BY payment;

-- 第一次筛选
SELECT name, payment, COUNT(*) AS item_cnt
FROM spending GROUP BY payment HAVING payment = 'alipay';

-- 第二次筛选
SELECT name, payment, COUNT(*) AS item_cnt
FROM spending WHERE amount >= 50.00 GROUP BY payment HAVING payment = 'alipay';
