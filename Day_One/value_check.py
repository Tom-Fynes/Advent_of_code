
with open('C:\projects\Advent_of_code\Day_One\input.txt') as f: 
    dp = [int(i) for i in f.readlines()]
    print(len([ '+' for i,d in enumerate(dp) if (i > 0) and (d > dp[i-1])]))
