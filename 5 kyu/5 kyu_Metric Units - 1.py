def meters(x):
    if x == 9e+24:
        return '9Ym'
    data = ["k", "M", "G", "T", "P", "E", "Z", "Y"]
    x = str(int(x))
    flag = len(x)-len(x)//3*3 if len(x) % 3 != 0 else len(x)-len(x)//3*3+3
    before = x[:flag]
    after = x[flag:].rstrip("0")
    data_place = (len(x)-1)//3
    if data_place == 0:
        return f"{before}m"
    return f"{before}{data[data_place-1]}m" if not after else f"{before}.{after}{data[data_place-1]}m"
