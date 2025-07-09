# Write your MySQL query statement below
select u.name,IFNULL(SUM(r.distance), 0) as travelled_distance
from users u left join Rides r
on u.id=r.user_id
group by u.id,u.name
order by travelled_distance desc,name;
