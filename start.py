#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desarrollado por Edwin Ariza <edwin.ariza@systemico.co>

import OpenSSL
import datetime
import ssl

#CLASIFICAMOS LOS COLORES A UTILIZAR EN AL TERMINAL
class COLOR:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#MENU DE LA APP
def menu():
    print("=================================================")
    print(COLOR.BOLD+"CERTIBOT \ "+COLOR.ENDC, end='')
    print(" DESARROLLADO POR "+COLOR.BOLD+"HTTPS://SYSTEMICO.CO "+COLOR.ENDC)
    print("=================================================\n")
    

#METODO DE VERIFICACION DEL TIEMPO DE VENCIMIENTO DEL CERTIFICADO
def check():
    print(COLOR.HEADER+"## INICIANDO EL PROCESO DE VERIFICACIÓN DE DOMINIOS:"+COLOR.ENDC+"\n")
    domains = ["wapp.grumpyturtle.co", "dit.systemico.co", "soporte.systemico.co",  "tickets.edwinariza.com", "ideas.edwinariza.com"]
    port = 443
    cont = 1
    print("-------------------------------------------------------------------------------------")
    for hostname in domains:
        longitud=len(hostname)
        max=40

        print("| " + str(cont) + " | " + COLOR.BOLD + COLOR.OKBLUE + hostname + COLOR.ENDC + " ", end='')
        #Calculamos los espacios
        for i in range(1, max-longitud):
            print(' ', end='')
        print('|', end='')

        num_days = 15
        cert = ssl.get_server_certificate(
            (hostname, port), ssl_version=ssl.PROTOCOL_TLS)
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        expiry_date = x509.get_notAfter()
        #print(str(expiry_date))
        assert expiry_date, "El certificado no tiene fecha de vencimiento."
        ssl_date_fmt = r'%Y%m%d%H%M%SZ'
        expires = datetime.datetime.strptime(str(expiry_date)[2:-1], ssl_date_fmt)
        remaining = (expires - datetime.datetime.utcnow()).days

        if remaining <= num_days:
            print(COLOR.FAIL+"    ALERTA!:"+COLOR.ENDC+"El dominio vence en "+COLOR.FAIL+str(remaining)+COLOR.ENDC+"   |")
        else:
            print(COLOR.OKGREEN+"         OK, faltan " + str(remaining) + " días  "+ COLOR.ENDC+"        |")
        cont = cont + 1
        print("-------------------------------------------------------------------------------------")

#EJECUCION DE LAS OPERACIONES DE VERIFICACION
menu()
check()