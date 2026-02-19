CREATE DATABASE IF NOT EXISTS PFYS;
USE PFYS;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    ativo TINYINT(1) NOT NULL DEFAULT 1,
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),
    documento VARCHAR(20),
    endereco VARCHAR(255),
    observacoes VARCHAR(250),
    ativo BOOL DEFAULT 1,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS veiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    marca VARCHAR(99),
    modelo VARCHAR(99),
    placa VARCHAR(99),
    ano VARCHAR(99),
    observacoes VARCHAR(250),
    ativo BOOL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE TABLE IF NOT EXISTS mecanicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    especialidade VARCHAR(100),
    telefone VARCHAR(20),
    observacoes VARCHAR(250),
    ativo BOOL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS pecas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    codigo VARCHAR(100),
    quantidade_estoque INT DEFAULT 0,
    custo FLOAT,
    preco_venda FLOAT,
    observacoes VARCHAR(250),
    ativo BOOL DEFAULT 1,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ordem_servicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    veiculo_id INT,
    usuario_abertura_id INT,
    mecanico_id INT,
    data_abertura DATETIME DEFAULT CURRENT_TIMESTAMP,
    data_prevista_entrega DATETIME,
    data_conclusao DATETIME,
    status VARCHAR(67),
    problema_relatado VARCHAR(250),
    diagnostico VARCHAR(250),
    observacoes VARCHAR(250),
    valor_total FLOAT,
    
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (veiculo_id) REFERENCES veiculos(id),
    FOREIGN KEY (usuario_abertura_id) REFERENCES usuarios(id),
    FOREIGN KEY (mecanico_id) REFERENCES mecanicos(id)
);

CREATE TABLE IF NOT EXISTS os_itens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    os_id INT,
    peca_id INT,
    descricao VARCHAR(250),
    tipo VARCHAR(20),
    quantidade INT,
    valor_unitario FLOAT,
    valor_total FLOAT,
    FOREIGN KEY (os_id) REFERENCES ordem_servicos(id),
    FOREIGN KEY (peca_id) REFERENCES pecas(id)
);


SELECT * FROM clientes;
SELECT * FROM os_itens;
SELECT * FROM veiculos;
SELECT * FROM ordem_servicos;
SELECT * FROM usuarios;
SELECT * FROM mecanicos;
SELECT * FROM pecas;
