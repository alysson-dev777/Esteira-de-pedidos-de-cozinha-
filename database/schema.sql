create database if not exists kitchenflow;
use kitchenflow;

create table cardapio(
id_prato int primary key auto_increment,
nome_prato varchar(100) not null unique,
preco decimal (10, 2) not null,

constraint ck_cardapio_preco
	check (preco >= 0)
);

create table comandas(
numero_comanda int primary key,
mesa int not null,
id_prato int not null,
status varchar(30) not null default 'Na Fila',
data_hora_envio timestamp not null default current_timestamp,

constraint ck_comandas_mesa 
	check (mesa > 0),
	
constraint ck_comandas_status
	check (status in ('Na Fila', 'Preparando')),

constraint fk_comandas_cardapio
	foreign key (id_prato) 
	references cardapio(id_prato)
	on delete restrict
);

create table historico(
id_historico int primary key auto_increment,
numero_comanda int not null,
acao varchar(30) not null,
data_hora timestamp not null default current_timestamp,

constraint fk_historico_comandas
	foreign key (numero_comanda)
	references comandas(numero_comanda)
	on delete cascade,

constraint ck_historico_acao
	check (acao in ('NOVO_PEDIDO', 'INICIAR_PREPARO'))
);
