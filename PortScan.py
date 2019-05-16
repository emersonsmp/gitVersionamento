########################################### 
#   UNIVERSIDADE FEDERAL DO MATO GROSSO   #
# EMERSON NASCIMENTO SAMPAIO 201511722011 #
###########################################

#comit 2


#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime


#remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServer    = "www.google.com" #manual
remoteServerIP  = socket.gethostbyname(remoteServer)

# BANNER
print("-" * 60)
print("Aguarde, escaneamento do host remoto ", remoteServerIP)
print( "-" * 60)

# TEMPO INICIAL
t1 = datetime.now()

# RANGE PARA VARRER PORTAS DE 1 ATE 1024--------------------------
try:
    for port in range(1,1025):
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        sock.settimeout(0.1)
        result = sock.connect_ex((remoteServerIP, port))        
        if result == 0:
            print("Porta {0}: Aberta".format(port)+", Serviço: "+socket.getservbyport(port))
        sock.close()

# TRATAMENTO DE ERROS----------------------------------------------
except KeyboardInterrupt:
    print("Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Erro com Hostname. Exiting')
    sys.exit()

except socket.error:
    print("Não foi possível conectar ao servidor")
    sys.exit()
# -----------------------------------------------------------------

# TEMPO FINAL
t2 = datetime.now()

# CALCULA DIFERENÇA DE TEMPO
total =  t2 - t1

# PRINTA A INFORMAÇÃO NA TELA
print('Varredura Completa em: ', total)
