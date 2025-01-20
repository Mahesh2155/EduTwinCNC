# toolpath_utils.py
def scale_toolpath(toolpath, scale_factor):
    """Scale toolpath coordinates."""
    for path in toolpath:
        path['start'] = (path['start'][0] * scale_factor, path['start'][1] * scale_factor)
        path['end'] = (path['end'][0] * scale_factor, path['end'][1] * scale_factor)
    return toolpath

def offset_toolpath(toolpath, offset):
    """Offset toolpath by a given distance."""
    for path in toolpath:
        path['start'] = (path['start'][0] + offset[0], path['start'][1] + offset[1])
        path['end'] = (path['end'][0] + offset[0], path['end'][1] + offset[1])
    return toolpath
