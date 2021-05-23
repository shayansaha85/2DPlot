import pandas as pd

d = {
    "X" : [1,2,3,4,5],
    "Y" : ['A','B','C','D','E']
}

df = pd.DataFrame(d)

df.to_excel("output.xlsx", index=False)