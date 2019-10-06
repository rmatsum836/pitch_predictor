import numpy as np

def _calc_v_start(v, a, t_start, coord):
    """
    calculate velocities at start
    """
    if coord = 'x':
        i = 0
    elif coord = 'y':
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


def calc_movement(p_o, v_o, a)::
    """
    Function that computes the movement of a given pitch

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
    y_start = 40 # Need to figure out why this is
    t_start = (-v_o[1] - np.sqrt(v_o**2-2*a[1]*(p_o[1]-y_start))) / a[1]
    v_xstart = _calc_v_start(v_o, a_0, t_start, 'x')
    v_ystart = _calc_v_start(v_o, a_0, t_start, 'y')
    v_zstart = _calc_v_start(v_o, a_0, t_start, 'z')
    time = (-v_ystart - np.sqrt(v_y_start**2-2*a[1]*(y_start-(17/12)))) / a[1]

    # Calculate the mean velocity components
    v_x = _calc_vbar(v_xstart, a[0], time)
    v_y = _calc_vbar(v_ystart, a[1], time)
    v_z = _calc_vbar(v_zstart, a[2], time)

    v_bar = np.sqrt(v_x**2+v_y**2+v_z**2)

    # Calculate drag acceleration
    adrag = np.abs(a[0]*v_x+a[1]*v_y+(a[2]+32.179)*v_z) / v_bar

    # Compute magnus force components
    amag_x = _calc_magnus(a[0], adrag, v_x, v_bar)
    amag_y = _calc_magnus(a[1], adrag, v_y, v_bar)
    amag_z = _calc_magnus(a[2], adrag, v_z, v_bar)

    mov_x = _calc_move(amag_x, time)
    mov_y = _calc_move(amag_y, time)
    mov_z = calc_move(amag_z, time)

    return [mov_x, mov_y, mov_z]
