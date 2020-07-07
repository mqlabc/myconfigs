" vim-plug配置
call plug#begin('~/.vim/plugged')
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
" Plug 'ycm-core/YouCompleteMe'
Plug 'bronson/vim-trailing-whitespace'
Plug 'jiangmiao/auto-pairs'
Plug 'scrooloose/nerdtree'

" snips实现：弃用ultisnips（需要python3支持）
Plug 'MarcWeber/vim-addon-mw-utils'
Plug 'tomtom/tlib_vim'
Plug 'garbas/vim-snipmate'
Plug 'honza/vim-snippets'
call plug#end()

" ****************************************基本配置****************************************
set encoding=utf-8
syntax on
set nu
set relativenumber
" 跳转窗口
" 使用ctrl+w+w

" 主题
colo molokai
" 使得airline颜色变得正常
set termguicolors
" 使用时的外观
set cursorline
set hlsearch
" airline主题
let g:airline_powerline_fonts = 1
let g:airline_theme='solarized'
let g:airline_solarized_bg='dark'

" 缩进
set tabstop=4
set softtabstop=4
set shiftwidth=4
set autoindent

" 搜索时忽略和智能忽略大小写
set ignorecase
set smartcase

" 启用鼠标
if has('mouse')
    set mouse+=a
endif

" 切换粘贴
set pastetoggle=<F2>


" ****************************************插件配置****************************************

" ycm配置
" 关闭上方的ycm窗口
set completeopt=menu
" 为ultisnips留出tab
let g:ycm_key_list_select_completion = ['<c-n>', '<Down>']
let g:ycm_key_list_previous_completion = ['<c-p>', '<Up>']

" nerdtree配置
 map <F3> :NERDTreeToggle<CR>
 autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") &&b:NERDTreeType == "primary") | q | endif
 " 不打开特定文件时显示nerdtree
 autocmd StdinReadPre * let s:std_in=1
 autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif


" ****************************************无用配置****************************************
" set paste
" set showmode
" set showcmd
" filetype plugin on
" filetype indent on
" let &t_SI = "\<Esc>]50;CursorShape=1\x7"
" let &t_SR = "\<Esc>]50;CursorShape=2\x7"
" let &t_EI = "\<Esc>]50;CursorShape=0\x7"
