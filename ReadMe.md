# Aivo Challenge

## Use

You can run this project by installing the packages in the `requirements.txt` file

    pip install -r requirements.txt

and then running:
    
    python manage.py runserver


## Details
Once the server is running you can send GET requests to `http://localhost:8000/endpoint/`
It currently takes `value` as a parameter and accepts `indicator` as well in case a different one is required (the default is 'Life satisfaction')