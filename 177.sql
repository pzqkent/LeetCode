CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      # select IFNULL((select distinct salary from employee order by salary desc limit N,1),NULL)
      SELECT IFNULL((
        SELECT DISTINCT salary 
        FROM employee 
        ORDER BY salary DESC 
        LIMIT 1 OFFSET N),NULL)
      
  );
END