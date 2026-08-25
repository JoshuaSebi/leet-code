class Solution:
    def myAtoi(self, s: str) -> int:
        str1=s.lstrip(" ")
        if len(str1)==0:
            return 0
        ints=0
        if str1[0]=="-":
            sig=-1
            str1=str1[1:]
        elif str1[0]=="+":
            sig=1
            str1=str1[1:]
        else:
            sig=1
        newstr=str1.lstrip("0")
        if len(newstr)==0:
            return 0
        for i in newstr:
            if i.isdigit():
                dig=int(i)
                ints=10*ints+dig
            else:
                break
        retval=ints*sig
        if retval<=(-(2**31)):
            return (-(2**31))
        if retval>=(2**31-1):
            return (2**31-1)
        return retval