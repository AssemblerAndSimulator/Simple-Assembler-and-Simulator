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
instrtypes={"R":['add','sub','slt','sltu','and','or','xor','sll','srl'],"I":["lw","addi","sltiu","jalr"],"J":["jal"],"S":["sw"],"B":["beq","bne","blt","bge","bltu","bgeu"],"U":["lui","auipc"]}
allinstr=['add','sub','slt','sltu','and','or','xor','sll','srl',"lw","addi","sltiu","jalr","jal","sw","beq","bne","blt","bge","bltu","bgeu","lui","auipc"]
def identifyinstrtype(str1):
  for i in instrtypes:
    if str1 in instrtypes[i]:
      return i
#khushi
def identifyRinstr(lst):
    rlist0='0110011'
    funct3={'add':'000', 'sub':'000', 'sll':'001', 'slt':'010', 'sltu':'011', 'xor':'100', 'srl':'101', 'or':'110', 'and':'111'}
    if lst[1] in regdict.keys():
      rlistrd=str(regdict[lst[1]])
    else:
      rlistrd=abidict[lst[1]]
    if lst[2] in regdict.keys():
      rlistr1=str(regdict[lst[2]])
    else:
      rlistr1=str(abidict[lst[2]])
    if lst[3] in regdict.keys():
      rlistr2=str(regdict[lst[3]])
    else:
      rlistr2=str(abidict[lst[3]])


    if lst[0]=='sub':
        funct7='0100000'
    else:
        funct7='0000000'
    
    result=funct7+rlistr2+rlistr1+funct3[lst[0]]+rlistrd+rlist0

    return result

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
  if rd in regdict.keys():
    rdbin=regdict[rd]
  else:
    rdbin=abidict[rd]
  if rs1 in regdict.keys():
    rs1bin=regdict[rs1]
  else:
    rs1bin=abidict[rs1] 
  a=binconv(int(imm))[-12:]+rs1bin+funct3[opc]+rdbin+opcodes[opc]
  return a

def identifyJinstr(lst):
    jlist0='1101111'
    if lst[1] in regdict.keys():
        jlistrd=str(regdict[lst[1]])
    else:
        jlistrd=str(abidict[lst[1]])

    label=int(lst[2])
    labelbin=binconv(label)
    x=labelbin[11:31]
    imm=x[0]+x[10:20]+x[9]+x[1:9]

    return imm+jlistrd+jlist0

#kanu
def identifyBinstr(lst):
    b_funct3={'beq':'000','bne':'001','blt':'100','bge':'101','bltu':'110','bgeu':'111'}
    lst_0='1100011'
    if lst[1] in regdict.keys():
      lst_1=regdict[lst[1]]
    else:
      lst_1=abidict[lst[1]]
    
    if lst[2] in regdict.keys():
      lst_2=regdict[lst[2]]
    else:
      lst_2=abidict[lst[2]]
    bf_3=b_funct3[lst[0]]
    
    lst_3=binconv(int(lst[3]))
    lst_3=lst_3[19:31]
    imm=lst_3
    imm_l=imm[0]+imm[2:8]
    imm_r=imm[8:12]+imm[1]
    b_f=imm_l+lst_2+lst_1+bf_3+imm_r+lst_0
    return b_f
    
  
def identifyUinstr(lst):
  if lst[0]=='lui':
    opcode = "0110111"
  else:
    opcode= "0010111"

  imm = binconv(int(lst[2]))
  imm_31_12 = imm[0:20]

  if lst[1] in regdict.keys():
    rd_bin = regdict[lst[1]]
  else:
    rd_bin = abidict[lst[1]]

  u_instr = imm_31_12 + rd_bin + opcode
  return u_instr

def identifySinstr(lst):
    lst_0='0100011'
    imm=binconv(int(lst[2]))
    imm=imm[20:32]
    reg=lst[3]
    if lst[1] not in regdict.keys():
      lst_1=abidict[lst[1]]
    else:
      lst_1=regdict[lst[1]]

    if reg not in regdict.keys():
      lst_3=abidict[reg]
    else:
      lst_3=regdict[reg]

    imm_l=imm[0:7]
    imm_r=imm[7:]
    funct3='010'
    s_f=imm_l+lst_1+lst_3+funct3+imm_r+lst_0
    return s_f
errorname=''
writelst=[]
def final():
  global errorname
  error=False
  vth=['beq','zero,zero,0']
  mainlst=readassembly()
  b=mainlst[-1].split()
  if (b==vth or b[1:]==vth)==False:
    errorname= ("syntax error: no virtual halt")
    error=True
  elif ('beq zero,zero,0' in mainlst[k] for k in range(len(mainlst))):
    errorname= ("syntax error: incorrectly used virtual halt")
    error=True
  else:
    for i in mainlst[:-1]:
      j=i.split()
      if i!='\n':
        newi=i.replace(","," ").replace("("," ").replace(")"," ")
        a=newi.split()
        if (a[0] not in allinstr) and (a[1] in allinstr):
          a=a[1:]
        elif (a[0] not in allinstr) and (a[1] not in allinstr):
          errorname=("syntax error: incorrect instruction")
          error=True
        type=identifyinstrtype(a[0])
        if type=='R':
          writelst.append(identifyRinstr(a)+'\n')
        elif type=='I':
          writelst.append(identifyIinstr(a)+'\n')
        elif type=='B':
          writelst.append(identifyBinstr(a)+'\n')
        elif type=='S':
          writelst.append(identifySinstr(a)+'\n')
        elif type=='J':
          writelst.append(identifyJinstr(a)+'\n')
        elif type=='U':
          writelst.append(identifyUinstr(a)+'\n')
      writelst.append("00000000000000000000000001100011")
      return error
a=final()
f1=open("result.txt",'w')
if a==False:
  f1.writelines(writelst)
else:
  f1.write(errorname)
f1.close()



