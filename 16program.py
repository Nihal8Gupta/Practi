#16 WAP for print this input: func('TRACXN',0) output: 'RCN'  input: func('TRACXN',1) output: 'TAX'
def func(s,n):
    if n==0:
        ns =[ s[i] for i in range(len(s)) if i%2 ==1 ]
        return "".join(ns)
    else:
        ns =[ s[i] for i in range(len(s)) if i%2 ==0 ]
        return "".join(ns)

func('TRACXN',0)