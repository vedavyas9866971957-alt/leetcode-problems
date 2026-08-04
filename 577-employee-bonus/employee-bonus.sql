SELECT e.name, b.bonus 
FROM employee e 
LEFT JOIN bonus b ON e.empid = b.empid where b.bonus<1000 or b.bonus is null;
