# Hotel Administrator

Welcome to the hotel administrator website! In order to run this program in your local computer you need to download it by either forking the repository or dowloading the .zip file.

Once all the files are in your computer, open a terminal and with the command *cd* move to the directory of the project. To make sure you have all the required packages, please type: *pip install -r requirements.txt*. This will install all the necessary python 3 packages.

Before runing the server and being able to see the website, first you need to migrate the models and dowload the data base.

To migrate the models run the command: *python manage.py migrate*. To populate the models with the data from the website, please run the command: *python manage.py loadfiles*. 

Now you are ready to run the server. Please run the command: *python manage.py runserver*. This will create the server. Now, open a web browser and go to the following url: *http://localhost:8000/*. Here you can see the built webside. You can choose a city from the drop-down menu. Once selected click *Select* and it will take you to the next url where it will show you all the hotels in that city. If you want to search for another city, click the button *Back* which will take you to the inital screen. There you can make another selection.

## Additional features

If you want to create an administator of the website, run the command: *python manage.py superuser*. You will need to provide a username, email and password for this. After you provide these details, you can go to the following url: *http://localhost:8000/admin/*. Here you will have access to the data base where you can add/delete/edit anything yo want.
