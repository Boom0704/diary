CREATE TABLE ex2_1(
     col1 VARCHAR2(100)
    ,col2 NUMBER
    ,col3 DATE
);
-- INSERT ������ ����
-- ���1.�⺻���� �÷��� �ۼ�
INSERT INTO ex2_1 (col1, col2, col3)
VALUES('nick', 10, sysdate);   
--���ڿ� Ÿ���� '' ���ڴ� �׳� ���� ������ ���ڿ��ε� ���ڶ�� ����
INSERT INTO ex2_1 (col1, col2, col3)
VALUES('jack', '10', sysdate); 
SELECT  * FROM ex2_1;
--Ư�� �÷����� �����Ҷ��� ������ �÷��� �����.
INSERT INTO ex2_1 (col1)
VALUES('judy');
-- ���2.���̺� �ִ� ��ü �÷��� �����Ҷ��� �Ƚᵵ��.
INSERT INTO ex2_1 VALUES('�ؼ�', 10, sysdate);
-- ���3.SELECT ~ INSERT ��ȸ ����� ����
INSERT INTO ex2_1 (col1)
SELECT emp_name 
FROM employees; 

-- UPDATE ������ ���� 
UPDATE ex2_1 
SET col3 = sysdate;  -- set ���� �����ϰ����ϴ� ������ 
-- where���� ������ ���̺� ��ü ������Ʈ ��.
UPDATE ex2_1
SET col2 = 20
  , col3 = sysdate     -- ���� �÷��� ������ , <-- 
WHERE col1 = 'nick';    
COMMIT;    -- �����̷� �ݿ�
ROLLBACK;  -- �����̷� ���

-- DELETE ������ ���� 
DELETE ex2_1;  -- ���̺� ���� ��ü ����
-- delete�� update�� ���� �˻����� �߿���
DELETE ex2_1
WHERE col1 ='nick'; -- �ش� ������ �����ϴ� ���� ����.
-- �������ǵ� ���� �� ���̺� ���� 
DROP TABLE dep CASCADE CONSTRAINTS; 

--��� ������ *+/- 
--���� ������ (���ڿ� ���ϱ�) 
SELECT employee_id  || '-' || emp_name as emp_info
FROM employees;
-- �� ������ : >,<,>=,<=,=,<>,!=,^= 
SELECT * FROM employees WHERE salary = 2600;  --����
SELECT * FROM employees WHERE salary <> 2600; --���� �ʴ�
SELECT * FROM employees WHERE salary != 2600; --���� �ʴ�
SELECT * FROM employees WHERE salary ^= 2600; --���� �ʴ�
SELECT * FROM employees WHERE salary > 2600;  --�ʰ�
SELECT * FROM employees WHERE salary < 2600;  --�̸�
SELECT * FROM employees WHERE salary <= 2600; --����
SELECT * FROM employees WHERE salary >= 2600; --�̻�














