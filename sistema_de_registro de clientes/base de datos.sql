create database if not exists negocio_de_pulgas;
use negocio_de_pulgas;
#----------------------------------------------------------------------------------------------------
create table if not exists Empleados(
	Cedula int not null,
	nombre varchar(15) not null,
    apellido varchar(15) not null,
    rango varchar(15) not null,
    fecha_de_nacimiento varchar(50)
);
drop table Empleados;
#-----------------------------------------------------------------------------------------------------
create table if not exists Clientes(
	nombre varchar(50),
    apodo varchar(50),
    Cedula int,
    Saldo_a_deber float
);
#------------------------------------------------------------------------------------------------------
create table if not exists productos(
	_Key int not null,
	fabricante varchar(10),
    modelo varchar(50),
    precio float
);




