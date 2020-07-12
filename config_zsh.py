# config .zshrc

general_append='''
# ****************************My configuration****************************
alias la="ls -a"
alias ll="ls -thal"

alias sai="sudo apt install"
alias saud="sudo apt update"
alias saug="sudo apt upgrade"

# load bin
export PATH=~/bin:"$PATH"
'''

pyenv_append='''
# load pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="/home/username/.pyenv/bin:$PATH"
export PYTHON_CONFIGURE_OPTS="--enable-shared"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
'''

linux_append='''

'''

wsl_config='''
# ****************************Wsl settings****************************
alias edge="'/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'"
alias xxt="edge http://nuaa.fanya.chaoxing.com/portal"
alias oe="explorer.exe"

alias cdd="cd /mnt/e/desktop"
alias cdg="cd /mnt/e/gitdir"
alias cda="cd '/mnt/e/OneDrive - nuaa.edu.cn/Algorithm'"
alias cdod="cd '/mnt/e/OneDrive - nuaa.edu.cn'"
alias cdod="cd '/mnt/e/OneDrive - nuaa.edu.cn'"
'''

def config_zsh():
    q0 = input("What's your username?\n")
    path = "/home/username/.zshrc".replace("username",q0)
    with open(path,"a") as f:
        f.write(general_append)

    q1 = input("Do you want to use pyenv? y) yes; n) no\n")
    if q1 == "y":
        with open(path,"a") as f:
            f.write(pyenv_append.replace("username",q0))

    q2 = input("Which OS are you using? a) Linux; b) WSL\n")
    with open(path,"a") as f:
        if q2 == 'a':
            f.write(linux_append)
        else:
            f.write(wsl_config)
    f.close()

if __name__ == '__main__':
    config_zsh()
