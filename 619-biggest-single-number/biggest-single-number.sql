# Write your MySQL query statement below
Select Max(num) as num from
myNumbers
where num in (select num from myNumbers
group by num
having count(num)=1);