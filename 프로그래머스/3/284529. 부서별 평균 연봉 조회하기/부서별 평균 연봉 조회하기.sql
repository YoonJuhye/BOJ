-- 코드를 작성해주세요
select 
    a.dept_id, 
    dept_name_en,
    round(avg(sal), 0) as AVG_SAL
    # a.dept_id, dept_name_kr, emp_no, emp_name
from hr_department a
join hr_employees b
on a.dept_id = b.dept_id
group by a.dept_id
order by avg_sal desc