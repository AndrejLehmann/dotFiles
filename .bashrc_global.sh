# bashrc lines common in all my systems

# use vi as editor in the command line
set -o vi

# https://wiki.archlinux.de/title/Xmodmap
# find keycode: $ xev
#xmodmap -e 'clear Lock' -e 'keycode 0x42 = Escape' # switches Caps Lock and Esc
#                              v-- key stroke with shift
#xmodmap -e 'keycode 47 = colon semicolon' # switches ; and :
#                        ^-- key stroke alone

export PS1="\[\e[31m\]\h\[\e[m\]\[\e[32m\]:\[\e[m\]\[\e[33m\]\w\[\e[m\]\[\e[32m\]\\$\[\e[m\] "  # costom prompt http://ezprompt.net/


# v-- added by fuzzy finder -------------------------------------------#
[ -f ~/.fzf.bash ] && source ~/.fzf.bash                               #
# v-- added by myself                                                  #
export FZF_DEFAULT_OPTS="--color hl+:214,hl:202 --extended --reverse"  #
# ---------------------------------------------------------------------#



# v-- Wegen des Fehlers: "Catastrophic error: could not set locale "" to allow processing of multibyte character" beim compilieren des Otsuki-solvers
export LC_ALL=en_US.UTF-8                #
export LANG=en_US.UTF-8                  #
export LANGUAGE=en_US.UTF-8              #
# ---------------------------------------#



# enable color support of ls and also add handy aliases$
if [ -x /usr/bin/dircolors ]; then
    test -r ~/dircolors && eval "$(dircolors -b ~/dircolors/dircolors.256dark)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi



cs() { builtin cd "$@" && ls; }

alias ll='ls -l'
alias la='ls -A'
alias l='ls -CF'
alias dir='ls -d --color=auto --format=vertical'
alias vdir='ls -d --color=auto --format=long'

