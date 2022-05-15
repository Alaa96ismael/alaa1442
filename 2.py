def f(d):
    l=list()
    while d!=0:
        i=d%2
        d//=2
        l.append(i)
    l.reverse()
    for i in l:
        print(i,end=" ")

def main():
    numb=int(input('enter number'))
    f(numb)

if __name__=="__main__":
    main()
