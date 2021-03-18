# Bruno Dutra

import matplotlib.pyplot as plt
import serial
import time
import numpy as np
import daqduino

#variáveis de inicialização
nit=2009;
Ts=0.01;
k=0;
t=np.arange(0, nit);#var=0:ts:nit*ts
#var=(var/var)*2;
y=np.arange(0, nit*Ts, Ts)*0;

#aquisição de dados
daqduino.start('COM4','9600')
time.sleep(1)
daqduino.write(1,Ts);
time.sleep(1)
while k<nit:
    
    #daqduino.write(var[k],Ts);
#    y[k]=daqduino.read();
    string=daqduino.readStr();
    print(string);
    k=k+1;
    
daqduino.end();  
  
#plota os gráficos
t = np.arange(0, nit*Ts, Ts);
plt.plot(t,y,antialiased=False,label='y')
plt.ylabel('eixo y')
plt.xlabel('eixo x')
plt.legend()
plt.grid(color='k', linestyle='--', linewidth=0.1)
plt.show()
