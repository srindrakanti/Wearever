To run:

If using conda env:
Create conda env with django
Open a conda prompt
>conda activate <env>

>cd <project directory>
	(may have to do >d: first if on different drive)
django-admin runserver --pythonpath=. --settings=<main python file>

NEW:

no longer need /wearever to access home page

oauth working for sign in (still need to determine what happens after sign in)

Algo: 

rows = Get user data
If no data:
	insert dummy data into db
	rows = Get user data (again)
elif last row from today:
	 return last row
Generate recommendation via ML
Add recommendation to database
return generated rec directly