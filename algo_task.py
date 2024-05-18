# Input:   xallar = [5,3,4,2,1]
# Output:  yerlər=['1-ci','3-cu','2-ci','4-cu','5-ci']

# 1)En boyuyu tapiriq ve ...
# 2)Sonra digerleri max-dan ne qeder kicikdirse o ferqi basqa deyisene beraber edirik k=5-3=2, k=5-4=1
# 3)Ve bu deyisenin qiymetini eyni loopun icinde evvelki 1-in ustune gelirik   1+2=3, 1+1=2

def olmpus():
    xallar = [5, 3, 4, 2, 1]
    yerler = []
    max_xal = max(xallar)
    n = 1
    for xal in xallar:
        k = max_xal - xal  #k = 5 - 5 = 0
        n = k + 1          #n = 0 + 1 = 1
        n = f"{n}-ci"
        yerler.append(n)
    return yerler
        

print(olmpus())