-- 코드를 작성해주세요
with recursive cte as (
    select 
        ID,
        PARENT_ID,
        1 GENERATION
    from ecoli_data
    where parent_id is null
    
    union all
    
    select
        a.ID,
        a.PARENT_ID,
        b.GENERATION + 1
    from ecoli_data a
    join cte b
    on a.parent_id = b.id
)

select ID
from cte
where GENERATION = 3
order by id