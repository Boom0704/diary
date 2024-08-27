/*
    table ���̺�
    1.���̺�� �÷����� �ִ� ũ��� 30byte (������1�� 1byte)
    2.���̺�� �÷������� ������ ����� �� ����.(select, varchar2...)
    3.���̺�� �÷������� ����, ����, _, $, #�� ����� �� ������ 
      ù ���ڴ� ���ڸ� �� �� ����.
    4.�� ���̺� ��� ������ �÷��� �ִ� 255��
*/
-- ��ɾ�� ��ҹ��� �������� ����. 
-- �����ʹ� ��ҹ��� ������.
CREATE TABLE ex1_1(
    col1 CHAR(10)
   ,col2 VARCHAR2(10)   -- �ϳ��� �÷��� �ϳ��� Ÿ�԰� ����� ����
);
-- ���̺� ���� 
DROP TABLE ex1_1; 
-- INSERT ������ ���� 
INSERT INTO ex1_1 (col1, col2)
VALUES ('oracle', '����');
INSERT INTO ex1_1 (col1, col2)
VALUES ('oracle', '����Ŭ');
INSERT INTO ex1_1 (col1, col2)
VALUES ('oracle', '����Ŭdb');
-- ������ ��ȸ
SELECT *  -- * ��ü(�÷�)�� �ǹ���.
FROM ex1_1;

SELECT col1 -- ��ȸ�ϰ� ���� �÷��ۼ�
FROM ex1_1;

SELECT length(col1)
     , length(col2)
     , lengthb(col1)
     , lengthb(col2) 
FROM ex1_1;
-- ��ɾ�� ��ҹ��ڸ� �������� ����.
-- ��ɾ ���� �����Ϸ��� ��ҹ��ڸ� ���
-- SQL���� ���� ���� �鿩���⸦ �ؼ� �ۼ�
SELECT *
FROM employees; -- from ���� ��ȸ�ϰ��� �ϴ� ���̺� �ۼ�
-- ���̺� ���� ��ȸ
DESC employees;
SELECT emp_name     as nm   --AS, as(alias ��Ī)
     , hire_date    hd      -- �޸��� �������� �÷��� ���� ���� ����
                                  -- ��Ī���� �ν�
     , salary         sa_la       -- ��Ī���� ����� �ȵ�
     , department_id "�μ����̵�"   -- �ѱ��� "" ������ �ѱ� ��Ī�� �Ⱦ�
FROM employees;
-- �˻����� where 
SELECT *
FROM employees
WHERE salary >= 20000;
-- �˻����� ������ AND or OR
SELECT *
FROM employees
WHERE salary >= 10000   -- and �� �׸����� �ǹ� (�Ѵ� ��)
AND   salary < 11000
AND   department_id = 80;

SELECT *
FROM employees
WHERE department_id = 30
OR    department_id = 60;
-- �������� order by   ASC ��������, DESC ��������
SELECT emp_name
     , department_id
FROM employees
ORDER BY department_id, emp_name DESC;  -- default ASC
-- ��Ģ���� ��밡��
SELECT emp_name
     , salary as ����
     , salary - salary * 0.1 as �Ǽ��ɾ�
     , salary * 12  as ����
     , ROUND(salary / 30 , 2) as �ϴ�
FROM employees
ORDER BY ���� DESC;
-- ������� FROM-> WHERE-> GROUP BY -> HAVING -> SELECT -> ORDER BY 
/*
    ��������
    NOT NULL ���� ������� �ʰڴ�.
    UNIQU �ߺ��� ������� �ʰڴ�!
    CHECK Ư�� �����͸� �ްڴ�.
    PRIMARY KEY �⺻Ű(�ϳ��� ���̺� 1���� �������� (�ΰ��� �÷����ε� ����)
                      �ϳ��� ���� �����ϴ� �ĺ��� or Ű���̶�� �ϸ� PK�� ��.
                      PK�� �⺻������ UNIQUE �ϸ� NOT NULL��
    FOREIGN KEY �ܷ�Ű �ٸ� ���̺��� PK�� �����ϴ� Ű 
*/
CREATE TABLE ex1_2 (
    mem_id VARCHAR2(100) NOT NULL UNIQUE
   ,mem_nm VARCHAR2(100)
   ,mem_email VARCHAR2(100) NOT NULL
   ,CONSTRAINT uq_ex1_2 UNIQUE(mem_email)   -- ���������� �̸��� �����ϰ� ������
);
INSERT INTO ex1_2 (mem_id, mem_email)
VALUES ('a001', 'a001@gmail.com'); -- default�� null ����̱⶧���� mem_nm �����.
INSERT INTO ex1_2 (mem_id, mem_email)
VALUES ('A001', 'A001@gmail.com');
INSERT INTO ex1_2 (mem_id)
VALUES ('b001');
SELECT *
FROM user_constraints
WHERE table_name ='EX1_2';
SELECT *
FROM ex1_2;
/*  ���� ������ Ÿ��(number)
    number(p, s) p�� �Ҽ����� �������� ��� ��ȿ���� �ڸ����� �ǹ���.
                 s�� �Ҽ��� �ڸ����� �ǹ���(����Ʈ0)
                 s�� 2�̸� �Ҽ��� 2�ڸ����� (�������� �ݿø���)
                 s�� ���� �̸� �Ҽ��� ���� ���� �ڸ��� ��ŭ �ݿø�
*/
CREATE TABLE ex1_3(
    num1 NUMBER(3)     -- ������ 3�ڸ�
   ,num2 NUMBER(3, 2)  -- ����1, �Ҽ���2
   ,num3 NUMBER(5, -2) -- ���� �ڸ����� ���ø� (�� 7�ڸ�)
   ,num4 NUMBER --38
);
INSERT INTO ex1_3 (num1) VALUES(0.7898);
INSERT INTO ex1_3 (num1) VALUES(99.5);
INSERT INTO ex1_3 (num1) VALUES(1004); --������.

