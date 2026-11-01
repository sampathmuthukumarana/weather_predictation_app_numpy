import logging
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def to_numpy(data: dict):
    daily = data["daily"]

    dates = np.array(daily["time"], dtype='datetime64[D]')

    values = np.column_stack([
    np.array(daily["temperature_2m_max"], dtype='float'),
    np.array(daily["temperature_2m_min"], dtype='float'),
    np.array(daily["precipitation_sum"],  dtype='float'),
    np.array(daily["wind_speed_10m_max"], dtype='float')
    ])

    # logging.info(daily)
    logger.info("Daily data: %s", values)

    return dates[:-1], values[:-1]