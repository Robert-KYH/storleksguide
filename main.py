
import pandas as pd
from collections import Counter


män = pd.read_csv("män.csv")
kvinnor = pd.read_csv("kvinnor.csv")


# K-nearest neighbors

def knn(längd, vikt, df, k):
  # gå igenom alla rader och lägg in avståndet (i kvadrat) samt storleken i en ny lista
  data = [[(längd-l)**2+(vikt-v)**2,s] for _,l,v,s in df.itertuples()]
  # sortera på avståndet och returnera en lista med de närmsta storlekarna
  data.sort(key=lambda d:d[0])
  return [s[1] for s in data[:k]]


längd = float(input("Din längd i cm: "))
vikt = float(input("Din vikt i kg: "))

# läs ut de 11 närmsta storlekarna från båda tabeller, och hitta den mest förekommande

data_m = knn(längd, vikt, män, 11)
data_k = knn(längd, vikt, kvinnor, 11)
sm = Counter(data_m).most_common(1)[0][0]
sk = Counter(data_k).most_common(1)[0][0]

print(f"Som man bör du välja {sm} och som kvinna bör du välja {sk}")
