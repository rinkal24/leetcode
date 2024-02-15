# Write your MySQL query statement below


SELECT
    (select DISTINCT salary 
    from Employee
    order by salary desc
    limit 1 OFFSET 1
     ) as SecondHighestSalary
    
 