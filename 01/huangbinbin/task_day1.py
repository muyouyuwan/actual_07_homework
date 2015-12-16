#!/usr/bin/python
#-*- coding: utf-8 -*-

def getTwoMaxNum(argvlist):
    """This function is used to find the maximum number of two in the list.
       Tips: the argument must be a list of the parameters to be called!

    """
    try:
        if type(argvlist) == list and len(argvlist) >= 2:
            tlist = argvlist[:]
        else:
            print('Parameter non list or list length is less than two!')
            return -1

        len_list = len(tlist)
        while len_list:
            for i in range(len_list-1):
                if int(tlist[i]) > int(tlist[i+1]):
                    t = tlist[i]
                    tlist[i], tlist[i+1] = tlist[i+1], t
            len_list -= 1
        max1_index = argvlist.index(tlist[-1])
        max2_index = argvlist.index(tlist[-2])
        if max1_index == max2_index:
            max2_index = argvlist.index(tlist[-2], max1_index+1)
        print('The two maximum number are %s and %s!' % (tlist[-2], tlist[-1]))
        print('The index of two maximum number are #%d and #%d!' % (max2_index, max1_index))
    except:
        print('The list exist a element not a number!')
        return -2


temp_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
getTwoMaxNum(temp_list)
