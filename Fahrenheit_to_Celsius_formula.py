def warm_changeFC(x):      #攝氏轉華氏
    y = (x * 9 /5) + 32
    return y
def warm_changeCF(x):      #華氏轉攝氏
    y = ( x - 32 ) * 5 / 9
    return y


f = float(input("請輸入攝氏溫度:"))
print(f"華氏溫度是{warm_changeFC(f)}度")

c = float(input("請輸入華氏溫度:"))
print(f"攝氏溫度是{warm_changeFC(c)}")

