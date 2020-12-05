-- MySQL Script generated by MySQL Workbench
-- Tue Dec  1 16:06:07 2020
-- Model: New Model    Version: 1.0


-- -----------------------------------------------------
-- Base de datos

DROP DATABASE IF EXISTS Drawings;
CREATE SCHEMA IF NOT EXISTS Drawings CHARACTER SET utf8 ;

USE Drawings;

-- -----------------------------------------------------
-- Tabla Role
-- -----------------------------------------------------
DROP TABLE IF EXISTS Roles;

CREATE TABLE IF NOT EXISTS Roles (
  id INT AUTO_INCREMENT NOT NULL,
  tex_name TEXT NOT NULL,
  PRIMARY KEY (id))
  ;


-- -----------------------------------------------------
-- Table User
-- -----------------------------------------------------
DROP TABLE IF EXISTS User;

CREATE TABLE IF NOT EXISTS User (
  id INT NOT NULL AUTO_INCREMENT,
  id_role INT NOT NULL DEFAULT 2,
  tex_userName TEXT NOT NULL,
  tex_password TEXT NOT NULL,
  PRIMARY KEY (id), 
  FOREIGN KEY (id_role) REFERENCES Roles(id)
);



-- -----------------------------------------------------
-- Tabla Drawing
-- -----------------------------------------------------
DROP TABLE IF EXISTS Drawing ;

CREATE TABLE IF NOT EXISTS Drawing (
  id INT NOT NULL,
  id_user INT NOT NULL,
  tex_name VARCHAR(45) NOT NULL,
  blo_drawingData BLOB NOT NULL,
  PRIMARY KEY (id),
    FOREIGN KEY (id_user) REFERENCES User(id)
);


-- -----------------------------------------------------
-- Table Binnacle
-- -----------------------------------------------------
DROP TABLE IF EXISTS Binnacle;

CREATE TABLE IF NOT EXISTS Binnacle (
  id INT NOT NULL,
  id_user INT NOT NULL,
  dat_date DATETIME NOT NULL,
  tex_command TEXT NOT NULL,
  PRIMARY KEY (id),
   FOREIGN KEY (id_user) REFERENCES User(id)
);



-- -----------------------------------------------------
-- Tabla DrawingConfig
-- -----------------------------------------------------
DROP TABLE IF EXISTS DrawingConfig;

CREATE TABLE IF NOT EXISTS DrawingConfig(
  chr_penColor CHAR(7) NOT NULL DEFAULT "#000000",
  chr_fillColor CHAR(7) NOT NULL DEFAULT "#000000"
);

-- -----------------------------------------------------
--                      PROCEDURES
-- -----------------------------------------------------

