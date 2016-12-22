https://github.com/ulgoon/fcwps-pre

# pyenv 레포를 .pyenv에 복사

$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv


# vi ~/.bashrc or ~/.bash_profile

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

eval "$(pyenv init -)"

# ubuntu requirement
$ apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils

# pyenv operation

$ pyenv
$ pyenv install 3.5.2
$ pyenv shell 3.5.2
$ pyenv deactivate









