-- script that lists cities in db
SELECT id, name FROM cities JOIN states ON cities.id = states.state_id; 
