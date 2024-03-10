def readassembly():
  f1=open('file.txt','r')
  lst=f1.readlines()
  f1.close()
  return lst
def binconv(num):
  numbin=''
  if num<0:
    num=2**32+num
  while num>0:
    numbin=str(num%2)+numbin
    num//=2
  if len(numbin)<32:
    numbin="0"*(32-len(numbin))+numbin
  else:
    numbin=numbin[-32:]
  return numbin
regdict={'x0':'00000','x1':'00001','x2':'00010','x3':'00011','x4':'00100','x5':'00101','x6':'00110','x7':'00111','x8':'01000','x9':'01001','x10':'01010','x11':'01011','x12':'01100','x13':'01101','x14':'01110','x15':'01111','x16':'10000','x17':'10001','x18':'10010','x19':'10011','x20':'10100','x21':'10101','x22':'10110','x23':'10111','x24':'11000','x25':'11001','x26':'11010','x27':'11011','x28':'11100','x29':'11101','x30':'11110','x31':'11111'}
abidict={'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100','t0':'00101','t1':'00110','t2':'00111','s0':'01000','fp':'01000','s1':'01001','a0':'01010','a1':'01011','a2':'01100','a3':'01101','a4':'01110','a5':'01111','a6':'10000','a7':'10001','s2':'10010','s3':'10011','s4':'10100','s5':'10101','s6':'10110','s7':'10111','s8':'11000','s9':'11001','s10':'11010','s11':'11011','t3':'11100','t4':'11101','t5':'11110','t6':'11111'}
#gunika
instrtypes={"R":['add','sub','slt','sltu','and','or','xor','sll','srl'],"I":["lw","addi","sltiu","jalr"],"J":["jal"],"S":["sw"],"B":["bew","bne","blt","bge","bltu","bgeu"],"U":["lui","auipc"]}
def identifyinstrtype(str1):
  for i in instrtypes:
    if str1 in instrtypes[i]:
      return i
#khushi
def identifyRinstr(l):
  return 0
def identifyIinstr(lst):
  opcodes={'lw':'0000011','addi':'0010011','sltiu':'0010011','jalr':'1100111'}
  funct3={'lw':'010','addi':'000','sltiu':'011','jalr':'000'}
  a=''
  opc=lst[0]
  rd=lst[1]
  rs1=lst[2]
  imm=lst[3]
  if lst[0]=='lw':
    rs1,imm=imm,rs1
  a=binconv(int(imm))[-12:]+abidict[rs1]+funct3[opc]+abidict[rd]+opcodes[opc]
  return a

def identifyJinstr(lst):
  return 0
#kanu
def identifyBinstr(lst):
    b_funct3={'beq':'000','bne':'001','blt':'100','bge':'101','bltu':'110','bgeu':'111'}
    lst_0='1100011'
    lst_1=regdict(lst[1])
    lst_2=regdict(lst[2])
    bf_3=b_funct3[lst[0]]
    
    lst_3=converttobinary(lst[3])
    lst_3=str(lst_3)
    if len(lst_3)<12:
      lst_3=((12-(len(lst_3)))*'0')+lst_3
    
  
def identifyUinstr(lst):
  return 0
def identifySinstr(lst):
  return 0
def converttobinary():
  return 0


mainlst=readassembly()
for i in mainlst:
  newi=i.replace(","," ").replace("("," ").replace(")"," ")
  a=newi.split()
  type=identifyinstrtype(a[0])
  if type=='I':
    print(identifyIinstr(a))



