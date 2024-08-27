CREATE TABLE ex2_1(
     col1 VARCHAR2(100)
    ,col2 NUMBER
    ,col3 DATE
);
-- INSERT 데이터 삽입
-- 방법1.기본형태 컬럼명 작성
INSERT INTO ex2_1 (col1, col2, col3)
VALUES('nick', 10, sysdate);   
--문자열 타입은 '' 숫자는 그냥 숫자 하지만 문자열인데 숫자라면 가능
INSERT INTO ex2_1 (col1, col2, col3)
VALUES('jack', '10', sysdate); 
SELECT  * FROM ex2_1;
--특정 컬럼에만 삽입할때는 무조건 컬럼명 써야함.
INSERT INTO ex2_1 (col1)
VALUES('judy');
-- 방법2.테이블에 있는 전체 컬럼에 삽입할때는 안써도됨.
INSERT INTO ex2_1 VALUES('팽수', 10, sysdate);
-- 방법3.SELECT ~ INSERT 조회 결과를 삽입
INSERT INTO ex2_1 (col1)
SELECT emp_name 
FROM employees; 

-- UPDATE 데이터 수정 
UPDATE ex2_1 
SET col3 = sysdate;  -- set 에는 수정하고자하는 데이터 
-- where절이 없으면 테이블 전체 업데이트 됨.
UPDATE ex2_1
SET col2 = 20
  , col3 = sysdate     -- 수정 컬럼이 많으면 , <-- 
WHERE col1 = 'nick';    
COMMIT;    -- 변경이력 반영
ROLLBACK;  -- 변경이력 취소

-- DELETE 데이터 삭제 
DELETE ex2_1;  -- 테이블 내용 전체 삭제
-- delete도 update와 같이 검색조건 중요함
DELETE ex2_1
WHERE col1 ='nick'; -- 해당 조건이 만족하는 행을 삭제.
-- 제약조건도 삭제 후 테이블 삭제 
DROP TABLE dep CASCADE CONSTRAINTS; 

--산술 연산자 *+/- 
--문자 연산자 (문자열 더하기) 
SELECT employee_id  || '-' || emp_name as emp_info
FROM employees;
-- 논리 연산자 : >,<,>=,<=,=,<>,!=,^= 
SELECT * FROM employees WHERE salary = 2600;  --같다
SELECT * FROM employees WHERE salary <> 2600; --같지 않다
SELECT * FROM employees WHERE salary != 2600; --같지 않다
SELECT * FROM employees WHERE salary ^= 2600; --같지 않다
SELECT * FROM employees WHERE salary > 2600;  --초과
SELECT * FROM employees WHERE salary < 2600;  --미만
SELECT * FROM employees WHERE salary <= 2600; --이하
SELECT * FROM employees WHERE salary >= 2600; --이상














