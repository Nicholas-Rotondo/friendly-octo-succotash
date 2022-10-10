import os
from random import randint


letters = ['q', 'w', 'e', 'r', 't,' 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '.']
valid_doms = []
valid_ips = []

def gen_domain():
    this_domain = ''
    for j in range(randint(1, 100)):
        this_domain = this_domain + letters[randint(0, len(letters))]
    return this_domain

def gen_ip():
    this_ip = ''
    for j in range(randint(4, 16)):
        this_ip = this_ip + numbers[randint(0, len(numbers))]
    return this_ip

def make_entry(domain, ip):
    line = domain + " " + ip + " A"
    return line

def gen_inputs():
    f = open('PROJ2-DNSTS1.txt', 'w')
    
    for i in range(randint(1, 100)):
        this_domain = gen_domain()
        
        this_ip = gen_ip()
        valid_doms.append(this_domain)
        valid_ips.append(this_ip)
        this_line = make_entry(this_domain, this_ip)
        
        print(this_line, f = f)
    f.close()

    f = open('PROJ2-DNSTS2.txt', 'w')
    
    for i in range(randint(1, 100)):
        this_domain = gen_domain()
        this_ip = gen_ip()
        
        valid_doms.append(this_domain)
        valid_ips.append(this_ip)
        this_line = make_entry(this_domain, this_ip)
        print(this_line, f = f)
    f.close()

    f3 = open('PROJ2-HNS.txt', 'w')
    f1 = open('PROJ2-DNSTS1.txt', 'r')
    f2 = open('PROJ2-DNSTS2.txt', 'r')

    for line in f1:
        this_rand = randint(1, 4)
        if(this_rand != 3):
            print(line, f=f3)
        else:
            dom = gen_domain()
            ip = gen_ip()
            line = make_entry(dom, ip)
            print(line, f=f3)


            
    for line in f2:
        this_rand = randint(1, 4)
        if(this_rand != 3):
            print(line, f=f3)
        else:
            dom = gen_domain()
            ip = gen_ip()
            line = make_entry(dom, ip)
            print(line, f=f3)

    

    f1.close()
    f2.close()
    f3.close()

def check_answers():
    f = open('RESOLVED.txt', 'r')
    num_lines = 0
    for line in f:
        num_lines = num_lines + 1
        split_up = line.split(" ")
        first = split_up[0]
        second = split_up[1]
        if first not in valid_doms:
            print("{} not a valid domain".format(first))
        if(valid_ips[valid_doms.index(first)] != second):
            print("domain {} does not match ip {}".format(first, second))

    f.close()
    f = open('PROJ2-HNS.txt', 'r')

    for line in f:
        num_lines = num_lines - 1
    f.close()

    if(num_lines == 1):
        return "it worked!"
    
        
                
    
    
    

if __name__ == "__main__":
    os.system("python2 ts1.py")
    os.system("python2 ts2.py")
    os.system("python2 ls.py")
    os.system("python2 client.py")

