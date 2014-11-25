# Tiny API Framework

## How to use

Like this examples in the taf.py you have to use the @get, @post. @put, @head, @delete decorator
to handle each request
    
    @get('/path/(?P<var>[0-9]+)\.(?P<format>(json|xml))')
        def func(vars):
            print c.request.headers.items()
            return vars

An instance of earch Request is stored in URLDispatchers request variable. 
You can access it in the requested function like this `c.request.<whatever>`.
`c` is an instance of URLDispatcher.

For more clearness print out `dir(c.request)`

`<var>` is stored in `vars`. `vars` is a Dict. Try this in `func`:

`print vars.get('var')`

## Questions?

Feel free to contact me on Twitter ( twitter.com/timoreinhold ). Feel also free to fork and improve it!