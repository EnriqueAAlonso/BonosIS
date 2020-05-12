CREATE TABLE `bonosup`.`bono` (
  `idBono` INT NOT NULL,
  `idUsuario` INT NULL,
  `flavor` VARCHAR(50) NULL,
  `isbn` VARCHAR(50) NULL,
  `maturity` DATETIME NULL,
  PRIMARY KEY (`idBono`));
