# laplacian-foveation

## Installation

laplace-foveation requires a Python distribution (with NumPy and pybind11 packages installed), OpenCV 4, a C++ compiler and CMake.

### Windows
These steps assume the Anaconda Python Distribution is used, OpenCV is downloaded and extracted, and Visual Studio is installed.

- On Windows 11, you might need to install the [Media Feature Pack](https://support.microsoft.com/en-us/topic/media-feature-pack-list-for-windows-n-editions-c1c6fffa-d052-8338-7a79-a4bb980a700a)
- Open an Anaconda Prompt and [install pybind11](https://anaconda.org/conda-forge/pybind11) and *opencv* packages:
    ```sh
    conda install -c conda-forge pybind11
	pip install opencv-python
    ```
- Clone this repository and create a **build** directory in the root directory (*laplacian-foveation/build*)
- Open CMake and specify the cloned repository directory as *source* and the created build subdirectory to *build* the binaries
- The first time you hit *Configure* some errors will likely be thrown, here are fixes/what you might need to define manually:
    | Name | Value |
    | ------ | ------ |
    | OpenCV_DIR | **%path_to_extracted_opencv_folder%/build** |
    | pybind11_DIR | **%path_to_anaconda%/anaconda3/Lib/site-packages/pybind11/share/cmake/pybind11** |
    | PYTHON_EXECUTABLE | **%path_to_anaconda%/anaconda3/python.exe** |
- When *Configure* is successful, hit *Generate* and then *Open Project* to open Visual Studio on the generated files
- In Visual Studio, change **Debug/x64** to **Release/x64** in the upper bar near the menu and, on the right side, right-click *laplacian-foveation* and select **Build(/Rebuild)**
- If the build process succeeded, go to *laplacian_foveation/build/Release/* and copy the file *pysmooth_foveation.**PYD*** to *%path_to_anaconda%/anaconda3/Lib/site-packages/*
- Add OpenCV *bin* directory to PATH (*%path_to_extracted_opencv_folder%/build/x64/vc15/bin*)
-- if you have any Anaconda terminal window open, you need to close and reopen it so it is aware of the change to PATH
- Test the build and installation of *laplacian_foveation* by running (Python):
    ```sh
    import laplacian_foveation as fv
    ```
- The *test.py* script provides a demo on foveating an image from the COCO dataset:
    ```sh
	conda install -c anaconda scikit-image
    python test.py
    ```