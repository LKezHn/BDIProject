--- -------------------------------------------------------------
--- @authors eglopezl@unah.hn lemartinezm@unah.hn
--- -------------------------------------------------------------

------------------------------------------------------------------
------------------------------------------------------------------
--                      BASE DE DATOS "A"                       --
------------------------------------------------------------------
------------------------------------------------------------------
DROP DATABASE IF EXISTS Drawings;
CREATE DATABASE Drawings CHARACTER SET utf8 ;
USE Drawings;

CREATE TABLE IF NOT EXISTS Roles (
  id INT AUTO_INCREMENT NOT NULL COMMENT "Auto  Incremental",
  str_name TEXT NOT NULL COMMENT "Name of the role",
  PRIMARY KEY (id)
) COMMENT "Table of Roles";

CREATE TABLE IF NOT EXISTS User (
  id INT NOT NULL AUTO_INCREMENT COMMENT "Auto Incremental",
  id_role INT NOT NULL DEFAULT 2 COMMENT "Role of the user",
  str_userName VARCHAR(40) NOT NULL UNIQUE COMMENT "Username",
  str_password TEXT NOT NULL COMMENT "Password of the user",
  PRIMARY KEY (id), 
  FOREIGN KEY (id_role) REFERENCES Roles(id)
) COMMENT "Table of users";

CREATE TABLE IF NOT EXISTS Drawing (
  id INT AUTO_INCREMENT NOT NULL COMMENT "Auto Incremental",
  id_user INT NOT NULL COMMENT "id of the drawing creator",
  str_name VARCHAR(45) NOT NULL COMMENT "Name of the drawing",
  jso_drawingData JSON NOT NULL COMMENT "Drawing content",
  PRIMARY KEY (id),
  FOREIGN KEY (id_user) REFERENCES User(id)
) COMMENT "Table of drawings";

CREATE TABLE IF NOT EXISTS Binnacle (
  id INT AUTO_INCREMENT NOT NULL COMMENT "record id",
  id_user INT NOT NULL COMMENT "id of the user",
  num_user INT COMMENT "User modified",
  num_draw INT COMMENT "id of inserted drawing",
  bit_config BIT DEFAULT 0 COMMENT "Config of drawing are updated or not",
  dat_date DATETIME NOT NULL DEFAULT NOW() COMMENT "Date of the event",
  str_command TEXT NOT NULL COMMENT "Command used",
  PRIMARY KEY (id)
) COMMENT "Binnacle table ";

CREATE TABLE IF NOT EXISTS DrawingConfig(
  str_penColor CHAR(7) NOT NULL DEFAULT "#000000" COMMENT "Pen color value",
  str_fillColor CHAR(7) NOT NULL DEFAULT "#000000" COMMENT "Fill color value"
) COMMENT "Drawing Colors Config";

INSERT INTO DrawingConfig() VALUES ();
INSERT INTO Roles(str_name) VALUES ("Administrador"), ("Operador");
INSERT INTO User(str_userName, str_password, id_role) VALUES (HEX(AES_ENCRYPT("admin","admin")), "admin", 1);

------------------------------------------------------------------
------------------------------------------------------------------
--                      BASE DE DATOS "B"                       --
------------------------------------------------------------------
------------------------------------------------------------------
DROP DATABASE IF EXISTS DrawingsBackup;
CREATE DATABASE DrawingsBackup CHARACTER SET utf8 ;
USE DrawingsBackup;

CREATE TABLE IF NOT EXISTS Roles (
  id INT AUTO_INCREMENT NOT NULL COMMENT "Auto  Incremental",
  str_name TEXT NOT NULL COMMENT "Name of the role",
  PRIMARY KEY (id)
) COMMENT "Table of Roles";

CREATE TABLE IF NOT EXISTS User (
  id INT NOT NULL AUTO_INCREMENT COMMENT "Auto Incremental",
  id_role INT NOT NULL DEFAULT 2 COMMENT "Role of the user",
  str_userName VARCHAR(40) NOT NULL UNIQUE COMMENT "Username",
  str_password TEXT NOT NULL COMMENT "Password of the user",
  PRIMARY KEY (id), 
  FOREIGN KEY (id_role) REFERENCES Roles(id)
) COMMENT "Table of users";

CREATE TABLE IF NOT EXISTS Drawing (
  id INT AUTO_INCREMENT NOT NULL COMMENT "Auto Incremental",
  id_user INT NOT NULL COMMENT "id of the drawing creator",
  str_name VARCHAR(45) NOT NULL COMMENT "Name of the drawing",
  blo_drawingData BLOB NOT NULL COMMENT "Drawing content",
  PRIMARY KEY (id),
  FOREIGN KEY (id_user) REFERENCES User(id) ON DELETE CASCADE
) COMMENT "Table of drawings";

CREATE TABLE IF NOT EXISTS DrawingConfig(
  str_penColor CHAR(7) NOT NULL DEFAULT "#000000" COMMENT "Pen color value",
  str_fillColor CHAR(7) NOT NULL DEFAULT "#000000" COMMENT "Fill color value"
) COMMENT "Drawing Colors Config";

INSERT INTO DrawingConfig() VALUES ();
INSERT INTO Roles(str_name) VALUES ("Administrador"), ("Operador");
INSERT INTO User(str_userName, str_password, id_role) VALUES (HEX(AES_ENCRYPT("admin","admin")), "admin", 1);