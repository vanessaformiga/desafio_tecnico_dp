``````

Tabela: Usuario
Campo	Tipo	Chave/Constraint	Observação
id_usuario	INT	PK, AUTO_INCREMENT	Identificador do usuário
id_servidor	INT	FK → Servidor(matricula), UNIQUE	1:1 com Servidor, opcional se for responsável por DP
nome	VARCHAR(255)	NOT NULL	Nome do usuário
email	VARCHAR(255)	UNIQUE, NOT NULL	Email do usuário
senha	VARCHAR(255)	NOT NULL	Senha do usuário
tipo_usuario	VARCHAR(50)		Tipo ou perfil do usuário
data_criacao	DATETIME	DEFAULT CURRENT_TIMESTAMP	Data de criação do usuário
ultimo_login	DATETIME		Último login do usuário
id_dp	INT	FK → Departamento_Pessoal(id_dp)	Se o usuário estiver vinculado a DP

Tabela: Servidor
Campo	Tipo	Chave/Constraint	Observação
matricula	INT	PK	Identificador do servidor
nome	VARCHAR(255)	NOT NULL	Nome do servidor
id_orgao	INT	FK → Orgao(id_orgao), NOT NULL	Órgão ao qual pertence
id_departamento	INT	FK → Departamento(id_departamento), NOT NULL	Departamento ao qual pertence
cargo	VARCHAR(100)		Cargo do servidor
data_admissao	DATE		Data de admissão
tipo_servidor	VARCHAR(50)		Tipo do servidor (ex: efetivo, comissionado)

Tabela: Orgao
Campo	Tipo	Chave/Constraint	Observação
id_orgao	INT	PK, AUTO_INCREMENT	Identificador do órgão
nome	VARCHAR(255)	NOT NULL	Nome do órgão
tipo_orgao	VARCHAR(50)		Tipo do órgão

Tabela: Departamento
Campo	Tipo	Chave/Constraint	Observação
id_departamento	INT	PK, AUTO_INCREMENT	Identificador do departamento
nome	VARCHAR(255)	NOT NULL	Nome do departamento
id_orgao	INT	FK → Orgao(id_orgao), NOT NULL	Órgão ao qual pertence

Tabela: Departamento_Pessoal
Campo	Tipo	Chave/Constraint	Observação
id_dp	INT	PK, AUTO_INCREMENT	Identificador do DP
nome	VARCHAR(255)	NOT NULL	Nome do DP
responsavel	VARCHAR(255)		Nome do responsável
contato	VARCHAR(100)		Contato do responsável
observacao	TEXT		Observações adicionais

Tabela: Assiduidade
Campo	Tipo	Chave/Constraint	Observação
id_assiduidade	INT	PK, AUTO_INCREMENT	Identificador do registro
id_servidor	INT	FK → Servidor(matricula), NOT NULL	Servidor relacionado
data	DATE	NOT NULL	Data da atividade
tipo_atividade	VARCHAR(100)		Tipo de atividade realizada
status_presenca	VARCHAR(50)		Presente, ausente, etc.
observacao	TEXT		Observações

Tabela: Duvida
Campo	Tipo	Chave/Constraint	Observação
id_duvida	INT	PK, AUTO_INCREMENT	Identificador da dúvida
id_servidor	INT	FK → Servidor(matricula), NOT NULL	Servidor que enviou a dúvida
data_hora	DATETIME	DEFAULT CURRENT_TIMESTAMP	Momento da criação

Tabela: Treinamento
Campo	Tipo	Chave/Constraint	Observação
id_treinamento	INT	PK, AUTO_INCREMENT	Identificador do treinamento
nome	VARCHAR(255)	NOT NULL	Nome do treinamento
descricao	TEXT		Descrição
data_inicio	DATE		Início do treinamento
data_fim	DATE		Fim do treinamento
observacao	TEXT		Observações
id_servidor	INT	FK → Servidor(matricula)	Servidor participante
id_departamento	INT	FK → Departamento(id_departamento)	Departamento relacionado

Tabela: Certificacao
Campo	Tipo	Chave/Constraint	Observação
id_certificacao	INT	PK, AUTO_INCREMENT	Identificador da certificação
nome	VARCHAR(255)	NOT NULL	Nome da certificação
descricao	TEXT		Descrição
data_aplicacao	DATE		Data de aplicação
nota_obtida	DECIMAL(5,2)		Nota obtida
gera_certificado	BOOLEAN		Se gera certificado ou não
id_servidor	INT	FK → Servidor(matricula)	Servidor relacionado
id_departamento	INT	FK → Departamento(id_departamento)	Departamento relacionado

Tabela: Clima_Organizacional
Campo	Tipo	Chave/Constraint	Observação
id_clima	INT	PK, AUTO_INCREMENT	Identificador do registro
id_departamento	INT	FK → Departamento(id_departamento), NOT NULL	Departamento avaliado
periodo	VARCHAR(50)		Período da pesquisa
data_da_realizacao	DATE		Data de realização
indice_obtido	DECIMAL(5,2)		Índice do clima organizacional
comentarios	TEXT		Comentários gerais
id_servidor	INT	FK → Servidor(matricula)	Servidor responsável pelo registro

``````