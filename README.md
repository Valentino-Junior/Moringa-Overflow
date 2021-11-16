# Moringa-Overflow

## App Structure
~~~
|-Moringa-Overflow
    |-app/
        |-auth/
            |-__init__.py
            |-forms.py
            |-views.py
        |-main/
            |-__init__.py
            |-errors.py
            |-forms.py
            |-views.py
        |-static/
            |-css/
            |-photos/
        |-templates/
            |-auth/
                |-login.html
                |-signup.html
            |-email/
                |-welcome_user.html
                |-welcome_user.txt
            |-profile/
                |-profile.html
                |-update.html
            |-base.html
            |-comments.html
            |-fourOwfour.html
            |-post.html
            |-index.html
            |-downvote.html
            |-upvote.html
            |-macros.html
            |-navbar.html
            |-new_post.html
        |-__init__.py
        |-email.py
        |-models.py
    |-migrations/
    |-tests/
        |-test_comments.py
        |-test_downvote.py
        |-test_pitch.py
        |-test_upvote.py
        |-test_user.py
    |-virtual/
    |-config.py
    |-.gitignore
    |-LICENSE
    |-manage.py
    |-Procfile
    |-README.md
    |-requirements.txt
    |-start.sh
~~~

## Proposed additional functions
* editing the posts (prob & soln) and comments
* verification of the posts by admin