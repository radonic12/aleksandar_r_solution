# Gotta Process Them All

## Setup
1. Install requirements.txt
2. Run spool_data.py - It will harvest the pokemon data 
3. Run dashboard.py - It will display the harvested data in a dashboard

## Answer to questions
**Main requirements, Question 6 - "Prepare the data in an appropriate data format. Consider if it should be multiple or a single file."**

The data task seems highly structured and very specific as to what datapoints are of interest and the data size is small therefor I have decided to go with a single file. If the task had been more unstructured and explorative in its nature (this could be the case if the data should be used for initial quantitative analysis and the importance of certain datapoints were based on best guesses or assumptions that hadn't been tested yet) storing each api response in a seperate json file could be better. By storing in seperate json files new API calls would not need to be made if new datapoints from response needs to be extracted. Had the volume of the dataset been larger hadoop/spark could have been applied where seperate notes can process the files in parallel.

**Bonus requirements, Question 1 - "Imagine the Pokémon are subject to the GDPR. How would you pseudonymize the data to no longer make it re-identifiable?"**

With my setup the name needs to be replaced when stored in database. An easy fix would be to name the first pokemon "Pokemon1" and increment upwards but this would corelate with the pokemons id. One could argue that the pokemons id is also sensitive, since it can be used to look up the pokemon in the API. So encrypting the name and id would be my recommendation and as I understand the GDPR rules the encryption should be non reversible.  

**Bonus requirements, Question 2 - "Imagine you had to build a system in the cloud that would continiously deliver updates to the investor with updates about Pokémon. Draw an architecture for exposing new changes to the existing Pokémon to the investor."**

I would have to add updated_at and created_at columns to my database table. The created_at is set when an Pokemon is added for the first time to my database and the updated_at is set the last time a parameter was updated on the given row. The created_at and updated_at column would be used to know when I have last harvested the API. I would then ask the API developer to enable me to add a query parameter where I can insert a date and only get Pokemons that have been created or updated on or after that date. That way I avoid looping through all pokemons everytime I have need to check for changes. Then I would run a scripts that get the maximum updated_at/created_at from my database, call the API to get pokemons that have been created before or after that date, and insert or update them in database. 
Another solution would be to setup an event queue and have the API developer sent events to my queue when pokemons are added or updated and then these events can be spooled into my database. Event queue is also more scalable if the data size increases since with a FIFO queue multiple instances can read of the queue at the same time and process messages in parallel.

**Bonus requirements, Question 3 - "Make a interactable dashboard using the data where users can get a detailed page about the Pokémon, including showing the image from the url of the sprite."**

By running dashboard.py you can see a small dashboard example. I wasn't able to inject an image tag so only the url is present. I have kept the dashboard at a bare minimum. More filter options could have been added, as well could a chart placing pokemons in an obese, normal or underweight category based on their BMI.

**Bonus requirements, Question 4 - "If a spark compatible framework was not already chosen for the primary requirements, consider how the code would change to be executed on a spark engine."**
Partly answered in my answer to main requirements, question 6. The way I have seen the architecture drawn up in AWS i storing files to be processed in S3 and then deploying a Hadoop instance that auto scales with nodes if it needs more processing power.