# NLP

## Two types of ML techniques :
	> *Supervised ML
		- Classification
		- Regression
	> Unsupervised ML (do not require any pre-labelled training data samples)

We have a collection of data points (text or numeric)
We extract features from data points using a process known

trying to group together similar data points using techniques like    clustering or summarizing documents based on topic models

There are two main processes in the supervised text classification:
	> Training
	> Prediction

Labelled training data is necessary for supervised text classification

we split the training dataset itself into training and validation sets by random sampling

## Text classification blueprint
	1. Prepare train and test datasets	
	2. Text normalization
		• Expanding contractions
		• Text standardization through lemmatization
		• Removing special characters and symbols
		• Removing stopwords
	3. Feature extraction (nltk, gensim, and scikit-learn lib)
		• Bag of Words model
		• TF-IDF model
		• Advanced word vectorization models
	4. Model training
		• Multinomial Naïve Bayes
		• Support vector machines
	5. Model prediction and evaluation
		• Accuracy
		• Precision
		• Recall
		• F1 score
	6. Model deployment

