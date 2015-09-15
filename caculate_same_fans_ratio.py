import os
import sys
#######################################
#author:cw
#date:2015.09.15
#计算两账号的共有粉丝数，进行统计
#########################################
def same_fans_statistic():
	cust_lis=[]
	simi_lis=[]
	common_fans=0
	with open('./sig_cust_fans.txt','r') as fr1:
		for line in fr1:
			line=line.strip()
			cust_lis=line.split(',')
	with open('./sig_simi_fans.txt','r') as fr1:
		for line in fr1:
			line=line.strip()
			simi_lis=line.split(',')
	for i in cust_lis:
		if i in simi_lis:
			common_fans +=1
	print 'common_fans:',common_fans
	print 'common_fans_ratio:' float(common_fans)/len(cust_lis)
 def main():
 	same_fans_statistic()
if __name__ == '__main__':
	main()
