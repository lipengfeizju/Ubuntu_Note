## Install Texlive from .iso file
### 1. mount `.iso` file
```shell
    sudo mkdir /media/texlive   
    sudo mount texlive2013-20130530.iso  /media/texlive  
```
### 2. Install 
```shell
cd /media/texlive
./install-tl  
```
### 3. Update Env Variables 
```shell
echo '# TeX Live 2015' >> ~/.bashrc
echo 'PATH=/usr/local/texlive/2017/bin/x86_64-linux:$PATH; export PATH' >> ~/.bashrc
echo 'MANPATH=/usr/local/texlive/2017/texmf-dist/doc/man:$MANPATH; export MANPATH' >> ~/.bashrc
echo 'INFOPATH=/usr/local/texlive/2017/texmf-dist/doc/info:$INFOPATH; export INFOPATH' >> ~/.bashrc

```

### 4. Install Chinese Font Packages
```shell
sudo apt-get install latex-cjk-all  
```


### 5. Test Document
```Latex
\documentclass{article}  
\usepackage{CJKutf8}  
\begin{document}  
\begin{CJK}{UTF8}{gkai}  
这是一个楷体中文测试，处理简体字。  
\end{CJK}  
\begin{CJK}{UTF8}{gbsn}  
这是一个宋体中文测试，处理简体字。  
\end{CJK}  
\begin{CJK}{UTF8}{bkai}  
這是一個big5編碼的楷體中文測試，處理繁體文字。  
\end{CJK}  
\begin{CJK}{UTF8}{bsmi}  
這是一個个big5編碼的明體中文測試，處理繁體文字。  
\end{CJK}  
\end{document}  
```

### 6. Install other fonts
```shell
sudo mkdir /usr/share/fonts/latex
sudo cp *.TTF /usr/share/fonts/latex
cd /usr/share/fonts/latex
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fv
```
### 7. Other test

```latex
\documentclass[11pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{STZhongsong}
\begin{document}
TeX Live, XeLaTeX, Texworks, 你们好! !
\end{document}
```







