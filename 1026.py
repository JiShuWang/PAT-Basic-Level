# 时间复杂度：O(1)
# 解题思想：
# 1.思考一个算法，提供秒，可以得到对应的小时数、分钟数、秒数
# 2.对秒数进行四舍五入
# 3.不足2位的输出需要补0

Start, End = map(int, input().split())  # 输入起始和结束时间

# 获取小时、分钟、秒的算法，/100的打点常数获得具体的秒数
Hour = int((End - Start) / 100 / 3600)
Minute = int((End - Start) / 100 % 3600 / 60)
Seconds = (End - Start) / 100 % 3600 % 60

if Seconds - int(Seconds) >= 0.5:  # 实现四舍五入，例如42.6秒，通过int转换后为42秒
    Seconds += int(Seconds) + 1  # 转为43秒

# 补足0，例如1:26:3需要补足为01:26:03
Hour = (2 - len(str(Hour) + '')) * '0' + str(Hour)
Minute = (2 - len(str(Minute) + '')) * '0' + str(Minute)
Seconds = (2 - len(str(Seconds) + '')) * '0' + str(Seconds)

print(Hour + ':' + Minute + ':' + Seconds + '')
