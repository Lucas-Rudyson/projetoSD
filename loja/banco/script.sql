CREATE DATABASE IF NOT EXISTS pets;
USE pets;
CREATE TABLE IF NOT EXISTS material(
   id VARCHAR(50) NOT NULL AUTO_INCREMENT,
   nome VARCHAR(50),
   valor VARCHAR(50),
   unidade VARCHAR(50)
)ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8;

