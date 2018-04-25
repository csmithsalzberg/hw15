def pcheck(pword):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXTYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    upnum = [1 for x in pword if x in upper]
    lownum = [1 for x in pword if x in lower]
    numnum = [1 for x in pword if x in num]

    
    
    return (1 in upnum and 1 in lownum and 1 in numnum)

print pcheck("Hell0")
