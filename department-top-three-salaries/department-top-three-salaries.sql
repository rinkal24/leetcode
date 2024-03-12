# Write your MySQL query statement below

SELECT
X.Department, 
X.Employee, 
X.Salary
FROM 
(
    SELECT d.name as Department, e.name as Employee , salary as Salary,
    DENSE_RANK()OVER(PARTITION BY d.id ORDER BY salary DESC) as rnk
    FROM Employee e
    JOIN Department d
        ON e.departmentId = d.id
    
)X
WHERE X.rnk <= 3

