
" ----- Unmap the arrow keys -----

"no <down> <Nop>
"no <left> <Nop>
"no <right> <Nop>
"no <up> <Nop>
"ino <down> <Nop>
"ino <left> <Nop>
"ino <right> <Nop>
"ino <up> <Nop>
"vno <down> <Nop>
"vno <left> <Nop>
"vno <right> <Nop>
"vno <up> <Nop>



autocmd! bufwritepost .vimrc source %

" ----- Remap Esc to Caps Lock -----

"if $DISPLAY
"Maps Esc to the Caps lock key when Vim entered
"au VimEnter * !xmodmap -e 'clear Lock' -e 'keycode 0x42 = Escape' "<-- included in .bashrc


"Returns normal functionality to caps lock when Vim quited
"au VimLeave * !xmodmap -e 'clear Lock' -e 'keycode 0x42 = Caps_Lock'

"endif



" ----- Allow us to use Ctrl-s and Ctrl-q as keybinds -----
silent !stty -ixon
" Restore default behaviour when leaving Vim.
autocmd VimLeave * silent !stty ixon



" ----- spell checking set to Ctrl-s -----

noremap <C-s> :setlocal spell! spelllang=en_us<CR>

" press Ctrl-n or Ctrl-p in insert-mode to complete the word
"set complete+=kspell

" add a word to a dictionary: cursor over the word and type 'zg'



" ----- Enable syntax and plugins (for netrw) -----

syntax enable
filetype plugin on



" ---- modifiable -----
set ma


" ----- vim-vinegar initializes dot files hidden -----

let g:netrw_list_hide = '\(^\|\s\s\)\zs\.\S\+'
let g:netrw_bufsettings = 'noma nomod nu nobl nowrap ro'



" ----- Finding files -----

"  Kritik: tpope/vim-apathy
"Hit tab to :find by partial math
"Use * to make it fuzzy
"set path+=** "Search down into subfolder. Provides tab-completion for all file-related tasks
set wildmode=longest:full
set wildmenu

set rtp+=~/.fzf " for fzf in vim



" ----- Undo settings -----

set undofile
set undodir=~/.vim/undo
set undolevels=5000 "Number of undos
set undoreload=50000 "Number of lines to save for undo
set backupdir=~/.vim/backup/
set directory=~/.vim/backup/



" ----- Leader key -----

let mapleader = '\'



" ----- Vundel ----- "

set nocompatible "Be iMproved
filetype off

set rtp+=~/.vim/bundle/Vundle.vim "The runtime path

" Keep Plugin commands between vundle#begin/end.

call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'ludovicchabant/vim-gutentags' " Use ctags first to set up tags
Plugin 'morhetz/gruvbox' " colorscheme
Plugin 'w0ng/vim-hybrid' " colorscheme
Plugin 'tpope/vim-vinegar'
"Plugin 'SirVer/ultisnips' " Track the engine. Tutorials on github.
"Plugin 'honza/vim-snippets' " Snippets are separated from the engine. Add this if you want them.
Plugin 'tpope/vim-fugitive' " git wrapper. For help and bindings :Gstatus, g? .Tutorials on github 
Plugin 'brennier/quicktex'  "ab vim 7.8
Plugin 'tpope/vim-repeat' " Adding support to a plugin is generally as simple as the following command at the end of your map functions:
                                                                                                                                       " silent! call repeat#set("\<Plug>MyWonderfulMap", v:count)
"Plugin 'tpope/vim-surround'   " find examples at github
"Plugin 'tpope/vim-commentary' " gc2j : Comment down two lines
                               " gcc  : Comment out the current line
                               " gcip : Comment out the current paragraph
                               " If a file type isn't supported, adjust 'commentstring': autocmd FileType apache setlocal commentstring=#\ %s

Plugin 'christoomey/vim-system-copy' " cpi' : copy inside single quotes to system clipboard
                                     " cvi' : paste inside single quotes from system clipboard
                                     " cP   : copy the current line
                                     " cV   : paste the content of system clipboard to the next line.
                                     " Clipboard Utilities: OSX - pbcopy and pbpaste, Linux - xsel

Plugin 'kana/vim-textobj-user' " for the following text objects
Plugin 'bkad/CamelCaseMotion'       " indentifies CamelCase  and underscore_notation as words
Plugin 'vim-scripts/argtextobj.vim' " text-object 'a' (argument). E.g. 'daa' :  delete around argument
Plugin 'rbonvall/vim-textobj-latex' " a\ i\ : Inline math surrounded by \( and \). $asfasdf$
                                    " a$ i$ : Inline math surrounded by dollar signs.
                                    " aq iq : Single-quoted text `like this'.
                                    " aQ iQ : Double-quoted text ``like this''.
                                    " ae ie : Environment \begin{…} to \end{…}
