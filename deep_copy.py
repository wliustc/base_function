# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import copy
def copy_case():
    list1=[1,2,3,['a',',b','d','d']]
    list2=list1
    print list1
    list1.append(5)
    print list1
    list1[3].append('e')
    print list1
    print list1[3][2]

    print "list2",list2
copy_case()
