all_nums = set(range(1, 10001))
nonself = set()
for nums in all_nums:
    n=nums
    sumn = 0
    while n>0:
        i = n%10
        sumn += i
        n = n//10
    n = sumn+ nums
    if n<=10000:
        nonself.add(n)
selfnum = all_nums - nonself

selflist = list(selfnum)
selflist.sort()
for num in selflist:
    print(num)
