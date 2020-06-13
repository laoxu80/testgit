# Python 练习实例1


class ExPyhton:
    def __init__(self):
        pass

    def ex01(self):
        """
        题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
        程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。
        """
        sum=0
        for i in range(1,5):
            for j in range(1,5):
                for k in range(1,5):
                    if (i!=j) and (i!=k) and (j!=k):
                        #print(i,j,k)
                        sum+=1
        return sum

    def ex02(self, x):
        """
        题目：企业发放的奖金根据利润提成。
        利润(I)低于或等于10万元时，奖金可提10%；
        利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
        20万到40万之间时，高于20万元的部分，可提成5%；
        40万到60万之间时高于40万元的部分，可提成3%；
        60万到100万之间时，高于60万元的部分，可提成1.5%，
        高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
        :return: 奖金总数bonus
        """
        elirun = float(x)
        if elirun <= 10**5:
            bonus = elirun*0.1
        elif elirun <= 2*(10**5):
            bonus = 10**5*0.1+(elirun-10**5)*0.075
        elif elirun <= 4*(10**5):
            bonus = 10**5*0.1+(200000-10**5)*0.075+(elirun-200000)*0.05
        elif elirun <=600000:
            bonus = 10**5*0.1+(200000-10**5)*0.075+(400000-200000)*0.05+(elirun-400000)*0.03
        elif elirun <= 1000000:
            bonus = 10**5*0.1+(200000-10**5)*0.075+(400000-200000)*0.05+(600000-400000)*0.03+(elirun-600000)*0.015
        else:
            bonus= 10**5*0.1+(200000-10**5)*0.075+(400000-200000)*0.05+(600000-400000)*0.03+(1000000-600000)*0.015+(elirun-1000000)*0.01
        return bonus

    def ex03(self, i):
        arr = [1000000, 600000, 400000, 200000, 100000, 0]
        rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
        r = 0
        for idx in range(0, 6):
            if i > arr[idx]:
                r += (i - arr[idx]) * rat[idx]
                i = arr[idx]
        return r

    def ex04(self):
        """
        题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
        x+100=n**2
        (x+100)**2+168=m**2
        m**2-n**2=168,(m+n)(m-n)=168
        :return:
        """
        for i in range(1, 85):
            if 168 % i == 0:
                j = 168 / i
                if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
                    m = (i + j) / 2
                    n = (i - j) / 2
                    x = n * n - 100
                    print(x)
        return None

    def extip(self):
        """
        计算5元和2元共11张，合计34元，其中5元和2元分别多少张
        :return:满足条件的列表
        """
        sumlist = []
        for i in range(0, 11):
            if 5*i + 2*(11-i) == 34:
               sumlist.append(i)
        return sumlist

    def ex05(self, y, m, d):
        """
        输入某年某月某日，判断这一天是这一年的第几天？
        :return:天数
        """
        mlist = {'1': 0, '2': 31, '3': 59, '4': 90, '5': 120, '6': 151,
                 '7': 181, '8': 212, '9': 243, '10': 273, '11': 304, '12': 334}
        if (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0)):
            if m >= 3:
                daynum = mlist[str(m)]+d+1
            else:
                daynum = mlist[str(m)]+d
        else:
            daynum = mlist[str(m)]+d
        return daynum

    def ex06(self):

        pass


if __name__=='__main__':
    laoxuex=ExPyhton()


    #print(laoxuex.ex01())
    #print(laoxuex.ex02(298789.11))
    #print(laoxuex.ex03(298789.11))
    #print(laoxuex.extip())
    #print(laoxuex.ex05(2016,8,24))

