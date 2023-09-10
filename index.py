#a = list(range(1,11))

def z_f(nums: list,retrn= "A"):
    '''
    in (retrn) writ E for return even,write O for return odd and write A for print all.
    (list)--->(list)
    give a list of numbers to function
    and get even and odd list
    '''
    even = []
    odd = []
    for i in nums:
        if i % 2 == 1:
            odd.append(i)
        elif i % 2 == 0:
            even.append(i)
    if retrn == "E":
        return even
    elif retrn == "O":
        return odd
    else:
        print(f"zoj: {even} \nfard: {odd}")
    
#print(z_f(a,"O"))
