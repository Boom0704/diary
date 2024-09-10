
def adder(a, b):
    sum = a+b
    return sum

print(adder(1,2))
print(adder(1,2))

def return_test():
    return 10, "ff", 3.14

a,b,c =return_test()
print(a,b,c)
data =return_test()
print(data)

def fn_default(nm, level =1):
    print(nm, level)

fn_default("d", 2)
fn_default("fe")


def fn_cal(oper, *args):
    print(oper)
    for n in args:
        print(n)

fn_cal("fe",3,3,4,5,6,7,8)
fn_cal("fe",3,3,4)