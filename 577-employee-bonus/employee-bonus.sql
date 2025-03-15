# Write your MySQL query statement below
select  a.name,COALESCE(b.bonus, Null) AS bonus  from
Employee  a left join bonus b
on a.empid=b.empid
where b.bonus<1000 or b.bonus is Null;