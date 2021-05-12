#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

def chick_calc( ):
    """ 今有鸡翁一，值钱伍；鸡母一，值钱三；鸡雏三，值钱一。凡百钱买鸡百只，
    问鸡翁、母、雏各几何？ 出自《张邱建算经》
    """
    result = []
    for rooster in range(100//5 +1 ):
        for hen in range((100-rooster*5)//3 + 1):
            if 7 * rooster + 4 * hen == 100:    #  300 = 5*3 rooster + 3*3 hen + (100-rooster-hen)
                result.append((rooster,hen,100-rooster-hen))

    print('总共有%d个解' % len(result))
    for index,value in enumerate(result,1):
        print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' % (index, *value))

def chick_calc_list( ):
    """ 今有鸡翁一，值钱伍；鸡母一，值钱三；鸡雏三，值钱一。凡百钱买鸡百只，
    问鸡翁、母、雏各几何？ 出自《张邱建算经》
    """

    result = [ (rooster,hen,100-rooster-hen) for rooster in range(100//5 +1 )
               for hen in range((100-rooster*5)//3 + 1)
               if 7 * rooster + 4 * hen == 100]
 
    print('总共有%d个解' % len(result))
    for index,value in enumerate(result,1):
        print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' % (index, *value))
  
if __name__ == '__main__':
    chick_calc()
    print()
    chick_calc_list()
    
