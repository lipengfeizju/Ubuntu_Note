If A can connect to B, but B can't connect to A

On the server A side
```shell
Host home_jump
  Hostname 71.83.199.236
  User anny
  Port 937
  RemoteForward 7435 localhost:22
```

On the server B side
```shell
Host server_jump
    HostName 127.0.0.1
    Port 7435
    User khuang@kean.edu
```

Then you first use `ssh home_jump` on server A to establish Tunnel, then you can use `ssh home_jump` on server B to connect back to server A.
