# Input:   xallar = [25,18,14,6,3]
# Output:  yerlər=['1-ci','3-cu','2-ci','4-cu','5-ci']

# 1)En boyuyu tapiriq ve ...
# 2)Sonra digerleri max-dan ne qeder kicikdirse o ferqi basqa deyisene beraber edirik k=5-3=2, k=5-4=1
# 3)Ve bu deyisenin qiymetini eyni loopun icinde evvelki 1-in ustune gelirik   1+2=3, 1+1=2

# def olympus():
#     xallar = [5, 3, 4, 2, 1]
#     yerler = []
#     max_xal = max(xallar)
#     n = 1
#     for xal in xallar:
#         k = max_xal - xal  #k = 5 - 5 = 0
#         n = k + 1          #n = 0 + 1 = 1
#         n = f"{n}-ci"
#         yerler.append(n)
#     return yerler
        

# print(olympus())

# _____________________________Other methods_____________________________________________


points = [45, 88, 34, 16, 3]
sorted_indices = sorted(range(len(points)), key=lambda i: points[i], reverse=True)
places = [''] * len(points)

for rank, index in enumerate(sorted_indices):
    places[index] = f"{rank + 1}th"

print("points =", points)
print("places =", places)


# ______________________________________________________________________________

# points = [45, 48, 44, 46, 43]
# sorted_indices = sorted(range(len(points)), key=lambda i: points[i], reverse=True)
# print(sorted_indices)
# places = []

# for rank, index in enumerate(sorted_indices):
#     places.append(f"{index+ 1}th ({points[index]} points)")
    
# print("points =", points)
# print("places =", places)

# ____________________________________________________________