DELIMITER $$
  -- -----------------------------------------------------
  -- Get all the users
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_getAllUsers$$

  CREATE PROCEDURE sp_getAllUsers()
  BEGIN
    SELECT User.id AS "id", User.tex_userName AS "Username" FROM User;
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
    SELECT User.id, User.tex_userName, User.id_role INTO id, user, user_role FROM User WHERE User.id = id_user;
    SELECT id, user, user_role;
  END$$
  
  -- -----------------------------------------------------
  -- Get user password
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_authUser$$

  CREATE PROCEDURE sp_authUser(IN username TEXT)
  BEGIN
    DECLARE user_password TEXT DEFAULT "None";
    DECLARE id_user INT DEFAULT 0;
    SELECT User.tex_password, User.id INTO user_password, id_user FROM User WHERE User.tex_userName = username;
    SELECT id_user, user_password;
  END$$
  
  -- -----------------------------------------------------
  -- Get all the users with operator role
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_getOperators$$

  CREATE PROCEDURE sp_getOperators()
  BEGIN
    SELECT User.id, User.tex_userName FROM User JOIN Roles ON User.id_role = Roles.id WHERE User.id_role = 2;
  END$$

  -- -----------------------------------------------------
  -- Add a new user
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_addUser$$
  
  CREATE PROCEDURE sp_addUser(IN new_username TEXT, IN new_password TEXT, IN new_idrole CHAR(3))
  BEGIN
    INSERT INTO User(id_role, tex_userName, tex_password) VALUES (new_idrole, new_username, new_password);
  END$$

  -- -----------------------------------------------------
  -- Modify user's info
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_updateUserInfo$$

  CREATE PROCEDURE sp_updateUserInfo(IN id_user INT, IN new_username TEXT, IN new_password TEXT, IN new_role CHAR(3))
  BEGIN
    UPDATE User SET tex_userName = new_username, tex_password = new_password, id_role = new_role WHERE User.id = id_user;
  END$$
  -- -----------------------------------------------------
  -- Delete an user
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_deleteUser$$
  
  CREATE PROCEDURE sp_deleteUser(IN id_user INT)
  BEGIN
    DELETE FROM User WHERE User.id = id_user;
  END$$
  
  -- -----------------------------------------------------
  -- Get name and id of all the drawings
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_getDrawingList$$
  
  CREATE PROCEDURE sp_getDrawingList()
  BEGIN
    SELECT Drawing.id AS "id", Drawing.tex_name AS "Name" FROM Drawing;
  END$$
  
  -- -----------------------------------------------------
  -- Get name and id of all the drawings of an user
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_getUserDrawingList$$
  
  CREATE PROCEDURE sp_getUserDrawingList(IN id_user INT)
  BEGIN
    SELECT
      Drawing.id AS "id", Drawing.tex_name AS "Name"
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
    SELECT * FROM Drawing WHERE Drawing.id = id_drawing;
  END$$
  
  -- -----------------------------------------------------
  -- Add a new drawing
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_addDrawing$$
  
  CREATE PROCEDURE sp_addDrawing(IN id_user INT, IN drawing_name TEXT, IN drawingData BLOB)
  BEGIN
    INSERT INTO Drawing(id_user ,tex_name, blo_drawingData) VALUES(id_user, drawing_name, drawingData);
  END$$
  
  -- -----------------------------------------------------
  -- Modify a drawing
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_updateDrawing$$
  
  CREATE PROCEDURE sp_updateDrawing(IN id_drawing INT, IN drawing_name TEXT, IN drawingData BLOB)
  BEGIN
    UPDATE Drawing SET tex_name = drawing_name, blo_drawingData = drawingData WHERE Drawing.id = id_drawing;
  END$$
  
  -- -----------------------------------------------------
  -- Delete a drawing
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_deleteDrawing$$
  
  CREATE PROCEDURE sp_deleteDrawing(IN id_drawing INT)
  BEGIN
    DELETE FROM Drawing WHERE Drawing.id = id_drawing ;
  END$$
  
  -- -----------------------------------------------------
  -- Change the colorConfig
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_updateColorConfig$$
  
  CREATE PROCEDURE sp_updateColorConfig(IN pen_color TEXT, IN fill_color TEXT)
  BEGIN
    UPDATE DrawingConfig SET chr_penColor = pen_color, chr_fillColor = fill_color;
  END$$
  
  -- -----------------------------------------------------
  -- Change the colorConfig
  -- -----------------------------------------------------
  DROP PROCEDURE IF EXISTS sp_getColorConfig$$
  
  CREATE PROCEDURE sp_getColorConfig()
  BEGIN
    DECLARE penColor TEXT DEFAULT "";
    DECLARE fillColor TEXT DEFAULT "";

    SELECT chr_penColor INTO penColor FROM DrawingConfig;
    SELECT chr_fillColor INTO fillColor FROM DrawingConfig;
    SELECT penColor, fillColor;
  END$$

-- -----------------------------------------------------
DELIMITER ;
-- -----------------------------------------------------
INSERT INTO DrawingConfig() VALUES ();
INSERT INTO Roles(tex_name) VALUES
	("Administrador"),
  ("Operador");

CALL sp_addUser("admin", "admin", 1);
CALL sp_addUser("LKez", "luis", 2);