INSERT INTO ex1_3 (num2) VALUES(0.7898);
INSERT INTO ex1_3 (num2) VALUES(1.7898);
INSERT INTO ex1_3 (num2) VALUES(9.9999); -- ���� 
INSERT INTO ex1_3 (num2) VALUES(32);     -- ����

INSERT INTO ex1_3 (num3) VALUES(12345.2345);
INSERT INTO ex1_3 (num3) VALUES(1234569.2345);
INSERT INTO ex1_3 (num3) VALUES(12345699.2345); -- ���� 7�ڸ� ����

INSERT INTO ex1_3 (num4) VALUES(14123493.34892340);
SELECT * FROM ex1_3;
/*
     ��¥ ������ Ÿ��(date ����Ͻú���, timestamp ����Ͻú���.�и���) 
     sysdate <--����ð�, systimestamp <-- ���� �и��ʱ��� 
*/
CREATE TABLE ex1_4(
     date1 DATE
    ,date2 TIMESTAMP
);
INSERT INTO ex1_4 VALUES (SYSDATE, SYSTIMESTAMP);
SELECT * FROM ex1_4;
/* check �������� */
CREATE TABLE ex1_5 (
     nm VARCHAR2(100)
    ,age NUMBER
    ,gender VARCHAR2(1)
    ,CONSTRAINT ck_ex1_5_age CHECK(age BETWEEN 1 AND 150)
    ,CONSTRAINT ck_ex1_5_gender CHECK(gender IN ('F','M'))
);
INSERT INTO  ex1_5 VALUES('�ؼ�', 10, 'M');
INSERT INTO  ex1_5 VALUES('�浿', 200, 'M');

CREATE TABLE dep(
   deptno NUMBER(3) PRIMARY KEY -- �⺻Ű 
  ,dept_nm VARCHAR2(20)
  ,dep_floor NUMBER(5)
);
CREATE TABLE emp (
  empno NUMBER(5) PRIMARY KEY  
 ,emp_nm VARCHAR2(20)
 ,title  VARCHAR2(20)           -- �ش� ���̺��� �÷��� �����ϰڴ�~
 ,dno NUMBER(3) CONSTRAINT emp_fk REFERENCES dep(deptno) -- �ܷ�Ű
);
INSERT INTO dep VALUES (1, '����', 8);
INSERT INTO dep VALUES (2, '��ȹ', 9);
INSERT INTO dep VALUES (3, '����', 10);
INSERT INTO emp VALUES(100, '�ؼ�', '�븮', 2);
INSERT INTO emp VALUES(200, '�浿', '����', 3);
INSERT INTO emp VALUES(300, '����', '����', 1);
--INSERT INTO emp VALUES(300, '����', '�̻�', 4); -- ������

SELECT *
FROM dep;
SELECT *
FROM emp;
delete dep;
SELECT *
FROM emp, dep
WHERE emp.dno = dep.deptno -- ����(���踦 �δ� ���)
AND emp.emp_nm = '�ؼ�';


delete  tb_info;

select *
from emp;
commit;


CREATE TABLE TB_INFO(
   INFO_NO	NUMBER(2) PRIMARY KEY
 , PC_NO		VARCHAR2(10) NOT NULL UNIQUE
 , NM		    VARCHAR2(20) NOT NULL
 , EMAIL		VARCHAR2(50) NOT NULL
 , HOBBY		VARCHAR2(1000)
 , TEAM	 	     NUMBER(2) 
 , CREATE_DT	 	DATE DEFAULT SYSDATE
 , UPDATE_DT	 	DATE DEFAULT SYSDATE
);










