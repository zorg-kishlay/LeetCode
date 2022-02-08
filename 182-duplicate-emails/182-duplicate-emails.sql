# Write your MySQL query statement below

SELECT email as Email from 
(Select email, count(email) as c from Person group by email) as temp
where c>1
