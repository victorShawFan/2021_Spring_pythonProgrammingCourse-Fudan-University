def main():
    week=['星期日','星期一','星期二','星期三','星期四','星期五','星期六']
    #用for循环实现
    tempDict={}
    for day in week:
        tempDict[day] = int(input("请输入%s平均温度(摄氏度):" % day))
    print(tempDict)
    
    #用zip实现
    tempList=[int(input("请输入%s平均温度(摄氏度):" % day)) for day in week]
    tempDict = dict(zip(week,tempList))
    print(tempDict)

    #用字典推导式实现
    tempDict = {day:int(input("请输入%s平均温度(摄氏度):" % day)) for day in week}
    print(tempDict)
    
    temps = tempDict.values()
    average = sum(temps)/len(week)
    print("本周的平均气温(精确到小数点后两位)是%5.2f摄氏度" % average)

    highestTemp = max(temps)
    highestDays =[day for day,temp in tempDict.items() if temp == highestTemp]
    print("本周气温最高是%d(摄氏度):"% highestTemp,"发生在:",end=" ")
    for day in highestDays:
        print(day,end=" ")



if __name__ == "__main__":
    main()
