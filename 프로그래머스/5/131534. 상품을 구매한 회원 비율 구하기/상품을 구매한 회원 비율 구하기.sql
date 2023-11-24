-- 코드를 입력하세요
with all_cnt as (
    SELECT 
    count(distinct (user_id)) as cnt
    from user_info
    where joined like '2021-%'
)
select 
    year(a.sales_date) as YEAR, 
    month(a.sales_date) as MONTH, 
    count(distinct (a.user_id)) as PUCHASED_USERS,
    round(count(distinct (a.user_id))/(select cnt from all_cnt), 1) as PUCHASED_RATIO
from online_sale a
join user_info b
on a.user_id = b.user_id
where sales_date is not null and b.joined like '2021-%'
# where user_id in (
#     select user_id
#     from user_info
#     where joined like '2021-%'
group by YEAR, MONTH