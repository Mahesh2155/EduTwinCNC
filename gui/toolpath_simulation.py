from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class ToolpathSimulation(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Add a button to select a file
        self.select_file_button = QPushButton("Select File for 2D/3D View", self)
        self.select_file_button.setIcon(QIcon('assets/icons/simulate_icon.png'))
        self.select_file_button.setIconSize(Qt.QSize(24, 24))
        self.select_file_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.select_file_button)

        # Label to show the selected file name
        self.file_label = QLabel("No file selected", self)
        self.layout.addWidget(self.file_label)

    def select_file(self):
        # Open a file dialog to select a G-code or STL file
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "G-Code Files (*.gcode);;STL Files (*.stl)")
        if file_path:
            self.file_label.setText(f"Selected: {file_path}")
            self.display_file(file_path)

    def display_file(self, file_path):
        # Check file type and display the 2D or 3D visualization
        if file_path.endswith(".gcode"):
            self.display_toolpath(file_path)
        elif file_path.endswith(".stl"):
            self.display_3d_model(file_path)
        else:
            self.file_label.setText("Unsupported file type")

    def display_toolpath(self, file_path):
        """Parse the G-code file and display toolpath in 2D or 3D."""
        x_coords = []
        y_coords = []
        z_coords = []

        # Parse the G-code file
        with open(file_path, "r") as file:
            for line in file:
                if line.startswith("G") and ("X" in line or "Y" in line or "Z" in line):
                    try:
                        # Extract X, Y, Z coordinates if they exist in the line
                        x = float(line.split("X")[1].split()[0]) if "X" in line else None
                        y = float(line.split("Y")[1].split()[0]) if "Y" in line else None
                        z = float(line.split("Z")[1].split()[0]) if "Z" in line else None

                        if x is not None:
                            x_coords.append(x)
                        if y is not None:
                            y_coords.append(y)
                        if z is not None:
                            z_coords.append(z)
                    except Exception as e:
                        print(f"Error parsing line: {line}, {e}")

        # Check if Z-axis data is present for 3D visualization
        if z_coords:
            self.display_3d_toolpath(x_coords, y_coords, z_coords)
        else:
            self.display_2d_toolpath(x_coords, y_coords)

    def display_2d_toolpath(self, x_coords, y_coords):
        """Display a 2D toolpath."""
        plt.figure()
        plt.plot(x_coords, y_coords, label="2D Toolpath")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("2D Toolpath")
        plt.legend()
        plt.grid()
        plt.show()

    def display_3d_toolpath(self, x_coords, y_coords, z_coords):
        """Display a 3D toolpath."""
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the toolpath in 3D
        ax.plot(x_coords, y_coords, z_coords, label="3D Toolpath")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Z-axis")
        ax.set_title("3D Toolpath")
        ax.legend()
        plt.show()

    def display_3d_model(self, file_path):
        """Display a 3D model from an STL file."""
        try:
            from stl import mesh
            import numpy as np

            # Load the STL file
            stl_mesh = mesh.Mesh.from_file(file_path)

            # Extract the vectors (triangles) from the mesh
            x = stl_mesh.vectors[:, :, 0].flatten()  # X-coordinates
            y = stl_mesh.vectors[:, :, 1].flatten()  # Y-coordinates
            z = stl_mesh.vectors[:, :, 2].flatten()  # Z-coordinates

            # Create a 3D plot
            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")

            # Plot the surface of the STL using trisurf
            ax.plot_trisurf(x, y, z, triangles=np.arange(len(x)).reshape(-1, 3), cmap='viridis', edgecolor='none')

            # Auto scale to the mesh size
            ax.set_xlabel("X-axis")
            ax.set_ylabel("Y-axis")
            ax.set_zlabel("Z-axis")
            ax.set_title("3D Model Visualization")
            plt.show()

        except ImportError:
            self.file_label.setText("Error: Install numpy-stl and matplotlib for STL visualization")
        except Exception as e:
            self.file_label.setText(f"Error visualizing STL file: {e}")

