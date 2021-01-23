create table if not exists Usuarios(
	id int unsigned not null,
	nombre varchar(20),
    apellido varchar(20)
);

#drop table Usuarios;
#truncate Usuarios;

use prueba;

select * from Usuarios;

insert into Usuarios(id, nombre, apellido) values(1, 'juan', 'Rodriguez');
insert into Usuarios(id, nombre, apellido) values(2, 'Jose', 'Pena');
insert into Usuarios(id, nombre, apellido) values(3, 'Manolo', 'galvan');
insert into Usuarios(id, nombre, apellido) values(4, 'Maria', 'valenzuela');



