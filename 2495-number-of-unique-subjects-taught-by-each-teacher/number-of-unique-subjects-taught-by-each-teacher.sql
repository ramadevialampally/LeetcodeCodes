# Write your MySQL query statement below
select teacher_id,Count(Distinct(subject_id)) as cnt
from teacher
group by teacher_id;
