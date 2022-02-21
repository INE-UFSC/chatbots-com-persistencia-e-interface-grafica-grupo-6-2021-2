from abc import ABC
from Bots.BotFeliz import BotFeliz
# import pickle
import sys
import json
import os
import io

from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class DAO(ABC):
    def __init__(self, datasource=''):
        self.datasource = datasource
        self.objCache = {}
        self.objListCache = {}
        self.keyCache = 0
        self.__create_file(self.datasource)

        try:
            self.__load()
        except IOError:
            self.__dump()

    def __dump(self):
        with open(self.datasource, 'w') as json_file:
            bot_to_string = json.dumps(
                self.objListCache, cls=MyEncoder, indent=4, sort_keys=True, ensure_ascii=False)
            json_file.write(bot_to_string)
        json_file.close()

    def __file_exists(self, path):
        return os.path.isfile(path) and os.access(path, os.R_OK)

    def __create_file(self, path):
        if not self.__file_exists(self.datasource):
            with io.open(path, 'w') as json_file:
                json_file.write(json.dumps({}))

    def __load(self):
        if self.__file_exists(self.datasource):
            with open(self.datasource, encoding='latin-1', mode='r') as json_file:
                json_data = json.load(json_file)
                self.objListCache = json_data
                json_file.close()
        else:
            pass

    #Adiciona um bot ao dao e ao json
    def add(self, key, obj):
        if key in self.objListCache.keys():
            return False
        self.objCache = obj
        self.keyCache = key
        self.objListCache[str(self.keyCache)] = dict(self.objCache)
        self.__dump()
        return True

    #Remove um bot do json e do dao
    def remove(self, key):
        deletou = False
        with open(self.datasource, encoding='latin-1', mode='r') as obj:
            content = json.load(obj)
            for x in content:
                if str(x) == key:
                    deletou = True
                    del self.objListCache[key]  
                    break
            obj.close()
        self.__dump()
        if deletou:
            return True
        else:
            print('Chave não encontrada')
            return False

    #Proura o conteudo de um bot especifico com base no id
    def get(self, key):
        try:
            return self.objListCache[key]
        except KeyError:
            print('Chave não encontrada')
            return False

    #Pega todo o conteudo de todos os bots
    def get_all(self):
        return self.objListCache.items()

    #Pega a lista de todos os ids no dao
    def get_ids(self):
        lista = []
        for x in self.objListCache:
            lista.append(x)
        return lista

    #Troca o datasource atual do DAO e limpa os caches para utilizar apenas os bots da nova source
    def set_data_source(self, path: str):
        if '.json' not in path:
            path = path + '.json'
        self.objListCache = {}
        self.objCache = {}
        self.datasource = path
        self.__dump

    #Importa bot de outro arquivo e salva eles no datasource atual (ignora bots com id igual aos já existentes)
    def import_source(self, path: str):
        if '.json' not in path:
            path = path + '.json'
        with open(os.path.abspath(path),
                  encoding='latin-1', mode='r') as json_file:
            json_data = json.load(json_file)
        json_file.close()
        for x in json_data:
            if x not in self.objListCache:
                self.objListCache[x] = json_data[x]
        self.__dump()


if __name__ == '__main__':
    dao = DAO('teste.json')
    #p1 = BotFeliz('felipe')
    #dao.add(p1.id, p1)
    #dao.remove('895')
    #p1 = dao.get_ids()
    #print(p1)
    #print(dao.get('620'))
    #print(dao.get_all())
    #dao.set_data_source('teste2')
    #p1 = BotFeliz('jorge')
    #dao.add(p1.id, p1)

    #print('old', dao.objListCache)
    #dao.import_source('teste2')
    
    
    