# Write your MySQL query statement below
select a.id from weather a
join weather b on DATEDIFF(a.recordDate,b.recordDate)=1
where a.temperature>b.temperature;