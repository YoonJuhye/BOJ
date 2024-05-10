-- 코드를 작성해주세요
-- 1. 보유 형질을 구한다. 10진수에서 2진수 변환, 자리 확인 
-- 2. 부모를 찾는다.
-- 3. 부모의 형질을 구한다.
-- 4. 보유 형질과 부모의 형질을 비교한다. 모두 보유한 컬럼만 출력
select a.id, 
    a.genotype, 
    b.genotype as parent_genotype 
from ecoli_data a
join ecoli_data b
on a.parent_id = b.id
where a.genotype & b.genotype = b.genotype
order by a.id

