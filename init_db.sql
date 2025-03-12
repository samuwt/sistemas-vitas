CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    tipo TEXT NOT NULL CHECK(tipo IN ('Medico', 'Enfermeiro', 'Recepcionista', 'Administrador', 'Financeiro', 'Suporte', 'Paciente'))
);

INSERT INTO usuarios (nome, email, senha, tipo) VALUES
('Dr. João', 'medico@clinica.com', '$2b$12$ExemploDeSenhaHasheada', 'Medico'),
('Maria', 'recepcao@clinica.com', '$2b$12$OutraSenhaHasheada', 'Recepcionista');
