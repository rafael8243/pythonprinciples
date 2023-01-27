## Challenge 1 - Capital indexes
## ================================================================================

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
## ================================================================================

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
## ================================================================================

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
## ================================================================================

def only_ints(a,b):
    r = type(a) == int and type(b) == int
    print('Does {} and {} are int numbers?\n - Resp: {}\n'.format(a,b,r))
    return r

only_ints(1, 2)
only_ints("a", 9)

## Challenge  6 - Double letters
## ================================================================================

def double_letters(s):
    r = any([ a == b for a,b in zip(s,s[1:])])
    print(r)
    return(r)
    
double_letters('hello')
double_letters('nonono')

## Challenge  7 - Capital indexes
## ================================================================================

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
## ================================================================================

def count(s):
    r = s.count('-')+1
    print('{} possui {} sílabas'.format(s,r))
    return r
    
count("ho-tel")
count("cat")
count("met-a-phor")
count("ter-min-a-tor")

## Challenge  9 - Anagrams
## ================================================================================

def is_anagram(a,b):
    
    r = sorted(a) == sorted(b)

    print('Does {} and {} are anagrams?\n - {}.\n'.format(a,b,r))
    return r
    

is_anagram("typhoon", "opython") 
is_anagram("Alice", "Bob")

# Better solution: count letters from each word and compare values: numeric comparison:

def count_letters(s):
    return {l: s.count(l) for l in s}       # returns a dict with sum of each letter

def is_anagram(a, b):
    return count_letters(a) == count_letters(b)

## Challenge 10 - Flatten a list
## ================================================================================

def flatten(l):
    
    r = []
    
    for sl in l:
        for i in sl:
          r.append(i)  
    
    print(r)
    return r

flatten([[1, 2], [3, 4]])

## Challenge 10 - Capital indexes
## ================================================================================

## Challenge 10 - Capital indexes
## ================================================================================

## Challenge 10 - Capital indexes
## ================================================================================

## Challenge 10 - Capital indexes
## ================================================================================

## Challenge 10 - Capital indexes
## ================================================================================

## Challenge 10 - Capital indexes
## ================================================================================

## Challenge 10 - Capital indexes
## ================================================================================
