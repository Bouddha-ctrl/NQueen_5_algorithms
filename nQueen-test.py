

import matplotlib.pyplot as plt

sat = [0.001, 0.001, 0.001, 0.001, 0.002, 0.003, 0.002, 0.004, 0.005, 0.006, 0.008, 0.009, 0.011, 0.014, 0.016, 0.021]
    
genetic = [0.003, 0.015, 0.065, 0.004, 0.052, 0.081, 0.189, 0.486, 0.137, 0.263, 0.151, 0.517, 0.118, 0.486, 0.671, 0.774]

beam= [0.001, 0.001, 0.004, 0.005, 0.012, 0.020, 0.026, 0.042, 0.080, 0.076, 0.152, 0.189, 0.271, 0.324, 0.499, 0.754]

hill = [0.001, 0.001, 0.043, 0.002, 0.003, 0.002, 0.004, 0.008, 0.007, 0.412, 0.016, 0.020, 0.022, 0.032, 0.035, 0.034]

brut_force = [0.000, 0.001, 0.002, 0.034, 0.14, 1.514, 1.514, 1.514, 1.514, 1.514, 1.514, 1.514, 1.514, 1.514, 1.514, 1.514]

back_tracking = [0.001, 0.001, 0.0, 0.001, 0.001, 0.002, 0.001, 0.005, 0.002, 0.036, 0.029, 0.242, 0.138 , 1.126, 0.08 ,1.514]  

X = [5, 6, 7, 8, 9, 10, 11 ,12, 13, 14, 15, 16, 17, 18, 19, 20]

plt.xlabel('taille du puzzle')
plt.ylabel('seconde')

plt.plot(X,sat,'red',label='SAT')
plt.plot(X,hill,'yellow',label="Hill climbing")
plt.plot(X,beam,'black',label='Beam Search')
plt.plot(X,genetic,'blue',label='algorithme genetique')
plt.plot(X,back_tracking,'orange',label="back_tracking")
plt.plot(X,brut_force,'green',label="brut force")

plt.legend()
plt.show()

