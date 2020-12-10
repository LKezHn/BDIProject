--- -------------------------------------------------------------
--- @authors eglopezl@unah.hn lemartinezm@unah.hn
--- -------------------------------------------------------------
------------------------------------------------------------------
------------------------------------------------------------------
--                 PROCEDURES BASE DE DATOS "A"                 --
------------------------------------------------------------------
------------------------------------------------------------------
USE Drawings;

SET @authID = 0;

DELIMITER $$
  -- -----------------------------------------------------
  -- Get all the users
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_getAllUsers$$
  CREATE PROCEDURE sp_getAllUsers()
  BEGIN
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1; 
    SELECT 
      User.id AS "id", AES_DECRYPT(UNHEX(User.str_userName),@key),
      AES_DECRYPT(UNHEX(User.str_password),@key), 
      Roles.str_name AS "Rol", 
      (SELECT COUNT(*) FROM Drawing JOIN User AS SubUser ON Drawing.id_user = SubUser.id WHERE User.id = SubUser.id) 
    FROM User JOIN Roles ON User.id_role = Roles.id WHERE User.id NOT IN (1);
  END$$
  
  DROP PROCEDURE IF EXISTS sp_visualizeUserList$$

  CREATE PROCEDURE sp_visualizeUserList(IN idUser INT) BEGIN
    INSERT INTO Binnacle(id_user, str_command) VALUES (idUser, "visualizeUserList");
  END$$

  -- -----------------------------------------------------
  -- Get one user
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_getUser$$
  CREATE PROCEDURE sp_getUser(IN id_user TEXT)
  BEGIN
    DECLARE id INT DEFAULT 0;
    DECLARE user TEXT DEFAULT "";
    DECLARE user_role INT DEFAULT 0;
    SELECT User.id, User.str_userName, User.id_role INTO id, user, user_role FROM User WHERE User.id = id_user;
    SELECT id, user, user_role;
  END$$
  
  -- -----------------------------------------------------
  -- Register authentication
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_isAuth$$
  CREATE PROCEDURE sp_isAuth(IN idUser INT)
  BEGIN
    SET @authID = idUser;
    INSERT INTO Binnacle(id_user, str_command) VALUES(idUser, "auth");
  END$$

  -- -----------------------------------------------------
  -- Get user password
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_authUser$$
  CREATE PROCEDURE sp_authUser(IN username TEXT)
  BEGIN
    DECLARE user_password TEXT DEFAULT "None";
    DECLARE id_user INT DEFAULT 0;
    
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;

    IF STRCMP(username, "admin") = 0 THEN
      SELECT 
        User.str_password, User.id 
      INTO 
        user_password, id_user 
      FROM 
        User
      WHERE AES_DECRYPT(UNHEX(User.str_userName),@key) = username;
    ELSE
      SELECT 
        AES_DECRYPT(UNHEX(User.str_password), @key), User.id 
      INTO 
        user_password, id_user 
      FROM User WHERE AES_DECRYPT(UNHEX(User.str_userName),@key) = username;
    END IF;

    SELECT id_user, user_password;
  END$$

  -- -----------------------------------------------------
  -- Get user username
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_authUserName$$

  CREATE PROCEDURE sp_authUserName(IN auth_username TEXT)
  BEGIN
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;

    SELECT 
      AES_DECRYPT(UNHEX(User.str_userName),@key) 
    FROM 
      User
    WHERE AES_DECRYPT(UNHEX(User.str_userName), @key) = auth_username;
  END$$  
  -- -----------------------------------------------------
  -- Add a new user
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_addUser$$
  
  CREATE PROCEDURE sp_addUser(IN new_username TEXT, IN new_password TEXT, IN new_idrole INT)
  BEGIN
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;
    
    INSERT INTO
      User(id_role, str_userName, str_password)
    VALUES
      (new_idrole, HEX(AES_ENCRYPT(new_username,@key)), HEX(AES_ENCRYPT(new_password,@key)));
  END$$

  -- -----------------------------------------------------
  -- Modify user's info
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_updateUserInfo$$

  CREATE PROCEDURE sp_updateUserInfo(IN username_user TEXT, IN new_username TEXT, IN new_password TEXT)
  BEGIN
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;

    UPDATE User SET
      str_userName = HEX(AES_ENCRYPT(new_username, @key)),
      str_password = HEX(AES_ENCRYPT(new_password, @key))
    WHERE AES_DECRYPT(UNHEX(User.str_userName), @key) = username_user;
  END$$
  -- -----------------------------------------------------
  -- Delete an user
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_deleteUser$$
  
  CREATE PROCEDURE sp_deleteUser(IN user_username TEXT)
  BEGIN
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;

    DELETE FROM User WHERE AES_DECRYPT(UNHEX(User.str_userName),@key) = user_username;
  END$$
  
  -- -----------------------------------------------------
  -- Get name and id of all the drawings
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_getDrawingList$$
  
  CREATE PROCEDURE sp_getDrawingList()
  BEGIN
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;

    SELECT 
      Drawing.id, 
      AES_DECRYPT(UNHEX(Drawing.str_name),@key), AES_DECRYPT(UNHEX(User.str_userName),@key) 
    FROM 
      Drawing
    JOIN User ON Drawing.id_user = User.id;
  END$$
  
  -- -----------------------------------------------------
  -- Get name and id of all the drawings of an user
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_getUserDrawingList$$
  
  CREATE PROCEDURE sp_getUserDrawingList(IN id_user INT)
  BEGIN
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;
    
    SELECT
      Drawing.id, 
      AES_DECRYPT(UNHEX(Drawing.str_name), @key)
    FROM 
      Drawing 
    JOIN 
      User 
    ON Drawing.id_user = User.id WHERE Drawing.id_user = id_user;
  END$$
  
  -- -----------------------------------------------------
  -- Get one drawing
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_getOneDrawing$$
  
  CREATE PROCEDURE sp_getOneDrawing(IN id_drawing INT)
  BEGIN
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;

    SELECT 
      id, 
      AES_DECRYPT(UNHEX(str_name),@key), AES_DECRYPT(UNHEX(jso_drawingData),@key) FROM Drawing WHERE Drawing.id = id_drawing;
  END$$
  
  -- -----------------------------------------------------  
  -- Add a new drawing
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_addDrawing$$
  
  CREATE PROCEDURE sp_addDrawing(IN idUser INT, IN drawing_name TEXT, IN drawingData JSON)
  BEGIN
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;

    INSERT INTO 
      Drawing(id_user ,str_name, jso_drawingData)
    VALUES ( idUser, HEX(AES_ENCRYPT(drawing_name, @key)), HEX(AES_ENCRYPT(drawingData, @key)));
  END$$
  
  -- -----------------------------------------------------
  -- Modify a drawing
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_updateDrawing$$
  
  CREATE PROCEDURE sp_updateDrawing(IN idUser INT, IN id_drawing INT, IN drawing_name TEXT, IN drawingData JSON)
  BEGIN
    SET @authID = idUser;
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;

    UPDATE 
      Drawing 
    SET 
      str_name = HEX(AES_ENCRYPT(drawing_name, @key)),
      jso_drawingData = HEX(AES_ENCRYPT(drawingData, @key)) WHERE Drawing.id = id_drawing;
  END$$

  -- -----------------------------------------------------
  -- Visualize a drawing
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_visualizeDraw$$

  CREATE PROCEDURE sp_visualizeDraw(IN idUser INT, IN id_Drawing INT) BEGIN
    INSERT INTO Binnacle(id_user, num_draw, str_command) VALUES( idUser, id_Drawing, "visualizeDraw");
  END$$
  -- -----------------------------------------------------
  -- Change the colorConfig
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_updateColorConfig$$
  
  CREATE PROCEDURE sp_updateColorConfig(IN pen_color TEXT, IN fill_color TEXT)
  BEGIN
    UPDATE DrawingConfig SET str_penColor = pen_color, str_fillColor = fill_color;
  END$$
  
  -- -----------------------------------------------------
  -- Change the colorConfig
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_getColorConfig$$
  
  CREATE PROCEDURE sp_getColorConfig()
  BEGIN
    DECLARE penColor TEXT DEFAULT "";
    DECLARE fillColor TEXT DEFAULT "";

    SELECT str_penColor INTO penColor FROM DrawingConfig;
    SELECT str_fillColor INTO fillColor FROM DrawingConfig;
    SELECT penColor, fillColor;
  END$$
