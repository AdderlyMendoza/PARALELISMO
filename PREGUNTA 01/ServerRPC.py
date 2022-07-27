# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 12:46:50 2021

@author: Mendoza Adderly
"""

from xmlrpc.server import SimpleXMLRPCServer

class RPC:
    metodos_rpc = ['mensaje']
    
    def __init__(self, direccion):
        self._servidor = SimpleXMLRPCServer(direccion, allow_none=True)
        
        for metodo in self.metodos_rpc:
            self._servidor.register_function(getattr(self,metodo))
            
    def mensaje(self, mensaje_r, palabra_r): # palabra_r = palabra a contar
        self._datos = mensaje_r  # GUARDAMOS SMS RECIBIDO
                            
        return self._datos.count(palabra_r)  # DEVUELVE NUM DE PALABRAS 
        
    def iniciar_servidor(self):
        self._servidor.serve_forever()
        
rpc = RPC(('', 20050))
print('Servidor RPC iniciado...')
rpc.iniciar_servidor()
        

        
        
        
        
        
        
        