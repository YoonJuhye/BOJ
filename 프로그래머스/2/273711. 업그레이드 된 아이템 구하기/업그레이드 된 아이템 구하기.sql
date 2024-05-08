# -- 코드를 작성해주세요
select A.item_id, A.item_name, A.rarity from item_info A
join item_tree B
on A.item_id = B.item_id
where B.parent_item_id in (
    select item_id from item_info
    where rarity = "RARE"
    )
order by A.item_id desc