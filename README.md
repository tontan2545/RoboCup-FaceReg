# RoboCup-FaceReg
Facial recognition system for Robocup 2022 Competition
## Installation

### Requirements

  * Python 3.3+ or Python 2.7
  * macOS or Linux (Windows not officially supported, but might work)

### Installation Options:

#### Installing on Mac or Linux

First, make sure you have dlib already installed with Python bindings:

  * [How to install dlib from source on macOS or Ubuntu](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)
  
Then, make sure you have cmake installed:  
 
```brew install cmake```

Finally, install this module from pypi using `pip3` (or `pip2` for Python 2):

```bash
pip3 install face_recognition
```

Alternatively, you can try this library with [Docker](https://www.docker.com/), see [this section](#deployment).

If you are having trouble with installation, you can also try out a
[pre-configured VM](https://medium.com/@ageitgey/try-deep-learning-in-python-now-with-a-fully-pre-configured-vm-1d97d4c3e9b).

#### Installing on an Nvidia Jetson Nano board

 * [Jetson Nano installation instructions](https://medium.com/@ageitgey/build-a-hardware-based-face-recognition-system-for-150-with-the-nvidia-jetson-nano-and-python-a25cb8c891fd)
   * Please follow the instructions in the article carefully. There is current a bug in the CUDA libraries on the Jetson Nano that will cause this library to fail silently if you don't follow the instructions in the article to comment out a line in dlib and recompile it.

#### Installing on Raspberry Pi 2+

  * [Raspberry Pi 2+ installation instructions](https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65)

#### Installing on FreeBSD

```bash
pkg install graphics/py-face_recognition
```

#### Installing on Windows

While Windows isn't officially supported, helpful users have posted instructions on how to install this library:

  * [@masoudr's Windows 10 installation guide (dlib + face_recognition)](https://github.com/ageitgey/face_recognition/issues/175#issue-257710508)

#### Installing a pre-configured Virtual Machine image

  * [Download the pre-configured VM image](https://medium.com/@ageitgey/try-deep-learning-in-python-now-with-a-fully-pre-configured-vm-1d97d4c3e9b) (for VMware Player or VirtualBox).

## API Reference
Documentation of utility functions in `RAFaceRecognition` class

### Object instantiation
Initialize RAFaceRecognition class

#### Function

```bash
  raFaceRecognition = RAFaceRecognition(db_path)
```
#### Parameters
| Name | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `db_path` | `string` | **Required**. path to database for storing face encodings |


### Register Image
Registers the most significant face in the img as encodings to the db_path folder

#### Function

```bash
  raFaceRecognition.register(name, img)
```
#### Parameters
| Name | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**. Register name |
| `img` | `string` | **Required**. 2D Array of Image |

#### Return
| Type     | Description                |
| :-------- | :------- |
| `dictionary` | `{message: string, isOk: boolean}` |

### Detect Face
Detect a face/ faces in the image

#### Function

```bash
  raFaceRecognition.detectFace(img)
```
#### Parameters
| Name | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `img` | `string` | **Required**. 2D Array of Image |

#### Return
| Type     | Description                |
| :-------- | :------- |
| `dictionary` | `Return known faces in the image and it's coordinates in the form of { name: (top, right, bottom, left) }` |

