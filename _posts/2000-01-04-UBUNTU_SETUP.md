---
title: (정리) ubuntu 포맷이후 할일들 
layout: post 
---

### About this doc

> 우분투에서 여러가지 개발환경을 설정하는 방법을 포스팅 하겠다. 

### 한글설정

> 아래와 같이 커맨드에 친다. 
```
ibus-setup
```
이걸 치면 IBus Preferences 라는 창이 나오는데 여기에서 (1) Input Method 탭 클릭 (2) Add 버튼 클릭 (3) Korean 선택 (4) Hangul 선택을 한다. 

> 위의 단계에서 Korean이 안보이면 Language Support로 가서 한국어팩을 설치하고 리부팅 하면 된다. (보통 실행하자마자 알아서 설치되더라.. 설치가 안되면 Install / Remove Languages... 이라는 탭을 클릭해서 설치하자) 리부팅을 꼭 해야한다는 것에 주의하자. 

> 이제 Region & Language로 가서 설정하면 된다. 

### 그래픽카드 드라이버설치

> 전체적인 내용은 [여기](https://gist.github.com/bendangnuksung/981408031699e0ddc50a6f6fdcf185c2)를 참고하자. 

> 우선 gedit를 열고 아래를 복사해서 붙여넣는다. 
```
blacklist nouveau
options nouveau modeset=0
```
파일이름을 'blacklist-nouveau.conf'로 home에 저장한다. 그 다음 'ctrl+alt+F3'을 눌러서 까만화면으로 간다. 아래입력한다. 
```
sudo -i
```
아이디와 비밀번호를 입력하고 루트권한을 얻는다. 아래를 입력한다. 
```
sudo cp /home/cgb2/blacklist-nouveau.conf /etc/modprobe.d
sudo update-initramfs -u
exit
```
재부팅을한다. 

> 커맨드에서 아래를 실행하자.
```
sudo apt install gcc
sudo apt install build-essential
```
그리고 드라이버 설치파일을 다운받는다. [앤비디아공식홈페이지](https://www.geforce.com/drivers)에서 다운받자. OS를 리눅스 64-bit으로 선택하고 검색을 누르면 다운받아진다. 다운받은뒤에는 파일이 있는 폴더로 이동하여 
```
chmod +x NVIDIA-Linux-x86_64-410.78.run
```
를 실행하자. 보통 NVI까지치고 적당히 탭을 누르면 알아서 뒷부분이 완성된다. 이 과정은 추후에 드라이버를 실행할수 있도록 권한을 풀어두는 것이다. 그리고 아래를 실행한다.
```
sudo ./NVIDIA-Linux-x86_64-410.78.run
```
그 다음 드라이버가 잘 설치되었는지 확인한다. 
```
nvidia-smi
```

### 아나콘다

> 아나콘다를 다운받은 폴더로 가서 아래와 같이 실행한다. 
```
bash Anaconda3-2019.03-Linux-x86_64.sh
```
대충 bash Ana 정도까지만 치고 tab을 누르면 알아서 완성된다. 

> 커맨드를 키고  아래를 실행한다. 
```
conda create -n py20190129
conda create -name py20190129
```
둘 중 아무거나 실행해도 된다. 파이썬 환경이 너무 높으면 나중에 conda tensorflow-gpu 가 먹히지 않으니 환경을 만들때 파이썬버전을 3.7.6으로 통일하자. (현시점 2020년 2월28일기준 3.8.x이면 conda tensorflow-gpu 가 동작하지 않음.)
```
conda create -n py20190129 python=3.7.6
conda create -name py20190129 python=3.7.6
```

### 주피터 원격제어

- 콘다 가상환경에서 주피터랩을 설치한다. 
```
~conda activate py20190129~
conda install jupyterlab
```
사실 위에서 주피터랩을 따로 설치안해도 주피터랩이 잘만 실행된다. 하지만 이렇게하니까 나중에 R커널을 만들기위해 IRkernel::installspec()을 실행할때 아래와 같은 에러가 난다. 
```
Error in IRkernel::installspec(user = FALSE) : 
  jupyter-client has to be installed but “jupyter kernelspec --version” exited with code 127.
```
그러니까 그냥 남들하는대로 주피터랩 설치하고 넘어가자. 주피터랩은 보통 로칼로 접속하는데 이를 원격으로 접속할 수 있게 만들어보자. 우선 커맨드에서 아래를 실행하자.
```
~conda activate py20190129~
jupyter notebook --generate-config
```
이렇게 하면 `/home/cgb/.jupyter` 디렉토리에 `jupyter_notebook_config.py` 파일이 만들어진다. 나중에 이 파일에 접근해서 뭔가를 바꿔야하는데 우선 그전에 파이썬을 실행하자. 그리고 아래를 입력한다. 
```python
from notebook.auth import passwd
passwd()
```
패스워드를 설정하고 나오는 `sha1:어쩌고..` 부분을 복사한다. 


> 이제 처음에 생성한 `/home/cgb/.jupyter/jupyter_notebook_config.py` 파일을 연다. 이 파일에 접근하기 위해서는 아래의 순서를 따른다. (1) 파일관리자를 키고 홈탭을 누른다. (이러면 자동으로 /home/cgb 폴더로 접근함.) (2) 컨트롤+h를 누른다. (여기에서 .jupyter 는 숨겨진 폴더라서 바로는 안보이고 컨트롤+h를 눌러야 보인다.) (3) jupyter_notebook_config.py 를 더블클릭한다. 또는 그냥 단순히 아래를 실행한다. 
```
sudo nano ~/.jupyter/jupyter_notebook_config.py
```

> 원하는대로 수정하면 되는데 아래는 꼭 수정한다. 
```python
c.NotebookApp.open_browser = False
c.NotebookApp.ip = '192.168.0.4'
c.NotebookApp.password = 'sha1:1969b198e067:915d665111e284538ffe3e63d08de9a0a4dba5e7'
c.NotebookApp.port = 1306
```
여기에서 `192.168.0.4` 는 내부아이피다. 즉 `ifconfig`로 확인할 수 있는걸 쓴다. 

> 패스워드 없이 주피터를 띄우려면 아래와 같이 한다. 
```
jupyter lab --LabApp.token='' --LabApp.password=''
```

### `CUDA`, `cuDNN`, `tensorflow-gpu`, `pytorch`
> 콘다환경으로 가서아래를 실행한다. 
```
conda install pytorch-gpu
conda install tensorflow-gpu
```
그러면 알아서 `CUDA`, `cuDNN`, `pytorch`, `tensorflow-gpu`가 깔린다. 현재는 파이썬 환경이 너무 높으면 깔리지 않는 현상이 있으니 환경을 만들때 파이썬버전을 `3.7.6`으로 통일하자. 참고로 gpu사용량은 아래와 같이 모니터링 할 수 있다.
```
watch -n 5 nvidia-smi -a --display=utilization
```

### 주피터에 R커널 연결 
> 콘다환경으로 가서 아래를 실행한다. 
```
conda install -c r r
```
이러면 콘다환경에는 R이 깔리고 base에는 R이 깔리지 않는다. 그리고 콘다환경에서 R을 실행한다. Rstudio가 아니라 커맨드에서 R을 실행해야한다. 그리고 `devtools`와 `IRkernel`을 설치한다. (`devtools`는 지금 당장 꼭 설치할 필요는 없다.) 
```r
install.packages("devtools")
install.packages("IRkernel")
```
그리고 아래를 실행하면 주피터랩과 R환경이 연결된다. 
```r
IRkernel::installspec()
```
이제 주피터랩에서 R kernel을 사용할 수 있다. 

### Rstudio server 
> 이제 Rstudio server를 설치한다. 이건 콘다환경의 `R`과 연결이 안된다. 그래서 보통은 (base)에 R을 깔고 그 R과 연결해야한다. 하지만 우분투 18.04는 base에서 R을 깔기 위해서 아래와 같이 실행하면 기본적으로 R이 3.4버전으로 깔린다. 
```
~sudo apt install r-base~ ## 이걸 실행하지 말자. 
```
그러니까 위와 같이 실행하지 말자. (base)에 높은 버전의 R을 억지로 까는 방법이 있긴 있다. 추천하는 방법은 아니다. 대신 콘다환경 (py20190129)에서 가서 억지로 Rstudio를 연결하는 방법을 알아보자. 관련내용은 [여기](https://github.com/grst/rstudio-server-conda)를 참고했다. 

> 먼저 Rstudio를 깐다. 참고로 Rstudio server 설치하는법은 [여기](https://rstudio.com/products/rstudio/download-server/debian-ubuntu/)를 참고하라. 
```
sudo apt-get install gdebi-core
wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.2.5033-amd64.deb
sudo gdebi rstudio-server-1.2.5033-amd64.deb
```
보통 여기까지하면 Rstudio 설치가 끝난다. 이제 아래를 실행한다. 
```
sudo apt install uuid
sudo apt install git
git clone https://github.com/grst/rstudio-server-conda.git
```
위에 두줄은 [이사람](https://github.com/grst/rstudio-server-conda)이 만든 어떤 프로그램을 쓰기 위한 사전준비작업이다. 마지막줄을 실행하면 [이사람](https://github.com/grst/rstudio-server-conda)이 만든 프로그램이 다운받아진다. 이게 프로그램 설치가 완료된것이다. 이제 컴퓨터 껐다 킬때마다 아래를 실행한다. 
```
conda activate py20190129
~/rstudio-server-conda/start_rstudio_server.sh 8787 # use any free port number here. 
```
이제 `192.168.0.4:8787` 따위의 주소로 접속하면 `Rstudio`를 쓸 수 있다. 참고로 system-wide Rstudio server를 죽여야 할 때가 있다. 그럴땐 아래 명령을 치면 된다. 
```
sudo systemctl disable rstudio-server.service
sudo systemctl stop rstudio-server.service
```

### `Rstudio`셋팅이후 하면 좋은것: `devtools::install_github()`가 먹히지 않을 경우대비 

> Rstudio를 쓰기전에 커맨드에 가서 아래를 실행하자. 
```
sudo ln -s /bin/tar /bin/gtar
```
이렇게 해야 나중에 R스튜디오에서 `devtools::install_github()`로 패키지를 깔때 잘깔린다. 예를들면 `kormaps2014`와 같은 패키지. 

### `keras` in R
> 이제 아까 띄운 Rstudio-server에서 아래를 설치하자. 
```
install.packages("keras")
library(keras)
install_keras(tensorflow = "gpu")
```
만약에 gpu버전을 설치하고 싶지 않다면 맨 마지막줄을 아래로 바꾼다. 
```
install_keras()
```
아무튼 이러면 실행하자마 아래와 같은 메시지가 뜨는데 보는것처럼 n을 눌러야 한다. 
```
Would you like to install Miniconda? [Y/n]: n
```
우리는 Rstudio-server를 이미 콘다내에서 실행했으므로 미니콘다를 추가로 깔지 않는다. 

> 참고로 여기까지 끝내면 Rstudio에서 업데이트 가능한 패키지를 찾아서 모조리 업데이트하자. 그리고 IRkernel 같은 것이 깨져있을수도 있으니 (케라스를 깔면서 먼가 깨지는듯?) 이것도 다시 연결하자. 

### `rpy2`
> 콘다환경에서 아래와 같이 입력하여 설치한다. 
```
pip install rpy2
```
절대로 `conda install rpy2`로 설치하지말자. 기본적으로 낮은버전 `rpy2`가 설치되는데 내가 만든 `push`등 여러파일들이 3.0 이상에서 동작하도록 만들어져 있다. 따라서 코드가 모두 꼬여버린다. 

### `pandas`, `matplotlib`
> 이제 콘다환경에서 나머지 패키지들을 깔아보자. 
```
conda activate py20190129
conda install pandas
conda install matplotlib
```

### `julia` 
> [여기](https://julialang.org/downloads/)에 접속한다. 스크롤링하여 Generic Linux Binaries for x86 / 64-bit(GPG)를 찾는다. 그리고 64-bit를 클릭해서 다운받는다. (참고로 왼쪽에 help를 누르면 설치페이지 설명서가 나온다.) 그러면 아래와 같은 파일이 나온다. 
```
julia-1.3.1-linux-x86_64.tar.gz
```
이 파일을 더블클릭해서 압축을 풀어준다. 압축을 풀면 `julia-1.3.1`라는 폴더가 생긴다. 이 폴더를 원하는 위치로 (줄리아가 설치되기를 원하는 위치) 이동시킨다. 나는 home에 이동시켰다. 

> 그 담에 아래를 실행시킨다. (둘중 아무거나 실행해도됨) 
```
/home/cgb/julia-1.3.1/bin/julia
~/julia-1.3.1/bin/julia
```
혹은 /home/cgb/julia-1.3.1/bin 으로 가서  ./julia와 같이 친다. 
```
cd /home/cgb/julia-1.3.1/bin
./julia
```
여기가지하면 줄리아가 실행된다. 

> 줄리아를 실행한뒤에 아래를 입력하면 주피터노트북에 연결된다. 
```
using Pkg
Pkg.add("IJulia")
```

> 한 가지 의문점이 있다. 나같은 경우는 `(base)`에서 줄리아를 실행하고 연결하였다. 그런데 혹시 몰라서 `(py20190129)`에서도 줄리아를 실행해봤는데 잘 실행되었다. 줄리아를 실행시키고 위의 명령 Pkg.add("IJulia")를 다시쳤는데, 이미 연결되어서 더이상 변화시킨게 없다는 메시지가 떴다. 이러면 `(base)`에 설치된 줄리아가 `(py20190129)`에서도 실행된 줄리아와 동일하다는 의미일까? --> 그렇다. 왜냐하면 줄리아는 `anaconda`내의 폴더에 설치한 것이 아니기 때문에. `home`에 보통 설치하니깐. 

> 참고로 어디서든 줄리아를 실행시키고 싶다면 환경변수를 조작하면 된다. 아래를 실행해서 나노에디터를 킨다. 
```
sudo nano /etc/environment
```
맨끝에 다음과 같이 되어있을 것이다. 
```
~~ usr/local/games"
```
마지막에 `/home/cgb/julia-1.3.1/bin/julia`를 추가한다. 즉 아래와 같이 만든다.
```
~~ usr/local/games:/home/cgb/julia-1.3.1/bin/julia"
```
세이브하고 나온다. (그런데 이 과정을 안거쳐도 되는것 같음.) 이제  커맨드에서 아래를 실행한다. 
```
export PATH=$PATH:/home/cgb/julia-1.3.1/bin
```
이렇게하면 이제 단순히 `julia`라고만 쳐도 `julia`가 실행된다. 

### github desktop 
> [여기](https://github.com/shiftkey/desktop/releases)로 간다.

> 한 챕터의 (2.3.1 Linux RC1 와 같이 되어있음) 아래쪽에 보면 **▶ Assets** 라고 되어있는데 이걸 클릭하면 다운받을 수 있는 파일들이 나온다. 확장자가 .deb로 끝나는걸 골라서 다운받은뒤에 실행한다. 

### `sublime text` and `TeX`
> Ubuntu Software에 가서 `sublime Text`를 치면 다운받을 수 있다. 다운받은뒤에 `file` -> `open folder`를 활용하여 깃허브의 로칼저장소를 열어두면 편리하다. 

> 아래를 실행하여 `TeX`을 깐다. 
```
sudo apt install texlive-full
```

> 이제 sublime과 latex을 연결하여보자. [여기](https://latextools.readthedocs.io/en/latest/install/#requirements-and-setup)를 참고하자. (1) `sublime`을 키고 `컨트롤+쉬프트+p`를 눌러 `Install Package Control` 선택 (2) 다시 `컨트롤+쉬프트+p` 를 눌러 `Package Control: Install Package`를 실행 (3) 그러면 바로 검색창이 나오는데 거기서 `LaTeXTools`를 입력해서 실행 (4) 다시 `컨트롤+쉬프트+p`를 누르고 `LaTeXTools: Check system` 선택. 모두 `available`이 나오면 잘된것이다. 이게 끝이다. 

> 아무 `tex`파일을 열고 `컨트롤+b`를 누르자. 처음이면 어떤 메뉴들이 보일텐데 그냥 `Latex`을 선택하자. 그러면 코딩결과가 pdf로 나온다. 

> `Perferences` > `Packages Setting` > `LaTeXTools` > `Settings-User`를 선택한다. `93번째라인`에 `preview_math_mode`를 "all"로 바꾼다. 그러면 수식들이 미리 출력된다. 그외에도 자유롭게 셋팅을 조정할 수 있다. 원래셋팅은  `Perferences` > `Packages Setting` > `LaTeXTools` > `Settings-Defaults` 에 있다. 

