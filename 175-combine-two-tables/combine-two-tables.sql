# Write your MySQL query statement below
select a.firstName,a.lastName,b.city,b.state
from person a left Join address b on a.personId=b.personid;