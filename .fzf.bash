# Setup fzf
# ---------
if [[ ! "$PATH" == */afs/physnet.uni-hamburg.de/users/th1_li/alehmann/.fzf/bin* ]]; then
  export PATH="${PATH:+${PATH}:}/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/.fzf/bin"
fi

# Auto-completion
# ---------------
[[ $- == *i* ]] && source "/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/.fzf/shell/completion.bash" 2> /dev/null

# Key bindings
# ------------
source "/afs/physnet.uni-hamburg.de/users/th1_li/alehmann/.fzf/shell/key-bindings.bash"
