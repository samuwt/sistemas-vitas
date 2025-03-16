CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

INSERT INTO usuarios (nome, email, senha) VALUES
('JORGE', 'medico@clinica.com', '$2y$10$yghYzaEuJ.SgSNDGPkO7fuFspjUPRSwvn7TCq1aM9QAXZX22poREO'),
('KARINA', 'recepcao@clinica.com', '$2y$10$rFWCOTVeuXla/CeFSJCWyemz5hZbA.GSsKLbpfk.02oDP0fufJpSO');