# bashrc lines common in all my systems

# use vi as editor in the command line
set -o vi

# https://wiki.archlinux.de/title/Xmodmap
# find keycode: $ xev
xmodmap -e 'clear Lock' -e 'keycode 0x42 = Escape' # switches Caps Lock and Esc
#                              v-- key stroke with shift
#xmodmap -e 'keycode 47 = colon semicolon' # switches ; and :
#                        ^-- key stroke alone



# v-- added by fuzzy finder -------------------------------------------#
[ -f ~/.fzf.bash ] && source ~/.fzf.bash                               #
# v-- added by myself                                                  #
export FZF_DEFAULT_OPTS="--color hl+:214,hl:202 --extended --reverse"  #
# ---------------------------------------------------------------------#


# v-- Wegen des Fehlers: "Catastrophic error: could not set locale "" to allow processing of multibyte character" beim compilieren des Otsuki-solvers
export LC_ALL=en_US.UTF-8                #
export LANG=en_US.UTF-8                  #
export LANGUAGE=en_US.UTF-8              #
# -----------------------------------------
