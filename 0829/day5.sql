/*
    집계함수와 그룹바이절 
    집계함수 대상 데이터에 대해 총합, 평균, 최댓값, 최솟값 등을 구하는 함수
    그룹바이 절 대상 데이터를 특정그룹으로 묶는 방법
*/
-- COUNT 로우 수를 반환하는 집계함수.
SELECT COUNT(*)                      -- null 포함
    ,  COUNT(department_id)          --default ALL
    ,  COUNT(ALL department_id)      --중복 포함, null x
    ,  COUNT(DISTINCT department_id) --중복 제거 
    ,  COUNT(employee_id)            -- employees테이블의 pk (*) 같음
FROM employees;

SELECT SUM(salary)          as 합계
    ,  MAX(salary)          as 최대
    ,  MIN(salary)          as 최소
    ,  ROUND(AVG(salary),2) as 평균
    ,  COUNT(employee_id)   as 직원수
FROM employees; -- <-- 집계 대상 

SELECT department_id
    ,  SUM(salary)          as 합계
    ,  MAX(salary)          as 최대
    ,  MIN(salary)          as 최소
    ,  ROUND(AVG(salary),2) as 평균
    ,  COUNT(employee_id)   as 직원수
FROM employees           -- 직원 테이블의 
WHERE department_id IS NOT NULL -- 검색조건이 있다면 FROM 사이에 GROUP
AND department_id IN (30,60,90)      
GROUP BY department_id   -- 부서 별 (그룹으로 집계)
ORDER BY 1;

-- 회원수와 마일리지 합계,마일리지 평균(소수점 둘째자리까지)을 출력하시오 
SELECT *
FROM member;

SELECT COUNT(*)
     , COUNT(mem_id) as 회원수
     , SUM(mem_mileage) as 마일리지합계
     , ROUND(AVG(mem_mileage),2) as 마일리지평균
FROM member;
-- 직업별 회원수와 마일리지 합계,평균 출력(마일리지 합계 내림차순)


SELECT mem_job as 직업
     , COUNT(mem_id) as 회원수
     , SUM(mem_mileage) as 마일리지합계
     , ROUND(AVG(mem_mileage),2) as 마일리지평균
FROM member
GROUP BY mem_job
ORDER BY 3 DESC;

-- ROWNUM 의사컬럼 테이블에는 없지만 있는것 처럼 사용가능
SELECT  ROWNUM as rnum
      , mem_name
FROM member
WHERE ROWNUM <= 10;

-- HAVING 집계 결과에 대해서 검색조건을 추가하고싶을때 사용
--ex) 직업별 마일리지 합계가 10000 이상 
SELECT mem_job as 직업
     , COUNT(mem_id) as 회원수
     , SUM(mem_mileage) as 마일리지합계
     , ROUND(AVG(mem_mileage),2) as 마일리지평균
FROM member
GROUP BY mem_job
HAVING SUM(mem_mileage) >= 10000 -- 집계결과에 검색조건 
ORDER BY 3 DESC;

-- kor_loan_status(java계정) 테이블의 loan_jan_amt(대출액)
-- 2013년도 기간별, 지역별 총 대출잔액을 출력하시오 
SELECT SUBSTR(period,1,4) as 년도
     , region             as 지역
     , SUM(loan_jan_amt)  as 대출합
FROM kor_loan_status
--WHERE period LIKE '2013%';
WHERE SUBSTR(period,1,4) = '2013'
GROUP BY SUBSTR(period,1,4), region;
-- 2013년도 지역별, 구분별 합계
SELECT SUBSTR(period,1,4) as 년도
     , region             as 지역
     , gubun              as 구분
     , SUM(loan_jan_amt)  as 대출합
FROM kor_loan_status
WHERE SUBSTR(period,1,4) = '2013'
GROUP BY SUBSTR(period,1,4), region, gubun
ORDER BY 2;

-- 지역별 대출의 합계가 200000 이상인 결과를 출력하시오 
-- 대출잔액 내림차순
SELECT region             as 지역
     , SUM(loan_jan_amt)  as 대출합
FROM kor_loan_status
GROUP BY region
HAVING SUM(loan_jan_amt) >= 200000
ORDER BY 2 DESC;



-- 대전, 서울, 부산의 
-- 년도별 대출의 합계에서 
-- 대출의 합이 60000 넘는 결과를 출력하시오
-- 정렬 지역 오름차순, 대출합 내림차순
SELECT SUBSTR(period, 1, 4) as 년도
     , region
     , SUM(loan_jan_amt)    as 대출합계
FROM kor_loan_status
WHERE region IN ('대전','서울','부산')
GROUP BY SUBSTR(period, 1, 4), region
HAVING SUM(loan_jan_amt) >= 60000
ORDER BY 2, 3 DESC;



-- employees 직원들의 입사년도별 직원수를 출력하시오 
-- hire_date 사용 (정렬 년도 오름차순)
SELECT TO_CHAR(hire_date,'YYYY') 년도
    ,  COUNT(*) as 직원수
