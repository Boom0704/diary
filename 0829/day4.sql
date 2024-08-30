-- DECODE ǥ���� 
SELECT cust_name
     , cust_gender
     --       (����÷�, ����1, true�϶�)
     , DECODE(cust_gender, 'M', '����') as gender
     --       (����÷�, ����1, true�϶�, �׹ۿ�)
     , DECODE(cust_gender, 'M', '����', '����') as gender
     --       (����÷�, ����1, true�϶�, ����2, true�϶�)
     , DECODE(cust_gender, 'M', '����', 'F', '����') as gender
     , DECODE(cust_gender, 'M', '����', 'F', '����', '?') as gender
FROM customers;

SELECT mem_name, mem_regno2
     , DECODE(SUBSTR(mem_regno2,1,1),'1','����','2','����') as gender
FROM member;

/*  ��ȯ�Լ�(Ÿ��) Ÿ�Ժ�ȯ ������.***
    TO_CHAR ����������
    TO_DATE ��¥������
    TO_NUMBER ���������� 
*/
SELECT TO_CHAR(123456, '999,999,999') as ex1
     , TO_CHAR(SYSDATE, 'YYYY-MM-DD') as ex2
     , TO_CHAR(SYSDATE, 'YYYYMMDD')   as ex3
     , TO_CHAR(SYSDATE, 'YYYY/MM/DD HH24:MI:SS') as ex4
     , TO_CHAR(SYSDATE, 'YYYY/MM/DD HH12:MI:SS') as ex5
     , TO_CHAR(SYSDATE, 'day')  AS ex6
     , TO_CHAR(SYSDATE, 'YYYY') AS ex7
     , TO_CHAR(SYSDATE, 'YY')   AS ex8
     , TO_CHAR(SYSDATE, 'dd')   AS ex9
     , TO_CHAR(SYSDATE, 'd')    AS ex10
FROM dual;
-- TO_DATE 
SELECT TO_DATE('231229','YYMMDD') AS ex1
      ,TO_DATE('2024 08 02 09:10:00', 'YYYY MM DD HH24:MI:SS') as ex2
      ,TO_DATE('24', 'YY') as ex3
      ,TO_DATE('45', 'YY') as ex4
      -- RR�� ���⸦ �ڵ����� ���� 50 -> 1950, 49 -> 2049
      -- Y2K 2000�� ������ ���� ����å���� ���Ե�.
      ,TO_DATE('50', 'RR') as ex5
FROM dual;
CREATE TABLE ex4_1(
     title VARCHAR2(100)
    ,d_day DATE
);
INSERT INTO ex4_1 VALUES('������','20240802');
INSERT INTO ex4_1 VALUES('������','2025.01.17');

INSERT INTO ex4_1 VALUES('ź�ұ���','2024 09 04');
INSERT INTO ex4_1 VALUES('ȸ��','2024 09 06 18:05:00'); -- ������
INSERT INTO ex4_1 
VALUES('ȸ��',TO_DATE('2024 09 06 18:05:00','YYYY MM DD HH24:MI:SS'));
SELECT * FROM ex4_1;
CREATE TABLE ex4_2(
     seq1 VARCHAR2(100)
    ,seq2 NUMBER
);
INSERT INTO ex4_2 VALUES('1234','1234');
INSERT INTO ex4_2 VALUES('99','99');
INSERT INTO ex4_2 VALUES('195','195');
SELECT *
FROM ex4_2
ORDER BY TO_NUMBER(seq1) DESC; 

-- member ȸ���� ��������� �̿��Ͽ� ���̸� ����Ͻÿ� 
-- ���س⵵�� �̿��Ͽ� (ex 2024 - 2000 -> 24��) 
-- ������ ���� ��������
SELECT mem_name, mem_bir
     , TO_CHAR(mem_bir,'YYYY') 
     , TO_CHAR(SYSDATE,'YYYY')
     , TO_CHAR(SYSDATE,'YYYY')- TO_CHAR(mem_bir,'YYYY') ||'��' as age
FROM member
ORDER BY mem_bir ASC;
SELECT 1
FROM member;
/* ���� �Լ� (�Ű����� ������)
   ABS:���밪, ROUND:�ݿø�, TRUNC:����, CEIL:�ø�, MOD:��������, SQRT:������*/
SELECT ABS(-10) as ex1
     , ABS(10)  as ex2
     , ROUND(10.5555, 1) as ex3
     , ROUND(10.5555)    as ex4
     , TRUNC(10.5555,1)  as ex5
     , CEIL(10.5555)     as ex6
     , MOD(4, 2)         as ex7
     , MOD(5, 2)         as ex8