Plugin 'michaeljsmith/vim-indent-object' "V <count>ai : around Indentation level and line above.
                                         "V <count>ii : inner Indentation level (no line above).
                                         "V <count>aI : around Indentation level and lines above/below.
                                         "V <count>iI : inner Indentation level (no lines above/below).
Plugin 'bps/vim-textobj-python' " af : around function
                                " if : inner function
                                " ac : around class
                                " ic : inner class
                                " [pf ]pf: move to next/previous function
                                " [pc ]pc: move to next/previous class
                                " change mapping (e.g. to avoid conflicts with other plugins) like: nmap aF <Plug>(textobj-python-function-a)
Plugin 'libclang-vim/libclang-vim' " for vim-textobj-clang
Plugin 'libclang-vim/vim-textobj-clang' " c/c++ text objects:
                                        " i;  : selects the element under cursor. a; selects the most inner definition under cursor.
                                        " i;m : select the most inner definition
                                        " i;c : select class blocks
                                        " i;f : select function blocks
                                        " i;e : select an expression
                                        " i;s : select an statement
                                        " i;p : select an parameter and a template parameter
                                        " i;n : select a namespace
                                        " i;u : select an element under cursor
                                        " i;a : select expression, statement,
                                        "              function, class or namespace

Plugin 'sjl/gundo.vim' " graphical undo history. Requirements: Vim 7.3+, Python support for Vim, Python 2.4+
Plugin 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' } " Install fzf in command line and vim
Plugin 'junegunn/fzf.vim'
"Plugin 'cyboflash/hlnext' " delete 'gg' in .vim/bundle/hlnext/plugin/hlnext.vim L.68: let &cpo = s:save_cpogg . It is still buggy.
"Plugin 'gioele/vim-autoswap' " autohandle .swp files:
                              " 1. Is file already open in another Vim session in some other window?
                              "    If so, swap to the window where we are editing that file.
                              " 2. Otherwise, if swapfile is older than file itself, delete it.
                              " 3. Otherwise, open file read-only so we can have a look at it and may save it.

call vundle#end()



" ----- fzf -----

nnoremap <silent> <leader>o :FZF<CR>
nnoremap <silent> <leader>O :FZF!<CR>
nnoremap <silent> <leader>: :History:<CR>
nnoremap <silent> <leader>/ :History/<CR>
nnoremap <silent> <leader>m :Marks<CR>
nnoremap <silent> <leader>C :Commands<CR>
nnoremap <silent> <leader>l :BLines<CR>



" ----- UltiSnips -----

" Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.
"let g:UltiSnipsExpandTrigger="<tab>"
"let g:UltiSnipsJumpForwardTrigger="<c-b>"
"let g:UltiSnipsJumpBackwardTrigger="<c-z>"

" If you want :UltiSnipsEdit to split your window.
"let g:UltiSnipsEditSplit="vertical"



filetype plugin indent on

"" To ignore plugin indent changes, instead use:
"filetype plugin on



" ----- CamelCaseMotion -----

let g:camelcasemotion_key = '<leader>' " usage with leader key like \w
" v-- usual usage
"map <silent> w <Plug>CamelCaseMotion_w
"map <silent> b <Plug>CamelCaseMotion_b
"map <silent> e <Plug>CamelCaseMotion_e
"map <silent> ge <Plug>CamelCaseMotion_ge
"sunmap w
"sunmap b
"sunmap e
"sunmap ge
"omap <silent> iw <Plug>CamelCaseMotion_iw
"xmap <silent> iw <Plug>CamelCaseMotion_iw
"omap <silent> ib <Plug>CamelCaseMotion_ib
"xmap <silent> ib <Plug>CamelCaseMotion_ib
"omap <silent> ie <Plug>CamelCaseMotion_ie
"xmap <silent> ie <Plug>CamelCaseMotion_ie



" ----- argtextobj.vim -----

let g:argumentobject_force_toplevel = 0
" ^-- e.g.: function(1, (20*30)+40, somefunc2(<press 'cia' here>3, 4))
"           function(1, (20*30)+40, somefunc2(<cursor here>4))
"g:argumentobject_force_toplevel = 1
" ^-- e.g.: function(1, (20*30)+40, somefunc2(<press 'cia' here>3, 4))
"           function(1, (20*30)+40, <cursor here>) " sub-level function is deleted because it is a argument in terms of the outer



" ----- vimtex -----

"let g:vimtex_view_general_viewer = 'evince'



" ----- Airline configurations -----

