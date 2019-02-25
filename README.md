####RestFul API####

=>Assumption
  *Project will be running on Windows platform
  *python PATH is added on environmental variables
  *Terminal is opened in project directory

=>Pre-requisites
  *Python3.6.8 should be installed
  *pip install -r Requirements.txt
  *MySQL is installed on system / SQLALCHEMY_DATABASE_URI should be changed from RestAPI.py according to the platform
  *student_database is present on MySQL
  
=>Following commands are used for migrating models to database
  *python migration.py db init
  *python migration.py db migrate
  *python migration.py db upgrade
  
=> Runserver :: python apis.py

=>This API has following end points for User (Student)
	*create (http://localhost:5000/api)           => method = 'POST'
	*get    (http://localhost:5000/api/roll_no)   => method = 'GET'
	*update (http://localhost:5000/api/roll_no)   => method = 'PUT'
	*delete (http://localhost:5000/api/roll_no)   => method = 'DELETE'
	
=>Authentication is required if user wants to update data or retrieve data
  *He/She should provide correct password along with username for retrieving data 
  *He/She should provide correct password along with username for updating data
  *He/She should provide correct password along with username for deleting data
  *In case of wrong password data is not accessed and unauthorized access message is sent as request response

  
=>A sample test file (test_restapi.py) is present in the project folder and can be run using following command
	*python -m pytest
