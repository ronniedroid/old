# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH
# Keep 1000 lines of history within the shell and save it to ~/.zsh_history:
HISTSIZE=1000
SAVEHIST=1000
HISTFILE=~/.zsh_history

# Paths
export EDITOR=nvim

#############################
#PowerLineShell
#############################

function powerline_precmd() {
    PS1="$(powerline-shell --shell zsh $?)"
}

function install_powerline_precmd() {
  for s in "${precmd_functions[@]}"; do
    if [ "$s" = "powerline_precmd" ]; then
      return
    fi
  done
  precmd_functions+=(powerline_precmd)
}

if [ "$TERM" != "linux" ]; then
    install_powerline_precmd
fi

# Path to your oh-my-zsh installation.
  export ZSH="/home/ron/.oh-my-zsh"

ZSH_THEME="dracula"

plugins=(git)

source $ZSH/oh-my-zsh.sh

alias i3conf="sudo vim ~/.config/i3/config"
alias polyconf="sudo vim ~/.config/polybar/config"
alias off="sudo poweroff"
alias reboot="sudo reboot"
alias bspc="sudo vim ~/.config/bspwm/bspwmrc"
alias bspcx="sudo vim ~/.config/sxhkd/sxhkdrc"
alias vim="sudo vim"
alias c="~/.config/"
alias s="~/Scripts/"
alias d="~/Downloads/"
alias h="~/"
