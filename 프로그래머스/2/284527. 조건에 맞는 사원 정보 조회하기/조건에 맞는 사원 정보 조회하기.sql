-- 코드를 작성해주세요
select sum(score) as score, b.emp_no, emp_name, position, email
from hr_department a
join hr_employees b
on a.dept_id = b.dept_id
join hr_grade c
on b.emp_no = c.emp_no
group by b.emp_no
order by score desc
limit 1
