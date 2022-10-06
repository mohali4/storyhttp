from django.db import models

class base_model:
    def __init__ (self, *args,**wargs):
        for name , item in wargs.items():
            self.__dict__[name] = item


    def __get_set_attribute (self, name:str):
        if name[:4] == 'set_':
            class setter:
                def __init__ (self,_class,name):
                    self.self = _class
                    self.set_name = name
                def set(self,item):
                    exec(f'self.self.{self.set_name}=item')
                    return self.self
            return setter(self,name[4:]).set

    def __getattribute__(self, name: str) :
        try :
            return super().__getattribute__(name)
        except  AttributeError:
            if name [:4] == 'set_':
                try:
                    return self.__get_set_attribute(name)
                except:
                    ...
            return super().__getattribute__(name)
                
    def copy(self)  :
        from copy import deepcopy as copy
        return copy(self)

    def __eq__(self, __o) -> bool:
        return (self.__dict__ == __o.__dict__) and (type(self) == type(__o))

    @property
    def cls (self):
        return type(self)

class List (list, base_model):
    def filter (self,key):
        res = self.copy()
        for condidate in self:
            if not key(condidate):
                res.remove(condidate)
        return res

    def append_if_not_exists (self,item):
        if not item in self :
            self.append(item)
    def __eq__ (self,o):
        i = self.copy()
        o = List(o)
        for _o in o :
            if not _o in i :
                return False
            else:
                o.remove(_o)
        if len (o) == 0 :
            return True
        return False
