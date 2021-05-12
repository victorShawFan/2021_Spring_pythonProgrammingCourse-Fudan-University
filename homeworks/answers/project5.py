def main():
    week=['星期日','星期一','星期二','星期三','星期四','星期五','星期六']
##    tempList=[]
##    for day in week:
##        temp = float(input("请输入%s平均温度(摄氏度):" % day))
##        tempList.append(temp)
    tempList=[float(input("请输入%s平均温度(摄氏度):" % day)) for day in week]
    average = sum(tempList)/len(week)
    print("本周的平均气温(精确到小数点后两位)是%5.2f摄氏度" % average)
    sortList = sorted(tempList,reverse = True)
    print("本周气温从高到低依次是(摄氏度):",end=" ")
    for temp in sortList:
        print("%5.2f" % temp,end=" ")


if __name__ == "__main__":
    main()
