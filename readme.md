## Model Server
To load model and use it from API call

 ## Set up the Project
 
 1. Install Python 3.10
 
 2. Create a virtualenv and activate it
 
    ```
    $ pip install virtualenv
    $ virtualenv venv
    $ venv\Scripts\activate        # For Windows
    $ source venv/bin/activate     # For Linux
    ```
 
 3. Goto project directory and install dependencies
    ```
    cd jwt-flask
    pip install -r requirements.txt
    ```
 
 <br/>
 
 ## Run the Project
    
 * Open terminal and go to project directory in terminal and run the command
    
    ```
    cd jwt-flask
    flask db_create
    python main.py
    ```
  
    - load the postman collection file in postman desktop app
    - see the json body, modify it as your requirements and test it
    - for more help execute, flask --help in terminal