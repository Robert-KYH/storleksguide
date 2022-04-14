
import pandas as pd


'''
storleksguide för t-shirts, amerikanska mått
enligt tabeller på sizechart.com/t-shirt

för män:

     midja     bröstkorg
     -------------------
XXS	 26-27''	 29-31''
XS	 27-29''	 30-32''
S	   29-31''	 33-36''
M	   31-32''	 38-40''
L	   33-34''	 42-44''
XL	 34-36''	 46-48''
XXL	 36-40''	 48-50''
3XL	 40-46''	 50-52''

för kvinnor:

            midja    byst
            -------------
XXS (00)  	20-22''	 26-28''
XS (0)	    23-24''	 28-30''
S (0-2)    	25-26''	 30-32''
M (4-6)   	27-28''	 32-34''
L (8-10)  	30-32''	 36-38''
XL (12-14)	33-34''	 40-42''
XXL (16-18)	36-38''	 44-46''
'''


# läs in tabeller, plocka ut och byt namn på relevanta kolumner

män = pd.read_csv("male.csv")
kvinnor = pd.read_csv("female.csv")

män = män[["stature", "chestcircumference", "waistcircumference", "weightkg"]]
kvinnor = kvinnor[["stature", "chestcircumference", "waistcircumference", "weightkg"]]

män.rename(columns = {"stature":"längd", "weightkg":"vikt", "chestcircumference":"bröst", "waistcircumference":"midja"}, inplace=True)
kvinnor.rename(columns = {"stature":"längd", "weightkg":"vikt", "chestcircumference":"byst", "waistcircumference":"midja"}, inplace=True)


# gör om längd och vikt till cm och kg

män.längd = män.längd.transform(func=lambda l:l/10)
män.vikt = män.vikt.transform(func=lambda v:v/10)
kvinnor.längd = kvinnor.längd.transform(func=lambda l:l/10)
kvinnor.vikt = kvinnor.vikt.transform(func=lambda v:v/10)


# använd storleksguiden för att sätta en referensstorlek på personerna i tabellerna

storlekar = ["XXS", "XS", "S", "M", "L", "XL", "XXL", "3XL"]

def storlek_man(data):
  # hitta rätt index in i storlekar[] från det givna måttet
  ms = 0
  m = data["midja"]/25.4    # från mm till tum
  if m > 27:  ms += 1
  if m > 29:  ms += 1
  if m > 31:  ms += 1
  if m > 33:  ms += 1
  if m > 34:  ms += 1
  if m > 36:  ms += 1
  if m > 40:  ms += 1

  bs = 0
  b = data["bröst"]/25.4
  if b > 29:    bs += 1
  if b > 30.5:  bs += 1
  if b > 32.5:  bs += 1
  if b > 37:    bs += 1
  if b > 41:    bs += 1
  if b > 45:    bs += 1
  if b > 48:    bs += 1

  # om bröst och midja faller på olika storlekar väljer män den större storleken

  return storlekar[max(bs, ms)]


def storlek_kvinna(data):
  ms = 0
  m = data["midja"]/25.4
  if m > 22.5:  ms += 1
  if m > 24.5:  ms += 1
  if m > 26.5:  ms += 1
  if m > 29:    ms += 1
  if m > 32.5:  ms += 1
  if m > 35:    ms += 1

  bs = 0
  b = data["byst"]/25.4
  if b > 28:  bs += 1
  if b > 30:  bs += 1
  if b > 32:  bs += 1
  if b > 36:  bs += 1
  if b > 39:  bs += 1
  if b > 43:  bs += 1

  # kvinnor väljer den mindre storleken

  return storlekar[min(bs, ms)]


# lägg till storlekskolumnen i tabellerna m.h.a. storleksfunktionerna

män["storlek"] = män.apply(func=storlek_man, axis="columns")
kvinnor["storlek"] = kvinnor.apply(func=storlek_kvinna, axis="columns")

# justera tabellen till formatet "längd, vikt, storlek" och spara som ny csv

män = män[["längd", "vikt", "storlek"]]
män.to_csv("män.csv", index=False)
kvinnor = kvinnor[["längd", "vikt", "storlek"]]
kvinnor.to_csv("kvinnor.csv", index=False)
