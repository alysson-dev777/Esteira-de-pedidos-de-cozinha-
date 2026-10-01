insert into cardapio (nome_prato, preco) values
('Hambúrguer Artesanal', 25.90),
('Pizza', 35.00),
('Batata Frita', 15.00),
('Água', 5.00);

insert into comandas (numero_comanda, mesa, id_prato) values
(201, 5, 1),
(202, 8, 2),
(203, 3, 3);

insert into historico (numero_comanda, acao) values
(201, 'NOVO_PEDIDO'),
(202, 'NOVO_PEDIDO'),
(203, 'NOVO_PEDIDO');

update comandas 
set status = 'Preparando'
where numero_comanda = 201;

insert into historico (numero_comanda, acao) values
(201, 'INICIAR_PREPARO');



insert into comandas (numero_comanda, mesa, id_prato, status) values
(204, 10, 1, 'Cancelado');

insert into comandas (numero_comanda, mesa, id_prato) values
(205, 7, 99);

insert into cardapio (nome_prato, preco) values
('Pizza', 35.00);

select * from historico
where numero_comanda = 202;

delete from comandas
where numero_comanda = 202;

select * from historico
where numero_comanda = 202;
