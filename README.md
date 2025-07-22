📘 Public Transport Ridership Forecasting Using Machine Learning: A Case Study of Rapid Bus KL in Malaysia

This project analyzes how weather, holidays, and festivals affect bus ridership in Kuala Lumpur using machine learning. Data from Rapid Bus KL (2022–2024) is used to train four models: Linear Regression, ARIMA, Random Forest, and XGBoost. Among them, Random Forest achieved the best performance with R² = 0.9656 and MAPE = 3.4%.

🔍 Key Highlights

📍 Location: Kuala Lumpur, Malaysia

🚌 Transit System: Rapid KL

📅 Data Range: Jan 2022 – Aug 2024

🧠 Models Used: Linear Regression, ARIMA, Random Forest, XGBoost

✅ Best Model: Random Forest

📈 Top Predictors: Weekday/Weekend, Temperature, Festivals

📁 Repo Includes

Preprocessed datasets

Jupyter notebooks for training and visualization

Trained model files

Figures: prediction plots, boxplots, trendline

Source scripts

📊 Main Results

Model	MAE	RMSE	MAPE
Linear Regression	11715.35	14291.59	6.3%
ARIMA	31489.32	38435.29	16.1%
XGBoost	9928.72	12838.57	4.9%
Random Forest	5139.06	7642.27	3.4%

📚 Data Sources

Malaysia Open Data: data.gov.my

Weather: Visual Crossing

🧭 Future Work

Hourly-level forecasts

Integration with metro and rideshare data

Real-time prediction with traffic sensors

Deep learning (LSTM, GRU)
