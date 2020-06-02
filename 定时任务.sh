--清理mongodb过期数据
* */1 * * *  sh /jboss/mongodb3.2/mongoclean.sh

[jboss@app_1 jboss]$ cat /jboss/mongodb3.2/mongoclean.sh
mongo /jboss/mongodb3.2/mongoclean.js >>/dev/null

[jboss@app_1 jboss]$ cat /jboss/mongodb3.2/mongoclean.js
conn = new Mongo();
db = conn.getDB("isb_dev");
db.auth("isb_dev","isb_dev");
var date = new Date();
print("time"+date);
var currentHours=date.getHours();
if(currentHours>=1){
        date.setHours(date.getHours()-1);
        print("time1"+date);
        db.ISB_FLOW_INSTANCE_TEMP_DATA.remove({"createTime":{"$lt":date}});
}





--日志压缩存储脚本

0 7 * * * /app/log_lists/BPO_log_cleaner.sh

[jboss@app_1 jboss]$ cat /app/log_lists/BPO_log_cleaner.sh
log_home=/app/BPO/WEB-INF/classes/
bak_home=/app/log_lists/
cd $log_home
logfile=`ls |grep tyblog01 |tail -1`
var=`ls |grep tyblog01|grep -v $logfile`
cd $bak_home
for i in $var
do
mv $log_home$i $bak_home
zip $i.zip $i
rm -rf $i
done





--清理 jboss日志
30 7 28 * * /jboss/jboss-eap-6.2/bin/user_shells/log_clear.sh

[jboss@app_1 jboss]$ cat /jboss/jboss-eap-6.2/bin/user_shells/log_clear.sh
DATE=`date -d last-month +%Y-%m`
YJTB_LOG_DIR=/jboss/jboss-eap-6.2/standalone/log/
JYS_LOG_DIR=/jboss/jboss-eap-6.2/standaloneJys/log/
CRM_LOG_DIR=/jboss/jboss-eap-6.2/standaloneCrm/log/
find $YJTB_LOG_DIR -name 'server.log.'$DATE'*' -delete
find $JYS_LOG_DIR -name 'server.log.'$DATE'*' -delete
find $CRM_LOG_DIR -name 'server.log.'$DATE'*' -delete
>/jboss/logs/jboss6.2/jboss-jys.out
>/jboss/logs/jboss6.2/jboss-crm.out





--清理内存空间
# 超过 5000M 便会清理内存cache
[root@app_1 ~]# cat /root/ebt_jobs/ClearCache.sh
weekday=`date +%w`
if [ $weekday -eq 1 ]
  then  > /jboss/trace.log
        echo "The trace log has been cleared !" >> /jboss/trace.log
fi

freemem=`free -m | tr [:blank:] \\\n | grep [0-9] | sed -n '3p'`
if [ $freemem -lt 5000 ]
then
echo 1 > /proc/sys/vm/drop_caches
echo 0 > /proc/sys/vm/drop_caches
echo "The cache has been cleared!"
echo "-------------------------------------------------------" >> /jboss/trace.log
echo "内存已清理" >> /jboss/trace.log
echo `date` >> /jboss/trace.log
else
echo "good"
echo "-------------------------------------------------------" >> /jboss/trace.log
echo "内存正常:" >> /jboss/trace.log
echo `date` >> /jboss/trace.log
fi





--apache命令切割日志
# 每 500M分一个日志
|/usr/sbin/rotatelogs tyblog01_%Y%m%d%H%M%S.log 512M +480 &







--nginx日志清理
[root@mail ~]# cat /opt/ebt_jobs/nginx_log.sh
#!/bin/bash  
# set log_homes
LOG_HOME="/data/wwwlogs/"
LOG_HOME1="/usr/local/nginx/logs"

# set bak_names
LOG_PATH_BAK="$(date -d yesterday +%Y%m%d%H%M)".access.log
LOG_PATH_BAK1="$(date -d yesterday +%Y%m%d%H%M)".ssl-access.log

# rename bak_names
mv ${LOG_HOME}/access.log ${LOG_HOME}/${LOG_PATH_BAK}.log
mv ${LOG_HOME1}/ssl-access.log ${LOG_HOME1}/${LOG_PATH_BAK1}.log

# open new logs
kill -USR1 `cat /usr/local/nginx/logs/nginx.pid` 

# delete old baks
rm -rf ${LOG_HOME}/${LOG_PATH_BAK}.log
rm -rf ${LOG_HOME1}/${LOG_PATH_BAK1}.log





--清理uwsgi、mongodb日志
[ybweb@mail data]$ cat /opt/ebt_jobs/Clear_Uwsgi_Mongo_log.sh
#!/bin/bash  
# set log_homes
LOG_HOME="/data/app/logs"

# set bak_names
LOG_PATH_BAK_INS=insengine.log."$(date -d yesterday +%Y%m%d%H%M)"

# rename bak_names
mv ${LOG_HOME}/insengine.log ${LOG_HOME}/${LOG_PATH_BAK_INS}.log

# open new logs
kill -9 `ps -ef|grep uwsgi|grep -v grep|awk '{print $2}'`
/usr/local/uwsgi/uwsgi --ini /data/app/insengine/InsCal/insengine.ini -b 12288 -p 24 -l 8192 -M -R 100000 -z30 -L --post-buffering 100M --cpu affinity --buffer-size 65535 --memory-report --enable-threads --threads 24 --listen 12288 --daemonize /data/app/logs/insengine.log

# delete old baks
rm -rf ${LOG_HOME}/${LOG_PATH_BAK_INS}.log
rm -rf ${LOG_HOME}/mongod.log.*




