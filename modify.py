import os
import sys
def modify(i):
    path="/root/test/hyperledger/4-peers-hosti.yml"
    for vp_num in ['vp4','vp5','vp6','vp7']:
        f = open(path, 'r+')
        linelist = f.readlines()
        f.seek(0)
        new_num = '%d' % i
        for line in linelist:
            line=line.replace(vp_num,'vp'+new_num)
            f.write(line)
        f.close()
        i=i+1
    print 'finished!'

a=sys.argv[1]
b=int(a)
modify(b)
