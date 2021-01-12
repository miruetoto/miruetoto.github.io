## 1. remove trash
#!rm -rf ~/.local/share/Trash/files/*

## 2. load useful functions
#import requests
exec(requests.get('http://miruetoto.github.io/source/datahandling.py').text)
ro.r('source_url("http://miruetoto.github.io/source/datahandling.r")')

## 3. for R user
%load_ext rpy2.ipython

## 4. plt setting 
pp.dpi(150)

## 5. check gpu
checkgpu()
