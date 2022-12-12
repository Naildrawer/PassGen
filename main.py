import random as r
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
neodnoz = 'il1Lo0O'
chars = ''

def count():
 kpass = input('Сколько паролей сгенерировать - ')
 while kpass.isdigit() == False:
   print('Введите корректное знаечение')
   kpass = input('Сколько паролей сгенерировать - ')
 return int(kpass)

def lenp():
 lenpass = input('Какой длины? ')
 while lenpass.isdigit() == False:
   print('Какой длины? ')
   lenpass = input('Какой длины? ')
 return int(lenpass)
  
def digit():
  cifrpass = input('Включать ли цирфы 0123456789?(Y/N) ')
  while cifrpass.lower() not in ['y', 'n']:
    print('Введите кореектное значение')
    cifrpass = input('Включать ли цирфы 0123456789?(Y/N) ')
  return cifrpass 

def islow():
 propispass = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?(Y/N) ')
 while propispass.lower() not in ['y', 'n']:
    print('Введите кореектное значение')
    propispass = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?(Y/N) ')
 return propispass

def isstroch():
  strochpass = input('Включать ли строчные буквы? abcdefghijklmnopqrstuvwxyz(Y/N)')
  while strochpass.lower() not in ['y', 'n']:
    print('Введите кореектное значение')
    strochpass = input('Включать ли строчные буквы? abcdefghijklmnopqrstuvwxyz(Y/N) ')
  return strochpass   

def ispropis(): 
  propispass = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?(Y/N) ')
  while propispass.lower() not in ['y', 'n']:
    print('Введите кореектное значение')
    propispass = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?(Y/N) ')
  return propispass
def isspec():  
  specpass = input('Включать ли спецсимволы? !#$%&*+-=?@^_(Y/N) ')
  while specpass.lower() not in ['y', 'n']:
    print('Введите кореектное значение')
    specpass = input('Включать ли спецсимволы? !#$%&*+-=?@^_(Y/N) ')
  return specpass
def delsymb():  
  neodnoz = input('Искючать ли неоднозначные символы? il1Lo0O  Y/N ')
  while neodnoz.lower() not in ['y', 'n']:
    print('Введите кореектное значение')
    neodnoz = input('Включать ли спецсимволы? !#$%&*+-=?@^_(Y/N) ')
  return(neodnoz) 

def genchars():
  chars = ""
  if cifrpass.lower() == "y":
    chars += digits
  if propispass.lower() == "y":
    chars += lowercase_letters
  if strochpass.lower() == 'y':
    chars += uppercase_letters
  if specpass.lower() == 'y':
    chars += punctuation
  if neodnoz.lower() == 'y':
    for c in "il1Lo0O":
      chars = chars.replace(c, '')
  return chars
def gen(lenpass, chars):
  password =''
  for i in range(lenpass):
    password += r.choice(chars)
  print(password)
kpass = count()
lenpass = lenp()
cifrpass = digit()
propispasspropispass = islow()
strochpass = isstroch()
propispass = ispropis()
specpass =  isspec()
neodnoz = delsymb()
chars = genchars()
for _ in range(kpass):
  gen(lenpass, chars)