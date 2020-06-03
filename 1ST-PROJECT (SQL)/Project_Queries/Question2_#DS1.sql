/* Question 2 Set #1 
Now we need to know how the length of rental duration of these family-friendly movies compares to the duration that all movies are rented for.
Can you provide a table with the movie titles and divide them into 4 levels (first_quarter, second_quarter, third_quarter, and final_quarter) based on the quartiles (25%, 50%, 75%) of the rental duration for movies across all categories?
Make sure to also indicate the category that these family-friendly movies fall into.
Answer: The question is rather ambiguous about how one subset of data (duration of these family-friendly movies) should be compared to another subset of data (duration that all movies are rented for). 
Below I provide 3 ways to answer the above question.
*/

SELECT f.title AS film_title,
       c.name  AS category_name,
       f.rental_duration ,
       NTILE(4) OVER (ORDER BY f.rental_duration) AS standard_quartile
  FROM film f
	  JOIN film_category fc 
          ON f.film_id = fc.film_id

	  JOIN category c 
          ON c.category_id = fc.category_id
  WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
ORDER BY 3;
