Wearever 
by Aneek Barua, Timothy Corcoran, and Srikar Indrakanti

Wearever is an app that utilizes real-time weather data, alongside previously collected data on an individual basis to predict what the optimal attire for your next day is! By utilizing an SGDCLassifier per attribute of an outfit (Top, Bottom, Footwear), there are three individually trained classifiers that take in the same data, the dummy data which is made for new users, alongside any data from that user themselves.

Our SGDCLassifier is linked to an SQLite database with Django to create a seamless user experience, utilzing user data efficiently and in a meaningful way. By dynamically adding to the database as the user uses the app, we hope to achieve seamless adjustments not only towards the current season, but the clothing style of our users.

Requirements: 
Python 3.9.2
python packages pyowm, scikit-learn, django
VS Code

How to Run:

1. Setup a virtual environment with django using this tutorial: https://code.visualstudio.com/docs/python/tutorial-django
2. Install required python packages mentioned above.
3. Relocate to the .\Wearever\wearever directory.
4. In the terminal use "python manage.py runserver".
5. In browser, go to localhost:8000.
6. You are now at the home page. Click "Login" to sign up using a Google account. Since we can only use basic Google AllAuth capabilities, you will have to use your Stony Brook emails: niranjan@cs.stonybrook.edu, tianyi.zhao@stonybrook.edu, tao.sun.1@stonybrook.edu (emails have to be given prior clearance to properly login).
7. Once signed in, you will have a default model that recommends clothing based on heat index and wind chill. As you continue to use the app over time and provide feedback on the clothing recommendations, the model will personalize to your preferences and provide accurate recommendations for the clothing you will be comfortable wearing on any given day. You can provide feedback in the lower left-hand side of the application, where you can modify the recommendation made to you the previous time you used the application. This information will be relayed to the database and adjust future recommendations accordingly.


