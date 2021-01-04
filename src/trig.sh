#! /bin/env bash
  
    #connect and execute python script. change password and use@host info
    sshpass -p "sweet155" ssh -o StrictHostKeyChecking=no z08330@192.86.32.153 << PSCRIPT
        python3 mtmlog.py
    PSCRIPT
    