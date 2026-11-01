import logging
from tabnanny import NannyNag

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

def summarize(dates, values):
    logger.info("Daily data: %s", dates)
    logger.info("Daily data: %s", values)
    max_temp = values[:, 0]
    rain = values[:, 2]
    logger.info("max temp: %s", max_temp)
    avg_max_temp = np.nanmean(max_temp)
    total_rain = float(np.nansum(rain))
    trend = max_temp[-1]-max_temp[0]

    lines =[]
    for related_date,row in zip(dates, values):
        logger.info("related date: %s", related_date)
        logger.info("row: %s", row)
        lines.append(
            f"{related_date}: max {row[0]:.1f}°C, "
            f"min {row[1]:.1f}°C, "
            f"rain {row[2]:.1f} mm, "
            f"wind {row[3]:.1f} km/h"
        )
    logger.info(lines)
    text = "\n".join(lines)
    return (
        f"{text}\n\n"
        f"Summary: average max temperature {avg_max_temp: .1f}°C, "
        f"total rain {total_rain:.1f}mm, "
        f"temperature trend {trend:.1f}°C, "
    )