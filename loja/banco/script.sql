CREATE DATABASE IF NOT EXISTS pets;
USE pets;
CREATE TABLE IF NOT EXISTS material(
   id INT NOT NULL AUTO_INCREMENT,
   nome VARCHAR(50),
   valor DECIMAL(4,2),
   unidade INT
);
 
INSERT INTO material(id,nome, valor) values(1,'ração dog 15kg',20.5);
INSERT INTO material(id,nome, valor) values(2,'ração cat 15kg',25.5);
INSERT INTO material(id,nome, valor) values(3,'OSSO 1kg ',11.5);
