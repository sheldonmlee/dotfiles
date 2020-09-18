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

