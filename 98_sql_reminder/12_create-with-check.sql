CREATE TABLE PeopleBornIn95(
    id int PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age int NOT NULL,
    CHECK (age<28),
    created TIMESTAMP,
);

SELECT * FROM UsersInfo WHERE User="Henry" Or fakecolumn="Mark";