--定期删除mongodb日志
[ybweb@mail data]$ cat /data/app/mongodb/mongolog/MongoLogManager.sh
#!/bin/sh
# Switch logs and delete the logs 30 days ago!
for i in 175 002 003
  do
    datafile=/data/app/mongodb/mongodata/mdata_$i
    logfile=/data/app/mongodb/mongolog/log_$i
    days=30
    /bin/kill -SIGUSR1 `cat $datafile/mongod.lock`
    find $logfile/ -mtime +$days -delete
  done

  

  
  
--mongodb转移表数据
mongo 10.1.47.2:10001/yb_pics -u yb_pics  -p yb_pics deleteTemData.js

[ybpic@localhost ~]$ cat deleteTemData.js
var end_date = new Date();
end_date.setHours(end_date.getHours() + 8);
end_date.setDate(end_date.getDate() - 30);
db.Eb_Image_Para.find({ "createDate": { "$lt": end_date } }).forEach(function(doc) {
db.Eb_Image_Para_bak.insert(doc);
});
db.Eb_Image_Para.remove({ "createDate": { "$lt": end_date } });




--mongodb备份
[ybpic@localhost ~]$ cat /mongodb_prd/backup/mongodb_bak.sh
DUMP=/mongodb_prd/mongodb3.2/bin/mongodump
OUT_DIR=/mongodb_prd/backup/mongodb_bak/mongodb_bak_now
TAR_DIR=/mongodb_prd/backup/mongodb_bak/mongodb_bak_list
DATE=`date +%Y_%m_%d`
DAYS=7
TAR_BAK="mongod_bak_$DATE.tar.gz"
cd $OUT_DIR
rm -rf $OUT_DIR/*
mkdir -p $OUT_DIR/$DATE
$DUMP --port 10001 -u backup -p backup -d yb_pics -o $OUT_DIR/$DATE
tar -zcvf $TAR_DIR/$TAR_BAK $OUT_DIR/$DATE
rm -rf $OUT_DIR/*
find $TAR_DIR/ -mtime +$DAYS -delete




--mongodb日志清理
[ybpic@localhost ~]$ cat /mongodb_prd/MongoLogManager.sh
#!/bin/sh
# Switch logs and delete the logs 30 days ago!
for i in wpt yjtb
  do
    datafile=/mongodb_prd/$i/data
    logfile=/mongodb_prd/$i/logs
    days=30
    /bin/kill -SIGUSR1 `cat $datafile/mongod.lock`
    find $logfile/ -mtime +$days -delete
  done





--mysql检查从库延迟
pj_check @cgprd2 SLAVE -> pwd
/mysql/pj_check
pj_check @cgprd2 SLAVE -> cat check_mysql.sh 
#!/bin/bash
source ~/.bash_profile

SLAVE_USER=root

pass='K4RpZ49a8Tc0Cg=='
SLAVE_PWD=`echo $pass|base64 -d`

SQLCMD="show slave status"

IO_STATUS=`mysql -u${SLAVE_USER} -p${SLAVE_PWD} -e "${SQLCMD}\G;" | awk '$1=="Slave_IO_Running:" {print $2}'`
SQL_STATUS=`mysql -u${SLAVE_USER} -p${SLAVE_PWD} -e "${SQLCMD}\G;" | awk '$1=="Slave_SQL_Running:" {print $2}'`

if [[ "${IO_STATUS}" != "Yes" || "${SQL_STATUS}" != "Yes" ]]; then
    ret='10.0.1.101 servers: caigou The MySQL Replication is not synchronous at: '`date +%F" "%H-%M-%S`'  MUST CALL DBA TO RESOLVE!!!!!'
    echo `date +%Y%m%d%H%M`' ' $ret >> /mysql/pj_check/pj_check.log
    ssh oracle@10.0.1.123 /bmc/msend/sqlplus_bmc.sh "'$ret'" < /dev/null
    exit 1
else
    echo `date +%Y%m%d%H%M`" !!!Normal!!!" >> /mysql/pj_check/pj_check.log
fi
pj_check @cgprd2 SLAVE -> 




--shareplex自动巡检脚本
#!/bin/bash

sp_ctrl  <<! | grep -e Backlog -e Name -e Import -e MTPost >/home/oracle/pj_shareplex/check.txt
show
qstatus
show sync
!

status=''
time=0

cat /home/oracle/pj_shareplex/check.txt | while read line
do
list_01=`echo $line|awk '{print $1}'`
if [ $list_01 == 'Import' -o $list_01 == 'MTPost' ];then
	status=`echo $line|awk '{print $4}'`
	queue=`echo $line|awk '{print $2}'`
	#echo 'queue: '$queue', status: '$status
elif [ $list_01 == 'Name:' ];then
	name=`echo $line|awk '{print $2}'`
elif [ $list_01 == 'Backlog' ];then
	time=`echo $line|awk '{print int($5)}'`
fi
#echo $name
#echo $status
#echo $queue
#echo $time
if [ ! $status ];then
	:;
elif [ $status != 'Running' ];then
	ret='10.1.82.4 queue: '$queue' STATUS: '$status' MUST CALL DBA TO RESOLVE!!!!!'
        echo $ret
        ssh 10.1.83.156 /bmc/msend/sqlplus_bmc.sh "'$ret'" < /dev/null
        status=''
elif [ ! $time ];then
	:;
elif [ $time -ge 60 ];then
        ret='10.0.1.101 queue: '$name' TIMEOUT: '$time' MUST CALL DBA TO RESOLVE!!!!!'
	echo $ret
	ssh 10.0.1.123 /bmc/msend/sqlplus_bmc.sh "'$ret'" < /dev/null
	time=0
fi
done












































