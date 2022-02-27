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

## I make load test to api with using soapui 
I tryed 1000 thread same time and with 60 sec duration, service running with 1 worker and handled 1243 requests in 1 min (min/max/avg is millisecond type)
![Load Test](https://github.com/mcagricaliskan/turkish-news-classification/blob/master/README/Screenshot%202022-02-27%20233123.png?raw=true)

## I copied news from another website and test model by myself

I will take some parts of news not full text

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