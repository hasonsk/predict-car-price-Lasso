# 🚗 Predict Car Price with LassoCV
This project focuses on predicting car prices using two machine learning models: Lasso Regression and Decision Tree Regression. The goal of this project is sử dụng mô hình hồi quy Lasso với Cross Validation để dự đoán giá của xe đã được xử dụng.

## Dataset
You can download this dataset in [**kaggle**](https://www.kaggle.com/datasets/avikasliwal/used-cars-price-prediction).

The dataset used for this project contains information about different cars, including variables such as `Name`, `Location`, `Year`, `Fuel_Type`,	`Engine`, `Seats` and other relevant features. It also includes the corresponding price of each car. This dataset is used for training and evaluating machine learning models.

## Installation and Setup
Clone the repository: 
```git
git clone https://github.com/hasonsk/predict-car-price-Lasso.git
```


Move to the project directory: ```cd predict-car-price-Lasso```

Install the required libraries: ```pip install -r requirements.txt```

Run the Jupyter Notebook: ```jupyter notebook model.ipynb```

## Usage
1. Load the dataset using ```pd.read_csv()``` function.
2. Clean the data and handle missing values.
3. Split the dataset into training and testing sets using ```train_test_split()``` function.
4. Create an instance of the Lasso Regression model: ```Lasso(alpha=1.0)``` and find the optimal alpha coefficient that minimizes the MAE (Mean Absolute Error).




## Model
### Lasso Regression Model
Lasso Regression is a linear regression model that performs both feature selection and regularization. It helps in reducing the complexity of the model by shrinking the coefficient estimates towards zero. The Lasso Regression model is utilized for predicting car prices based on the dataset.

## Deployment
To deploy the application, run the following command:
```bash
python3 app.py
```

Here is a sample image demonstrating the usage of the API. Feel free to try it out and explore, you might find it excited! 
![Alt text](app_web.png)
![Alt text](image-result.png)


😄 I am very grateful for receiving your feedback and contributions!!!