#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- author: zx51 -*-
"""
Esse programa pode ser usado como um cliente/servidor, para acesso remoto
como o ssh, para sistemas Linux. (desenvolvimento)
"""
# Importar modulos
import socket
import subprocess

# Variaveis fixas para testes
Host = '' # localhost/127.0.0.1/0.0.0.0
Port = 8022 # Porta padrão do programa

User = "usuario" # temporario
Password = "senha" # temporario

print(":: Servidor ligado ::")

# Configurando socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Funções Cliente ou Servidor

# Função Servidor

sock.bind((Host, Port))
sock.listen(4)
while True:
    try:
        conexão, endereço = sock.accept()
        print(":: O cliente {}, se conectou. ::".format(endereço))

        # Pegar Usuario e Senha
        conexão.send(b':: Porfavor, Informe o Usuario: ')
        user = conexão.recv(1024).decode('utf-8')
        conexão.send(b':: Porfavor, Informe a Senha: ')
        password = conexão.recv(1024).decode('utf-8')
        # Checar usuario e senha correto
        if user != User:
            conexão.send(b':: Usuario Incorreto ::')
            conexão.close()
        elif password != Password:
            conexão.send(b':: Senha Incorreta ::')
            conexão.close()

        else:
            conexão.send(b':: Usuario e Senha aceitos')
            # Principal função, mandar textos ao servidor
            while True:
                cmd = conexão.recv(1024)

                cmd = cmd.decode('utf-8')
                out = str(getoutput(cmd))

                print("Log:", cmd, "=", out)


                data = conexão.recv(1024)
                if not data: break
                conexão.send(b':: Recebido pelo Servidor: ' + data)
                conexão.close()
                break
    except KeyboardInterrupt:
        print(":: Servidor desligado ::")
        try:
            conexão.close()
        except:
            print(":: Erro na conexão ::")
        finally:
            exit()
