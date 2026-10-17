DROP DATABASE IF EXISTS suspect_db;
CREATE DATABASE suspect_db;
USE suspect_db;

CREATE TABLE `SUSPECTS`(
   `id` INT AUTO_INCREMENT PRIMARY KEY,
   `suspect_name` VARCHAR(100) NOT NULL,
   `suspect_surname` VARCHAR(100) NOT NULL,
   `age` INT NOT NULL
);

CREATE TABLE `SUSPECT_IMAGE_TABLE`(
   `id` INT AUTO_INCREMENT PRIMARY KEY,
   `suspect_name` VARCHAR(255) NOT NULL,
   `suspect_surname` VARCHAR(255) NOT NULL,
   `image_path` VARCHAR(255) NOT NULL
);

INSERT INTO `SUSPECTS` (`suspect_name`, `suspect_surname`, `age`) VALUES
('Eva', 'Smith', 30),
('Andrey', 'Bizenko', 34),
('Xao', 'Chi', 24),
('Omar', 'Mohammed', 27);

INSERT INTO `SUSPECT_IMAGE_TABLE` (`suspect_name`, `suspect_surname`, `image_path`) VALUES
('Eva', 'Smith', 'images/EvaSmith.png'),
('Andrey', 'Bizenko', 'images/AndreyBizenko.png'),
('Xao', 'Chi', 'images/XaoChi.png'),
('Omar', 'Mohammed', 'images/OmarMohammed.png');

SHOW TABLES;

SELECT
`SUSPECTS`.`id`,
`SUSPECTS`.`suspect_name`,
`SUSPECTS`.`suspect_surname`,
`SUSPECTS`.`age`,
`SUSPECT_IMAGE_TABLE`.`image_path`
FROM `SUSPECT_IMAGE_TABLE`
JOIN `SUSPECTS`
  WHERE `SUSPECTS`.`suspect_name` = `SUSPECT_IMAGE_TABLE`.`suspect_name` 
  AND `SUSPECTS`.`suspect_surname` = `SUSPECT_IMAGE_TABLE`.`suspect_surname`;
