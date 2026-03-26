create database 10k;
use 10k;
create table admin(
sno int unique auto_increment,
name varchar(100),
email varchar(100) unique not null,
password varchar(100),
phone bigint);
insert into admin (name,email,password,phone) values ('Yash','y@gmail.com','123@Y',6487347573);
select * from admin;
create table trainer(
sno int unique auto_increment,
name varchar(100),
email varchar(100) unique not null,
password varchar(100),
phone bigint);
select * from trainer;
create table pm(
sno int unique auto_increment,
name varchar(100),
email varchar(100) unique not null,
password varchar(100),
phone bigint);
select * from pm;
create table student(
sno int unique auto_increment,
name varchar(100),
email varchar(100) unique not null,
password varchar(100),
course varchar(100),
branch varchar(100),
passout_year int,
phone bigint);
select * from student;