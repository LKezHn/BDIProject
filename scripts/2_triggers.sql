USE Drawings;

DELIMITER $$
    DROP TRIGGER IF EXISTS tr_insertedUser$$
    
    CREATE TRIGGER tr_insertedUser AFTER INSERT ON User FOR EACH ROW
    BEGIN
        INSERT INTO Binnacle(id_user, num_user, str_command) VALUES(1, new.id, "userInserted"); 
    END$$
    
    DROP TRIGGER IF EXISTS tr_modifiedUser$$
    CREATE TRIGGER tr_modifiedUser AFTER UPDATE ON User FOR EACH ROW
    BEGIN
        INSERT INTO Binnacle(id_user, num_user, str_command) VALUES(1, new.id, "userModified"); 
    END$$
    
    DROP TRIGGER IF EXISTS tr_deletedUser$$
    CREATE TRIGGER tr_deletedUser AFTER DELETE ON User FOR EACH ROW
    BEGIN
        INSERT INTO Binnacle(id_user, num_user, str_command) VALUES(1, old.id, "userDeleted"); 
    END$$

    DROP TRIGGER IF EXISTS tr_insertedDraw$$
    CREATE TRIGGER tr_insertedDraw AFTER INSERT ON Drawing FOR EACH ROW
    BEGIN
        INSERT INTO Binnacle(id_user, num_draw, str_command) VALUES( new.id_user, new.id, "drawingInserted");
    END$$
    
    DROP TRIGGER IF EXISTS tr_updatedDraw$$
    CREATE TRIGGER tr_updatedDraw AFTER UPDATE ON Drawing FOR EACH ROW
    BEGIN
        INSERT INTO Binnacle(id_user, num_draw, str_command) VALUES( @authID, new.id, "drawingModified");
    END$$
    
    DROP TRIGGER IF EXISTS tr_updatedConfig$$
    CREATE TRIGGER tr_updatedConfig AFTER UPDATE ON DrawingConfig FOR EACH ROW
    BEGIN
        INSERT INTO Binnacle(id_user, bit_config, str_command) VALUES( 1, 1, "configModified");
    END$$



DELIMITER ;
