nothing to see here

curl -u 'sutt' https://api.github.com/user/repos -d '{"name":"wnba"}'

Data subdir is kept empty, to avoid large file transfer...
  ...scripts can be run locally to build the contents:
  
  1. Download train and test, unzip to /data/orig/
  
  2. Run scripts/split_train.py
      this will split train.csv into /data/main/train_10/...
		training_1.csv, training_2.csv .. training_10.csv
       
	    (takes > 10 mins)
	
  3. Run scripts/split_again.py...
        ...this will split training_1 again into 10 parts
		

