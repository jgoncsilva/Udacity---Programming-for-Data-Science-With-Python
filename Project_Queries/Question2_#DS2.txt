/* Question 2 Set #2 
We would like to know who were our top 10 paying customers, how many payments they made on a monthly basis during 2007, 
and what was the amount of the monthly payments. Can you write a query to capture the customer name, month and year of 
payment, and total payment amount for each month by these top 10 paying customers?
*/

WITH t1 AS    (SELECT CONCAT(c.first_name, ' ', c.last_name) AS full_name,
                      SUM(p.amount) AS total_amount
	         FROM payment p
		   	JOIN customer c 
                        ON p.customer_id = c.customer_id
	       GROUP BY 1
               ORDER BY 2 DESC
               LIMIT 10)

SELECT DATE_TRUNC('month', p.payment_date) AS payment_month,
       CONCAT(c.first_name, ' ', c.last_name) AS full_name, 
       COUNT(p.amount) AS pay_count_per_month, 
       SUM(p.amount) AS pay_amount
  FROM payment p
 		JOIN customer c 
                ON c.customer_id = p.customer_id
 WHERE (p.payment_date BETWEEN '2007-01-01' AND '2008-01-01') 
   AND  CONCAT(c.first_name, ' ', c.last_name) 
    IN (SELECT full_name 
          FROM t1)
GROUP BY 2, 1 
ORDER BY 2, 1, 3;