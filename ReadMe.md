# Tensored Django

In this project I demonstrated how to use the tensorflow library to create a neural network that can be used to classify 6 different categories of animals.

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

## Setup Instructions

- Download and Install the latest Python 3 on your computer. [Install Now](https://www.python.org/downloads/)
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

- Start the server.

```bash
<!-- run django app -->
python manage.py runserver
<!-- visit http://localhost:8000/ on your browser -->
```

## Resources

- [TensorFlow CNN Example](https://www.tensorflow.org/tutorials/images/cnn)
