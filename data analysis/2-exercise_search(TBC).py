import pandas as pd

df_1 = pd.read_excel('奖励名单 核对.xlsx')
df_2 = pd.read_excel('奖励名单 核对.xlsx',sheet_name = 1)

code_original = df_1['兑换码']
code_user = df_2['兑奖码']
#print(code_original)
#print(len(code_original))

for x in range(len(code_original)):
    for y in range(len(code_user)):
        if code_original.loc[:x,:1] == code_user.loc[:y,:1]:
            result = df_2.loc[y]
            print(result)