# Write your MySQL query statement below
update salary
set sex=Case
    when sex='m' Then 'f'
    when sex='f' then 'm'
    end;
