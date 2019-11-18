# Always pass the default parameters after the non default parameters
def cal_area(radius, pi=3.142):
    result = (radius ** 2) * pi
    # print(result)
    return result


res = cal_area(5)
print(res)
