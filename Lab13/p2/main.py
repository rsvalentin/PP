n=int(input("Introdu n ="))
init_list=(n ** 2 for n in range(n))
init_list=list(init_list)
print(init_list)
res=list(filter(lambda x: x % 2 == 0 , init_list))
print(res)