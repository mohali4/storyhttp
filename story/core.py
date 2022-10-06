from .models import List
from pathlib import Path
import os

if True :
    class dir :

        def __init__(self,root:Path):
            self.root = root
        
        def lspath (self,path:Path):
            folders = List(os.listdir(path)).filter(lambda _path :os.path.isdir(path/_path))
            folders.sort()
            return folders
            
        def dec (self,path:str):
            from copy import deepcopy
            sys_path = deepcopy(self.root)
            nums = [] 
            for num in path.split('/') : nums.append(int(num)) if num != '' else ...
            for num in nums:
                sys_path = sys_path / self.lspath(sys_path)[num]
        
            return sys_path
        
        def enc (self,path):
            import re
            if isinstance(path,str):
                path = Path(path)
            path = str(re.sub(f'^({str(self.root)}/?)','',str(path)))
            from copy import deepcopy
            proxy_path = deepcopy(self.root)
            num_path = '/'
            if path == '' or path == '/' :
                return '/'
            for name in path.split('/'):
                num_path += str(self.lspath(proxy_path).index(name))+'/'
                proxy_path /= name
            return num_path


from django.http import HttpRequest

class story :
            
            

    def __init__ (self,root):
        self.root = Path(root)
        self.dir = dir(self.root)

    def serv (self,request:HttpRequest):
        from django.shortcuts import render

        path = request.path
        path = Path (self.dir.dec(path)) #type: ignore
        folders = []
        if request.path != '/':
            ret = ['بازگشت']
            ret.append (str(self.dir.enc(path.parent)))
            folders.append(ret)
        for folder in self.dir.lspath(path):
            url = self.dir.enc(path/folder)
            folders.append([folder,url])
        return render(request,'story.html',{'choices':folders})
        
         