/* Question 3 Set #1 
Finally, provide a table with the family-friendly film category, each of the quartiles, and the corresponding count of movies within each combination of film category for each corresponding rental duration category.
*/

SELECT category_name,
       standard_quartile,
       COUNT(standard_quartile)
  FROM
	     (SELECT f.title AS film_title, 
             	     c.name AS category_name, 
	             f.rental_duration,
                     NTILE(4) OVER (ORDER BY f.rental_duration) AS standard_quartile
                FROM film f
    			JOIN film_category fc 
                        ON f.film_id = fc.film_id

    			JOIN category c 
                        ON c.category_id = fc.category_id
    	      WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
              ORDER BY 3) sub1        
GROUP BY 1, 2
ORDER BY 1, 2;