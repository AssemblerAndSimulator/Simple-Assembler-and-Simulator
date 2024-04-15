#FOR THE LOVE OF GOD PLEASE FIX LW AND SW
global pc
pc=0
branch=False
opcodedict = {
    'R': ['0110011'],
    'I': ['0000011', '0010011', '1100111'],
    'S': ['0100011'],
    'B': ['1100011'],
    'U': ['0110111', '0010111'],
    'J': ['1101111']
}
regabidict = {
    'zero': '00000000000000000000000000000000',
    'ra': '00000000000000000000000000000000',
    'sp': '00000000000000000000000100000000',
    'gp': '00000000000000000000000000000000',
    'tp': '00000000000000000000000000000000',
    't0': '00000000000000000000000000000000',
    't1': '00000000000000000000000000000000',
    't2': '00000000000000000000000000000000',
    'fp': '00000000000000000000000000000000',
    's1': '00000000000000000000000000000000',
    'a0': '00000000000000000000000000000000',
    'a1': '00000000000000000000000000000000',
    'a2': '00000000000000000000000000000000',
    'a3': '00000000000000000000000000000000',
    'a4': '00000000000000000000000000000000',
    'a5': '00000000000000000000000000000000',
    'a6': '00000000000000000000000000000000',
    'a7': '00000000000000000000000000000000',
    's2': '00000000000000000000000000000000',
    's3': '00000000000000000000000000000000',
    's4': '00000000000000000000000000000000',
    's5': '00000000000000000000000000000000',
    's6': '00000000000000000000000000000000',
    's7': '00000000000000000000000000000000',
    's8': '00000000000000000000000000000000',
    's9': '00000000000000000000000000000000',
    's10': '00000000000000000000000000000000',
    's11': '00000000000000000000000000000000',
    't3': '00000000000000000000000000000000',
    't4': '00000000000000000000000000000000',
    't5': '00000000000000000000000000000000',
    't6': '00000000000000000000000000000000'
}
abidict={'00000': 'zero', '00001': 'ra', '00010': 'sp', '00011': 'gp', '00100': 'tp', '00101': 't0', '00110': 't1', '00111': 't2', '01000': 'fp', '01001': 's1', '01010': 'a0', '01011': 'a1', '01100': 'a2', '01101': 'a3', '01110': 'a4', '01111': 'a5', '10000': 'a6', '10001': 'a7', '10010': 's2', '10011': 's3', '10100': 's4', '10101': 's5', '10110': 's6', '10111': 's7', '11000': 's8', '11001': 's9', '11010': 's10', '11011': 's11', '11100': 't3', '11101': 't4', '11110': 't5', '11111': 't6'}
memory_add={'00010000':'00000000000000000000000000000000',
'00010004':'00000000000000000000000000000000',
'00010008':'00000000000000000000000000000000',
'0001000c':'00000000000000000000000000000000',
'00010010':'00000000000000000000000000000000',
'00010014':'00000000000000000000000000000000',
'00010018':'00000000000000000000000000000000',
'0001001c':'00000000000000000000000000000000',
'00010020':'00000000000000000000000000000000',
'00010024':'00000000000000000000000000000000',
'00010028':'00000000000000000000000000000000',
'0001002c':'00000000000000000000000000000000',
'00010030':'00000000000000000000000000000000',
'00010034':'00000000000000000000000000000000',
'00010038':'00000000000000000000000000000000',
'0001003c':'00000000000000000000000000000000',
'00010040':'00000000000000000000000000000000',
'00010044':'00000000000000000000000000000000',
'00010048':'00000000000000000000000000000000',
'0001004c':'00000000000000000000000000000000',
'00010050':'00000000000000000000000000000000',
'00010054':'00000000000000000000000000000000',
'00010058':'00000000000000000000000000000000',
'0001005c':'00000000000000000000000000000000',
'00010060':'00000000000000000000000000000000',
'00010064':'00000000000000000000000000000000',
'00010068':'00000000000000000000000000000000',
'0001006c':'00000000000000000000000000000000',
'00010070':'00000000000000000000000000000000',
'00010074':'00000000000000000000000000000000',
'00010078':'00000000000000000000000000000000',
'0001007c':'00000000000000000000000000000000'
}

def bin_decimal(bin):
  dec = 0
  for i in range(0, len(bin)):
    dec += (2**i) * int(bin[len(bin) - 1 - i])
  return dec

