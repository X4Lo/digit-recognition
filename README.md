# Digit Recognition Project
This project utilizes TensorFlow and Tkinter to create a simple digit recognition application. The model is trained on the [MNIST](https://www.tensorflow.org/datasets/catalog/mnist) dataset for recognizing handwritten digits.

## Getting Started
### Prerequisites
Make sure you have the following packages installed:

- [TensorFlow](https://pypi.org/project/tensorflow/)
- [NumPy](https://pypi.org/project/numpy/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [OpenCV (cv2)](https://pypi.org/project/opencv-python/)
- [Pillow (PIL)](https://pypi.org/project/pillow/)

You can install the required packages using the following commands:
```bash
pip install tensorflow numpy opencv-python Pillow
```

### Project Structure
- **model.py**: Contains the code for training the digit recognition model using TensorFlow.
- **main.py**: Implements a Tkinter-based GUI for drawing digits and predicting their values using the trained model.

## Running the Application
1. Clone the repository:
```bash
git clone https://github.com/X4Lo/digit-recognition.git cd digit-recognition
```

2. Run the main application:
```bash
python main.py
```
## Usage
1. Draw a digit on the canvas.
2. Click the "Save" button to save the drawing.
3. Click the "Predict" button to use the trained model to predict the digit.
4. Use the "Clear Image" button to reset the canvas.

## Model Training
The digit recognition model is trained on the MNIST dataset. The training script (`model.py`) loads the dataset, normalizes the data, and creates a simple neural network using TensorFlow.

To train the model, run:
```bash
python model.py
```

The trained model will be saved as `mnist_model.model`.

Feel free to explore and enhance the project as needed and happy coding!

---
**[X4Lo](https://github.com/X4Lo)**