# test_bitfury

## Quick Start:

1) Create `.env` file with you enviriment variables, example:
```
DATABASE_URL=postgres://postgres:@localhost/db
```

2) Install Pipenv
```
    pip install pipenv
```

3) Activate Pipenv
```
    pipenv shell
```

4) Install dependencies
```
    pipenv install
```

5) Django start
```
    pipenv run migrate
    pipenv run collectstatic
    pipenv run runserver
```

## Additional notes

#####There are two ways to do shareholders logic

1) Abstract model for general share and each type of shareholder object has its
 own model with changed "object" field. (This is the way i've done this task)  
 
 pros: all pretty simple and optimized queries  
 
 cons: more models and not fully DRY code + if we need to get all shares for 
 some users - then we will need to do some extra queries or extra model.
 
2) Single table for all shares  together using Generic foreign key. 
 
pros: reduced amount of models(1 instead of 4), easy to get different types of 
share together 
  
cons: not so good queries, harder to work with single type of share, more
 complicated code
---
##### In task said that Patent and Product should have identification number
I doesn't add extra field with id, because I think that database pk counts as
as such identification number. If you think that it is not - just tell me and I
will add some uuid field to mentioned models.
