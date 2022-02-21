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

    def add(self, key, obj):
        if key in self.objListCache.keys():
            return False
        self.objCache = obj
        self.keyCache = key
        self.objListCache[str(self.keyCache)] = dict(self.objCache)
        self.__dump()
        return True

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

    def get(self, key):
        try:
            return self.objListCache[key]
        except KeyError:
            print('Chave não encontrada')
            return False

    def get_all(self):
        return self.objListCache.items()

    def get_ids(self): #Verify if it works
        lista = []
        for x in self.objListCache:
            lista.append(x)
        return lista

    def set_data_source(self, path: str): #Verify if it works
        if '.json' not in path:
            path = path + '.json'
        with open(self.datasource, 'w') as json_file:
            json.dump(self.objCache, json_file)
        json_file.close()

    def import_source(self, path: str): #Verify if it works
        with open(os.path.abspath(self.datasource,),
                  encoding='latin-1', mode='rb') as json_file:
            json_data = json.load(json_file)
        json_file.close()
        for cliente in json_data.values():
            self.objCache[cliente.codigo] = cliente
        self.__dump()


if __name__ == '__main__':
    dao = DAO('teste.json')
    #p1 = BotFeliz('felipe')
    #dao.add(p1.id, p1)
    #dao.remove('895')
    #print('old', dao.objListCache)
    #p1 = dao.get_ids()
    #print(p1)
    #print(dao.get('620'))
    #print(dao.get_all())
    