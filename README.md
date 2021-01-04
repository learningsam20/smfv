# SMFV
Smart MainFrame Visualizer (SMFV)

This repository consists of brief intro and description of how the mainframe analyzer works

## Introduction

SMF holds wealth of info for various mainframe subsystems, including SDSF. Users cannot access this info readily. SMFV attempts to analyze & visualize a part of SDSF job info. It analyzes DA job queue at pre-defined interval and shows tableau dashboard with top resource consuming jobs/users, frequently executed jobs, class & priority wise job distribution, execution trend & more. While this is a representative analysis, it could be extended to additional SDSF attributes and SMF data.


## Pre-requisites

The following pre-requisites must be met in order to successfully use SMFV
- A Mainframe host with accessible SSH port and a user credentials
- Access to Mainframe Unix subsystem (USS)
- Access to cloud/native MySQL installation
- Access to Tableau online server
- Availability of necessary Python, ZOAU packages on Mainframes
- A system to schedule the script that would invoke SDSF monitoring job every 5 minutes (configurable)


## Installation Instructions

- Copy necessary files from git clone https://github.com/learningsam20/smfv
- Copy SDSFJCL in a mainframe JCL PDS and change/add params if any to the job card
- Connect to any MySQL server and execute the mtm.sql. Provide necessary firewall exception to the IP of MF host and Tableau host
- Copy mtmlog.py in mainframe USS and change database connection info as above (line 35, defaults to GCP based instance created)
- Copy trig.sh in any linux machine, modify user, password, host info for Mainframe (default MTM MF) and job prefix to analyze (default Z*). and execute following. 
	chmod 777 trig.sh 
	while true; do './trig.sh'; sleep 300; done
- Copy MTMProject.twb and modify connection info if needed (default above connection). Publish it to server. Currently hosted instance available at https://prod-apnortheast-a.online.tableau.com/#/site/testsam/workbooks/118064