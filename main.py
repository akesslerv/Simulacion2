import os
import zipfile
import datetime
import paramiko
import time
import smtplib

from getpass import getpass

# Configuracion hacia el equipo B
host = '192.168.100.25'   #EquipoB
port = 22
usuario = 'akessler'
clave = '12345'

# Conf directorio y tiempo limite para seleccion la copia de archivos
directorio_path = 'home/Desktop/EquipoB'
time_limit = datetime.datetime.now() - datetime.timedelta(days=5)

# Lugar de destino y nombre de archivo comprimido en equipo A
local_path = '/Desktop/Local Path'
archivo_remoto = f'backup_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.zip'

#
# Para Iniciar la conexion con equipo_B

if __name__ == '__main__':
    try:
        client = paramiko.SSHClient()
        clave = getpass("Clave: ")
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, port=22,  username=usuario, password=clave)

        stand_input, stand_output, stand_error = client.exec_command('ls /')
        time.sleep(1)

        resultado = stand_output.read().decode()
        print(resultado)

        client.close()

    except paramiko.ssh_exception.AuthenticationException as e:
        print("No se pudo conectar")

# Para seleccionar archivos del directorio del equipo B

archivos_txt = []
for archivo in os.listdir(directorio_path):
    path_archivo = os.path.join(directorio_path, archivo)
if os.path.isfile(path_archivo) and os.path.getctime(path_archivo) < time_limit.timestamp():
    archivos_txt.append(path_archivo)

# Para comprimir los archivos que se seleccionaron en el Equipo B
with zipfile.ZipFile(archivo_remoto, 'w') as zip_file:
    for path_archivo in archivos_txt:
        zip_file.write(path_archivo)

# Para enviar los archivos comprimidos al equipo local
sftp = ssh.open.sftp()
sftp.put(archivo_remoto, os.path.join(local_path, archivo_remoto))
sftp.close()

#Para eliminar los archivos del equipo B

for path_archivo in archivos_txt:
    os.remove(path_archivo)

#Para configurar el email donde se enviara el informe :

host_server = "server.smtp.com"
server = smtplib.SMTP(host)
FROM = "testpython@ufide.ac.cr"
TO = "akesslerv@test.com"
MSG = "Subjet: Informe Caso Simulacion 2"
server.sendmail(FROM, TO, MSG)

server.quit()
print("Email enviado")
