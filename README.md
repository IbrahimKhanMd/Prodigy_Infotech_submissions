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
