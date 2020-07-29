#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

# for nnn file manager
n ()
{
    # Block nesting of nnn in subshells
    if [ -n $NNNLVL ] && [ "${NNNLVL:-0}" -ge 1 ]; then
        echo "nnn is already running"
        return
    fi

    # The default behaviour is to cd on quit (nnn checks if NNN_TMPFILE is set)
    # To cd on quit only on ^G, remove the "export" as in:
    #     NNN_TMPFILE="${XDG_CONFIG_HOME:-$HOME/.config}/nnn/.lastd"
    # NOTE: NNN_TMPFILE is fixed, should not be modified
    export NNN_TMPFILE="${XDG_CONFIG_HOME:-$HOME/.config}/nnn/.lastd"

    # Unmask ^Q (, ^V etc.) (if required, see `stty -a`) to Quit nnn
    # stty start undef
    # stty stop undef
    # stty lwrap undef
    # stty lnext undef

    nnn "$@"

    if [ -f "$NNN_TMPFILE" ]; then
            . "$NNN_TMPFILE"
            rm -f "$NNN_TMPFILE" > /dev/null
    fi
}

#.dotfiles repo alias
alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
# show file sizes alias and sort by size
alias sizes='du -hs .[^.]* * | sort -h'
# tmux '-2' colors
alias tmux="tmux -2"
# bash tree alias
alias gittree="git log --all --decorate --oneline --graph"

# nnn
# bookmarks
export NNN_BMS='q:~/.config/qtile/;'
# use trashcan
export NNN_TRASH=1

# custom scripts
CUSTOM_SCRIPTS_FILE=~/.custom_bash_scripts.sh
if test -f $CUSTOM_SCRIPTS_FILE; then
	source $CUSTOM_SCRIPTS_FILE
else
	echo ".custom_bash_scripts.sh does not exist."
fi
# vi bindings
set -o vi

# default programs
export EDITOR=vim
export VISUAL=vim
