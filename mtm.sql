--drop database mtmlogdb;
create database mtmlogdb;
use mtmlogdb;
-- drop table joblog;
create table joblog(jobid varchar(8) not null primary key, jobname varchar(8) not null,stepname varchar(8) null, 
 procname varchar(8) null, jobowner varchar(8) null, jobclass char(1) null, jobpos char(3) null, jobdp char(3) null,
 jobreal int not null, jobsio decimal(5,2) not null, jobcpupercent decimal(5,2) not null, jobexcp bigint not null, 
 jobcputime decimal(9,2) not null, jobsr char(2) null, jobparsedts datetime not null);