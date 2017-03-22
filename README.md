# mysql_process_log
MySQL Processlist Log<br>
Logging slow mysql queries<br>

**Usage: myprofiler.py [options]** <br>

Options:<br>
-h, --help            					Show this help message and exit<br>
-o OUT, --out=OUT     					Write raw queries to this file.<br>
-c CONFIG, --config=CONFIG  			Read MySQL configuration from. (default: '~/.my.cnf'<br>
-s SECTION, --section=SECTION  			Read MySQL configuration from this section. (default: '[DEFAULT]')<br>
-i INTERVAL, --interval=INTERVAL 		Interval of executing show processlist [sec]. (default:2.0)<br>
-m MINTIME, --mintime=MINTIME  			Minimum query execution time [sec]. (default: 10)<br>


**Config File** <br>
Default dir: '~/.my.cnf'<br>

[DEFAULT]<br>
host=localhost<br>
database=processos<br>
user=smaruki_user<br>
password=secret<br>

**Extra Dependencies**
pymysql
