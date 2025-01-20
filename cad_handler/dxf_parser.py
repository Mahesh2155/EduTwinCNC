# dxf_parser.py
import ezdxf

def parse_dxf(file_path):
    doc = ezdxf.readfile(file_path)
    model_space = doc.modelspace()
    
    # Extracting line entities for toolpath generation
    lines = []
    for line in model_space.query('LINE'):
        lines.append({
            'start': (line.dxf.start.x, line.dxf.start.y),
            'end': (line.dxf.end.x, line.dxf.end.y)
        })
    return lines
