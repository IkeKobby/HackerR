- Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).;
        - `SELECT COALESCE(
        (SELECT DISTINCT Salary
        FROM Employee
        WHERE Salary < (SELECT MAX(Salary) FROM Employee)
        ORDER BY Salary DESC
        LIMIT 1),
        null
    ) AS SecondHighestSalary;`

- Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.
        CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
        BEGIN
        RETURN (
            # Write your MySQL query statement below.
            select coalesce(
                        (select temp_table.salary from 
                            (select distinct salary from Employee order by salary desc limit N) as temp_table 
                            order by temp_table.salary asc 
                            limit 1
                        ), 
                        null
                    ) as NthHighestSalary
        );
        END


