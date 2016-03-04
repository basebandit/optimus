# Optimus

Optimus is an online movie store,that allows user checkout their favorite as well as latest movies.
The users get to see which movies are popular and also get to rate them as well.

## Features

1. Twitter authentication
2. Admin can add edit and delete movies from the store
3. Anonymous users(visitors) can view the latest movies as well as trending movies via tweeter feeds
   on the side bar.

## Installation

1. Download the zip folder
2. Ensure you have python 2.7.11 or 3.4.2 installed(Most preferably python 2.7.11)
    <p>sudo apt-get install python</p>
3. Install pip 
    <p>python install pip</p>
4. Install virtual env
    <p>pip install virtualenv</p>
5. Go to the app root folder
    <p>cd project-root-folder</p>
6. Create a virtual environment 
    <p>virualenv venv</p>
7. Install the required project requirements from the requirement.txt file
    <p>pip install -r requirements.txt</p>
8. Create the databases
    <p>python manage.py db init</p>
9. Create the database tables
    <p>python manage.py shell</p>
    <p>db.create_all()</p>
    <p>quit()</p>
10. Deploy the app locally
    <p>python manage.py runserver</p>


## Usage

TODO: Write usage instructions

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

TODO: Write credits

## License

This source code is distributed under MIT License.