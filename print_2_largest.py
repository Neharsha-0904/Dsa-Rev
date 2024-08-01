def print2largest(self, a):
        # Code Here
        l,l2=0,0
        for i in a:
            if i>l:
                l2=l
                l=i
            elif i>l2 and i!=l:
                l2=i
        return l2
