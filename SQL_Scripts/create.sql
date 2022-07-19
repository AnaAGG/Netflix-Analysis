-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Netflix
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Netflix
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Netflix` DEFAULT CHARACTER SET utf8 ;
USE `Netflix` ;

-- -----------------------------------------------------
-- Table `Netflix`.`directors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Netflix`.`directors` (
  `iddirectors` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`iddirectors`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Netflix`.`actors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Netflix`.`actors` (
  `idActors` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idActors`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Netflix`.`original_netflix`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Netflix`.`original_netflix` (
  `idoriginal_netflix` INT NOT NULL,
  `title` VARCHAR(45) NULL,
  PRIMARY KEY (`idoriginal_netflix`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Netflix`.`films`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Netflix`.`films` (
  `show_id` VARCHAR(45) NOT NULL,
  `description` LONGTEXT NOT NULL,
  `date_added` VARCHAR(45) NULL,
  `duration` VARCHAR(45) NULL,
  `directors_iddirectors` VARCHAR(45) NOT NULL,
  `actors_idActors` VARCHAR(45) NOT NULL,
  `duration_measure` VARCHAR(45) NOT NULL,
  `rating` INT NULL,
  `country` VARCHAR(45) NULL,
  `type` VARCHAR(45) NULL,
  `original_netflix_idoriginal_netflix` INT NOT NULL,
  PRIMARY KEY (`show_id`),
  INDEX `fk_films_directors_idx` (`directors_iddirectors` ASC) VISIBLE,
  INDEX `fk_films_actors1_idx` (`actors_idActors` ASC) VISIBLE,
  INDEX `fk_films_original_netflix1_idx` (`original_netflix_idoriginal_netflix` ASC) VISIBLE,
  CONSTRAINT `fk_films_directors`
    FOREIGN KEY (`directors_iddirectors`)
    REFERENCES `Netflix`.`directors` (`iddirectors`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_films_actors1`
    FOREIGN KEY (`actors_idActors`)
    REFERENCES `Netflix`.`actors` (`idActors`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_films_original_netflix1`
    FOREIGN KEY (`original_netflix_idoriginal_netflix`)
    REFERENCES `Netflix`.`original_netflix` (`idoriginal_netflix`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Netflix`.`genre`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Netflix`.`genre` (
  `idgenre` INT NOT NULL,
  `genre` VARCHAR(45) NULL,
  PRIMARY KEY (`idgenre`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Netflix`.`films_has_genre`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Netflix`.`films_has_genre` (
  `films_show_id` VARCHAR(45) NOT NULL,
  `genre_idgenre` INT NOT NULL,
  PRIMARY KEY (`films_show_id`, `genre_idgenre`),
  INDEX `fk_films_has_genre_genre1_idx` (`genre_idgenre` ASC) VISIBLE,
  INDEX `fk_films_has_genre_films1_idx` (`films_show_id` ASC) VISIBLE,
  CONSTRAINT `fk_films_has_genre_films1`
    FOREIGN KEY (`films_show_id`)
    REFERENCES `Netflix`.`films` (`show_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_films_has_genre_genre1`
    FOREIGN KEY (`genre_idgenre`)
    REFERENCES `Netflix`.`genre` (`idgenre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
