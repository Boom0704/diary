-- DECODE 표현식 
SELECT cust_name
     , cust_gender
     --       (대상컬럼, 조건1, true일때)
     , DECODE(cust_gender, 'M', '남자') as gender
     --       (대상컬럼, 조건1, true일때, 그밖에)
     , DECODE(cust_gender, 'M', '남자', '여자') as gender
     --       (대상컬럼, 조건1, true일때, 조건2, true일때)
     , DECODE(cust_gender, 'M', '남자', 'F', '여자') as gender
     , DECODE(cust_gender, 'M', '남자', 'F', '여자', '?') as gender
FROM customers;

SELECT mem_name, mem_regno2
     , DECODE(SUBSTR(mem_regno2,1,1),'1','남자','2','여자') as gender
FROM member;

/*  변환함수(타입) 타입변환 많이함.***
    TO_CHAR 문자형으로
    TO_DATE 날짜형으로
    TO_NUMBER 숫자형으로 
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
      -- RR은 세기를 자동으로 추적 50 -> 1950, 49 -> 2049
      -- Y2K 2000년 문제에 대한 대응책으로 도입됨.
      ,TO_DATE('50', 'RR') as ex5
FROM dual;
CREATE TABLE ex4_1(
     title VARCHAR2(100)
    ,d_day DATE
);
INSERT INTO ex4_1 VALUES('시작일','20240802');
INSERT INTO ex4_1 VALUES('종료일','2025.01.17');

INSERT INTO ex4_1 VALUES('탄소교육','2024 09 04');
INSERT INTO ex4_1 VALUES('회식','2024 09 06 18:05:00'); -- 오류남
INSERT INTO ex4_1 
VALUES('회식',TO_DATE('2024 09 06 18:05:00','YYYY MM DD HH24:MI:SS'));
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

-- member 회원의 생년월일을 이용하여 나이를 계산하시오 
-- 올해년도를 이용하여 (ex 2024 - 2000 -> 24세) 
-- 정렬은 나이 내림차순
SELECT mem_name, mem_bir
     , TO_CHAR(mem_bir,'YYYY') 
     , TO_CHAR(SYSDATE,'YYYY')
     , TO_CHAR(SYSDATE,'YYYY')- TO_CHAR(mem_bir,'YYYY') ||'세' as age
FROM member
ORDER BY mem_bir ASC;
SELECT 1
FROM member;
/* 숫자 함수 (매개변수 숫자형)
   ABS:절대값, ROUND:반올림, TRUNC:버림, CEIL:올림, MOD:나머지값, SQRT:제곱근*/
SELECT ABS(-10) as ex1
     , ABS(10)  as ex2
     , ROUND(10.5555, 1) as ex3
     , ROUND(10.5555)    as ex4
     , TRUNC(10.5555,1)  as ex5
     , CEIL(10.5555)     as ex6
     , MOD(4, 2)         as ex7
     , MOD(5, 2)         as ex8
FROM dual;
/* 날짜 함수 */ 
-- ADD_MONTHS(날짜데이터, 1)  다음달 
-- LAST_DAY 마지막날, NEXT_DAY 다음오는 요일 
SELECT ADD_MONTHS(SYSDATE, 1)     as ex1 -- 다음달
     , ADD_MONTHS(SYSDATE,-1)     as ex2 -- 전달
     , LAST_DAY(SYSDATE)          as ex3 -- 이번달 마지막날
     , NEXT_DAY(SYSDATE, '화요일') as ex4
     , NEXT_DAY(SYSDATE, '수요일') as ex5
FROM dual;
SELECT SYSDATE - 1  as ex1  -- 어제 
    ,  ADD_MONTHS(SYSDATE,1) - ADD_MONTHS(SYSDATE, -1) as ex2
FROM dual;

SELECT mem_name, mem_bir
 , sysdate - mem_bir
 , TO_CHAR(sysdate,'YYYYMMDD') -  TO_CHAR(mem_bir,'YYYYMMDD') as ex1 --숫자계산
 , TO_DATE(TO_CHAR(sysdate,'YYYYMMDD')) 
     - TO_DATE(TO_CHAR(mem_bir,'YYYYMMDD')) as ex2 --날짜계산 
FROM member;

-- 이번달은 몇일 남았을까요? 
-- 회식까지 몇일 ?

SELECT LAST_DAY(SYSDATE) - SYSDATE as 이번달
     , TO_DATE('20240906') - TO_DATE(TO_CHAR(SYSDATE,'YYYYMMDD')) as 회식까지
FROM dual;

-- DISTINCT 중복된 데이터를 제거하고 고유한 값을 반환(특정 컬럼의 고유한 값만 보고싶을때)
SELECT DISTINCT mem_job
FROM member;

SELECT DISTINCT mem_job, mem_like
     --행 조합이 중복되지 않는 행만 반환
FROM member;

--SELECT DISTINCT prod_category, prod_subcategory
--FROM products
--ORDER BY 1;


-- NVL(컬럼, 변환값)
SELECT emp_name
     , salary
     , commission_pct
     , salary + (salary * commission_pct) as 상여포함
     , salary + (salary * NVL(commission_pct, 0) ) as 상여포함2
FROM employees;

-- 직원중 근속년수가 25년 이상인 직원만 출력하시오 ! (근속년수 내림차순)
SELECT emp_name, hire_date
     , TO_CHAR(hire_date, 'YYYY')
     , TO_CHAR(SYSDATE, 'YYYY')
     , TO_CHAR(SYSDATE, 'YYYY') - TO_CHAR(hire_date, 'YYYY') as 근속년수
FROM employees
WHERE TO_CHAR(SYSDATE, 'YYYY') - TO_CHAR(hire_date, 'YYYY') >= 25
ORDER BY 근속년수 DESC;

 /*
 고객 테이블(CUSTOMERS)에는 
 고객의 출생년도(cust_year_of_birth) 컬럼이 있다. 
  현재일 기준으로 이 컬럼을 활용해 30대, 40대, 50대를 구분해 출력하고, 
 나머지 연령대는 '기타'로 출력하는 쿼리를 작성해보자. 
 ( 1990년 이상 출생 ) 정렬은 연령 오름차순
 */
 


SELECT CUST_YEAR_OF_BIRTH
       ,(TO_CHAR(SYSDATE, 'YYYY')  - CUST_YEAR_OF_BIRTH ) as 나이
--     , TRUNC((TO_CHAR(SYSDATE, 'YYYY')  - CUST_YEAR_OF_BIRTH ) / 10)
     , DECODE(TRUNC((TO_CHAR(SYSDATE, 'YYYY')  - CUST_YEAR_OF_BIRTH ) / 10), 3
                      ,'30대'
                      , 4,'40대', 5,'50대', '기타')  as 연령대
FROM customers
WHERE cust_gender = 'M'
AND cust_marital_status = 'single'
AND CUST_YEAR_OF_BIRTH <= 1990
ORDER BY CUST_YEAR_OF_BIRTH DESC;












SELECT emp_name
     , hire_date
     ,TO_CHAR(SYSDATE, 'YYYY') -  TO_CHAR(hire_date, 'YYYY') as 근속년수
FROM employees
WHERE TO_CHAR(SYSDATE, 'YYYY') -  TO_CHAR(hire_date, 'YYYY') >=25
ORDER BY 근속년수 desc;



















