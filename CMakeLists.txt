cmake_minimum_required(VERSION 2.8.12)
project(laplacian_foveation)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_LIST_DIR}/cmake/Modules/")

SET(CMAKE_CXX_FLAGS_RELEASE "-Wall -O3 -std=c++11")
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS_RELEASE}")
SET(CMAKE_CONFIGURATION_TYPES "Release")

find_package(OpenCV)
find_package(pybind11)

option(-std "std" c++11)

include_directories(
	include
	${PYTHON_INCLUDE_DIR}
	${PYTHON_NUMPY_INCLUDE_DIR}
)

set(GLOG_LIB glog)

include_directories(${CMAKE_CURRENT_SOURCE_DIR})

set(PYTHON_FILES smooth_foveation.cpp)

pybind11_add_module(laplacian_foveation src/laplacian_foveation.cpp src/python_bindings/smooth_foveation.cpp src/python_bindings/conversions.cpp)
target_link_libraries(laplacian_foveation PRIVATE pybind11::module ${OpenCV_LIBS})
set_target_properties(laplacian_foveation PROPERTIES PREFIX "${PYTHON_MODULE_PREFIX}" SUFFIX "${PYTHON_MODULE_EXTENSION}") 
configure_file(src/python_bindings/__init__.py src/python_bindings/__init__.py)






