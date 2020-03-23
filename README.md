## List recipes
`$ curl -H "Host: command.line" -H "Content-Type: application/json" http://127.0.0.1:8000/api/recipe/recipes/`
[{"name": "RecetaX", "description": "bla bla bla"}, {"name": "RecetaX", "description": "bla bla bla"}]

## Default Ingredient list

## Adding new recipes
In order to get rid of "CommandError: You must set settings.ALLOWED_HOSTS if DEBUG is False.", we add a host to the curl:

`$ curl -X POST -H "Host: command.line" -H "Content-Type: application/json" -d '{"name":"Pizza-2", "description": "BBB", "ingredients": [{"name": "garlic"}, {"name": "water"}]}' http://127.0.0.1:8000/api/recipe/recipes/`
