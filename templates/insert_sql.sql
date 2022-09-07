create schema AtividadeContinua;

use AtividadeContinua;

CREATE TABLE tabela_rena( id_usuario BIGINT NOT NULL AUTO_INCREMENT, nome VARCHAR(45) NULL, cpf VARCHAR(45) NULL, endereco VARCHAR(60) NULL, PRIMARY KEY (id_usuario));

DELIMITER // CREATE PROCEDURE sp_createUser( IN p_nome VARCHAR(20), IN p_cpf VARCHAR(20), IN p_endereco VARCHAR(20)) BEGIN IF ( select exists (select 1 from tabela_rena where p_cpf = p_cpf) ) THEN select 'CPF já existe';ELSE insert into AtividadeContinua ( nome, cpf, endereco ) values ( p_nome, p_cpf, p_endereco ); END IF; END // DELIMITER ;