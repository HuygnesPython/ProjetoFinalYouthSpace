CREATE DATABASE PFYS;
USE PFYS;

CREATE TABLE IF NOT EXISTS usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  senha_hash VARCHAR(255) NOT NULL,
  ativo TINYINT(1) NOT NULL DEFAULT 1,
  criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;
-- DAQUI PRA FRENTE NAO TEM NADA SALVO
CREATE TABLE IF NOT EXISTS clientes(
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  senha_hash VARCHAR(255) NOT NULL

);

CREATE TABLE IF NOT EXISTS veiculos(
id INT PRIMARY KEY AUTO_INCREMENT,
cliente_id INT,
marca varchar(99),
modelo varchar(99),
placa varchar(99),
ano VARCHAR(99),
obs VARCHAR(99),
ativo BOOL


);

CREATE TABLE IF NOT EXISTS ordem_servicos(
  id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT,
  veiculo_id INT,
  usuario_abertura_id INT,
  mecanico_id INT,
  data_abertura DATETIME DEFAULT current_timestamp,
  data_prevista_entrega DATETIME,
  status_entrega varchar(67),
  problema_relatado varchar(250),
  diagnostico varchar(250),
  observacoes varchar(200),
  valor_total float,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

INSERT INTO usuarios (nome,email,senha_hash) values
('Huygnes','opa@opa.opa','123');

INSERT INTO clientes (nome,email,senha_hash) values
('Dionizio','opa@opa.opa','123')