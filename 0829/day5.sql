/*
    �����Լ��� �׷������ 
    �����Լ� ��� �����Ϳ� ���� ����, ���, �ִ�, �ּڰ� ���� ���ϴ� �Լ�
    �׷���� �� ��� �����͸� Ư���׷����� ���� ���
*/
-- COUNT �ο� ���� ��ȯ�ϴ� �����Լ�.
SELECT COUNT(*)                      -- null ����
    ,  COUNT(department_id)          --default ALL
    ,  COUNT(ALL department_id)      --�ߺ� ����, null x
    ,  COUNT(DISTINCT department_id) --�ߺ� ���� 
    ,  COUNT(employee_id)            -- employees���̺��� pk (*) ����
FROM employees;

SELECT SUM(salary)          as �հ�
    ,  MAX(salary)          as �ִ�
    ,  MIN(salary)          as �ּ�
    ,  ROUND(AVG(salary),2) as ���
    ,  COUNT(employee_id)   as ������
FROM employees; -- <-- ���� ��� 

SELECT department_id
    ,  SUM(salary)          as �հ�
    ,  MAX(salary)          as �ִ�
    ,  MIN(salary)          as �ּ�
    ,  ROUND(AVG(salary),2) as ���
    ,  COUNT(employee_id)   as ������
FROM employees           -- ���� ���̺��� 
WHERE department_id IS NOT NULL -- �˻������� �ִٸ� FROM ���̿� GROUP
AND department_id IN (30,60,90)      
GROUP BY department_id   -- �μ� �� (�׷����� ����)
ORDER BY 1;

-- ȸ������ ���ϸ��� �հ�,���ϸ��� ���(�Ҽ��� ��°�ڸ�����)�� ����Ͻÿ� 
SELECT *
FROM member;

SELECT COUNT(*)
     , COUNT(mem_id) as ȸ����
     , SUM(mem_mileage) as ���ϸ����հ�
     , ROUND(AVG(mem_mileage),2) as ���ϸ������
FROM member;
-- ������ ȸ������ ���ϸ��� �հ�,��� ���(���ϸ��� �հ� ��������)


SELECT mem_job as ����
     , COUNT(mem_id) as ȸ����
     , SUM(mem_mileage) as ���ϸ����հ�
     , ROUND(AVG(mem_mileage),2) as ���ϸ������
FROM member
GROUP BY mem_job
ORDER BY 3 DESC;

-- ROWNUM �ǻ��÷� ���̺��� ������ �ִ°� ó�� ��밡��
SELECT  ROWNUM as rnum
      , mem_name
FROM member
WHERE ROWNUM <= 10;

-- HAVING ���� ����� ���ؼ� �˻������� �߰��ϰ������ ���
--ex) ������ ���ϸ��� �հ谡 10000 �̻� 
SELECT mem_job as ����
     , COUNT(mem_id) as ȸ����
     , SUM(mem_mileage) as ���ϸ����հ�
     , ROUND(AVG(mem_mileage),2) as ���ϸ������
FROM member
GROUP BY mem_job
HAVING SUM(mem_mileage) >= 10000 -- �������� �˻����� 
ORDER BY 3 DESC;

-- kor_loan_status(java����) ���̺��� loan_jan_amt(�����)
-- 2013�⵵ �Ⱓ��, ������ �� �����ܾ��� ����Ͻÿ� 
SELECT SUBSTR(period,1,4) as �⵵
     , region             as ����
     , SUM(loan_jan_amt)  as ������
FROM kor_loan_status
--WHERE period LIKE '2013%';
WHERE SUBSTR(period,1,4) = '2013'
GROUP BY SUBSTR(period,1,4), region;
-- 2013�⵵ ������, ���к� �հ�
SELECT SUBSTR(period,1,4) as �⵵
     , region             as ����
     , gubun              as ����
     , SUM(loan_jan_amt)  as ������
FROM kor_loan_status
WHERE SUBSTR(period,1,4) = '2013'
GROUP BY SUBSTR(period,1,4), region, gubun
ORDER BY 2;

-- ������ ������ �հ谡 200000 �̻��� ����� ����Ͻÿ� 
-- �����ܾ� ��������
SELECT region             as ����
     , SUM(loan_jan_amt)  as ������
FROM kor_loan_status
GROUP BY region
HAVING SUM(loan_jan_amt) >= 200000
ORDER BY 2 DESC;



-- ����, ����, �λ��� 
-- �⵵�� ������ �հ迡�� 
-- ������ ���� 60000 �Ѵ� ����� ����Ͻÿ�
-- ���� ���� ��������, ������ ��������
SELECT SUBSTR(period, 1, 4) as �⵵
     , region
     , SUM(loan_jan_amt)    as �����հ�
FROM kor_loan_status
WHERE region IN ('����','����','�λ�')
GROUP BY SUBSTR(period, 1, 4), region
HAVING SUM(loan_jan_amt) >= 60000
ORDER BY 2, 3 DESC;



-- employees �������� �Ի�⵵�� �������� ����Ͻÿ� 
-- hire_date ��� (���� �⵵ ��������)
SELECT TO_CHAR(hire_date,'YYYY') �⵵
    ,  COUNT(*) as ������
