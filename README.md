In order to get rid of "CommandError: You must set settings.ALLOWED_HOSTS if DEBUG is False.", we add a host to the curl: `-H "Host: command.line"`.


## List recipes
`curl -H "Host: command.line" -H "Content-Type: application/json" http://127.0.0.1:8000/api/recipe/recipes/`

```
[{"id":22,"name":"Pizza","description":"Put it in the oven","ingredients":[{"name":"base"},{"name":"oil"}]},{"id":24,"name":"Pizza","description":"Capresse","ingredients":[{"name":"base"},{"name":"cheese"}]}]
```


## Search for recipe
`curl -H "Host: command.line" -H "Content-Type: application/json" http://127.0.0.1:8000/api/recipe/recipes/?name=Pizza`

```
[{"id":22,"name":"Pizza","description":"Put it in the oven","ingredients":[{"name":"base"},{"name":"oil"}]}]
```


## Adding new recipes
`curl -X POST -H "Host: command.line" -H "Content-Type: application/json" -d '{"name":"Pizza", "description": "Capresse", "ingredients": [{"name": "base"}, {"name": "tomato", "name": "cheese"}]}' http://127.0.0.1:8000/api/recipe/recipes/`

```
{"id":24,"name":"Pizza","description":"Capresse","ingredients":[{"name":"base"},{"name":"cheese"}]}
```

## Editing a recipe
`curl -X PATCH -H "Host: command.line" -H "Content-Type: application/json" -d '{"name":"Pizza-2", "description": "Capresse without tomato", "ingredients": [{"name": "base"}, {"name": "tomato", "name": "salt"}]}' http://127.0.0.1:8000/api/recipe/recipes/24/`

```
{"id":24,"name":"Pizza-2","description":"Capresse without tomato","ingredients":[{"name":"base"},{"name":"salt"}]}
```

## Delete a recipe
`curl -X DELETE -H "Host: command.line" -H "Content-Type: application/json" http://127.0.0.1:8000/api/recipe/recipes/24/`
