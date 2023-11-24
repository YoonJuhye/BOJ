-- 코드를 입력하세요
with intack_id as 
(
    SELECT animal_id
    from animal_ins
    where sex_upon_intake like 'Intact%'
)

select a.animal_id, a.animal_type, a.name
from animal_outs a
join intack_id b
on a.animal_id = b.animal_id
where a.sex_upon_outcome like 'Neutered%' or a.sex_upon_outcome like 'Spayed%'
order by animal_id
