Hello Everyone,

This project is created for learning purposes

# Summary and steps: 

## scraper.py:
I create a web scraper with Beautifulsoup and requests library 
and try to speed up with multithreading. I saved scraped data to an excel file with using pandas library.
## Processing-Dataset.ipynb:
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
i evaluate model on test set using functions like classification report, recall, preccison
## main.py: for api
I create a api end using FastAPI.
I create a AI class. In AI class i intialize models and data create functions about cleaning incoming text data,
tf-idf vectorizing on cleaned data, making predictions on vectorized data.
I initialize AI class and connected it with endpoit for getting news text data from api and returning news class
## Dockerfile
I dockerized API for deploying to my server.

For building with docker:
```
docker build ./ -t turkish-news-classifier-service
```

For running docker build 
```
docker run -p 10001:10001 turkish-news-classifier-service
```
## test_model.py: I copied news from various websites and test model by myself
making progress

## load_test.py: I 

I tryed 1000 thread same time and with 60 sec duration, service running with 1 worker and handled 1243 requests in 1 min
![Load Test](https://github.com/mcagricaliskan/turkish-news-classification/blob/master/README/Screenshot%202022-02-27%20233123.png?raw=true)