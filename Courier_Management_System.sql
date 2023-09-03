create database courier_management;
use courier_management;

create table customer(
customer_id int auto_increment,
Name varchar(25),
mobile varchar(10),
address varchar(100),
primary key(customer_id));

create table packet(
id int auto_increment,
customer_id int,
weight numeric,
delivery_location varchar(100),
description varchar(100),
sent_date date,
primary key(id,delivery_location),
foreign key (customer_id) references customer(customer_id));

create table delivery(
id int,
receiver_name varchar(20),
receiver_mobile varchar(10),
recived_date date,
delivery_status varchar(18),
deliveryman_idandname varchar(60),
primary key(deliveryman_idandname,delivery_status),
foreign key (id) references packet(id));

select * from customer;
select * from delivery;
select * from packet;

SHOW databases;