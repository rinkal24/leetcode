# Write your MySQL query statement below
SELECT c.name as Customers
FROM Customers c
LEFT JOIN Orders o
on c.id = o.customerid
where o.id IS NULL
