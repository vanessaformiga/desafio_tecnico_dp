
CREATE TABLE Usuario (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    id_servidor INT UNIQUE, -- 1:1 com Servidor            -- se for responsável por DP (opcional)
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    tipo_usuario VARCHAR(50),
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ultimo_login DATETIME,
    FOREIGN KEY (id_servidor) REFERENCES Servidor(matricula),
    FOREIGN KEY (id_dp) REFERENCES Departamento_Pessoal(id_dp)
);

CREATE TABLE Servidor (
    matricula INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    id_orgao INT NOT NULL,
    id_departamento INT NOT NULL,
    cargo VARCHAR(100),
    data_admissao DATE,
    tipo_servidor VARCHAR(50),
    FOREIGN KEY (id_orgao) REFERENCES Orgao(id_orgao),
    FOREIGN KEY (id_departamento) REFERENCES Departamento(id_departamento)
);

CREATE TABLE Orgao (
    id_orgao INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    tipo_orgao VARCHAR(50)
);

CREATE TABLE Departamento (
    id_departamento INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    id_orgao INT NOT NULL,
    FOREIGN KEY (id_orgao) REFERENCES Orgao(id_orgao)
);

CREATE TABLE Departamento_Pessoal (
    id_dp INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    responsavel VARCHAR(255),
    contato VARCHAR(100),
    observacao TEXT
);

CREATE TABLE Assiduidade (
    id_assiduidade INT PRIMARY KEY AUTO_INCREMENT,
    id_servidor INT NOT NULL,
    data DATE NOT NULL,
    tipo_atividade VARCHAR(100),
    status_presenca VARCHAR(50),
    observacao TEXT,
    FOREIGN KEY (id_servidor) REFERENCES Servidor(matricula)
);

CREATE TABLE Duvida (
    id_duvida INT PRIMARY KEY AUTO_INCREMENT,
    id_servidor INT NOT NULL,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_servidor) REFERENCES Servidor(matricula)
);

CREATE TABLE Treinamento (
    id_treinamento INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    data_inicio DATE,
    data_fim DATE,
    observacao TEXT,
    id_servidor INT,
    id_departamento INT,
    FOREIGN KEY (id_servidor) REFERENCES Servidor(matricula),
    FOREIGN KEY (id_departamento) REFERENCES Departamento(id_departamento)
);

CREATE TABLE Certificacao (
    id_certificacao INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    data_aplicacao DATE,
    nota_obtida DECIMAL(5,2),
    gera_certificado BOOLEAN,
    id_servidor INT,
    id_departamento INT,
    FOREIGN KEY (id_servidor) REFERENCES Servidor(matricula),
    FOREIGN KEY (id_departamento) REFERENCES Departamento(id_departamento)
);

CREATE TABLE Clima_Organizacional (
    id_clima INT PRIMARY KEY AUTO_INCREMENT,
    id_departamento INT NOT NULL,
    periodo VARCHAR(50),
    data_da_realizacao DATE,
    indice_obtido DECIMAL(5,2),
    comentarios TEXT,
    id_servidor INT,
    FOREIGN KEY (id_departamento) REFERENCES Departamento(id_departamento),
    FOREIGN KEY (id_servidor) REFERENCES Servidor(matricula)
);