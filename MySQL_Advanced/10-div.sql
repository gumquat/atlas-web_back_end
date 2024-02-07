-- create a function `SaveDiv` that divides and then
-- returns the first number by the second number,
-- or returns 0 if the second number is equal to 0
DELIMITER //

CREATE FUNCTION SafeDiv (a INT, b INT)
-- 
RETURNS FLOAT
BEGIN
    -- check if second number is 0
    IF b = 0 THEN
        RETURN 0;
    END IF;
    RETURN a / b; -- do the math!
END;
//

-- resetting the delimiter is good practice
-- going back annd change that in other problems now
DELIMITER ;