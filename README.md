Hello Everyone,

I create this project for fun and learning purposes

# Summary and steps: 

- [Scraping News](#scraping-news-scraperpy)
- [Processing News Text and Preparing Dataset](#processing-news-text-and-preparing-dataset-processing-datasetipynb)
- [Training Model and Evaluate Result](#train-model-and-evaluate-result-trainipynb)
- [Creating API for trained model](#creating-api-for-trained-model-mainpy)
- [Dockerizing API for Deployment to My Server (I shared link API link!)](#dockerizing-api-for-deployment-to-my-server-dockerfile)
- [Load Test to API with SOAPUI](#load-test-to-api-with-soapui)
- [Testing Model Myself With News From to Another Website](#testing-model-with-news-from-another-website-including-api-link-which-i-created)

## Scraping News: scraper.py
Scraping news text from one website with their categories. Used requests library for getting websites html content, beautifulsoup for processing html content and getting text data, multi threading for speed up to scraping process. Scraped data saved into excel with using pandas library.
## Processing News Text and Preparing Dataset: Processing-Dataset.ipynb
In this notebook i processed news text for training model and saved processors for creating an api. Firstly i cleaned data, in this step i tokenized data, removed stop words, removed digits, removed words shorter then 2 letters and stemming words. After the cleaning part i create a tf-idf vectorizer and fitted with cleaning data and transformed cleaned data to tf-idf vectors.
## Train Model and Evaluate Result: Train.ipynb
I load tf-idf dataset and changed its type to numpy array. For training i split data to train and test (%30 of dataset) parts also shuffled data in spliting process.
I create a ANN with using Keras and trained network with tf-idf dataset. After training i evaluate model with using classification report and confussion matrix on test set and saved trained model as h5 file for apiç
## Creating API for trained model: main.py
I create an AI class for loading model and vectorizer before the starting api also i create data cleaning, processing, tf-idf vectorizing and predicting functions in class.
After the initializing models code will create an fastapi app and will start service. In every requests endpoints takes news text sending to ai class and returning class and probability of prediciton 
## Dockerizing API for Deployment to My Server: Dockerfile
I dockerized api for deploying to my server. 

For building image i used this command:
```
docker build ./ -t turkish-news-classifier-service
```

For running created image: 
```
docker run -p 10001:10001 turkish-news-classifier-service
```

## Load Test to API with SOAPUI
I tryed 1000 thread same time and with 60 sec duration, service running with 1 worker and handled 1243 requests in 1 min (min/max/avg is millisecond type)
![Load Test](https://github.com/mcagricaliskan/turkish-news-classification/blob/master/README/Screenshot%202022-02-27%20233123.png?raw=true)

## Testing Model With News From Another Website (Including api link which i created):

I visit mynet.com and getting some news text for testing my api.
If you want to test my api you can use postman or similar tool

Api address: 
```
newsnlp.mcagricaliskan.com/turkish-news-classifier/predict
```
Method: Post </br>
Schema: 
```
{
    "NewsText": "string"
}
```

Tests

------
Class: Health - https://www.mynet.com/patlamaya-hazir-bomba-gibi-hissediyorsaniz-bunu-mutlaka-deneyin-ne-dert-kalir-ne-tasa-110106919822 

Request Body
```
{
	"NewsText": "Sık sık stresli hissediyorsanız ve rahatlamak sizin için zorsa rafine şekeri ve kafeini hayatınızdan çıkararak iyi bir uykuya ilk adımı atabilirsiniz. Rafine şeker ve kafein stres seviyenizi olumsuz olarak etkilediği gibi birçok yiyecek de rahatlamanızı sağlayabilir. Bu yiyeceklerin sinir sistemine olan desteği ve strese karşı direnç sunması yedikten hemen sonra bile iyi hissetmenizi sağlıyor. İşte alışveriş listenize eklemeniz gereken 7 süper yiyecek! KEFİR Yoğurt ve süt arasında bir tadı olan fermente kefir hem stresi azaltıyor hem de bağırsak sistemine inanılmaz fayda sağlıyor. Kefiri evinizde kendiniz yapmak isterseniz bitkisel sütleri de kullanabilirsiniz. Bağırsak sistemini sağlıklı tutmanız uzun vadede stresten uzaklaşmanıza yardımcı olacak!"
}
```
Response
```
{
    "Class": "Health",
    "Probability": "1.00"
}
```
------

Class: Automobile - https://www.mynet.com/audi-q2-de-yolun-sonuna-geldi-ceo-markus-duesmann-q2-nin-halefi-olmayacak-110106913210

Request Body
```
{
    "NewsText": "Audi, otomobil modelleri ile piyasada olsa da, zaman zaman diğer pek çok otomobil üreticisi gibi elektriğe dönüş yolunda attığı adımlarla da gündeme geliyor. Audi'nin tek gündemi elektriğe dönüşüm de değil elbet. Şirket, mevcut ürün yelpazesindeki modelleri hakkında da önemli kararlar alıyor ve bu kararlar da konuşuluyor. Otomobil üreticisinin aldığı son karar ise Audi CEO'su Markus Duesmann tarafından açıklanmış durumda. Üstelik bu, sürpriz bir karar olarak değerlendirilebilir gibi görünüyor. AUDI CEO'SU SÜRPRİZ KARARI AÇIKLADI! AUDI A1 VE Q2... Her şey Audi CEO'su Markus Duesmann'ın Alman yayını Handelsblatt'a pazartesi günü yaptığı açıklamaya dayanıyor. Duesmann, açıklamasında Artık A1'i üretmemeye karar verdik ve Q2'nin halefi de olmayacak dedi. Duesmann böylece Audi Q2'nin yeni modelinin gelmeyeceğini doğruladı."
}
```
Response
```
{
    "Class": "Automobile",
    "Probability": "1.00"
}
```
------

Class: Sport - https://www.mynet.com/domenec-torrent-galibiyet-sonrasi-konustu-meyvelerini-topluyoruz-337530-myspor

Request Body
```
{
    "NewsText": "Galatasaray Teknik Direktörü Domenec Torrent, Çaykur Rizespor karşılaşmasının ardından açıklamalarda bulundu. Galibiyetle ilgili konuşan Domenec Torrent Güzel bir maç oldu. Bizim çok fazla fırsatımız vardı. Çok pozisyon yakaladık. Onlar da 2 güzel gol attı. Az pozisyonla golleri çıkardılar. Güzel oynadık. 1 ay boyunca antrenman yaptık. Bu 1 ayda kendimizi geliştirdik. Sezon öncesi gibi hazırlık yaptık. Meyvelerini topluyoruz. Maçın sonucundan memnunum. 2 hafta üst üste 3 puan almak güzel dedi. Kadro seçimi ve oyuncu değişiklikleriyle ilgili de açıklama yapan İspanyol teknik adam Bazen hocaların aldığı kararlar, sahayı doğrudan etkiliyor. Bazen kimin girip çıktığı etkilemiyor, bazen etkiliyor. Ben rotasyon yapıyorum. Rotasyonun pozitif etkileri olduğunu düşünüyorum ifadelerini kullandı."
}
```
Response
```
{
    "Class": "Sport",
    "Probability": "1.00"
}
```