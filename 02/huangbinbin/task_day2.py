#!/usr/bin/python
#-*- coding: utf-8 -*-

def sortList(argvlist):
    """This function is used to sort list by insertion algorithm"""
    try:
        if type(argvlist) != list or len(argvlist) < 2:
            print('The parameter must be list and the list length is larger than 1!') 
        else:
            #Insertion algorithm
            for i in range(1,len(argvlist)):
                contrast = argvlist[i]
                while i > 0 and int(contrast) < int(argvlist[i-1]):
                    argvlist[i] = argvlist[i-1]
                    i -= 1
                argvlist[i] = contrast
            print(argvlist)
            
    except:
        print('The list exist a element not a number!')
        return -1

temp_list = [1,2,3,2,12,3,1,3,21,2,2,3,65555,4111,22,3333,444,111,4,5,777,65555,45,33,45]
sortList(temp_list)
