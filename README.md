mysql_process_log
--------
MySQL Processlist Log<br>
Logging slow mysql queries<br>

**Usage: myprofiler.py [options]** <br>

Options:<br>
```
-h, --help                        Show this help message and exit
-o OUT, --out=OUT                 Write raw queries to this file.
-c CONFIG, --config=CONFIG        Read MySQL configuration from. (default: '~/.my.cnf'
-s SECTION, --section=SECTION     Read MySQL configuration from this section. (default: '[DEFAULT]')
-i INTERVAL, --interval=INTERVAL  Interval of executing show processlist [sec]. (default:2.0)
-m MINTIME, --mintime=MINTIME     Minimum query execution time [sec]. (default: 10)
```

**Config File** <br>
Default dir: '~/.my.cnf'<br>
```
[DEFAULT]
host=localhost
database=processos
user=smaruki_user
password=secret
```
**Extra Dependencies**
pymysql
