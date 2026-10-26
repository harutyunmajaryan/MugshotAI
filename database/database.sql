DROP DATABASE IF EXISTS JJ;
CREATE DATABASE IF NOT EXISTS JJ;
USE JJ;


CREATE TABLE `SUSPECTS`(
   `id` INT AUTO_INCREMENT PRIMARY KEY,
   `suspect_name` VARCHAR(100) NOT NULL,
   `suspect_surname` VARCHAR(100) NOT NULL,
   `age` INT NOT NULL,
   `suspect_address` VARCHAR(255) NOT NULL
);

CREATE TABLE `SUSPECT_IMAGE_TABLE`(
   `id` INT AUTO_INCREMENT PRIMARY KEY,
   `suspect_name` VARCHAR(255) NOT NULL,
   `suspect_surname` VARCHAR(255) NOT NULL,
   `image_path` VARCHAR(255) NOT NULL
);

DELIMITER $$
CREATE TRIGGER `check_age`
BEFORE INSERT ON `SUSPECTS`
FOR EACH ROW
BEGIN
   IF NEW.age < 0 THEN
     SIGNAL SQLSTATE '45000'
     SET MESSAGE_TEXT = "Age cannot be negative";
   END IF;
END $$
DELIMITER ;

INSERT INTO `SUSPECTS` (`suspect_name`, `suspect_surname`, `age`, `suspect_address`) VALUES
('Eva', 'Smith', 30, '45-89 Wilmslow Road, M13 0JQ'),
('Andrey', 'Bizenko', 34, 'Ratherford Road 14, M1 6BR'),
('Xao', 'Chi', 24, 'Salford 16, M23 9PP'),
('Omar', 'Mohammed', 27, '38-40 Oxney Road M14 5SZ'),
('Sara', 'Lorenzo', 22, 'Manchester 9PL Flat 13 Room 5d'),
('Maria', 'Sorento', 29, 'London 14-15 5HP Flat 1 Room E'),
('Anton', 'Malessy', 31, 'Sheffield 12-23 S15 8UI Flat 3 Room A');

INSERT INTO `SUSPECT_IMAGE_TABLE` (`suspect_name`, `suspect_surname`, `image_path`) VALUES
('Eva', 'Smith', 'images/EvaSmith.png'),
('Andrey', 'Bizenko', 'images/AndreyBizenko.png'),
('Xao', 'Chi', 'images/XaoChi.png'),
('Omar', 'Mohammed', 'images/OmarMohammed.png'),
('Sara', 'Lorenzo', 'images/SaraLorenzo.png'),
('Maria', 'Sorento', 'images/MariaSorento.png'),
('Anton', 'Malessy', 'images/AntonMalessy.png');

SELECT
    `SUSPECTS`.`id`,
    `SUSPECTS`.`suspect_name`,
    `SUSPECTS`.`suspect_surname`,
    `SUSPECTS`.`age`,
    `SUSPECTS`.`suspect_address`,
    `SUSPECT_IMAGE_TABLE`.`image_path`
FROM `SUSPECT_IMAGE_TABLE`
JOIN `SUSPECTS`
    ON `SUSPECTS`.`suspect_name` = `SUSPECT_IMAGE_TABLE`.`suspect_name` 
    AND `SUSPECTS`.`suspect_surname` = `SUSPECT_IMAGE_TABLE`.`suspect_surname`;
