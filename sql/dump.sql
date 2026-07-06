CREATE DATABASE concessionaria;

USE concessionaria;

CREATE TABLE marca (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE modelo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_marca INT NOT NULL,
    nome VARCHAR(50) NOT NULL,

    FOREIGN KEY (id_marca)
    REFERENCES marca(id)
);

CREATE TABLE carro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_modelo INT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    renavam BIGINT,
    placa VARCHAR(10),
    valor DECIMAL(10,2),
    ano INT,

    FOREIGN KEY (id_modelo)
    REFERENCES modelo(id)
);