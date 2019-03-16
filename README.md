## Project 1: LogsAnalysis 
## By Polineni Anil

LogsAnalysis,part of the udacity [fullstack web developer nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## Project Overview

This is single file project this generates the reports from the news article database.This reporting tool is a python program using the ``psycopg2`` module to connect to the ``PostgreSQL`` database.

## Requirements

1. Python         (Programming Language)
2. vagrant        (A virtual Environment)
3. virtual Box    (An Open Source Virtualization Product)
4. Git Bash or power shell (for windows)
5. psycopg2       (library)
6. postgreSQL     (database)


## Project Contents

1. log.py --> is the main file to run this logAnalysis Project executes the SQLQuaries.

2. README.md --> Step By Step Procedure to run this LogAnalysis project.

3. Newsdata ZipFile --> The Newsdata ZipFile contains populate news.

4. Output.txt --> Executed expected output my Project


## Project Setup

1.Install Vagrant [https://www.vagrantup.com/]

2.Install VirtualBox[https://www.virtualbox.org/wiki/Download_Old_Builds_5_1] to install and run your projects on virtual machine.

3.Vagrant Setup file to this Download or Clone fullstack-nanodegree-vm[https://github.com/udacity/fullstack-nanodegree-vm] repository.

4.Launch the vagrant VM inside vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using commands:

Step-1--> ``$vagrant up``

Step-2-->  ``$vagrant ssh`` 

Step-3--> Change Directory to vagrant -->  ``$cd /vagrant/``

Step-4--> Change Directory to project folder --> $cd logsanlysis

Step-5--> Download the [newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract newsdata.sql. This file should be inside the `vagrant/logsanalysis/`.

Step-6--> Load news data in database --> ``$psql -d news -f newsdata.sql ``

Step-7--> Connect news data to database -->  ``$psql -d news``

Step-8--> create helping view for third problem
create view using 
```
create view log_err_view as select to_char(date(time),'Mon DD,YYYY') as day, count(*) as requests, count(CASE WHEN status='404 NOT FOUND' THEN 1 END) as errors from log group by day;
```
Step-9--> Type `\q` command for exit from PostgreSQL.

Step-10--> Run Python file --> ``$python log.py``