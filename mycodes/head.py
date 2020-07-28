## 1. remove trash
!rm -rf ~/.local/share/Trash/files/*

## 2. load useful functions
import requests
exec(requests.get('http://miruetoto.github.io/my_code/datahandling.py').text)
exec(requests.get('http://miruetoto.github.io/my_code/plot.py').text)
ro.r('source_url("http://miruetoto.github.io/my_code/datahandling.r")')
ro.r('source_url("http://miruetoto.github.io/my_code/plot.r")')

## 3. Project Setting
exec(requests.get('http://miruetoto.github.io/my_code/HST/hstfunctions.py').text)
ro.r('source_url("http://miruetoto.github.io/my_code/HST/hstfunctions.r")')

## 4. for R user
%load_ext rpy2.ipython

## 5. plt setting 
pp.dpi(150)

## 6. check gpu
checkgpu()