import sys;
def findMinDiff(goddie_prices, n, m):
    if (m==0 or n==0):
        return 0
    arr=list(goddie_prices.values())
    arr.sort()#sort array
    if (n < m):
        return -1
    min_diff = sys.maxsize

    i=0
    item=[]
    while(i+m-1<n ):
     
        diff = arr[i+m-1] - arr[i]
        if (diff < min_diff):
            min_diff = diff
            lowest=i
            highest=i+m-1
        i+=1

    b=[]
    godd={}
    b.append(arr[lowest:highest+1])
    key_list = list(goddie_prices.keys())
    val_list = list(goddie_prices.values())
    for ind in b:
        for i in ind:
            key=key_list[val_list.index(i)]
            godd[key]=i
    print("Here the goodies that are selected for distribution are:")
    for i in godd:
        print(i,"\b:",godd[i])
    return min_diff
    
if __name__ == "__main__":

    goodie=['fitbit plus','ipods','mi bands','cult pass','mac book pro','digital camera','alexa','sandwich','microwave oven','Scale']
    prices=[7980,22349,999,2799,229900,11101,9999,2195,9800,4999]
    m = int(input("Number of Employees : "))#no employee
    n = len(prices)#no of goodies
    goodie_prices=dict(zip(goodie,prices))#array is appended to dictionary using zip
    d=findMinDiff(goodie_prices, n, m)

    print("And the difference between the choosen goodie with highest price and the lowest price is ",d)