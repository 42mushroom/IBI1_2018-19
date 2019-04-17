# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:08:13 2019

@author: 30389
"""
import pandas as pd
xlsx = pd.ExcelFile(r'C:\Users\30389\Desktop\ibi\github\IBI1_2018-19\pratical9\BLOSUM62.xlsx')
df = pd.read_excel(xlsx,'Sheet1')
seq1="MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
seq2="MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
seq3="WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL"
n=len(seq1)
edit_d=0
score=0
for i in range(n):
    score += df.at[seq1[i],seq2[i]]
    if seq1[i]!=seq2[i]:
        edit_d +=1
percent = 100-edit_d/n * 100
percent1 =score/n
print("edit_distance="+str(edit_d),"similarpercent="+str(percent)+"%","BLOSUMscore="+str(score),str(percent1))





contrast=""
for i in range(n):
    if (df.at[seq1[i],seq2[i]]>=0) and seq1[i]!=seq2[i]:
            contrast+="+"
    elif (df.at[seq1[i],seq2[i]]<0) and seq1[i]!=seq2[i]:
            contrast+="_"
    else:
        contrast+=seq1[i]
    
print("Sequenceforhuman="+seq1,"contrast="+contrast,"Sequenceofamouse="+seq2)
                
        