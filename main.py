from wrds import char,enc,dec,typ,txt,shf,wr,rpt,gb
end = 0
def caesar(dr,tt,stx):
  st = ""
  if dr == "decode":
    stx *= -1
  for letter in tt:
    if letter not in char:
      st += letter
    else :
      pos = char.index(letter)
      lnx = pos + stx
      st += char[lnx]
  print(f"The {dr}d result is : {st}")
while end == 0:
  direction = input(f"{typ}").lower()
  if not direction == "encode" and not direction == "decode":
    end = 1
    print(wr)
    break
  text = input(txt).lower()
  shift = int(input(shf))
  shift %= 26
  caesar(direction,text,shift)
  qs = input(rpt).lower()
  if qs == "no":
    end = 1
    print(gb)