-- -----------------------------------------------------
DELIMITER ;
-- -----------------------------------------------------
------------------------------------------------------------------
------------------------------------------------------------------
--                 PROCEDURES BASE DE DATOS "B"                 --
------------------------------------------------------------------
------------------------------------------------------------------
USE DrawingsBackup

DELIMITER $$
  -- -----------------------------------------------------
  -- Add a new user
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_addUser$$
  
  CREATE PROCEDURE sp_addUser(IN new_username TEXT, IN new_password TEXT, IN new_idrole INT)
  BEGIN
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;
    
    INSERT INTO
      User(id_role, str_userName, str_password)
    VALUES
      (new_idrole, HEX(AES_ENCRYPT(new_username,@key)), HEX(AES_ENCRYPT(new_password,@key)));
  END$$

  -- -----------------------------------------------------
  -- Modify user's info
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_updateUserInfo$$

  CREATE PROCEDURE sp_updateUserInfo(IN username_user TEXT, IN new_username TEXT, IN new_password TEXT)
  BEGIN
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;

    UPDATE User SET
      str_userName = HEX(AES_ENCRYPT(new_username, @key)),
      str_password = HEX(AES_ENCRYPT(new_password, @key))
    WHERE AES_DECRYPT(UNHEX(User.str_userName), @key) = username_user;
  END$$
  -- -----------------------------------------------------  
  -- Add a new drawing
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_addDrawing$$
  
  CREATE PROCEDURE sp_addDrawing(IN idUser INT, IN drawing_name TEXT, IN drawingData BLOB)
  BEGIN
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;

    INSERT INTO 
      Drawing(id_user ,str_name, blo_drawingData)
    VALUES ( idUser, HEX(AES_ENCRYPT(drawing_name, @key)), drawingData);
  END$$
  
  -- -----------------------------------------------------
  -- Modify a drawing
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_updateDrawing$$
  
  CREATE PROCEDURE sp_updateDrawing(IN idUser INT, IN id_drawing INT, IN drawing_name TEXT, IN drawingData BLOB)
  BEGIN
    SET @authID = idUser;
    SELECT User.str_password INTO @key FROM User WHERE User.id_role = 1;

    UPDATE 
      Drawing 
    SET 
      str_name = HEX(AES_ENCRYPT(drawing_name, @key)),
      blo_drawingData = drawingData WHERE Drawing.id = id_drawing;
  END$$

  -- -----------------------------------------------------
  -- Change the colorConfig
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_updateColorConfig$$
  
  CREATE PROCEDURE sp_updateColorConfig(IN pen_color TEXT, IN fill_color TEXT)
  BEGIN
    UPDATE DrawingConfig SET str_penColor = pen_color, str_fillColor = fill_color;
  END$$
  

DELIMITER ;