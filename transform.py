import pandas as pd
from time import sleep
import os
from extract import run






df1 = pd.read_csv('cripto.csv')
df2 = pd.read_csv('/content/drive/MyDrive/cripto_scrapy/base.csv')


df1.sort_values(by=['cripto'],ascending=True,inplace=True,ignore_index=True)
convert_dict = {'busd': float,
            'valor_de_compra': float,
            'valor_atual':float
            }
df2['valor_atual'] = df1['valor']
df2 = df2.astype(convert_dict)
df2['quantidade'] = df2['busd']/df2['valor_de_compra']
df2['liquido'] = (df2['valor_atual'] * df2['quantidade'])-df2['valor_de_compra']*df2['quantidade']
df2['porcentagem'] = df2['liquido']*100/df2['busd']

#df2['dolar/reais'] = (df2['BUSD(gasto)']+df2['Liquido'])*5,13 
df2 = df2.round(decimals=2)
os.system('clear')
print(df2[['cripto','busd','valor_de_compra','valor_atual','liquido','porcentagem']].to_markdown(index=False))
df2.to_csv('resultado.csv',index=False)

