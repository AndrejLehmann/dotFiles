# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes
force_bold_prompt=yes	# - (c) MiV  ;-)

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ -n "$force_bold_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput bold >&/dev/null; then
        # We have bold support; assume it's compliant with Ecma-48
        # (ISO/IEC-6429). (Lack of such support is extremely rare)..
        bold_prompt=yes
    else
        bold_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi

if [ "$bold_prompt" = yes ]; then
      PS1="${debian_chroot:+($debian_chroot)}\[`tput -Tvt100 bold`\]\u\[`tput -Tvt100 rmso`\]@\[`tput -Tvt100 bold`\]\h\[`tput -Tvt100 rmso`\]:\w\$ "
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt bold_prompt force_bold_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors/dircolors.256dark)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    alias dir='ls --color=auto --format=vertical'
    #alias vdir='vdir --color=auto'
    alias vdir='ls --color=auto --format=long'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

export PS1="\[\e[31m\]\h\[\e[m\]\[\e[32m\]:\[\e[m\]\[\e[33m\]\w\[\e[m\]\[\e[32m\]\\$\[\e[m\] "  # costom prompt http://ezprompt.net/

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bashAliases.sh
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# PHYSnet' Intel compiler..
#if [ -r /opt/intel/ics2011/composerxe/bin/compilervars.sh ]; then 
#    . /opt/intel/ics2011/composerxe/bin/compilervars.sh  intel64
#fi

[ -r /opt/sw/.physnetrc ] && . /opt/sw/.physnetrc


#---------------------------------------------------#
#  v-- ab hier alles editiert von mir: 12.06.19 --v #
#---------------------------------------------------#

# use vi as editor in the command line
set -o vi

# https://wiki.archlinux.de/title/Xmodmap
# find keycode: $ xev
xmodmap -e 'clear Lock' -e 'keycode 0x42 = Escape' # switches Caps Lock and Esc
#                              v-- key stroke with shift
#xmodmap -e 'keycode 47 = colon semicolon' # switches ; and :
#                        ^-- key stroke alone



# v-- added by fuzzy finder ---------------------
[ -f ~/.fzf.bash ] && source ~/.fzf.bash        #
# v-- added by myself                           #
export FZF_DEFAULT_OPTS="--color hl+:214,hl:202 --extended --reverse"  #
# -----------------------------------------------


# v-- Wegen des Fehlers "Catastrophic error: could not set locale "" to allow processing of multibyte character" beim compilieren des Otsuki-solvers
#export LC_ALL=en_US.UTF-8                #
#export LANG=en_US.UTF-8                  #
#export LANGUAGE=en_US.UTF-8              #
# -----------------------------------------

source ~/.bashAliases.sh
