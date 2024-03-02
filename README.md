# MSPL H.W. Week05-Object Detection

## Introduction

This is a **car counter** side project.

We use YOLO algorithm (yolov8) to detect the moving car and count their amount.

So we input the video `car.mp4` and output the result `Results/output.mp4`.

## Implementation

### Tool
| Tool           | Version       |
| -------------  | ------------- |
| IDE            | VScode        |
| Python         | 3.10.5        |

### Libraries version
| Library's name | Version       |
| -------------- | ------------- |
| ultralytics    | 8.1.19        |
| torch          | 2.2.1         |
| numpy          | 1.23.0        |
| opencv-python  | 4.5.4.60      |
| filterpy       | 1.4.5         |
| scikit-image   | 0.19.3        |
| lap            | 0.4.0         |
| cvzone         | 1.6.1         |

You can use the command to check the version of libraries：

```bash
pip show <module>
```

if you didn't install the library, then it will show a warning message `Package(s) not found` to you.

install python libraries:

```bash
pip install <module>
```

if you want to install the indicated version, then you can use:

```bash
pip install <module> == <version>
```

To make sure IDE can run the code, you can execute the `test.py` first:

```bash
python test.py
```

### Step：
* Preparation
    1.1 Ensure the Libraries and IDE can be worked.
    1.2. Make sure that data can be used in your code
    1.3. Use the yolo model to detect the object (car / truck / motorbike ... etc.), and display bounding boxes.
    1.4. Setting class names and confidence value

* Detecting & Counting (core)
    2.1 Decide detected region
    2.2 Build the **mask** (mask.jpg) to focus only on the region we detected to get the better results
    2.3 Bit-and operation with the original image (the output records in `Results/bitand_reuslt.mp4`)
    2.4 Create the tracker to trace object's moving trajectory (sort.py) and assign the id number for each car (we need to know where the cars go in next frame, and make sure every frame the same car keeps the same id number)
    2.5 Create the certain region (line) and use it as the counter when objects (car) go through (a center point touchs the line)
    2.6 Build a counting list as a counter and ensure counter will not count repetitively
    2.7 Finally output the length of counting list

* Beautify
    3.1 Add a graphic (graphics.png)
    3.2 Set a coordinate to put the graphics on the screen
    3.3 Check a counting number is correct or not
    3.4 Output a resulta as video (`Results/output.mp4`)

## References
- [Youtube](https://www.youtube.com/watch?v=WgPbbWmnXJ8)
- [YOLOv8](https://github.com/ultralytics/ultralytics)

Author: Jing Lu (D.S.)                                  
Date: 2024.03.