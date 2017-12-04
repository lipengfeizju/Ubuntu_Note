# Ubuntu_Note
Some notes about Ubuntu Installation.

[Guide](https://coding.net/help/doc/project/markdown.html) in MarkDown Grammar

[commonly used commands](http://blog.csdn.net/wojiaopanpan/article/details/7286430)

## Save the passward
use *touch* to create ~/.git-credentials, edit 

``` shell
touch .git-credentials
vim .git-credentials
https://{username}:{password}@github.com
```

Open a new terminal
``` bash
git config --global credential.helper store
```

Reference 

[[1]](https://www.cnblogs.com/wanqieddy/archive/2012/08/03/2621027.html)
[[2]](http://www.jianshu.com/p/f54053afecf2)

## Change the kernal 

sudo gedit /etc/default/grub
> GRUB_DEFAULT=saved
>
> GRUB_SAVEDEFAULT=true

sudo update-grub

[GRUB 2 modification](http://blog.csdn.net/lu_embedded/article/details/44353499)

## Copy a file via SSH
```shell
scp /home/test/item.txtroot@192.168.1.129:/etc/test
```

## Some important [notes](https://www.cnblogs.com/wangrx/p/5907013.html) about vim
