import numpy as np
import pandas as pd
import xarray as xr
from sklearn.linear_model import LinearRegression


def recompute_time_coords(mc_df):
    x = np.arange(mc_df.shape[0])[:, None]
    y = mc_df['Time'].values
    model = LinearRegression(fit_intercept=False)
    model.fit(x, y)
    time_coord = model.predict(x)
    return time_coord


def get_filename(subject, speed):
    str_speed = str(speed)[0] + str(speed)[-1]
    str_subject = str(subject)
    if subject < 10:
        filename = 'RBDS00' + str_subject + 'runT' + str_speed + 'markers.txt'
    if subject >= 10:
        filename = 'RBDS0' + str_subject + 'runT' + str_speed + 'markers.txt'
    return filename


def make_data_array(subject, speed):
    """
    stores the positions and velocities of each landmark of a
    subject at a fixed speed as a
    """
    filename = get_filename(subject, speed)
    # load dataframe
    df = pd.read_csv('../data/raw_data/' + filename,
                     delimiter='	')
    # change the time coordinate
    df['Time'] = recompute_time_coords(df)
    # set index
    df.set_index('Time', inplace=True)
    # change names
    new_columns = [(x[2:-1], x[0], x[-1]) for x in df.columns]
    df.columns = pd.MultiIndex.from_tuples(new_columns)
    df.columns.names = ['landmark', 'side', 'axis']
    df.index.names = ['time']
    # convert to xarray
    xdf = xr.DataArray(df)
    # unstack multi-index
    xdf = xdf.unstack('dim_1')
    # compute the lift to the tangent bundle
    der = xdf.differentiate('time')
    der = der.assign_coords({'axis': ['TX', 'TY', 'TZ']})
    # combine the two
    txdf = xr.concat([xdf, der], dim='axis')
    # reorder
    txdf = txdf.transpose('time', 'axis', 'landmark', 'side')
    # add meta data
    txdf.attrs['Speed'] = speed
    txdf.attrs['Subject'] = subject
    txdf.attrs['time units'] = 'sec'
    txdf.attrs['distance units'] = 'mm'
    txdf.attrs['velocity/tangle bundle units'] = 'mm/s'
    txdf.attrs['axis'] = 'ground'
    # give the array the obvious name:
    txdf = txdf.rename((subject, speed))
    return txdf
