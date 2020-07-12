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
let g:airline_theme='light'
" let g:airline_theme='raven'

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
set pastetoggle=<F4>


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
