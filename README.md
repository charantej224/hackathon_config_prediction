# hackathon_config_prediction

## Running Server :

Step 1:   
  clone the workspace using commands git clone https://github.com/charantej224/hackathon_config_prediction.git  
  
Step 2:  
  Install required dependencies well before starting of the server dependencies are  
  * numpy
  * flask
  * flask_cors
  
Step 3:
  Run the file "rest_endpoints.py" which should kick start the server. End points mentioned below are ready for consumption.
  Sample End Points:  
  * http://localhost:5000/config-prediction/api/v1.0/service/all-data?start_time=9/9/19 18:57&end_time=11/4/19 21:59  
  * http://localhost:5000/config-prediction/api/v1.0/service/config-data?start_time=9/9/19 18:57&end_time=11/4/19 21:59  
  * http://localhost:5000/config-prediction/api/v1.0/service/reliability-data?start_time=9/9/19 18:57&end_time=11/4/19 21:59  
  * http://localhost:5000/config-prediction/api/v1.0/service/efficiency?start_time=9/9/19 18:57&end_time=11/4/19 21:59  
  * http://localhost:5000/config-prediction/api/v1.0/service/retention?start_time=9/9/19 18:57&end_time=11/4/19 21:59  
