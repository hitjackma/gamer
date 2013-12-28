# try to get the frequence of op_type for each userGUID
filename1 = '/media/Elements/date_part/gn.merge_user_7017_201211/gn.merge_user_7017_20121107.log/gn.merge_user_7017_20121107.log'
filename = '/home/michael/gamer/user_log_weiwang.log'
user_log = open(filename)
output = [0]*30
counting = []

while 1:
    aline = user_log.readline()
    line = aline.strip().split('|')
    if not aline:
        break
    if int(line[5]) > 4 or int(line[5]) == 0:
        continue
    has = 0
    serverID = line[2]
    GUID = line[4]
    op_type = line[5]
    final_weiwang = line[6]
 
    for j in counting:
        if j['GUID'] == GUID:
            has = 1
            if j.has_key(op_type):
                j[op_type] += 1
            else:
                j[op_type] = 1
            j['finalWW'] = final_weiwang
    if not has:
        temp_dict = {'GUID':GUID, op_type:1, 'serverID':serverID, 'finalWW':final_weiwang}
        counting.append(temp_dict)


for i in counting:
    index = int( i['serverID'] )
    if output[index] == 0:
        output[index] = open('/home/michael/testSpace/gamer/result/%s.txt'% index, 'w')
    print >> output[index], 'GUID|%s' % i['GUID'],
    i.pop('serverID')
    i.pop('GUID')
    for j in i:
        print >> output[index], '|%s|%s' % (j, i[j]),
    print >> output[index], ''

user_log.close()
for i in range(0, 30):
    if output[i] != 0:
        output[i].close()
