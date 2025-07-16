# clean-architecture-python
learning Clean Architecture with python

Command Git
    git add . & git commit -m "Config: initial commits"
    current_branch=$(git rev-parse --abbrev-ref HEAD) && d=`date +%Y%m%d_%H%M%S` && git add . && git commit -m "Henrique's push into ${current_branch} at ${d}" && git push origin $current_branch && echo $d

Criar env
    python -m venv venv

Command env
    .\venv\Scripts\activate
    source venv/Scripts/activate
    .\venv\Scripts\pip3 freeze > requirements.txt
    .\venv\Scripts\pip3 install -r requirements.txt

pre-commit
    pre-commit install


    current_branch=$(git rev-parse --abbrev-ref HEAD) && d=`date +%Y%m%d_%H%M%S` && git push origin $current_branch && echo $d