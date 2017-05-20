# remap prefix to C-a
unbind C-b
set-option -g prefix C-a
bind-key C-a send-prefix

# sane splits
bind | split-window -h
bind - split-window -v
unbind '"'
unbind %

# pane-switching
bind -n M-Left select-pane -L
bind -n M-Right select-pane -R
bind -n M-Up select-pane -U
bind -n M-Down select-pane -D
