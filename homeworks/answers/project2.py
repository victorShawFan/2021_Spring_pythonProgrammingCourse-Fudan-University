'''Project1 规范表示厘米数''' 
def transform(cms):
    print('--规范化表示厘米数--')    
    meters = cms // 100
    left_cms = cms % 100
    dms = left_cms // 10
    left_cms = left_cms % 10
    print(cms,'厘米等价于:',meters,'米',dms,'分米',left_cms,'厘米')


def main():
    total_cms= int(input('请输入厘米数（整数）:'))
    
    transform(total_cms)


if __name__ == '__main__':
    main()








