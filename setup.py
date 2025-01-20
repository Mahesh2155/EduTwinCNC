# setup.py
from setuptools import setup

setup(
    name="CNC_Milling_CAM_Software",
    version="0.1",
    packages=["gui", "cad_handler", "toolpath_generation", "gcode_generation", "cnc_communication", "simulation", "utils"],
    install_requires=[
        "pyqt5",
        "numpy",
        "ezdxf",
        "pytest",
    ],
)
