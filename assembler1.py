def readassembly():
  return 0
def binconv():
  return 0
#gunika

regdict={'x0':'00000','x1':'00001','x2':'00010','x3':'00011','x4':'00100','x5':'00101','x6':'00110','x7':'00111','x8':'01000','x9':'01001','x10':'01010','x11':'01011','x12':'01100','x13':'01101','x14':'01110','x15':'01111','x16':'10000','x17':'10001','x18':'10010','x19':'10011','x20':'10100','x21':'10101','x22':'10110','x23':'10111','x24':'11000','x25':'11001','x26':'11010','x27':'11011','x28':'11100','x29':'11101','x30':'11110','x31':'11111'}
instrtypes={"R":[],"I":[],"J":[],"S":[],"B":[],"U":[]}
def identifyinstrtype():
  #ifelse for each
  return 0
#khushi
def identifyRinstr(l):
  return 0
def identifyIinstr(lst):
  return 0
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
    b_f=
    


def identifyUinstr(lst):
  return 0
def identifySinstr(lst):
  return 0
def converttobinary():
  return 0