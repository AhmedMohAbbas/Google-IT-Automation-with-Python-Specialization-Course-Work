#! python

import sys
import csv
import re


errormsgs_dic = {}
users_dic = {}

info_pattern = r"ticky: INFO:? ([\w' ]*).*\((.*)\)$"
error_pattern = r"ticky: ERROR:? ([\w' ]*).*\((.*)\)$"


with open("/home/student-03-9a2686f158f8/syslog.log", 'r') as fh:
    for line in fh:
        line = line.strip()
        if not 'ticky' in line:
            continue
        x = re.search(info_pattern, line)
        y = re.search(error_pattern, line)
        if not x is None:
            users_dic[x.group(2)]= users_dic.get(x.group(2))
            if users_dic[x.group(2)] is None:
                users_dic[x.group(2)] = {}
            users_dic[x.group(2)]["INFO"] = users_dic[x.group(2)].get("INFO",0) + 1
        elif not y is None:
            users_dic[y.group(2)]= users_dic.get(y.group(2))
            if users_dic[y.group(2)] is None:
                users_dic[y.group(2)] = {}
            users_dic[y.group(2)]["ERROR"] = users_dic[y.group(2)].get("ERROR",0) + 1
            errormsgs_dic[y.group(1)]= errormsgs_dic.get(y.group(1), 0) + 1

errors = sorted(errormsgs_dic.items(), reverse=True, key= lambda z: z[1] )
per_user = sorted(users_dic.items())
errors.insert(0, ('Error', 'Count'))

with open("error_message.csv", 'w') as fh2:
    for error in errors:
        a,b = error
        fh2.write(str(a)+','+str(b)+'\n')


with open("user_statistics.csv", 'w') as fh3:
    fh3.write("Username,INFO,ERROR\n")
    for stats in per_user:
        c, d = stats
        fh3.write(str(c)+','+str(d.get("INFO", '-'))+','+str(d.get("ERROR", '-'))+'\n')