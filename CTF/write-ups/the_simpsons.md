## The Simpsons
Challenge link: https://ctflearn.com/challenge/160


Challenge category: Cryptography, hard 

Challenge points: 80 points

Challenge description:

Ya know, I was thinking... wouldn't the Simpsons use octal as a base system? They have 8 fingers... Oh, right! The problem! Ummm, something seems odd about this image... https://mega.nz/#!yfp1nYrQ!LOz_eucuKkjAaDqVvz3GWgbfdKWn8BhussKZbx6bUMg

Challenge solution:

 1. firstly, go to the link provided and download it as jpg.

 2. open the jpg with notepad -- in case there is something hidden. 
 We open it in **notepad or cyber chef** is to check if there are any hidden text in the meta data of the photo which in this case there  is!
 this will show a series of garbled characters on the notepad.
   such as : **"L&@��dQ�Q15ǭ��z"**

    

> We open it in notepad or cyber chef is to check if there are any
> hidden text in the meta data of the photo which in this case there is!

3. scroll down to the bottom, there are lines of python code 
   the python code states that: 
   
	   
	   encoded = 152 162 152 145 162 167 150 172 153 162 145 170 141 162
	   
	   key = chr(SolutionToDis(110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151    156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164    150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154    165 163 040 146 157 165 162 051)).
	   
	   key = key + key + chr(ord(key)-4). 
	   print(DecodeDat(key=key,text=encoded))
	   
   
4. decode the `encoded` and key from the code above using octal
   this is done by using cyberchef, choose "from octal"
   then put in the series of encoded numbers `(152 162 152 145 162 167 150 172 153 162 145 170 141 162)` as input
	
  >why use octal? -- because it is mentioned by the description :
  "wouldn't the Simpsons use octal as a base system"

  
5. After decoding the encoded text above, you would get text like `jrjerwhzkrexar`
   it suggests that after converting this series of number from octal, it returns you the original text, which is        `jrjerwhzkrexar`.
   Check out the website of cyberchef: https://gchq.github.io/CyberChef/#recipe=From_Octal('Space')&input=MTUyIDE2MiAxNTIgMTQ1IDE2MiAxNjcgMTUwIDE3MiAxNTMgMTYyIDE0NSAxNzAgMTQxIDE2Mg
   
6. After which you can get key using the instructions as stated in the hex-dumped value of the picture. The instructions are as follows:
- 'How much did Maggie originally cost? 
- Divided by 8, to the nearest integer, and then plus four)'

7. search the answers of the question in key online and do calculation get `110`

   for the answer of the first question, it can be found on this website:
   https://mashable.com/2014/08/21/simpsons-facts/#:~:text=1.,raising%20a%20child%20in%201989.
   
   it gives `$847.67`
   then `847.67 / 8`, to the nearest integer, it will be `110`
   
8. follow the key - `use chr(the result of the key)`
 get key = n
   
    as the code states: `chr(the solution)`
   > **chr()** means **convert the number to letter according to the ACSII table**:
   the table can be found here : http://www.asciitable.com/
   
   the letter returned is `n` 
   
9. then the line below gives a new value of 
`key = key + key + chr(ord(key)-4)`, 
get **new key** as `nnj`

	  key is assigned to `key + key + chr(ord(key)-4)`
	   `key + key = n + n = nn`
	   then `chr(ord(key)-4)`:
    > **ord()** means to **convert the key value 
     back to the number according to the ascii table**
	   
	  so it gives value as 110, then `110 - 4 = 106`
	   so `chr(ord(key)-4) == chr(106) == j`
	   so `key = nnj` 
	   
10. finally, use the new key to decipher the text `jrjerwhzkrexar`

	   as it says need to decode the text `jrjerwhzkrexar`, 
	   it will be done on cyberchef again
	   use **vigenere decoded**, use **nnj as keyword**, put `jrjerwhzkrexar` in the input window 
	   then it will return `wearenumberone`
   
12. get the flag `wearenumberone`, submit 
