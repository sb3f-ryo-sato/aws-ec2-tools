# aws-ec2-tools

1. Generate a SSH config file for AWS EC2.

```
$ ./generate-ec2-ssh-config.py > ~/.ssh/ec2-ssh.conf
$ echo 'Include ~/.ssh/*.conf' >> ~/.ssh/config
$ chmod -v 0600 ~/.ssh/ec2-ssh.conf ~/.ssh/config
```

2. Generate a alias file for SSH config.

```
$ ./generate-ec2-aliases.py > ~/.bash_ec2_aliases
$ echo 'if [ -r ~/.bash_ec2_aliases ]; then . ~/.bash_ec2_aliases; fi' >> ~/.bashrc
```
