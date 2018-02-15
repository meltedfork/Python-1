#Query 1. Find countries that speak slovene, percentage in descending order
#SELECT name, languages.language, languages.percentage from countries
#JOIN languages ON countries.id = country_id
#WHERE language="Slovene"
#ORDER by languages.percentage DESC;

#Query 2. Display total number of cities for each country. Return country name, total cities, arrange number of cities in descending order
#SELECT countries.name, count(cities.id) as city_count from countries
#JOIN cities on countries.id = cities.country_id
#GROUP by countries.name
#ORDER by  city_count desc

#Query 3. 3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order. 
#SELECT name, population from cities
#Where country_id=136 and population > 500000
#Order by population desc

#4. What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange the result by percentage in descending order.
#SELECT name, languages.language, languages.percentage from countries
#JOIN languages on countries.id = languages.country_id
#WHERE languages.percentage > 89.0
#ORDER by languages.percentage desc

#5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000
#Select name, surface_area, population from countries
#where surface_area < 501 and population > 100000

#6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years?
#Select name, government_form, life_expectancy, capital from countries
#Where government_form = "constitutional monarchy" and life_expectancy > 75 and capital > 200

#7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population?
#Select countries.name, cities.name, cities.district, cities.population from countries
#JOIN cities on countries.id = cities.country_id
#Where countries.name = "Argentina" and cities.district = "Buenos Aires" and cities.population > 500000

#8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. Also, the query should arrange the result by the number of countries in descending order. 
#select countries.name, countries.region, count(countries.id) as country_count from countries
#Group by region
#Order by country_count desc

