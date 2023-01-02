import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

emo_type = ["happiness","surprise","anger","sadness","quiz_num","captured num"]
QUIZ_NUM = 30

filename = "quiz_u1_emopy_series.csv"
data = pd.read_csv(filename,delimiter=",")

print("select target type of emotion: 0-happiness, 1-surprise, 2-anger, 3-sadness")
emotype = emo_type[int(input())]
emo_data = data.loc[:,[emotype,"quiz_num","captured num"]]

mean_list = []
mode_list = []
max_list = []
min_list = []

for t in range(QUIZ_NUM):
#for t in range(4):
    plt.figure(figsize=(10,5))
    target_data = emo_data[emo_data["quiz_num"]==t]
    print(target_data[emotype])
    d=target_data[emotype]
    d_round=target_data[emotype].round(1)
    d20 = d.rolling(5).mean()
    print("mean:",d.mean(),"mode",d_round.mode(),"max:",d.max(),"min:",d.min())

    mode="no-show"
    print("graph is ",mode,"mode")
    if(mode=="show"):
        plt.subplot(1,2,1,xlabel="value of "+emotype,ylabel="count(quiz num="+str(t)+")")
        d.hist()
        plt.subplot(2,2,2,xlabel="the number of frame(30fps)", ylabel="value of "+emotype)
        plt.plot(d)
        plt.subplot(2,2,4,xlabel="the number of frame(30fps)", ylabel="value of "+emotype+"(moving ave)")
        plt.plot(d20,color="orange")
        plt.tight_layout()
        plt.show()

