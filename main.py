
import pandas as pd
from collections import Counter

män = pd.read_csv("män.csv")
män = män[["längd", "vikt", "storlek"]]
kvinnor = pd.read_csv("kvinnor.csv")
kvinnor = kvinnor[["längd", "vikt", "storlek"]]


def knn(längd, vikt, df, k):
  data = [[(längd-l)**2+(vikt-v)**2,s] for _,l,v,s in df.itertuples()]
  data.sort(key=lambda d:d[0])
  return [s[1] for s in data[:k]]

längd = float(input("Din längd i cm: "))
vikt = float(input("Din vikt i kg: "))

data_m = knn(längd, vikt, män, 11)
data_k = knn(längd, vikt, kvinnor, 11)
sm = Counter(data_m).most_common(1)[0][0]
sk = Counter(data_k).most_common(1)[0][0]

print(f"Som man bör du välja {sm} och som kvinna bör du välja {sk}")
