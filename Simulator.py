opcodedict={'R':['0110011'],'I':['0000011','0010011','1100111'],'S':['0100011'],'B':['1100011'],'U':['0110111','0010111'],'J':{'1101111'}}
regabidict={'zero':'','ra':0,'sp':0,'gp':0,'tp':0,'t0':0,'t1':0,'t2':0,'fp':0,'s1':0,'a0':0,'a1':0,'a2':0,'a3':0,'a4':0,'a5':0,'a6':0,'a7':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,
            's11':0,'t3':0,'t4':0,'t5':0,'t6':0}
abidict={'00000': 'zero', '00001': 'ra', '00010': 'sp', '00011': 'gp', '00100': 'tp', '00101': 't0', '00110': 't1', '00111': 't2', '01000': 'fp', '01001': 's1', '01010': 'a0', '01011': 'a1', '01100': 'a2', '01101': 'a3', '01110': 'a4', '01111': 'a5', '10000': 'a6', '10001': 'a7', '10010': 's2', '10011': 's3', '10100': 's4', '10101': 's5', '10110': 's6', '10111': 's7', '11000': 's8', '11001': 's9', '11010': 's10', '11011': 's11', '11100': 't3', '11101': 't4', '11110': 't5', '11111': 't6'}

def instrtype(binaryline):
    opcode=binaryline[-7:]
    for i in opcodedict:
        if opcode in opcodedict[i]:
            return i
#R type instruction functions!!!!!!!!!!!
def add(rs1,rs2,rd):
    regabidict[rd]=regabidict[rs1]+regabidict[rs2]  #check overflow if required
def sub(rs1,rs2,rd):
    regabidict[rd]=regabidict[rs1]-regabidict[rs2] #check x0 case if required
def slt(rs1,rs2,rd):
    regabidict[rd]=int(regabidict[rs1]<regabidict[rs2])
def sltu(rs1,rs2,rd):
    #PLEASE FIGURE OUT LATER
    return

def Rtype(binaryline):
    funct3=binaryline[-15:-12]
    funct7=binaryline[:7]
    funct3dict={'001':sll,'010':slt,'011':sltu,'100':xor,'101':srl,'110':Or,'111':And}
    rd=abidict[binaryline[-12:-7]]
    rs1=abidict[binaryline[-20:-15]]
    rs2=abidict[binaryline[-25:-20]]
    if funct3=='000':
        if funct7=='0000000':
            add(rs1,rs2,rd)
        elif funct7=='0100000':
            sub(rs1,rs2,rd)
    elif funct7=='0000000':
        funct3dict[funct3](rs1,rs2,rd)
    

