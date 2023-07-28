##### Encryption function #####
def encrypt(msg, shift):
  new_msg = ""
  for i in range(0, len(msg)):
    char = ord(msg[i]) + shift
    if(char > 122):
      char = char - 26
    elif(ord(msg[i]) < 97 or ord(msg[i]) > 122):
      new_msg += msg[i]
      continue
    new_msg += chr(char)
  print(new_msg)
  
##### Decryption function #####
def decrypt(msg, shift):
  new_msg = ""
  for i in range(0, len(msg)):
    char = ord(msg[i]) - shift
    if(char > 71 and char < 97):
      char = char + 26
    elif(ord(msg[i]) < 97 or ord(msg[i]) > 122):
      new_msg += msg[i]
      continue
    new_msg += chr(char)
  print(new_msg)
      
repeat = 'yes' ## default value
#########  iterative loop
while(repeat == 'yes'):
  order = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
  msg = input("Type your message:\n").lower()
  shift = int(input("Type shift number:\n"))
  if(order == "encode"):
    encrypt(msg, shift)
  elif(order == "decode"):
    decrypt(msg, shift)
  else:
    print("error")
  repeat = input("Type 'yes' if you want to go again, otherwise type 'no'.\n")

##### combine function encryption and decryption both#####
def caeser(cipher_direction, msg, shift):
  if(cipher_direction == "decode"):
    shift *= -1
  new_msg = ""
  for letter in msg:
    char = ord(letter) + shift
    if(char > 122):
      char = char - 26
    elif(ord(letter) < 97 or ord(letter) > 122):
      new_msg += letter
      continue
    elif(char > 71 and char < 97):
      char = char + 26
    new_msg += chr(char)
  print(new_msg)

repeat = 'yes' ## default value
#########  iterative loop
while(repeat == 'yes'):
  direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
  msg = input("Type your message:\n").lower()
  shift = int(input("Type shift number:\n"))
  caeser(cipher_direction = direction, shift = shift, msg = msg)
  repeat = input("Type 'yes' if you want to go again, otherwise type 'no'.\n")

    

