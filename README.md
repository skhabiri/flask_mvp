# flask_mvp
This is a single module flask app as a proof of concept. It uses an API in http://api.open-notify.org, which returns a jason data containing some information about the people currently in the international space station. There are a root and refresh route. The root roiute read the data from a sqlite database and render selected information as html. The refresh route creates the schema, pulls data from the api and store it in the database. 
