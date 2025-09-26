--UPDATE usuarios SET nome = 'Bernadinho' WHERE id=1;

--UPDATE usuarios SET (nome, email, senha_hash) = ('Lázaro', 'lazaro@email.com', '1234') 
 --WHERE id = 1;

SELECT (rua) FROM enderecos;
 --Comentário do PostgreSQL

 -- DELETE FROM ederecos;
 -- DELETE FROM usuarios;
 -- DELETE FROM notas;

 -- Currval pega o valor atual
 --SELECT currval('endereco_id_seq');

 --Nextval pega o próximo
 --SELECT nextval('endereco_id_seq')

INSERT INTO funcionarios (nome, email, senha_hash) VALUES
('Ana', 'ana@email.com', '123'),
('Bruno', 'bruno@email.com', '456'),
('Carlos', 'carlos@email.com', '789'),
('Daniela', 'daniela@email.com', '1011'),
('Eduardo', 'eduardo@email.com', '1213'),
('Fernanda', 'fernanda@email.com', '1415'),
('Gabriel', 'gabriel@email.com', '1617'),
('Helena', 'helena@email.com', '1819'),
('Igor', 'igor@email.com', '2021'),
('Juliana', 'juliana@email.com', '2223'),
('Kleber', 'kleber@email.com', '2425'),
('Larissa', 'larissa@email.com', '2627'),
('Marcos', 'marcos@email.com', '2829'),
('Natalia', 'natalia@email.com', '3031'),
('Otávio', 'otavio@email.com', '3233'),
('Patricia', 'patricia@email.com', '3435'),
('Quintino', 'quintino@email.com', '3637'),
('Renata', 'renata@email.com', '3839'),
('Samuel', 'samuel@email.com', '4041'),
('Tatiane', 'tatiane@email.com', '4243'),
('Ubiratan', 'ubiratan@email.com', '4445'),
('Vanessa', 'vanessa@email.com', '4647'),
('Wagner', 'wagner@email.com', '4849'),
('Xênia', 'xenia@email.com', '5051'),
('Yuri', 'yuri@email.com', '5253'),
('Zuleica', 'zuleica@email.com', '5455'),
('Ana', 'ana2@email.com', '5657'),
('Bruno', 'bruno2@email.com', '5859'),
('Carlos', 'carlos2@email.com', '6061'),
('Daniela', 'daniela2@email.com', '6263'),
('Eduardo', 'eduardo2@email.com', '6465'),
('Fernanda', 'fernanda2@email.com', '6667'),
('Gabriel', 'gabriel2@email.com', '6869'),
('Helena', 'helena2@email.com', '7071'),
('Igor', 'igor2@email.com', '7273'),
('Juliana', 'juliana2@email.com', '7475'),
('Luciana', 'luciana@email.com', '7677'),
('Maurício', 'mauricio@email.com', '7879'),
('Nádia', 'nadia@email.com', '1010'),
('Otto', 'otto@email.com', '2020'),
('Priscila', 'priscila@email.com', '3030'),
('Rafael', 'rafael@email.com', '4040'),
('Simone', 'simone@email.com', '5050'),
('Tiago', 'tiago@email.com', '6060'),
('Ulisses', 'ulisses@email.com', '7070'),
('Viviane', 'viviane@email.com', '8080'),
('Washington', 'washington@email.com', '9090'),
('Xavier', 'xavier@email.com', '1000'),
('Yasmin', 'yasmin@email.com', '2000'),
('Zeca', 'zeca@email.com', '3000'),
('Alan', 'alan@email.com', '4000'),
('Beatriz', 'beatriz@email.com', '5000'),
('Caio', 'caio@email.com', '6000'),
('Diana', 'diana@email.com', '7000'),
('Erick', 'erick@email.com', '8000'),
('Flávia', 'flavia@email.com', '9000'),
('Gilberto', 'gilberto@email.com', '1214'),
('Heloísa', 'heloisa@email.com', '1416'),
('Ícaro', 'icaro@email.com', '1519'),
('Jaqueline', 'jaqueline@email.com', '8985'),
('Luan', 'luan@email.com', '3216'),
('Mirela', 'mirela@email.com', '0123'),
('Noemi', 'noemi@email.com', '3210'),
('Orlando', 'orlando@email.com', '6542'),
('Pamela', 'pamela@email.com', '9876'),
('Quésia', 'quesia@email.com', '3036'),
('Rodrigo', 'rodrigo@email.com', '654'),
('Sabrina', 'sabrina@email.com', '321'),
('Talita', 'talita@email.com', '987'),
('Ursula', 'ursula@email.com', '23256'),
('Vitor', 'vitor@email.com', '98652'),
('Wesley', 'wesley@email.com', '01245'),
('Xuxa', 'xuxa@email.com', '78541'),
('Yago', 'yago@email.com', '021020'),
('Zenaide', 'zenaide@email.com', '36529'),