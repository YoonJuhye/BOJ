-- 코드를 입력하세요
SELECT MCDP_CD as "진료과코드", count(APNT_NO) as "5월예약건수" FROM APPOINTMENT

where left(APNT_YMD, 7) = "2022-05" 
# AND APNT_CNCL_YN != "Y"
group by MCDP_CD
order by count(APNT_NO), MCDP_CD 