mainlst=readassembly()
for i in mainlst:
  a=i.split()
  type=identifyinstrtype(a[0])
  