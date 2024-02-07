-- create a stored procedure `AddBonus` that
-- adds a new correction for a student

DELIMITER //

CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR (255), IN score INT)
BEGIN
    -- hold the project ID in an INT variable
    DECLARE project_id INT;
    -- select the project ID of the given project name
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    -- check if the project exists
    IF project_id IS NULL THEN
        -- if it doesnt exist, insert a new project with the given name
        INSERT INTO projects (name) VALUES (project_name);
        -- get the last inserted project's ID
        SET project_id = LAST_INSERT_ID();
END; //

DELIMITER;