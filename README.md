# RoboCup-FaceReg
Facial recognition system for Robocup 2022 Competition
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

