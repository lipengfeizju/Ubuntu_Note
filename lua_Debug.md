## Lua Debug Package
[detailed tutorial](https://github.com/Atcold/torch-Developer-Guide/blob/master/MobDebug/README.md)
```
th -e "require('mobdebug').listen()"

file
   require('mobdebug').start()

run    -- runs until next breakpoint
step   -- runs until next line, stepping into function calls
over   -- runs until next line, stepping over function calls
out    -- runs until line after returning from current function

setb <file> <line>   -- sets a breakpoint

listb   -- lists breakpoints

delb <file> <line>   -- removes a breakpoint
delallb              -- removes all breakpoints


eval <exp>   -- evaluates expression on the current context and returns its value
exec <stmt>   -- executes statement on the current context



setw <exp>   -- adds a new watch expression
     >setw tab.foo == 32
     >run

listw   -- lists watch expressions
delw <index>   -- removes the watch expression at index
delallw        -- removes all watch expressions 

exit   -- exits debugger
```