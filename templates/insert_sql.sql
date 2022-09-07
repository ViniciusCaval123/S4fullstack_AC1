create schema ac;

use ac;

CREATE TABLE usuario( id_usuario BIGINT NOT NULL AUTO_INCREMENT, nome VARCHAR(45) NULL, email VARCHAR(45) NULL, senha VARCHAR(45) NULL, PRIMARY KEY (id_usuario));

DELIMITER // CREATE PROCEDURE sp_createUser( IN p_nome VARCHAR(20), IN p_email VARCHAR(20), IN p_senha VARCHAR(20)) BEGIN IF ( select exists (select 1 from usuario where p_email = p_email) ) THEN select 'Email já existe';ELSE insert into usuario ( nome, email, senha ) values ( p_name, p_username, p_password ); END IF; END // DELIMITER ;