# 1. What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, last name, email, and address

#Select customer.first_name, customer.last_name, customer.email, address.address from city
#JOIN address on city.city_id = address.city_id
#JOIN customer on address.address_id = customer.address_id
#Where city.city_id=312

#2. What query would you run to get all comedy films? Your query should return film title, description, release year, rating, special features, and genre (category).?

#select film.title, film.description, film.release_year, film.rating, film.special_features, category.name 
#from film
#Join film_category on film.film_id = film_category.film_id
#Join category on film_category.category_id = category.category_id
#where category.category_id = 5

#3. What query would you run to get all the films joined by actor_id=5? Your query should return the actor id, actor name, film title, description, and release year.

#select film.title, film.description, film.release_year, actor.actor_id, actor.first_name, actor.last_name
#from film
#Join film_actor on film.film_id = film_actor.film_id
#Join actor on film_actor.actor_id = actor.actor_id
#Where actor.actor_id = 5

#4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? Your query should return customer first name, last name, email, and address

#select customer.first_name, customer.last_name, customer.email, address.address, store.store_id, city.city_id
#from customer
#Join address on customer.address_id = address.address_id
#JOIN city on address.city_id = city.city_id
#join store on customer.store_id = store.store_id
#Where store.store_id = 1 and city.city_id IN (1,42,312,459)

#5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? Your query should return the film title, description, release year, rating, and special feature. Hint: You may use LIKE function in getting the 'behind the scenes' part.

#select film.title, film.description, film.release_year,film.rating,film.special_features
#from film
#Join film_actor on film.film_id = film_actor.film_id
#Join actor on film_actor.actor_id = actor.actor_id
#where actor.actor_id = 15 and film.rating = "G" and film.special_features like'%behind%'

#6. What query would you run to get all the actors that joined in the film_id = 369? Your query should return the film_id, title, actor_id, and actor_name.

#select film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name
#from film
#Join film_actor on film.film_id = film_actor.film_id
#Join actor on film_actor.actor_id = actor.actor_id
#where film.film_id = 369

#7. What query would you run to get all drama films with a rental rate of 2.99? Your query should return film title, description, release year, rating, special features, and genre (category).

#select film.title, film.description, film.release_year, film.special_features, category.name
#from film
#Join film_category on film.film_id = film_category.film_id
#Join category on film_category.category_id = category.category_id
#Where film.rental_rate = 2.99 and category.name = "drama"

#. What query would you run to get all the action films which are joined by SANDRA KILMER? Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.
#select film.title, film.description, film.release_year, film.rating, film.special_features, actor.first_name, actor.last_name, category.name
#from film
#Join film_actor on film.film_id = film_actor.film_id
#Join actor on film_actor.actor_id = actor.actor_id
#Join film_category on film.film_id = film_category.film_id
#Join category on film_category.category_id = category.category_id
#where actor.first_name = "Sandra" and actor.last_name="Kilmer"