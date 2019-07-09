'''
钢条切割问题是这样的：给定一段长度为n英寸的钢条和一个价格表p[i]（i=1，2，...，n），求切割钢条方案，使得销售收益r[n]最大。
'''
'''
动态规划的核心就是找到一个更小规模的解决与当前规模的解决的关系，形如r[n] = f(r[n-1])或r[n] = f(r[n-1], r[n-2])（[]表示下标），然后自底向上解决问题，并通常用一个散列表保存之前计算过的子问题的结果（r[0],r[1]...)
在这个问题中，公式就是r[n] = max(p[i] + r[n-i])(1 <= i <= n)，p为不切割时的值
'''
'''
自底向上需要用循环从0开始计算，自顶向下可以从顶开始递归向下
'''

MINIMUN = -9999999999

def findLargestResult(n:int, priceTable:list):
    resultTempCache = [MINIMUN for i in range(0, n+1)] # 用于保存之前结果的缓存
    resultTempCache[0] = 0
    for i in range(1, n+1):
        maxI = calMax(i, priceTable, resultTempCache)    
        resultTempCache[i] = maxI

    return resultTempCache[n]

def calMax(n:int, priceTable:list, resultTempCache:list):
    max = MINIMUN
    for i in range(1, n + 1):
        r = priceTable[i] + resultTempCache[n - i]
        if r > max:
            max = r
    
    return max

if __name__ == "__main__":
    priceT = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    max = findLargestResult(4, priceT)
    print(max)