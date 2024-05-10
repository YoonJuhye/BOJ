-- 코드를 작성해주세요
with all_grade as (
    select emp_no, avg(score) as score
    from hr_grade
    group by emp_no
)
select 
    a.emp_no, 
    emp_name,
    case 
        when score >= 96 then 'S'
        when score >= 90 then 'A'
        when score >= 80 then 'B'
        else 'C'
    end as grade,
    case 
        when score >= 96 then sal * 0.2
        when score >= 90 then sal * 0.15
        when score >= 80 then sal * 0.1
        else 0
    end as bonus
from all_grade a
join hr_employees b
on a.emp_no = b.emp_no
order by a.emp_no
