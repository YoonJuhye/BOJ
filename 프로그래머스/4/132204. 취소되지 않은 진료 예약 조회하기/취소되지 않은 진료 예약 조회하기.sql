-- 코드를 입력하세요
SELECT a.APNT_NO, b.PT_NAME, b.PT_NO, a.MCDP_CD, c.DR_NAME, a.APNT_YMD
from APPOINTMENT a
join patient b
on a.pt_no = b.pt_no
join doctor c
on a.mddr_id = c.dr_id
where 
    a.MCDP_CD = 'CS' 
    and date_format(a.APNT_YMD, '%Y-%m-%d') = '2022-04-13' 
    and a.apnt_cncl_yn = 'N'
order by a.APNT_YMD