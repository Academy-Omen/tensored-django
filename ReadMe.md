# Tensored Django

In this project we demonstrated how to use the tensorflow library to create a neural network that can be used to classify 6 different animals.

## Classes

```python
LABELS
Cat 0
Dog 1
Monkey 2
Parrot 3
Elephant 4
Bear 5
```

## Prerequisites

- Knowledge in Python
- Basic understanding of Django and the Web

## Resources

- [TensorFlow CNN Example](https://www.tensorflow.org/tutorials/images/cnn)
- [Academy Omen Django Beginner's Tutorial](https://youtu.be/djNrEft8d_I)

## Tools

- [Python 3](https://www.python.org) : The Python Programming Language
- [Django](https://www.djangoproject.com) : The Web Framework for Python
- [TensorFlow](https://www.tensorflow.org) : The TensorFlow Machine Learning Library used to create the neural network

## Setup Instructions

- Download and Install the latest Python 3 on your computer. [Install Now](https://www.python.org/downloads/)

- Get the starter files [here](hhttps://github.com/Academy-Omen/tensored-django/tree/starter)

```bash
# Download the start files or Clone the repository
git clone https://github.com/Academy-Omen/tensored-django.git
# switch to the starter branch
cd tensored-django
git checkout starter
```

- Create a virtual environment where all packages will be installed.

```bash
# Windows
py -3 -m venv env
# Linux and Mac
python3 -m venv env
```

- Activate the virtual environment.

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```

- Install all the required packages.

```bash
pip install -r requirements.txt
```

## Prepare Dataset

We are building an Image classifier that can predict if the inputed image is a Cat, Dog, Monkey, Parrot, Elephant or Bear. We therefore need images of these animals. The images are going to be used to train our algorithm on how to recognize these animals. This is a supervised machine learning algorithm aka just like a teacher teaching a kid on how to recognize different animals.

We will used the [Download All Images Chrome Extension](https://chrome.google.com/webstore/detail/download-all-images/ifipmflagepipjokmbdecpmjbibjnakm?hl=en) which will help us download images automatically.

## Label Dataset

Just like a teacher will do, we will label each group of images so our kid (aka computer) can verify after performing a prediction.

```python

# temporal storage for labels and images
data=[]
labels=[]

# Cat 0
# Get the animal directory
cats = os.listdir(os.getcwd() + "/CNN/data/cat")
for x in cats:
    """
    Loop through all the images in the directory
    1. Convert to arrays
    2. Resize the images
    3. Add image to dataset
    4. Add the label
    """
    imag=cv2.imread(os.getcwd() + "/CNN/data/cat/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(0)

# load in animals and labels
animals=np.array(data)
labels=np.array(labels)
# save
np.save("animals",animals)
np.save("labels",labels)

```

## Train the Model

We will use [TensorFlow CNN Example](https://www.tensorflow.org/tutorials/images/cnn) to create our own CNN. Feel free to read more and to fine-tune the algorithm. We start by separating the dataset into train_set (90%) and test_set (10%) which are used for training and validation respectively.

```python
# train through 100 times
history = model.fit(x_train, y_train, epochs=100,
                    validation_data=(x_test, y_test))

# perform validation and get accuracy
test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=2)

print(test_acc)

# save the model or brain
model.save("model.h5")
```

## Setup Django App

- Create new django project

```bash
# create new project in the current directory
django-admin startproject core .
# run web app
python manage.py runserver
# visit http://localhost:8000/ on your browser
```

- We will go ahead and update our settings.py file and then create a view that will perform the prediction and pass it to the frontend.

## Let's Connect

- [Twitter](https://twitter.com/itz_omen/)
- [Youtube](https://www.youtube.com/channel/UCknaAfNfqKQDQFnqP2zMA6A)
