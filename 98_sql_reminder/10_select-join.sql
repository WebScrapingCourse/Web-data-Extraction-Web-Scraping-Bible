--CREATE TABLE PeopleInfo(
--    id int PRIMARY KEY,
--    animal VARCHAR(255),
--    married VARCHAR(255)
--);

--INSERT INTO PeopleInfo (id, animal, married) VALUES (32453532,'dog','yes');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (34254334,'cat','yes');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (45325234,'cat','no');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (23434320,'bird','yes');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (25423423,'cat','yes');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (45234324,'cat','no');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (45343455,'dog','yes');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (67456534,'dog','yes');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (67655888,'dog','yes');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (56655343,'dog','no');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (56775554,'dog','yes');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (36467676,'pig','no');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (24334667,'bird','no');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (30553465,'dog','no');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (40356457,'dog','no');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (50454367,'cat','no');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (30353422,'dog','yes');
--INSERT INTO PeopleInfo (id, animal, married) VALUES (40454577,'bird','no');

SELECT *
FROM PeopleBornIn95 AS t1
INNER JOIN PeopleInfo AS t2
ON t1.id = t2.id;

SELECT *
FROM PeopleBornIn95 AS t1
LEFT JOIN PeopleInfo AS t2
ON t1.id = t2.id;

SELECT * FROM PeopleBornIn95 AS t1
RIGHT JOIN PeopleInfo AS t2 ON t1.id = t2.id;

SELECT * FROM PeopleBornIn95 AS t1
FULL JOIN PeopleInfo AS t2 ON t1.id = t2.id;