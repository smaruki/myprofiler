#mysql_process_log
MySQL Processlist Log<br>
Logging slow mysql queries<br>

**Usage: myprofiler.py [options]** <br>

Options:<br>
  -h, --help            show this help message and exit<br>
  -o OUT, --out=OUT     write raw queries to this file.<br>
  -c CONFIG, --config=CONFIG<br>
                        read MySQL configuration from. (default: '~/.my.cnf'<br>
  -s SECTION, --section=SECTION<br>
                        read MySQL configuration from this section. (default: '[DEFAULT]')<br>
  -n K, --num-summary=K<br>
                        show most K common queries. (default: 10)<br>
  -i INTERVAL, --interval=INTERVAL<br>
                        Interval of executing show processlist [sec]. (default:2.0)<br>
  -m MINTIME, --mintime=MINTIME<br>
                        Minimum query execution time [sec]. (default: 10)<br>


**.my.cnf** <br>
Default dir: '~/.my.cnf'<br>
Config File:<br>
[spamegg]<br>
host=localhost<br>
database=processos<br>
user=smaruki_user<br>
password=secret<br>