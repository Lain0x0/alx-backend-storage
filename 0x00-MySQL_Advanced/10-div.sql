-- using math to create safediv function

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT DETERMINISTIC
BEGIN
    IF B != 0 THEN
        RETURN a / b;
    ELSE
	RETURN 0;
    END IF;
END $$
DELIMITER;
