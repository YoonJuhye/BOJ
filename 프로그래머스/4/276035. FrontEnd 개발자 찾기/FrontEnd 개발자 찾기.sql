-- 코드를 작성해주세요
select id, email, first_name, last_name
from developers a
where skill_code & (select sum(code) from skillcodes where category = 'Front End')
order by id