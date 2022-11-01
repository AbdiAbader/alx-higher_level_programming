-- full creation
SELECT INTO second_table FROM (VALUES(1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8)) as (id, name, score);