set ttimeoutlen=5
set laststatus=2
"let g:airline_theme='bubblegum'
"let g:airline_theme='gruvbox'
let g:airline_theme='onedark' " for atom-dark line
set noshowmode

""Makes Airline look like Poweline
"let g:airline_section_z = airline#section#create(['windowswap', '%3p%% ', 'linenr', ':%3v'])
if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif

"To type unixcode char: Ctrl+Shift+u => [codenumber]
"some unixcode char: ∥  ⭠ ⭡ » « 🔒  ⌥  Ξ ⮁ ⮃  ⊲ ⊳ ⋖ ⋗ ≪  ≫  ≺  ≻ ⍃ ⍄ ⎨ ⎬ ▶ ◀ ▸ ◂ ▷ ◁ ▹ ◃
let g:airline_left_sep = ''
let g:airline_right_sep = ''
let g:airline_symbols.crypt = ''
let g:airline_symbols.linenr = ''
let g:airline_symbols.maxlinenr = ''
let g:airline_symbols.branch = ''
let g:airline_symbols.paste = ''
let g:airline_symbols.whitespace = ''



" ----- Display unprintable characters ----- 

"  v--- https://stackoverflow.com/questions/32588604/vim-airline-what-is-trailing1
set list 
set listchars=tab:•\ ,trail:•,extends:»,precedes:« " Unprintable chars mapping
" More on highlighting unwanted spaces: http://vim.wikia.com/wiki/Highlight_unwanted_spaces



" ----- Powerline -----

"Powerline fonts are installed in /afs/physnet.uni-hamburg.de/users/th1_li/alehmann/.local/share/fonts



" ----- Clear all registers -----

" :ClearReg to clear all registers
function! ClearRegisters()
  let regs='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/-="'
  let i=0
  while (i<strlen(regs))
    exec 'let @'.regs[i].'=""'
    let i=i+1
  endwhile
endfunction
command! ClearReg call ClearRegisters()



" ----- Splits -----

"Easier split navigation
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

"More natural split opening
set splitbelow
set splitright

"The time in milliseconds that is waited for a key code or mapped key sequence to complete.
set timeoutlen=1000

set background=dark
"set background=light
syntax on
"colorscheme apprentice
"colorscheme hybrid
let g:gruvbox_contrast_dark = 'hard' " options for gruvbox --v
"let g:gruvbox_contrast_dark = 'medium' " options for gruvbox --v
"let g:gruvbox_contrast_dark = 'soft' " options for gruvbox --v
colorscheme gruvbox



" ----- highlight the 81 column -----
"highlight ColorColumn ctermbg=magenta
"set colorcolumn=81
"                            v-- regex
call matchadd('ColorColumn','\%81v',100) "only if line size > 81 columns



" ----- Use <,> for f/t searching -----
" <,> sind gemaped auf Einrueckungen
"no , <Nop>
"no ; <Nop>
"nnoremap < ,
"nnoremap > ;



" ----- n/N always searching forward -----

noremap n /<CR>
noremap N ?<CR>
"nnoremap <expr> n 'Nn'[v:searchforward]
"nnoremap <expr> N 'nN'[v:searchforward]
" or
"nnoremap <expr> n (v:searchforward ? 'n' : 'N')
"nnoremap <expr> N (v:searchforward ? 'N' : 'n')



" ----- highlight search -----
"
set hlsearch
nnoremap <C-c> :set hlsearch!<CR>



" ----- Line numbers & rel line numbers -----

set number
set relativenumber
"highlight LineNr ctermfg=grey
"highlight CursorLineNr ctermfg=yellow

"Ctrl+n to turn hybrid line number mode (relative/absolute) on/off
function! NumberToggle()
  set number!
  set relativenumber!
endfunc
nnoremap <C-n> :call NumberToggle()<cr>



" ----- Tabs -----

set tabstop=8 softtabstop=0 expandtab shiftwidth=2 smarttab

nnoremap <C-w> gt
noremap <C-e> gT
nnoremap <C-1> 1gt
nnoremap <C-2> 2gt
nnoremap <C-3> 3gt
nnoremap <C-4> 4gt
nnoremap <C-5> 5gt
nnoremap <C-6> 6gt
nnoremap <C-7> 7gt
nnoremap <C-8> 8gt
nnoremap <C-9> 9gt
nnoremap <C-0> :tablast<CR>



" ---- gundo settings ----
"         v-- press for graphical undo history
nnoremap <F5> :GundoToggle<CR>"
let g:gundo_width = 60
let g:gundo_preview_height = 40
" for more: https://sjl.bitbucket.io/gundo.vim/



" ----- use the clipboard as the default register -----

set pastetoggle=<F2>
set clipboard=unnamedplus
             "^-- the + register (X Window clipboard)



