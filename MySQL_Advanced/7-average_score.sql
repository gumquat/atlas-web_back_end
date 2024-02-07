-- show average score
DELIMITER //

-- create a stored procedure named 'ComputeAverageScoreForUser'
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    -- hold the average score in an INT variable
    DECLARE avg_score FLOAT;
    -- calculate the average score of the user from the corrections table
    SELECT AVG(score) INTO avg_score FROM corrections WHERE corrections.user_id = user_id;
    -- update that user's (selected by user_id) table with the new score
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END;
//
DELIMITER ;