FROM employees
GROUP BY TO_CHAR(hire_date,'YYYY')
ORDER BY 1;
--10���̻� �Ի��� �⵵ 
SELECT TO_CHAR(hire_date,'YYYY') �⵵
    ,  COUNT(*) as ������
FROM employees
GROUP BY TO_CHAR(hire_date,'YYYY')
HAVING COUNT(*) >= 10
ORDER BY 1;



-- customers ȸ���� ��ü ȸ����, ���� ȸ����, ���� ȸ������ ����Ͻÿ�
-- ����, ���ڶ�� �÷��� ����. 
-- customers ���̺��� �÷��� Ȱ���ؼ� ��������. 
SELECT COUNT(cust_gender) as ��ü 
     , COUNT(DECODE(cust_gender,'F','����')) as ����
     , SUM(DECODE(cust_gender,'F',1, 0)) as ����2
     , COUNT(DECODE(cust_gender,'M','����')) as ����
     , SUM(DECODE(cust_gender,'M',1, 0)) as ����2
FROM customers;







SELECT SUM(DECODE(cust_gender, 'F', 1, 0)) as ���� 
     , SUM(DECODE(cust_gender, 'M', 1, 0)) as ���� 
     , COUNT(cust_gender) as ��ü
FROM customers;

SELECT COUNT(DECODE(cust_gender, 'F', '����')) as ���� 
     , COUNT(DECODE(cust_gender, 'M', '����')) as ���� 
     , COUNT(cust_gender) as ��ü
FROM customers;

SELECT TO_CHAR(hire_date,'YYYY') as �⵵
     , COUNT(*) as ������
FROM employees
GROUP BY TO_CHAR(hire_date,'YYYY')
ORDER BY �⵵;



--1.���Ϻ� ������ ��������� ���� ����Ͻÿ� 
--  �Ͽ��� ���� ~ (employees, hire_date)���

SELECT NVL(DECODE(TO_CHAR(hire_date,'d'),1,'��',2,'��',3,'ȭ'
                             ,4,'��',5,'��',6,'��',7,'��'),'�Ѱ�') as ����
     , COUNT(*) as �Ի�������
FROM employees
GROUP BY ROLLUP(TO_CHAR(hire_date,'d'))
ORDER BY TO_CHAR(hire_date,'d');

SELECT NVL(TO_CHAR(hire_date,'day'),'�Ѱ�') as ����
     , COUNT(*) as �Ի�������
FROM employees
GROUP BY TO_CHAR(hire_date,'day');


--2.�⵵�� ������ ����ο����� ����Ͻÿ�
--(employees, hire_date)���
-- ���� �⵵ ��������

SELECT TO_CHAR(hire_date,'YYYY') as yyyy
      ,SUM(DECODE(TO_CHAR(hire_date,'d'),'1',1, 0)) as sun
      ,COUNT(*) as �⵵����������հ�
FROM employees
GROUP BY TO_CHAR(hire_date,'YYYY')
ORDER BY 1;


-- ���� ������ UNION ------------------------------------------------------------------------

CREATE TABLE exp_goods_asia (
       country VARCHAR2(10),
       seq     NUMBER,
       goods   VARCHAR2(80));

INSERT INTO exp_goods_asia VALUES ('�ѱ�', 1, '�������� ������');
INSERT INTO exp_goods_asia VALUES ('�ѱ�', 2, '�ڵ���');
INSERT INTO exp_goods_asia VALUES ('�ѱ�', 3, '��������ȸ��');
INSERT INTO exp_goods_asia VALUES ('�ѱ�', 4, '����');
INSERT INTO exp_goods_asia VALUES ('�ѱ�', 5,  'LCD');
INSERT INTO exp_goods_asia VALUES ('�ѱ�', 6,  '�ڵ�����ǰ');
INSERT INTO exp_goods_asia VALUES ('�ѱ�', 7,  '�޴���ȭ');
INSERT INTO exp_goods_asia VALUES ('�ѱ�', 8,  'ȯ��źȭ����');
INSERT INTO exp_goods_asia VALUES ('�ѱ�', 9,  '�����۽ű� ���÷��� �μ�ǰ');
INSERT INTO exp_goods_asia VALUES ('�ѱ�', 10,  'ö �Ǵ� ���ձݰ�');

INSERT INTO exp_goods_asia VALUES ('�Ϻ�', 1, '�ڵ���');
INSERT INTO exp_goods_asia VALUES ('�Ϻ�', 2, '�ڵ�����ǰ');
INSERT INTO exp_goods_asia VALUES ('�Ϻ�', 3, '��������ȸ��');
INSERT INTO exp_goods_asia VALUES ('�Ϻ�', 4, '����');
INSERT INTO exp_goods_asia VALUES ('�Ϻ�', 5, '�ݵ�ü������');
INSERT INTO exp_goods_asia VALUES ('�Ϻ�', 6, 'ȭ����');
INSERT INTO exp_goods_asia VALUES ('�Ϻ�', 7, '�������� ������');
INSERT INTO exp_goods_asia VALUES ('�Ϻ�', 8, '�Ǽ����');
INSERT INTO exp_goods_asia VALUES ('�Ϻ�', 9, '���̿���, Ʈ��������');
INSERT INTO exp_goods_asia VALUES ('�Ϻ�', 10, '����');

