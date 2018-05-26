## install pandoc

### 1. Install
```shell
sudo apt-get install pandoc
```

### 2. Usage
```shell
# 有目录
pandoc -N -s --toc --smart --latex-engine=xelatex -V CJKmainfont='STXingkai' -V mainfont='URW Palladio L' -V geometry:margin=1in readme.md  -o output.pdf
# 无目录
pandoc -N -s --smart --latex-engine=xelatex -V CJKmainfont='STXingkai' -V mainfont='URW Palladio L' -V geometry:margin=1in readme.md  -o output.pdf
```
