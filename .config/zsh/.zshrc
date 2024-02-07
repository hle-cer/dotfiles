
#       ███████╗███████╗██╗  ██╗██████╗  ██████╗
#       ╚══███╔╝██╔════╝██║  ██║██╔══██╗██╔════╝
#         ███╔╝ ███████╗███████║██████╔╝██║     
#        ███╔╝  ╚════██║██╔══██║██╔══██╗██║     
#    ██╗███████╗███████║██║  ██║██║  ██║╚██████╗
#    ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝
                                                                                                      
# History
HISTFILE=~/.config/zsh/history
HISTSIZE=10000
SAVEHIST=10000
setopt extended_history
setopt hist_expire_dups_first
setopt hist_ignore_dups # ignore duplication command history list
setopt hist_ignore_space
setopt hist_verify
setopt inc_append_history
setopt share_history

#completions
setopt auto_menu         # show completion menu on succesive tab press
setopt complete_in_word
setopt completealiases
setopt always_to_end

#    ███████╗██╗  ██╗██████╗  ██████╗ ██████╗ ████████╗███████╗
#    ██╔════╝╚██╗██╔╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝
#    █████╗   ╚███╔╝ ██████╔╝██║   ██║██████╔╝   ██║   ███████╗
#    ██╔══╝   ██╔██╗ ██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║
#    ███████╗██╔╝ ██╗██║     ╚██████╔╝██║  ██║   ██║   ███████║
#    ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
                                                    
export EDITOR="helix"
export BROWSER="firefox"

#    ██████╗ ██████╗  ██████╗ ███╗   ███╗██████╗ ████████╗
#    ██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝
#    ██████╔╝██████╔╝██║   ██║██╔████╔██║██████╔╝   ██║   
#    ██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██╔═══╝    ██║   
#    ██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║        ██║   
#    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝   

parse_git_dirty() {
  git_status="$(git status 2> /dev/null)"
  [[ "$git_status" =~ "Changes to be committed:" ]] && echo -n "%F{green}·%f "
  [[ "$git_status" =~ "Changes not staged for commit:" ]] && echo -n "%F{yellow}·%f "
  [[ "$git_status" =~ "Untracked files:" ]] && echo -n "%F{red}·%f "
}

setopt prompt_subst

NEWLINE=$'\n'

autoload -Uz vcs_info
precmd () { vcs_info }
zstyle ':vcs_info:git*' formats ' 󰊢 (%F{red}%b%F{gray})'

PS1='%F{blue}%(5~|%-1~/⋯/%3~|%4~)%F{gray}${vcs_info_msg_0_} $(parse_git_dirty)%F{blue}%f '

#     █████╗ ██╗     ██╗ █████╗ ███████╗███████╗███████╗
#    ██╔══██╗██║     ██║██╔══██╗██╔════╝██╔════╝██╔════╝
#    ███████║██║     ██║███████║███████╗█████╗  ███████╗
#    ██╔══██║██║     ██║██╔══██║╚════██║██╔══╝  ╚════██║
#    ██║  ██║███████╗██║██║  ██║███████║███████╗███████║
#    ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
                                                   
# Pacman
alias pac="sudo pacman"
alias pacs="sudo pacman -S --needed"
alias pacr="sudo pacman -Rns"
alias pacss="pacman -Ss"

# Helix
alias hx="helix"
alias shx="sudo helix"

# Ranger
alias rr="ranger"
alias srr="sudo ranger"

# Qtile
alias qconf="helix ~/.config/qtile/config.py"
alias qkey="helix ~/.config/qtile/keybindings.py"

# Zsh
alias zshconf="helix ~/.config/zsh/.zshrc"

# Coding template
alias tm="~/./projects/templates/release"
alias tmhx="~/./projects/templates/release && hx main.cpp" # also launch the template tn Helix

# QOL
alias cm="chmod +x"
alias ls="exa --icons -1"

# Mouse
# alias rma="~/./.local/bin/mouse.sh"

# Git
alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

#    ██████╗ ██╗     ██╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
#    ██╔══██╗██║     ██║   ██║██╔════╝ ██║████╗  ██║██╔════╝
#    ██████╔╝██║     ██║   ██║██║  ███╗██║██╔██╗ ██║███████╗
#    ██╔═══╝ ██║     ██║   ██║██║   ██║██║██║╚██╗██║╚════██║
#    ██║     ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║███████║
#    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝

PLUGINS=~/.config/zsh/plugins

# auto-suggest
source $PLUGINS/zsh-autosuggestions/zsh-autosuggestions.zsh

# syntax-highliting
source $PLUGINS/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# double tap Esc to add "sudo" infront of a command
source $PLUGINS/zsh-sudo/zsh-sudo.zsh

# auto-complete
source $PLUGINS/zsh-autocomplete/zsh-autocomplete.plugin.zsh
bindkey '\t' menu-select "$terminfo[kcbt]" menu-select
bindkey -M menuselect '\t' menu-complete "$terminfo[kcbt]" reverse-menu-complete
unsetopt completealiases
