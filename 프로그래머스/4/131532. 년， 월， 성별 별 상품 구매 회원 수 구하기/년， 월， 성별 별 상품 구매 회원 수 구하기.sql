-- 코드를 입력하세요
SELECT 
    YEAR(b.sales_date) as YEAR
    , MONTH(b.sales_date) as MONTH
    , a.gender as GENDER
    , count(distinct (a.user_id)) as USERS
from user_info a
join online_sale b
on a.user_id = b.user_id
where gender is not null
group by YEAR, MONTH, GENDER
# order by 