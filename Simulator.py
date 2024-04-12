global pc
pc=1
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
    'sp': '00000000000000000000000000000000',
    'gp': '00000000000000000000000000000000',
    'tp': '00000000000000000000000000000000',
    't0': '00000000000000000000000000000000',
    't1': '00000000000000000000000000000000',
    't2': '00000000000000000000000000000000',
    'fp': '00000000000000000000000000000000',
    's1': '00000000000000000000000000000000',
    'a0': '00000000000000000000000000000011',
    'a1': '00000000000000000000000000000010',
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
memory_add={}

def bin_decimal(bin):
  dec = 0
  for i in range(0, len(bin)):
    dec += (2**i) * int(bin[len(bin) - 1 - i])
  return dec


def instrtype(binaryline):
  opcode = binaryline[-7:]
  for i in opcodedict:
    if opcode in opcodedict[i]:
      return i


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
  regabidict[rd]=imm
  add(rd,rs1,rd)
  return

def lw(rd,rs1,imm):
  addi(rd,rs1,imm)
  
  
  return
  

def jalr(rd,x6,imm):
  
  
  
  return
#------------------------B type---------------------------------------
def beq(rs1, rs2, imm):
  if regabidict[rs1] == regabidict[rs2]:
    global pc
    pc = pc + bin_decimal(imm) // 4


def bne(rs1, rs2, imm):
  if regabidict[rs1] != regabidict[rs2]:
    global pc
    pc = pc + bin_decimal(imm) // 4

def blt(rs1, rs2, imm):
    if regabidict[rs1] < regabidict[rs2]:
    global pc
    pc = pc + bin_decimal(imm) // 4

def bge(rs1, rs2, imm):
    if regabidict[rs1] > regabidict[rs2]:
    global pc
    pc = pc + bin_decimal(imm) // 4

#------------------------------Utype ---------------------------------
def lui(rd, imm):
  bin_pc = format(pc, '032b')
  regabidict['temp']=bin_pc
  addi(rd, 'temp', imm)
  del regabidict['temp']

def auipc(rd, imm):
  regabidict[rd] = imm

#-----------------------------S type--------------------------------------
def sw(rs2,rs1,imm):
  imm = (32 - len(imm)) * imm[0] + imm
  rs2data = regabidict[rs1] + imm
  memory_add[rs2data]=regabidict[rs2]
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
  rs1=binaryline[12:17]
  rd=binaryline[20:25]
  opcode=binaryline[25:]
  opdict={'0000011':lw,'0010011':addi,'1100111':jalr}
#---------------------

def Stype(binaryline):
    imm=binaryline[:7]+binaryline[-12:-7]
    rs1=regabidict[binaryline[-20:-15]]
    rs2=regabidict[binaryline[-25:-20]]
    opcode=binaryline[-7:]
    sw(rs2, rs1, imm)

#---------------------

def Btype(binaryline):
    imm=binaryline[0]+binaryline[-8]+binaryline[1:7]+binaryline[-12:-7]
    rs1=regabidict[binaryline[-20:-15]]
    rs2=regabidict[binaryline[-25:-20]]
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
    rd=binaryline[-12:-7]
    opcode=binaryline[-7:]
    jal(rd,imm)
    
#---------------------
def Utype(binaryline):
  rd = binaryline[-12:-7]
  imm = binaryline[-32:-12]

  if imm[0] == '0':
    imm = '000000000000' + imm
  elif imm[0] == '1':
    imm = '111111111111' + imm

  if binaryline[:7] == '0110111':
    lui(rd, imm)
  elif binaryline[:7] == '0010111':
    auipc(rd, imm)

    

    
  

