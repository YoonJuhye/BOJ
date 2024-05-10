-- 코드를 작성해주세요
with size_rank as (
    select 
        id,
        ntile(4) over(order by size_of_colony) as size
    from ecoli_data
)

select 
    id, 
    case when size = 4 then 'CRITICAL'
        when size = 3 then 'HIGH'
        when size = 2 then 'MEDIUM'
        when size = 1 then 'LOW'
    end
    as colony_name
from size_rank
order by id