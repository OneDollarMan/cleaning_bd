CREATE SCHEMA `cleaning`;
USE `cleaning`;
CREATE TABLE `role` (`id` INT NOT NULL AUTO_INCREMENT, `name` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`)) ENGINE = InnoDB;
CREATE TABLE `user` (`id` INT NOT NULL AUTO_INCREMENT, `username` VARCHAR(45) NOT NULL, `password` VARCHAR(45) NOT NULL, `fio` VARCHAR(45) NOT NULL, `role_id` INT NOT NULL, '2fa' INT NOT NULL DEFAULT 0, 'secret_key' VARCHAR(45), PRIMARY KEY (`id`), INDEX `fk_user_role_idx` (`role_id` ASC) VISIBLE, CONSTRAINT `fk_user_role` FOREIGN KEY (`role_id`) REFERENCES `cleaning`.`role` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION) ENGINE = InnoDB;
CREATE TABLE `status` (`id` INT NOT NULL AUTO_INCREMENT, `name` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`)) ENGINE = InnoDB;
CREATE TABLE `client` (`id` INT NOT NULL AUTO_INCREMENT, `fio` VARCHAR(45) NOT NULL, `number` VARCHAR(45) NOT NULL, `address` VARCHAR(45) NOT NULL, `hidden` TINYINT NOT NULL DEFAULT 0, PRIMARY KEY (`id`)) ENGINE = InnoDB;
CREATE TABLE `cleaning_type` (`id` INT NOT NULL AUTO_INCREMENT, `name` VARCHAR(45) NOT NULL, `price` VARCHAR(45) NOT NULL, `hidden` TINYINT NOT NULL DEFAULT 0, PRIMARY KEY (`id`)) ENGINE = InnoDB;
CREATE TABLE `clothing_type` (`id` INT NOT NULL AUTO_INCREMENT, `name` VARCHAR(45) NOT NULL, `hidden` TINYINT NOT NULL DEFAULT 0, PRIMARY KEY (`id`)) ENGINE = InnoDB;
CREATE TABLE `order` (`id` INT NOT NULL AUTO_INCREMENT, `date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, `name` VARCHAR(45) NOT NULL, `status_id` INT NOT NULL DEFAULT 1, `client_id` INT NOT NULL, `cleaning_type_id` INT NOT NULL, `clothing_type_id` INT NOT NULL, PRIMARY KEY (`id`), INDEX `fk_order_status1_idx` (`status_id` ASC) VISIBLE, INDEX `fk_order_client1_idx` (`client_id` ASC) VISIBLE, INDEX `fk_order_cleaning_type1_idx` (`cleaning_type_id` ASC) VISIBLE, INDEX `fk_order_clothing_type1_idx` (`clothing_type_id` ASC) VISIBLE, CONSTRAINT `fk_order_status1` FOREIGN KEY (`status_id`) REFERENCES `cleaning`.`status` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION, CONSTRAINT `fk_order_client1` FOREIGN KEY (`client_id`) REFERENCES `cleaning`.`client` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION, CONSTRAINT `fk_order_cleaning_type1` FOREIGN KEY (`cleaning_type_id`) REFERENCES `cleaning`.`cleaning_type` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION, CONSTRAINT `fk_order_clothing_type1` FOREIGN KEY (`clothing_type_id`) REFERENCES `cleaning`.`clothing_type` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION) ENGINE = InnoDB;
INSERT INTO `cleaning_type` VALUES (1,'��������',500,0),(2,'��������� �����',100,0),(3,'�������������� �����',150,0),(4,'����',1000,0);
INSERT INTO `role` VALUES (1,'��������'),(2,'����������'),(3,'�������������');
INSERT INTO `status` VALUES (1,'�����'),(2,'� ������'),(3,'�����');
INSERT INTO `clothing_type` VALUES (1,'�����',0),(2,'������� ������',0),(3,'�������� ����',0),(4,'�����',0);
INSERT INTO `user` VALUES (1,'root','63a9f0ea7bb98050796b649e85481845','root',3);