FROM employees
GROUP BY TO_CHAR(hire_date,'YYYY')
ORDER BY 1;
--10명이상 입사한 년도 
SELECT TO_CHAR(hire_date,'YYYY') 년도
    ,  COUNT(*) as 직원수
FROM employees
GROUP BY TO_CHAR(hire_date,'YYYY')
HAVING COUNT(*) >= 10
ORDER BY 1;



-- customers 회원의 전체 회원수, 남자 회원수, 여자 회원수를 출력하시오
-- 남자, 여자라는 컬럼음 없음. 
-- customers 테이블의 컬럼을 활용해서 만들어야함. 
SELECT COUNT(cust_gender) as 전체 
     , COUNT(DECODE(cust_gender,'F','여자')) as 여자
     , SUM(DECODE(cust_gender,'F',1, 0)) as 여자2
     , COUNT(DECODE(cust_gender,'M','남자')) as 남자
     , SUM(DECODE(cust_gender,'M',1, 0)) as 남자2
FROM customers;







SELECT SUM(DECODE(cust_gender, 'F', 1, 0)) as 여자 
     , SUM(DECODE(cust_gender, 'M', 1, 0)) as 남자 
     , COUNT(cust_gender) as 전체
FROM customers;

SELECT COUNT(DECODE(cust_gender, 'F', '여자')) as 여자 
     , COUNT(DECODE(cust_gender, 'M', '남자')) as 남자 
     , COUNT(cust_gender) as 전체
FROM customers;

SELECT TO_CHAR(hire_date,'YYYY') as 년도
     , COUNT(*) as 직원수
FROM employees
GROUP BY TO_CHAR(hire_date,'YYYY')
ORDER BY 년도;



--1.요일별 직원의 고용직원의 수를 출력하시오 
--  일요일 부터 ~ (employees, hire_date)사용

SELECT NVL(DECODE(TO_CHAR(hire_date,'d'),1,'일',2,'월',3,'화'
                             ,4,'수',5,'목',6,'금',7,'토'),'총계') as 요일
     , COUNT(*) as 입사직원수
FROM employees
GROUP BY ROLLUP(TO_CHAR(hire_date,'d'))
ORDER BY TO_CHAR(hire_date,'d');

SELECT NVL(TO_CHAR(hire_date,'day'),'총계') as 요일
     , COUNT(*) as 입사직원수
FROM employees
GROUP BY TO_CHAR(hire_date,'day');


--2.년도별 요일의 고용인원수를 출력하시오
--(employees, hire_date)사용
-- 정렬 년도 오름차순

SELECT TO_CHAR(hire_date,'YYYY') as yyyy
      ,SUM(DECODE(TO_CHAR(hire_date,'d'),'1',1, 0)) as sun
      ,COUNT(*) as 년도별고용직원합계
FROM employees
GROUP BY TO_CHAR(hire_date,'YYYY')
ORDER BY 1;


-- 집합 연산자 UNION ------------------------------------------------------------------------

CREATE TABLE exp_goods_asia (
       country VARCHAR2(10),
       seq     NUMBER,
       goods   VARCHAR2(80));

INSERT INTO exp_goods_asia VALUES ('한국', 1, '원유제외 석유류');
INSERT INTO exp_goods_asia VALUES ('한국', 2, '자동차');
INSERT INTO exp_goods_asia VALUES ('한국', 3, '전자집적회로');
INSERT INTO exp_goods_asia VALUES ('한국', 4, '선박');
INSERT INTO exp_goods_asia VALUES ('한국', 5,  'LCD');
INSERT INTO exp_goods_asia VALUES ('한국', 6,  '자동차부품');
INSERT INTO exp_goods_asia VALUES ('한국', 7,  '휴대전화');
INSERT INTO exp_goods_asia VALUES ('한국', 8,  '환식탄화수소');
INSERT INTO exp_goods_asia VALUES ('한국', 9,  '무선송신기 디스플레이 부속품');
INSERT INTO exp_goods_asia VALUES ('한국', 10,  '철 또는 비합금강');

INSERT INTO exp_goods_asia VALUES ('일본', 1, '자동차');
INSERT INTO exp_goods_asia VALUES ('일본', 2, '자동차부품');
INSERT INTO exp_goods_asia VALUES ('일본', 3, '전자집적회로');
INSERT INTO exp_goods_asia VALUES ('일본', 4, '선박');
INSERT INTO exp_goods_asia VALUES ('일본', 5, '반도체웨이퍼');
INSERT INTO exp_goods_asia VALUES ('일본', 6, '화물차');
INSERT INTO exp_goods_asia VALUES ('일본', 7, '원유제외 석유류');
INSERT INTO exp_goods_asia VALUES ('일본', 8, '건설기계');
INSERT INTO exp_goods_asia VALUES ('일본', 9, '다이오드, 트랜지스터');
INSERT INTO exp_goods_asia VALUES ('일본', 10, '기계류');

