" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! style_entire_code()
python << endOfPython

from pythoncodestyle import *

vim.current.buffer[:] = style_code(list(vim.current.buffer))

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! style call style_entire_code()
