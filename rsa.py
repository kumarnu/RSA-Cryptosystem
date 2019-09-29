# -*- coding: utf-8 -*-
"""RSA_algorithm.ipynb
Team Members:
Anubhav Maity
Nitish Kumar
The program is written on Python3.6
"""

# import sys
# print(sys.version)

import random

bearcatti = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def ee_gcd(a,b):
  if b==0:
    return a, 1, 0
  else:
    r = a%b
    q = a//b
    g,s,t = ee_gcd(b,r)
    s_temp = s
    s = t
    t = s_temp - t*q
    return g,s,t

def power(a, n, p):
  res = 1
  a = a % p
  while n > 0:
    if ((n & 1) == 1):
      res = (res * a) % p
    n = n >> 1
    a = (a * a) % p
  return res

def is_prime(n, k):
  if (n <= 1 or n == 4):
    return False
  if (n <= 3):
    return True
  while (k > 0):
    a = 2 + (random.randrange(2, n - 2) % (n - 4))
    if (power(a, n - 1, n) != 1):
      return False
    k = k - 1
  return True

def find_prime():
  p_prime = False
  q_prime = False

  while (p_prime == False or q_prime == False ):
    p_random = random.randrange(1000000000000000, 5000000000000000)
    q_random = random.randrange(1000000000000000, 5000000000000000)
    if (is_prime(p_random, 3) == True):
      p = p_random
      p_prime = True
    if (is_prime(q_random, 3) == True):
      q = q_random
      q_prime = True
  return p, q

def compute_phi_n(p, q):
  return (p-1)*(q-1)

def encode_message(message):
  encoded_chars = []
  for char in message:
    encoded_chars.append(bearcatti.index(char.upper()))
  return encoded_chars

def decode_message(message):
  decoded_message = []
  for digit in message:
    decoded_message.append(bearcatti[digit])
  return "".join(decoded_message)

def horner(poly, x):  
  result = poly[0]   
  for i in range(1, len(poly)): 
    result = result*x + poly[i] 
  return result

def convert_to_decimal(elements, base):
  return horner(elements, base)

def convert_to_base(number, base):
  quotient = number
  base_list = []
  while quotient != 0:
    remainder = quotient % base
    base_list.insert(0, remainder)
    quotient = quotient//base
  return base_list

def get_private_key(e, phi_n):
  g, s, t = ee_gcd(e, phi_n)
  d = phi_n + s
  return d

def encrypt_message(m, e, n):
  decimal_message = convert_to_decimal(encode_message(m), 27)
  encrypted_message = power(decimal_message, e, n)
  return encrypted_message

def decrypt_message(m, d, n):
  decrypted_message =  power(m, d, n)
  return decode_message(convert_to_base(decrypted_message, 27))

def get_response_body(p, q, n, message, encrypted_message, decrypted_message):
  return {'p': p, 'q': q, 'n':n, 'M': message, 'C': encrypted_message, 'P': decrypted_message}

# submission = True is for handing purpose of the assignment
def rsa(submission=True, e=3, message = 'TEST'):
  try:
    while True:
      if not submission:
        e = int(input('Input a public key'))
      p, q = find_prime()
      phi_n = compute_phi_n(p, q)
      n = p*q
      g, s, t = ee_gcd(e, phi_n)
      if g == 1:
        if not submission:  
          message = input('Input message')
        d = get_private_key(e, phi_n)
        encrypted_message = encrypt_message(message, e, n)
        decrypted_message = decrypt_message(encrypted_message, d, n)
        return get_response_body(p, q, n, message, encrypted_message, decrypted_message)
  except Exception as e:
    print(e)

def main():
  
  print('For input: TEST')
  print(rsa())
  print('\n')

  print('For input: ANUBHAV')
  print(rsa(True, 3, 'ANUBHAV'))
  print('\n')
  
  print('For input: NITISH')
  print(rsa(True, 3, 'NITISH'))
  print('\n')

  print('For input: ALGORITHM')
  print(rsa(True, 3, 'ALGORITHM'))
  print('\n')

  print('For input: CRYPTOGRAPHY')
  print(rsa(True, 3, 'CRYPTOGRAPHY'))
  print('\n')

  print('For input: RASHID KARIM')
  print(rsa(True, 3, 'RASHID KARIM'))
  print('\n')

  print('For input: PROF KENNETH BERMAN')
  print(rsa(True, 3, 'PROF KENNETH BERMAN'))
  print('\n')

  print('For input: RIVEST SHAMIR ADLEMAN')
  print(rsa(True, 3, 'RIVEST SHAMIR ADLEMAN'))
  print('\n')

if __name__ == '__main__':
  main()
