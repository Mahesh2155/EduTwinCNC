from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QTabWidget, QPushButton, QLabel, QComboBox,
    QLineEdit, QGridLayout, QMessageBox, QFileDialog, QStatusBar
)
from PyQt5.QtCore import Qt, QSize
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QBrush
from mpl_toolkits.mplot3d import Axes3D
from stl import mesh  # Import STL library for 3D visualization


# ToolpathSimulation Widget
class ToolpathSimulation(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Add a button to select a file
        self.select_file_button = QPushButton("Select File for 2D/3D View", self)
        self.select_file_button.setIcon(QIcon('assets/icons/simulate_icon.png'))
        self.select_file_button.setIconSize(QSize(24, 24))
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
            self.display_2d_toolpath(file_path)
        elif file_path.endswith(".stl"):
            self.display_3d_model(file_path)
        else:
            self.file_label.setText("Unsupported file type")

    def display_2d_toolpath(self, file_path):
        # Parse the G-code file and extract 2D toolpath data
        x_coords = []
        y_coords = []
        with open(file_path, "r") as file:
            for line in file:
                if line.startswith("G") and "X" in line and "Y" in line:
                    try:
                        x = float(line.split("X")[1].split()[0])
                        y = float(line.split("Y")[1].split()[0])
                        x_coords.append(x)
                        y_coords.append(y)
                    except Exception as e:
                        print(f"Error parsing line: {line}, {e}")
        
        # Plot the 2D toolpath
        plt.figure()
        plt.plot(x_coords, y_coords, label="Toolpath")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("2D Toolpath")
        plt.legend()
        plt.grid()
        plt.show()

    def display_3d_model(self, file_path):
        # Import and use a library like numpy-stl or trimesh to render STL files
        try:
            stl_mesh = mesh.Mesh.from_file(file_path)

            # Create a 3D plot
            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")

            # Add the mesh to the plot
            ax.add_collection3d(plt.PolyCollection(stl_mesh.vectors))

            # Auto scale to the mesh size
            scale = stl_mesh.points.flatten()
            ax.auto_scale_xyz(scale, scale, scale)

            plt.title("3D Model")
            plt.show()
        except ImportError:
            self.file_label.setText("Error: Install numpy-stl for STL visualization")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CNC Milling CAM Software")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet(self.get_main_style())

        self.initUI()

    def initUI(self):
        # Main layout with tabs
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(self.get_tab_style())
        self.setCentralWidget(self.tabs)

        # Add tabs to the UI
        self.tabs.addTab(self.create_main_tab(), "Main Controls")
        self.tabs.addTab(self.create_position_tab(), "Position")
        self.tabs.addTab(self.create_jog_home_tab(), "Jog/Home")
        self.tabs.addTab(self.create_auto_mdi_tab(), "Auto/MDI")
        self.tabs.addTab(self.create_feed_spindle_tab(), "Feed & Spindle")
        self.tabs.addTab(self.create_visualization_tab(), "2D/3D Visualization")

        # Status Bar
        self.statusBar = QStatusBar()
        self.statusBar.setStyleSheet("background-color: #222; color: #fff; font-size: 12px;")
        self.setStatusBar(self.statusBar)

    def create_main_tab(self):
        # Main Controls Tab
        main_tab = QWidget()
        layout = QVBoxLayout()

        # Grid layout for Main Controls
        grid_layout = QGridLayout()
         # Toolpath Simulation Widget (File Selection and Visualization)
        self.toolpath_sim = ToolpathSimulation(self)
        layout.addWidget(self.toolpath_sim)

        # Load CAD File Button
        load_button = QPushButton('Load CAD File', self)
        load_button.clicked.connect(self.load_file)
        grid_layout.addWidget(load_button, 0, 0)

        # Toolpath Simulation Button
        simulate_button = QPushButton('Simulate Toolpath', self)
        simulate_button.clicked.connect(self.simulate_toolpath)
        grid_layout.addWidget(simulate_button, 1, 0)

        # G-code Generation Button
        gcode_button = QPushButton('Generate G-code', self)
        gcode_button.clicked.connect(self.generate_gcode)
        grid_layout.addWidget(gcode_button, 2, 0)

        # CNC Machine Control Button
        cnc_control_button = QPushButton('CNC Machine Control', self)
        cnc_control_button.clicked.connect(self.cnc_control)
        grid_layout.addWidget(cnc_control_button, 3, 0)

        layout.addLayout(grid_layout)
        cnc_control_button = QPushButton("Start CNC Operation")
        cnc_control_button.clicked.connect(self.start_cnc_operation)
        layout.addWidget(cnc_control_button)
        

        main_tab.setLayout(layout)
        return main_tab

    def create_position_tab(self):
        # Position Tab
        position_tab = QWidget()
        layout = QGridLayout()

        layout.addWidget(QLabel("X-Axis:"), 0, 0)
        self.x_position = QLabel("0.000")
        layout.addWidget(self.x_position, 0, 1)

        layout.addWidget(QLabel("Y-Axis:"), 1, 0)
        self.y_position = QLabel("0.000")
        layout.addWidget(self.y_position, 1, 1)

        layout.addWidget(QLabel("Z-Axis:"), 2, 0)
        self.z_position = QLabel("0.000")
        layout.addWidget(self.z_position, 2, 1)

        position_tab.setLayout(layout)
        return position_tab

    def create_jog_home_tab(self):
        # Jog/Home Tab
        jog_tab = QWidget()
        layout = QVBoxLayout()

        jog_button = QPushButton("Jog")
        jog_button.clicked.connect(self.jog_machine)
        layout.addWidget(jog_button)

        home_button = QPushButton("Home Machine")
        home_button.clicked.connect(self.home_machine)
        layout.addWidget(home_button)

        jog_tab.setLayout(layout)
        return jog_tab

    def create_auto_mdi_tab(self):
        # Auto/MDI Tab
        auto_tab = QWidget()
        layout = QVBoxLayout()

        auto_button = QPushButton("Run Auto Mode")
        auto_button.clicked.connect(self.run_auto_mode)
        layout.addWidget(auto_button)

        self.mdi_input = QLineEdit()
        self.mdi_input.setPlaceholderText("Enter G-code command")
        layout.addWidget(self.mdi_input)

        mdi_button = QPushButton("Run MDI Command")
        mdi_button.clicked.connect(self.run_mdi_command)
        layout.addWidget(mdi_button)

        auto_tab.setLayout(layout)
        return auto_tab

    def create_feed_spindle_tab(self):
        # Feed & Spindle Tab
        feed_tab = QWidget()
        layout = QGridLayout()

        layout.addWidget(QLabel("Feed Rate:"), 0, 0)
        self.feed_input = QLineEdit()
        self.feed_input.setPlaceholderText("Enter feed rate (mm/min)")
        layout.addWidget(self.feed_input, 0, 1)

        layout.addWidget(QLabel("Spindle Speed:"), 1, 0)
        self.spindle_input = QLineEdit()
        self.spindle_input.setPlaceholderText("Enter spindle speed (RPM)")
        layout.addWidget(self.spindle_input, 1, 1)

        update_button = QPushButton("Update")
        update_button.clicked.connect(self.update_feed_spindle)
        layout.addWidget(update_button, 2, 0, 1, 2)

        feed_tab.setLayout(layout)
        return feed_tab

    def create_visualization_tab(self):
        # Visualization Tab
        vis_tab = QWidget()
        layout = QVBoxLayout()

        # 2D Visualization Canvas
        self.figure_2d = plt.figure()
        self.canvas_2d = FigureCanvas(self.figure_2d)
        layout.addWidget(self.canvas_2d)

        # 3D Visualization Canvas
        self.figure_3d = plt.figure()
        self.canvas_3d = FigureCanvas(self.figure_3d)
        layout.addWidget(self.canvas_3d)

        # Buttons to toggle visualization modes
        visualize_2d_button = QPushButton("Visualize 2D Toolpath")
        visualize_2d_button.clicked.connect(self.visualize_2d)
        layout.addWidget(visualize_2d_button)

        visualize_3d_button = QPushButton("Visualize 3D Toolpath")
        visualize_3d_button.clicked.connect(self.visualize_3d)
        layout.addWidget(visualize_3d_button)

        vis_tab.setLayout(layout)
        return vis_tab
    
    # Style Helpers
    def get_main_style(self):
        return """
        QMainWindow {
            background-color: #f0f0f0;
        }
        QPushButton {
            background-color: #4CAF50;
            color: white;
            font-size: 14px;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #4CAF50;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QLabel {
            font-size: 14px;
            color: #333;
        }
        QLineEdit {
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 8px;
        }
        QTabWidget::pane {
            border: 1px solid #ccc;
            background-color: #eaeaea;
        }
        """

    def get_tab_style(self):
        return """
        QTabBar::tab {
            background: #ccc;
            border: 1px solid #aaa;
            padding: 10px;
            min-width: 120px;
            font-size: 14px;
        }
        QTabBar::tab:selected {
            background: #4CAF50;
            color: white;
        }
        QTabBar::tab:hover {
            background: #45a049;
            color: white;
        }
        """

    # Main Tab Functions
    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CAD File", "", "CAD Files (*.dxf *.step)")
        if file_path:
            self.statusBar.showMessage(f"Loaded CAD File: {file_path}")

    def simulate_toolpath(self):
        QMessageBox.information(self, "Simulation", "Simulating toolpath...")

    def generate_gcode(self):
        QMessageBox.information(self, "G-code Generation", "G-code generated successfully!")

    def start_cnc_operation(self):
        QMessageBox.information(self, "CNC Operation", "CNC operation started!")

    def cnc_control(self):
        QMessageBox.information(self, "CNC Control", "CNC machine control activated!")

    def jog_machine(self):
        """Simulate jog functionality for CNC."""
        self.statusBar.showMessage("Jogging the machine...")
        QMessageBox.information(self, "Jog Machine", "Jogging functionality executed! (Simulated)")

    def home_machine(self):
        """Simulate homing functionality for CNC."""
        self.statusBar.showMessage("Homing the machine...")
        QMessageBox.information(self, "Home Machine", "Machine returned to home position! (Simulated)")

    def run_auto_mode(self):
        QMessageBox.information(self, "Auto Mode", "Running Auto Mode...")

    def run_mdi_command(self):
        command = self.mdi_input.text()
        QMessageBox.information(self, "MDI Command", f"Executing MDI Command: {command}")

    def update_feed_spindle(self):
        feed = self.feed_input.text()
        spindle = self.spindle_input.text()
        QMessageBox.information(self, "Update Feed/Spindle", f"Feed Rate: {feed} mm/min\nSpindle Speed: {spindle} RPM")

    def visualize_2d(self):
        """Visualize 2D Toolpath."""
        self.figure_2d.clear()
        ax = self.figure_2d.add_subplot(111)
        ax.set_title("2D Toolpath")
        ax.set_xlabel("X (mm)")
        ax.set_ylabel("Y (mm)")

        # Example toolpath points
        x = [0, 10, 20, 30, 40]
        y = [0, 5, 10, 5, 0]

        ax.plot(x, y, marker="o", label="Toolpath")
        ax.grid(True)
        ax.legend()
        self.canvas_2d.draw()

    def visualize_3d(self):
        """Visualize 3D Toolpath."""
        self.figure_3d.clear()
        ax = self.figure_3d.add_subplot(111, projection="3d")
        ax.set_title("3D Toolpath")
        ax.set_xlabel("X (mm)")
        ax.set_ylabel("Y (mm)")
        ax.set_zlabel("Z (mm)")

        # Example toolpath points
        x = [0, 10, 20, 30, 40]
        y = [0, 5, 10, 5, 0]
        z = [0, 2, 4, 6, 8]

        ax.plot(x, y, z, marker="o", label="Toolpath")
        ax.legend()
        self.canvas_3d.draw()

    def update_position(self):
        """Simulate real-time position updates."""
        # Increment position for demonstration purposes
        self.current_position["X"] += 5.0
        self.current_position["Y"] += 2.5
        self.current_position["Z"] += 1.0

        # Update position labels
        self.x_position.setText(f"{self.current_position['X']:.3f}")
        self.y_position.setText(f"{self.current_position['Y']:.3f}")
        self.z_position.setText(f"{self.current_position['Z']:.3f}")

        # Stop the simulation after a certain limit
        if self.current_position["X"] > 50.0:
            self.timer.stop()
            QMessageBox.information(self, "Simulation Complete", "Toolpath simulation complete!")


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
