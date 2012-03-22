# Tiny API Framework

## How to use

Like the examples in the taf.py you have to use the @get, @post. @put, @head, @delete decorator
to handle each request

@c.get('/path/(?P<a>[0-9]+)\.(?P<format>(json))')
    def func(query, vars):
        vars['query'] = query
        return vars
