-- 코드를 입력하세요
WITH RECURSIVE CTE AS(
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR+1 FROM CTE
    WHERE HOUR < 23
)

SELECT 
    b.HOUR as HOUR
    , count(a.ANIMAL_ID) as COUNT 
FROM ANIMAL_OUTS a
right join CTE b
on b.hour = HOUR(a.datetime)
group by b.HOUR
order by b.HOUR