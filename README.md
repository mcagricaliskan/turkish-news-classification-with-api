Hello Everyone,

This project is created for learning purposes

# Summary and Steps: 

## Scraper.py:
I create a web scraper with Beautifulsoup and requests library 
and try to speed up with multithreading. I saved scraped data to an excel file with using pandas library.
## ProcessingDataset.ipynb:
Firstly i tokenized words with regex tokenizer after that i used cleaning steps;
lowerize words, removing stop words, removing digits, and stemming turkish words.
When data cleaned i create a tf-idf vectorizer using scikit-learn.
With tf-idf vectorizer i fit and transform cleaned dataset.
I saved the result vectors for training and tf-idf vectorizer for api
## Train.ipynb: for training
I load dataset and changed its type to numpy array. For training i split data to test and trains parts. 
I set test ratio as %30 of dataset. I shuffled data in spliting process.
After spliting dataset i create a ANN with Keras and set parameters for training.
I trained dataset and saved model as h5 file, after the training part
a create classification report, recall, preccison
## main.py: for api


Project Steps:
- scraper.py: I create a web scraper for one web site to scrap news
- ProcessingDataset.ipynb: Playing with data and processing it to tf-idf-dataset
- Train.ipynb: Training tf-idf dataset with different libs
- app.py: creating a web app with FastAPI for news classifier
- Dockerfile: Dockerizing web app for deployment

I will share link for trying api
