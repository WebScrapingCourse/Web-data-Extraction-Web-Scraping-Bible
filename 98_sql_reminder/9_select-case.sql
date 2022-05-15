-- Let's suppose that 27  are actually 87 (typing errors).
-- I'd like to see a column with the real age!!
SELECT *, CASE
WHEN age = 27 THEN age+60
WHEN age < 27 THEN age
END AS realAGE
FROM PeopleBornIn95;