def bin_hex(bin):
  dict1={'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'a','1011':'b','1100':'c','1101':'d','1110':'e','1111':'f'}
  result=''
  for i in range(0,32,4):
    result+=dict1[bin[i:i+4]]
  return result
def instrtype(binaryline):
  opcode = binaryline[-7:]
  for i in opcodedict:
    if opcode in opcodedict[i]:
      return i
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

#-------------------------------R TYPE---------------------------------
#R type instruction functions!!!!!!!!!!!
def add(rs1, rs2, rd):
  carry = 0
  result = ""
  rs1data = regabidict[rs1]
  rs2data = regabidict[rs2]
  for i in range(31, -1, -1):
    bit_sum = int(rs1data[i]) + int(rs2data[i]) + carry
    carry = bit_sum // 2
    result = str(bit_sum % 2) + result
  regabidict[rd] = result


def sub(rs1, rs2, rd):
  borrow = 0
  result = ""
  rs1data = regabidict[rs1]
  rs2data = regabidict[rs2]
  for i in range(31, -1, -1):
    digit1 = int(rs1data[i])
    digit2 = int(rs2data[i])
    subtraction = digit1 - digit2 - borrow
    if subtraction < 0:
      subtraction += 2
      borrow = 1
    else:
      borrow = 0
    result = str(subtraction) + result
  regabidict[rd] = result


def slt(rs1, rs2, rd):
  if (regabidict[rs1][0] == '1' and regabidict[rs2][0] == '0'):
    regabidict[rd] = '0' * 31 + "1"
  elif regabidict[rs1][0] == '0' and regabidict[rs2][0] == '0':
    if int(regabidict[rs1]) < int(regabidict[rs2]):
      regabidict[rd] = '0' * 31 + '1'
  elif regabidict[rs1][0] == "1" and regabidict[rs2][0] == "1":
    if int(regabidict[rs1]) > int(regabidict[rs2]):
      regabidict[rd] = "0" * 31 + "1"
  else:
    pass
  return


def sltu(rs1, rs2, rd):
  if int(regabidict[rs1]) < int(regabidict[rs2]):
    regabidict[rd] = '0' * 31 + '1'
  return


def xor(rs1, rs2, rd):
  result=""
  for i in range(0,32):
    result+=str((int(regabidict[rs1][i]))^(int(regabidict[rs2][i])))
  regabidict[rd] = result
  return


def sll(rs1, rs2, rd):
  shift =(regabidict[rs2][-5:])
  dec = bin_decimal(shift)
  s1 = regabidict[rs1]
  s1 = s1 + ('0' * dec)
  regabidict[rd] = s1[-32:]
  return


def srl(rs1, rs2, rd):
  shift =(regabidict[rs2][-5:])
  dec = bin_decimal(shift)
  s1 = regabidict[rs1]
  s1 = ('0' * dec) + s1
  regabidict[rd] = s1[:32]
  return


def Or(rs1, rs2, rd):
  result=""
  for i in range(0,32):
    result+=str((int(regabidict[rs1][i]))|(int(regabidict[rs2][i])))
  regabidict[rd] = result
  return

def And(rs1, rs2, rd):
  result=""
  for i in range(0,32):
    result+=str((int(regabidict[rs1][i]))&(int(regabidict[rs2][i])))
  regabidict[rd] = result
  return


#------------------------I type---------------------------------------
def addi(rd,rs1,imm):
  imm=(32-len(imm))*imm[0]+imm
  regabidict['temp']=imm
  add(rs1,'temp',rd)
  del regabidict['temp']
  return

def lw(rd,rs1,imm):
  imm = (32 - len(imm)) * imm[0] + imm
  addi('temp2',rs1, imm)
  regabidict[rd]=memory_add[bin_hex(regabidict['temp2'])]
  del regabidict['temp2']
  return

def jalr(rd,x6,imm):
  
  
  
  return
#------------------------B type---------------------------------------
def beq(rs1, rs2, imm):
  if regabidict[rs1] == regabidict[rs2]:
    global pc
    global branch
    pc = pc + bin_decimal(imm) // 4
    branch=True


def bne(rs1, rs2, imm):
  if regabidict[rs1] != regabidict[rs2]:
    global pc
    global branch
    pc = pc + bin_decimal(imm) // 4
    branch=True


def blt(rs1, rs2, imm):
    if regabidict[rs1] < regabidict[rs2]:
      global pc
      global branch
      pc = pc + bin_decimal(imm) // 4
      branch=True

def bge(rs1, rs2, imm):
    if regabidict[rs1] > regabidict[rs2]:
      global pc
      global branch
      pc = pc + bin_decimal(imm) // 4
      branch=True

#------------------------------Utype ---------------------------------
def lui(rd, imm):
  bin_pc = format(pc, '032b')
  regabidict['temp2']=bin_pc
  addi(rd, 'temp2', imm)
  del regabidict['temp2']

def auipc(rd, imm):
  regabidict[rd] = imm

#-----------------------------S type--------------------------------------
def sw(rs2,rs1,imm):
  imm = (32 - len(imm)) * imm[0] + imm
  addi('temp2',rs1, imm)
  memory_add[bin_hex(regabidict['temp2'])]=regabidict[rs2]
  del regabidict['temp2']
  return

#-----------------------------JType-----------------------------------------
def jal(rd,imm):
  imm = (32 - len(imm)) * imm[0] + imm
  return


#===========================================================================
#===========================================================================


def Rtype(binaryline):
  funct3 = binaryline[-15:-12]
  funct7 = binaryline[:7]
  funct3dict = {
      '001': sll,
      '010': slt,
      '011': sltu,
      '100': xor,
      '101': srl,
      '110': Or,
      '111': And
  }
  rd = abidict[binaryline[-12:-7]]
  rs1 = abidict[binaryline[-20:-15]]
  rs2 = abidict[binaryline[-25:-20]]
  if funct3 == '000':
    if funct7 == '0000000':
      add(rs1, rs2, rd)
    elif funct7 == '0100000':
      sub(rs1, rs2, rd)
  elif funct7 == '0000000':
    funct3dict[funct3](rs1, rs2, rd)


#xor('a1', 'a0', 'a2')
#print(regabidict['a2'])
#------------------
def Itype(binaryline):
  imm=binaryline[:12]
  rs1=abidict[binaryline[12:17]]
  rd=abidict[binaryline[20:25]]
  opcode=binaryline[25:]
  opdict={'0000011':lw,'0010011':addi,'1100111':jalr}
  opdict[opcode](rd,rs1,imm)
#---------------------

def Stype(binaryline):
    imm=binaryline[:7]+binaryline[-12:-7]
    rs1=abidict[binaryline[-20:-15]]
    rs2=abidict[binaryline[-25:-20]]
    opcode=binaryline[-7:]
    sw(rs2, rs1, imm)

#---------------------

def Btype(binaryline):
    imm=binaryline[0]+binaryline[-8]+binaryline[1:7]+binaryline[-12:-7]
    rs1=abidict[binaryline[-20:-15]]
    rs2=abidict[binaryline[-25:-20]]
    funct3=binaryline[-15:-12]
    opcode=binaryline[-7:]
    funct3dict={
        '000': beq,
        '001': bne,
        '100': bge,
        '110': blt,
    }
    funct3dict[funct3](rs1, rs2, imm)

#---------------------
def Jtype(binaryline):
    imm=binaryline[0]+binaryline[-20:-12]+binaryline[-21]+binaryline[1:12]
    rd=abidict[binaryline[-12:-7]]
    jal(rd,imm)
    
#---------------------
def Utype(binaryline):
  rd = abidict[binaryline[-12:-7]]
  imm = binaryline[-32:-12]

  if imm[0] == '0':
    imm = '000000000000' + imm
  elif imm[0] == '1':
    imm = '111111111111' + imm

  if binaryline[:7] == '0110111':
    lui(rd, imm)
  elif binaryline[:7] == '0010111':
    auipc(rd, imm)


file1='file.txt'
file2='result.txt'
f1=open(file1,'r')
mainlst=f1.readlines()
for i in range(len(mainlst)):
  mainlst[i]=mainlst[i].strip()
f1.close()
f2=open(file2,'w')
finallist=[]
while mainlst[pc]!='00000000000000000000000001100011':
  type=instrtype(mainlst[pc])
  if type=='R':
    Rtype(mainlst[pc])
  elif type=='I':
    Itype(mainlst[pc])
  elif type=='S':
    Stype(mainlst[pc])
  elif type=='B':
    Btype(mainlst[pc])
  elif type=='U':
    Utype(mainlst[pc])
  elif type=='J':
    Jtype(mainlst[pc])
  if not branch:
    pc+=1
  binpc='0b'+binconv(pc*4)
  line=binpc
  for i in regabidict:
    line=line+" 0b"+regabidict[i]
  finallist.append(line+'\n')
  branch=False
finallist.append(line+'\n')
for i in memory_add:
  line='0x'+i+': 0b'+memory_add[i]+'\n'
  finallist.append(line)
f2.writelines(finallist)
f2.close()
    
  

