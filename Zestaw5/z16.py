end=None

def zad16(s1,s2):

    def sam(chr):
        sam=["a","e","i","o","u","y"]
        if chr in sam:
            return True
        return False
    def ilesam(s):
        licz=0
        for chr in s:
            if sam(chr):
                licz+=1
        return licz
    def sumascii(s):
        sum=0
        for chr in s:
            sum+=ord(chr)
        return sum

    asciis1=sumascii(s1)
    samogs1=ilesam(s1)

    def reku(s2,twor="",ind=0):
        nonlocal asciis1,samogs1
        if sumascii(twor)==asciis1 and ilesam(twor)==samogs1:
            print("da się i to jest to słowo:",twor)
            return True
        elif ind<len(s2):
            return reku(s2,twor+s2[ind],ind+1) or reku(s2,twor,ind+1)
        else:
            return False
    if not reku(s2):
        print("nie da się")












s1,s2="exe","uila"
zad16(s1,s2)