#! /bin/env bash
  
    #connect and execute python script. change password and use@host info
    sshpass -p "password" ssh -o StrictHostKeyChecking=no user@mfip << PSCRIPT
        python3 mtmlog.py
    PSCRIPT
    
