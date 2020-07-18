# Hextroadinary

**Challenge link:** _https://ctflearn.com/challenge/158_

 **Challenge category:** _Cryptography_

**Challenge points:** _30 points_

**Challenge description:** 

Meet ROXy, a coder obsessed with being exclusively the worlds best hacker. She specializes in short cryptic hard to decipher secret codes. The below hex values for example, she did something with them to generate a secret code, can you figure out what? Your answer should start with 0x.            

0xc4115 0x4cf8

**Challenge solution:**

First, take out '0x' in front of each hex. Then, using XOR Calculator from http://xor.pw/# key in each individual input. Then click on 'Calculate XOR'. Then you would get the answer: c0ded. After this, you would need to add the 0x in front of your calculated XOR to give you the flag: 0xc0ded.
