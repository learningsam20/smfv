import mysql.connector
#Import the Z Open Automation Utilities libraries we need
from zoautil_py import MVSCmd, Datasets, Jobs
from zoautil_py.types import DDStatement
# Import datetime, needed so we can format the report
from datetime import datetime
# Import os, needed to get the environment variables
import os
import string
import time
#Take the contents of this data set and read it into content variables
USERID = os.getenv('USER')
hlq=Datasets.hlq()
print("running jobs for ",hlq)
damember="%s.OUTPUT.SDSFDAS" % hlq
da_contents = Datasets.read(damember)
#ckmember="%s.OUTPUT.SDSFCKS" % hlq
#hc_contents = Datasets.read(ckmember)

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

#Submit the job
jclmember="%s.JCL(SDSFJCL)" % hlq
jobid = Jobs.submit(dataset=jclmember)
while True:
    js=Jobs.list(job_id=jobid)[0]
    if(js["return"]!="?"):
        break
    else:
        print(js)
        time.sleep(5)

#gcpdemo-79cdf:us-central1:mtmdb@34.66.249.142
# change the database connection info as per newly allocated database
mydb = mysql.connector.connect(host="34.66.249.142",user="mtuser",password="infy@123",database="mtmlogdb",auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
sql = "INSERT INTO joblog (jobid,jobname,stepname,procname,jobowner,jobclass,\
jobpos,jobdp,jobreal,jobsio,jobcpupercent,jobexcp,jobcputime,jobsr,jobparsedts) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) \
on duplicate key update jobid=%s,jobname=%s,stepname=%s,procname=%s,jobowner=%s,jobclass=%s,\
jobpos=%s,jobdp=%s,jobreal=%s,jobsio=%s,jobcpupercent=%s,jobexcp=%s,jobcputime=%s,jobsr=%s"
dictMultiplier ={"T":10^3, "M": 10^6, "B": 10^9, "t":10^3, "m": 10^6, "b": 10^9}
for da in da_contents.splitlines():
    if da[25:26]!=" ":
        realval = da[46:50]                                                                                                     
        multiplier = (realval.strip()).strip(string.digits)
        if multiplier==" " or multiplier=="" or multiplier==None:
            multiplier = 1
        else:
            multiplier = dictMultiplier[multiplier]
        realval = int(realval.strip(string.ascii_letters))*multiplier
        daval= (da[24:32],da[0:8],da[8:16],da[16:24],da[32:40],da[40:41],da[41:44],da[44:46],realval,da[50:56],
        da[56:62],da[62:70],da[70:79],da[79:81],formatted_date)
        davalu = daval[:-1]
        daval+=davalu
        #print("processing",daval)
        mycursor.execute(sql, daval)                                                             
mydb.commit()
print(mycursor.rowcount, "record inserted.")