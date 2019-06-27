--Read Me--
Step 1: download the project with command 
        git clone https://github.com/dhirajko/wolt-pickUp-time-assignment

step 2: open project and setup the virtual environment and interpreter for the project on your IDE
        ( I am using pycharm.This particular step is for pycharm IDE)

        a. File > setting > click * > add >select New environment > Ok > ok
        b. close the terminal and re opem terminal. (you can see (venv) in the begining of your terminal)

step 3: Install the required package for project with follwing command. 
        pip install -r requirement.txt

        (You can also install manually if some error shown)

step 4: Run the project with command
        python manage.py runserver


Input for project.

    development server :  http://127.0.0.1:8000/

    Method : GET
    Url : http://127.0.0.1:8000/median-calculator?location_id=12&start_time=2019-01-09T11:00:00&end_time=2019-01-09T12:00:00

                    

	query params :
                        location_id : 12
                        start_time :   2019-01-09T11:00:00
                        end_time : 2019-01-09T12:00:00

    

Response : 
        Content-Type  : application/json
        
        {
            "median": 27
        }



PS: Please provide the time in above specific format (iso8601 timestamp) else the response will be invalid.