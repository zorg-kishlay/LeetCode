# Write your MySQL query statement below

# SELECT email as Email from 
# (Select email, count(email) as c from Person group by email) as temp
# where c>1

# Or using Having clause


Select email from Person 
group by email
Having count(email) > 1

