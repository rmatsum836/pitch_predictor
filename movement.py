import numpy as np

def _calc_v_start(v, a, t_start, coord):
    """
    calculate velocities at start
    """
    if coord == 'x':
        i = 0
    elif coord == 'y':
        i = 1
    else:
        i = 2

    return v[i] + (a[i]*t_start)

def _calc_vbar(v_io, a_i, time):
    """
    calculate v_bar
    """
    v_i = (2*v_io+a_i*time) / 2

    return v_i

def _calc_magnus(a_i, adrag, v_i, v_bar):
    """
    calculate magnus force components
    """
    a_mag = a_i + adrag * v_i / v_bar

    return a_mag

def _calc_move(amag_i, time):
    """
    calculate movement for component i
    """
    d_i = 0.5 * amag_i * time**2 * 12

    return d_i


def calc_movement(p_o, v_o, a):
    """
    Function that computes the movement of a given pitch that is corrected for drag

    Taken from: http://baseball.physics.illinois.edu/Movement.pdf

    Parameters
    ----------
    p_o: list
        Initial x,y, and z positions of pitch
    v_o: list
        Initial x, y, and z components of velocity
    a: list
        x, y, and z components of acceleration

    Returns
    -------
    movement: list
        dx, dz, and dzg movement components

    """
    # Compute velocities at start
    vxo = v_o[0]
    vyo = v_o[1]
    vzo = v_o[2]
    ax = a[0]
    ay = a[1]
    az = a[2]
    pxo = p_o[0]
    pyo = p_o[1]
    pzo = p_o[2]
    
    if isinstance(vxo,int) or isinstance(vxo,float):
        pass
    else:
        length_list = len(list(vxo))
    #y_start = [40] * length_list
    y_start = 40 # Need to figure out why this is
    t_start = (-vyo - np.sqrt(vyo**2-2*ay*(pyo-y_start))) / ay
    v_xstart = _calc_v_start(v_o, a, t_start, 'x')
    v_ystart = _calc_v_start(v_o, a, t_start, 'y')
    v_zstart = _calc_v_start(v_o, a, t_start, 'z')
    time = (-v_ystart - np.sqrt(v_ystart**2-2*ay*(y_start-(17/12)))) / ay

    # Calculate the mean velocity components
    v_x = _calc_vbar(v_xstart, ax, time)
    v_y = _calc_vbar(v_ystart, ay, time)
    v_z = _calc_vbar(v_zstart, az, time)

    v_bar = np.sqrt(v_x**2+v_y**2+v_z**2)

    # Calculate drag acceleration
    adrag = np.abs(ax*v_x+ay*v_y+(az+32.179)*v_z) / v_bar

    # Compute magnus force components
    amag_x = _calc_magnus(a[0], adrag, v_x, v_bar)
    amag_y = _calc_magnus(a[1], adrag, v_y, v_bar)
    #amag_z = _calc_magnus(a[2], adrag, v_z, v_bar)
    amag_z = az + adrag * v_z / v_bar + 32.179

    mov_x = _calc_move(amag_x, time)
    mov_z = _calc_move(amag_z, time)

    dzg = mov_z - 12 * 0.5 * 32.179 * time**2

    return [mov_x, mov_z, dzg]
