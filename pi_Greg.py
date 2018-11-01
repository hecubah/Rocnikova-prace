r=1

O=4*r**2 # plocha opsaneho
V=2*r**2 # plocha vepsaneho
n=4

print("Dvojice n-uhelniku")
for i in range(26):
  print("{} uhelnik: {} < pi < {}".format(n, V/r**2, O/r**2))
  VV=(V*O)**0.5
  O=(2*V*O)/(V+VV)
  V=VV
  n*=2

