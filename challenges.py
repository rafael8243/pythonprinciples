## Challenge 1 - Capital indexes

def capital_indexes(s):
    r = [] 
    for i,c in enumerate(s):
        if c.isupper():
            r.append(i)
    
    print(s,' = ',r)
    return r
    

capital_indexes("HeLlO")
capital_indexes("HI")

## Challenge  2 - Middle Letter

def mid(s):
    b = len(s)
    if b % 2 == 0:
        r = ''
    else:
        r = s[int(b/2)]
    
    print(s, ' = ',r)
    return r
        
mid("abc")
mid("baba")

## Challenge  3 - Online status

def online_count(l):
    n = [ 1 for u in l.values() if u == 'online']
    print(sum(n),'people online.')
    return sum(n)
    
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

online_count(statuses)

## Challenge  4 - Randomness

def random_number():
    import random
    r = random.randint(1,100)
    print(r)
    return(r)
    

random_number()
random_number()
random_number()

## Challenge  5 - Type check

def only_ints(a,b):
    r = type(a) == int and type(b) == int
    print('Does {} and {} are int numbers?\n - Resp: {}\n'.format(a,b,r))
    return r

only_ints(1, 2)
only_ints("a", 9)

## Challenge  6 - Double letters

def double_letters(s):
    r = any([ a == b for a,b in zip(s,s[1:])])
    print(r)
    return(r)
    
double_letters('hello')
double_letters('nonono')

## Challenge  7 - Capital indexes

def add_dots(s):
    r = '.'.join(s)
    print(r)
    return r

def remove_dots(s):
    r = s.split('.')
    r = ''.join(r)
    print(r)
    return r
    
def remove_dots2(s):
    # Permite string com '.'
    
    r = [s[i] for i in range(0,len(s),2)]
    r = ''.join(r)
    print(r)
    return r

add_dots("test") 
remove_dots2("t.e.s.t")

## Challenge  8 - Capital indexes
## Challenge  9 - Capital indexes
## Challenge 10 - Capital indexes
