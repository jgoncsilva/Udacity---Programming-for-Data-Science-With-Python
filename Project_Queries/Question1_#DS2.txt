/* Question 1 Set #2 
We want to find out how the two stores compare in their count of rental orders during every month for all the years 
we have data for. Write a query that returns the store ID for the store, the year and month and the number of rental
orders each store has fulfilled for that month. Your table should include a column for each of the following: year, month, 
store ID and count of rental orders fulfilled during that month.
*/

SELECT EXTRACT ('MONTH' FROM rental_date) AS rental_month, 
       EXTRACT ('YEAR' FROM rental_date) AS rental_year, 
       store_id, 
       COUNT(rental_id) AS count_rentals
  FROM rental r
            JOIN inventory i
            ON r.inventory_id = i.inventory_id
GROUP BY 1,2,3
ORDER BY count_rentals DESC;