FROM dual;
/* ��¥ �Լ� */ 
-- ADD_MONTHS(��¥������, 1)  ������ 
-- LAST_DAY ��������, NEXT_DAY �������� ���� 
SELECT ADD_MONTHS(SYSDATE, 1)     as ex1 -- ������
     , ADD_MONTHS(SYSDATE,-1)     as ex2 -- ����
     , LAST_DAY(SYSDATE)          as ex3 -- �̹��� ��������
     , NEXT_DAY(SYSDATE, 'ȭ����') as ex4
     , NEXT_DAY(SYSDATE, '������') as ex5
FROM dual;
SELECT SYSDATE - 1  as ex1  -- ���� 
    ,  ADD_MONTHS(SYSDATE,1) - ADD_MONTHS(SYSDATE, -1) as ex2
FROM dual;

SELECT mem_name, mem_bir
 , sysdate - mem_bir
 , TO_CHAR(sysdate,'YYYYMMDD') -  TO_CHAR(mem_bir,'YYYYMMDD') as ex1 --���ڰ��
 , TO_DATE(TO_CHAR(sysdate,'YYYYMMDD')) 
     - TO_DATE(TO_CHAR(mem_bir,'YYYYMMDD')) as ex2 --��¥��� 
FROM member;

-- �̹����� ���� ���������? 
-- ȸ�ı��� ���� ?

SELECT LAST_DAY(SYSDATE) - SYSDATE as �̹���
     , TO_DATE('20240906') - TO_DATE(TO_CHAR(SYSDATE,'YYYYMMDD')) as ȸ�ı���
FROM dual;

-- DISTINCT �ߺ��� �����͸� �����ϰ� ������ ���� ��ȯ(Ư�� �÷��� ������ ���� ����������)
SELECT DISTINCT mem_job
FROM member;

SELECT DISTINCT mem_job, mem_like
     --�� ������ �ߺ����� �ʴ� �ุ ��ȯ
FROM member;

--SELECT DISTINCT prod_category, prod_subcategory
--FROM products
--ORDER BY 1;


-- NVL(�÷�, ��ȯ��)
SELECT emp_name
     , salary
     , commission_pct
     , salary + (salary * commission_pct) as ������
     , salary + (salary * NVL(commission_pct, 0) ) as ������2
FROM employees;

-- ������ �ټӳ���� 25�� �̻��� ������ ����Ͻÿ� ! (�ټӳ�� ��������)
SELECT emp_name, hire_date
     , TO_CHAR(hire_date, 'YYYY')
     , TO_CHAR(SYSDATE, 'YYYY')
     , TO_CHAR(SYSDATE, 'YYYY') - TO_CHAR(hire_date, 'YYYY') as �ټӳ��
FROM employees
WHERE TO_CHAR(SYSDATE, 'YYYY') - TO_CHAR(hire_date, 'YYYY') >= 25
ORDER BY �ټӳ�� DESC;

 /*
 ���� ���̺�(CUSTOMERS)���� 
 ������ ����⵵(cust_year_of_birth) �÷��� �ִ�. 
  ������ �������� �� �÷��� Ȱ���� 30��, 40��, 50�븦 ������ ����ϰ�, 
 ������ ���ɴ�� '��Ÿ'�� ����ϴ� ������ �ۼ��غ���. 
 ( 1990�� �̻� ��� ) ������ ���� ��������
 */
 


SELECT CUST_YEAR_OF_BIRTH
       ,(TO_CHAR(SYSDATE, 'YYYY')  - CUST_YEAR_OF_BIRTH ) as ����
--     , TRUNC((TO_CHAR(SYSDATE, 'YYYY')  - CUST_YEAR_OF_BIRTH ) / 10)
     , DECODE(TRUNC((TO_CHAR(SYSDATE, 'YYYY')  - CUST_YEAR_OF_BIRTH ) / 10), 3
                      ,'30��'
                      , 4,'40��', 5,'50��', '��Ÿ')  as ���ɴ�
FROM customers
WHERE cust_gender = 'M'
AND cust_marital_status = 'single'
AND CUST_YEAR_OF_BIRTH <= 1990
ORDER BY CUST_YEAR_OF_BIRTH DESC;












SELECT emp_name
     , hire_date
     ,TO_CHAR(SYSDATE, 'YYYY') -  TO_CHAR(hire_date, 'YYYY') as �ټӳ��
FROM employees
WHERE TO_CHAR(SYSDATE, 'YYYY') -  TO_CHAR(hire_date, 'YYYY') >=25
ORDER BY �ټӳ�� desc;


















