# config .vimrc

def config_vim(vim_basic_config):
    q0 = input("What's your username?\n")
    plugin_list=[
        'vim-airline/vim-airline',
        'vim-airline/vim-airline-themes',
        'ycm-core/YouCompleteMe',
        'bronson/vim-trailing-whitespace',
        'jiangmiao/auto-pairs',
        'scrooloose/nerdtree',
        'SirVer/ultisnips',

        'MarcWeber/vim-addon-mw-utils',
        'tomtom/tlib_vim',
        'garbas/vim-snipmate',
        'honza/vim-snippets']
    for idx,ele in enumerate(plugin_list):
        print(str(idx)+") "+ ele)
    nums=input("Which ones do you NOT want? Input digits seperated by comma.\n")
    if nums!='':
        excluded_idxs=[int(i) for i in nums.split(',')]
    else:
        excluded_idxs=[]

    string='" vim-plug配置\ncall plug#begin()\n'
    for idx,ele in enumerate(plugin_list):
        if idx not in excluded_idxs:
            string+=('Plug \''+ele+'\'\n')
        else:
            string+=('" Plug \''+ele+'\'\n')
    string+="call plug#end()\n\n"

    vim_config=string+vim_basic_config
    with open('/home/'+q0+'/.vimrc','w') as f:
        f.write(vim_config)
    f.close()

if __name__ == '__main__':
    with open('./.vimrc','r') as f:
        vim_basic_config=f.read()
    f.close()
    config_vim(vim_basic_config)
