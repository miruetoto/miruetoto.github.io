---
title: (정리) ubuntu 사용법
layout: post 
---

### About this doc

> 우분투 명령어들을 다룬다. 


### 프로그램 설치 
>  프로그램을 지우기 위해서는 아래와 같이 하면 된다. 
```
sudo apt-get remove r-base-core
```

### 나노에디터 사용방법  
> 파일열려며 아래와 같이 한다. 
```
sudo nano /etc/apt/sources.list
```

> 파일을 만드는것도 동일하게 할 수 있다. 즉 아래와 같이 하면 `exam.txt`가 현재 폴더에 있다면 `열고`아니면 `만든다.`
```
sudo nano /home/cgb/Desktop/exam.txt
```
이때 위에처럼 `sudo`를 앞에쓰면 `read-only`로 만들어지고 아래와 같이 
```
nano /home/cgb/Desktop/exam.txt
```
라고만 하면 일반파일로 만들어 진다. 

> 나노에디터를 끄는방법은 `컨트롤+X`이다. 즉 `컨트롤+Q`대신에 `컨트롤+X`. 

> 나노에디터를 저장하는 방법은 `컨트롤+O`이다. 즉 `컨트롤+S`대신에 `컨트롤+O`.

> 단어찾는 방법은 `컨트롤+W`이다. 즉 `컨트롤+F`대신에 `컨트롤+W`. 

> 이전상태로 되돌리는 방법은 `알트+U` 이다. 즉 `컨트롤+Z`대신에 `알트+U`. 

### ssh연결 
- 처음에 ssh를 연결하기위해서는 연결**당하는** 컴퓨터에 가서 아래를 실행해야 한다. 
```
sudo apt install openssh-server
```

### 방화벽
- 1306번 포트를 여는 방법은 아래와 같다. 
```
sudo ufw allow 1306
```
이게 잘 적용되었는지 보려면 아래중 하나를 실행하면 된다. 
```
sudo ufw status
sudo ufw status numbered
```

### sublime

> `컨트롤+h`를 쓰면 찾아바꾸기를 할 수 있다. 
 

### conda 
> 가상환경 리스트를 보는법은 아래와 같다. 
```
conda env list
```

> 가상환경을 지우는 방법은 아래와 같다. 
```
conda env remove --name py20190129
```
 
### 폴더삭제
> 폴더를 삭제하려면 아래와 같이 한다. 
```
rm -r folderName
```

### 서버자체에서 프로세스 실행
> 서버에 접속한다. 
```
ssh lgcgb@10.178.144.65
```
아래와 같이 끝에 `&`을 붙이면 된다. 
```
conda activate py20190129
jupyter lab &
```
**실행하고 난뒤에는 엔터를 쳐서 빠져나온다.** 이렇게 하면 서버자체에 모니터를 연결하고 커널창을 띄운것과 같은 효과를 준다. 즉 서버에 접속한 컴퓨터를 끄는것과 상관없이 서버에서는 항상 주피터가 열려 있게 된다. 

### 서버자체에서 실행된 프로세스 죽이기
> 원격컴퓨터에 접속한다. 
```
ssh lgcgb@10.178.144.65
```
실행된 프로세스를 찾기위해 아래를 실행한다. 
```
ps aux | grep jupyter-lab
```
결과는 아래와 같이 나온다. 
```
lgcgb    26888  0.2  0.1 326760 86724 ?        Sl   10:14   0:12 /home/lgcgb/anaconda3/envs/py20190129/bin/python3.7 /home/lgcgb/anaconda3/envs/py20190129/bin/jupyter-lab
lgcgb    27146  0.0  0.0  15720  1008 pts/3    S+   11:56   0:00 grep --color=auto jupyter-lab
``` 
26888에 해당하는 것이 주피터를 띄운 커널이다. 이 번호를 기억했다가 프로세스를 아래와 같은 명령으로 죽인다. 
```
kill 26888
```

### 텍스트파일(sample.txt)만들기
> 텍스트파일을 만들기 원하는 폴더로가서 아래를 입력한다.
```
cat > sample.txt
```
아무것이나 치고 (예를들어 `asdf`) `컨트롤+C`를 눌러서 빠져나온다. 

> 나노에디터를 사용해도 된다. 

### github 사용방법

#### `clone` 

> 깃을 설치할 폴더로 이동하여 아래를 입력한다. 
```
cgb@cgb:~/Documents/Github$ git clone https://github.com/miruetoto/miruetoto.github.io.git
```

#### `download`
> 깃이 설치된 가장 상위폴더(Documents/Github/miruetoto.github.io)에 가서 아래를 입력한다.
```
git pull
```

#### `upload`
> 깃이 설치된 가장 상위폴더(Documents/Github/miruetoto.github.io)에 가서 아래를 순서대로 입력한다. 
```
git add .
git commit -m .
git push 
```
그리고 `아이디(miruetoto)`와 `비밀번호`를 차례로 입력한다. 

#### 깃허브주소보기 
> 깃이 설치된 가장 상위폴더(Documents/Github/miruetoto.github.io)에 가서 아래를 입력한다. 
```
(base) lgcgb2@lgcgb2:~/Documents/GitHub/miruetoto.github.io$ git remote -v
origin	https://github.com/miruetoto/miruetoto.github.io.git (fetch)
origin	https://github.com/miruetoto/miruetoto.github.io.git (push)
upstream	https://github.com/daattali/beautiful-jekyll.git (fetch)
upstream	https://github.com/daattali/beautiful-jekyll.git (push)
```

#### `branch`
> 서버에 이미 guebin이라는 브랜치가 있다면 아래와 같이 동기화 시킨다.
```
git chechout guebin
git push -u origin guebin
```
여기에서 `git push -u origin guebin`을 안해도 동기화가 잘될때도 있는데 아닐때도 있다. 

### `pip`로 파이썬 패키지 설치하기 
> 이미 깔린 패키지를 강제로 업그레이드 하는방법 
```
pip install --upgrade tensorflow
```
