# Prodigy_Infotech_submissions

This GitHub Repository contains all the projects that are completed under the Prodigy Infotech Machine Learning Internship
# Classifications of images of Dogs and Cats
1. Different models used in the code:

   a. MobileNet V2: This is used as a feature extractor, pre-trained on ImageNet.
   b. Custom Sequential Model: A simple model built on the MobileNet feature extractor.
   c. TFLite Model: A converted version of the trained mobile/edge deployment model.

2. Step-by-step processing:

   a. Data Preparation:
   - Load the Cats vs Dogs dataset using TensorFlow Datasets.
   - Split the data into train, validation, and test sets.
   - Preprocess images (resize to 224x224 and normalize).
   - Create batched datasets for training, validation, and testing.

 b. Model Architecture:
   - Load a pre-trained MobileNet V2 model as a feature extractor.
   - Create a Sequential model with the feature extractor and a Dense output layer.

   c. Model Compilation:
   - Compile the model with Adam optimizer and sparse categorical cross-entropy loss.

   d. Training:
   - Train the model for 5 epochs using the prepared training and validation batches.

   e. Model Saving:
   - Save the trained model in SavedModel format.
  f. TFLite Conversion:
   - Convert the SavedModel to TFLite format for mobile/edge deployment.

   g. Inference with the TFLite model:
   - Load the TFLite model.
   - Perform inference on 100 test images.
   - Calculate and report the accuracy of the TFLite model.

   h. Analyzing and Visualizing the data 


# House Price Prediction (Linear Regression)
Technical Description:
This project implements a machine learning model using linear regression to predict house prices. Key components include:

Data preprocessing: Handling missing values, feature scaling, and encoding categorical variables
Feature selection: Identifying the most relevant features affecting house prices
Model implementation: Using scikit-learn's LinearRegression class
Model evaluation: Employing metrics such as Mean Squared Error (MSE), R-squared, and Mean Absolute Error (MAE)
Cross-validation: Ensuring model robustness and generalizability
Visualization: Plotting residuals and feature importance for model interpretation

# Customer Segmentation (K-means Clustering)
Technical Description:
This project uses K-means clustering to segment customers based on retail sales data. Key aspects include:
Data cleaning and preparation: Handling outliers and normalizing features
Feature engineering: Creating relevant metrics like Recency, Frequency, and Monetary (RFM) values
Determining optimal cluster number: Using the elbow method and silhouette score
Implementing K-means: Utilizing scikit-learn's KMeans class
Cluster analysis: Characterizing each segment based on centroid values
Visualization: Creating scatter plots and radar charts to represent customer segments
Actionable insights: Providing business recommendations based on segment characteristics

# Virtual Mouse with Hand Gesture Recognition
Technical Description:
This project creates a virtual mouse using computer vision and hand gesture recognition. Key technologies and components include:

OpenCV: For image capture and processing from the webcam feed
MediaPipe: Employing the Hands module for accurate hand landmark detection
Gesture recognition: Implementing custom logic to interpret hand poses and movements
Mouse control: Using PyAutoGUI to translate gestures into mouse actions (movement, clicks, scrolling)
Real-time processing: Optimizing the pipeline for low-latency response
User interface: Developing a simple GUI to display the webcam feed and system status
Gesture customization: Allowing users to define and save custom gestures for different actions

The project integrates these technologies to create a seamless, hands-free computer interaction experience, demonstrating practical applications of computer vision and machine learning in human-computer interaction.
