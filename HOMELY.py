from pathlib import Path
from homely.files import symlink
from homely.system import haveexecutable, execute
from homely.install import installpkg


if haveexecutable('apt'):
    if not haveexecutable('git'):
        installpkg('git')
    if not haveexecutable('curl'):
        installpkg('curl')
    if not haveexecutable('wget'):
        installpkg('wget')
    if not haveexecutable('zsh'):       
        installpkg('zsh')
    if not haveexecutable('vim'):
        installpkg('vim')
    if not haveexecutable('tmux'):
        installpkg('tmux')


omz_dir = Path('~/.oh-my-zsh')
if not omz_dir.is_dir():
    execute(['sh', '-c', "'$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)'")
    
vundle_dir = Path('~/.vim/bundle/Vundle.vim')
if not vundle_dir.is_dir():
    execute(['git','clone','https://github.com/VundleVim/Vundle.vim.git', '~/.vim/bundle/Vundle.vim'])
    execute(['vim','+PluginInstall'])
   

    
symlink('tmux', "~/.tmux.conf")
symlink('git', "~/.gitconfig")
symlink('zsh', "~/.zshrc")
symlink('vim', "~/.vimrc")


