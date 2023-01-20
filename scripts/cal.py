# Description: Create a calendar heatmap for a given year
# adapted from SO_tourist's answer here:
# https://stackoverflow.com/questions/32485907/matplotlib-and-numpy-create-a-calendar-heatmap

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle

from holidays import is_holiday, get_holiday

# Settings
weeks = [1, 2, 3, 4, 5, 6]
days = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
month_names = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]


def generate_data():
    idx = pd.date_range('2018-01-01', periods=365, freq='D')
    return pd.Series(range(len(idx)), index=idx)


def split_months(df, year):
    """
    Take a df, slice by year, and produce a list of months,
    where each month is a 2D array in the shape of the calendar
    :param df: dataframe or series
    :return: matrix for daily values and numerals
    """
    df = df[df.index.year == year]

    # Empty matrices
    a = np.empty((6, 7))
    a[:] = np.nan

    day_nums = {m: np.copy(a) for m in range(1, 13)}  # matrix for day numbers
    day_vals = {m: np.copy(a) for m in range(1, 13)}  # matrix for day values

    # create new series with all days of the year as timestamps
    full_df = pd.Series(0, pd.date_range(f'{year}-01-01',
                                         periods=365,
                                         freq='D'))

    # fill in the values from the original series
    full_df.update(df)

    # get max value for heatmap
    max_val = full_df.max()

    # Logic to shape datetimes to matrices in calendar layout
    row = 0
    for d in full_df.items():
        day = d[0].day
        month = d[0].month
        col = d[0].dayofweek

        if d[0].is_month_start:
            row = 0

        if row < 6:
            day_nums[month][row, col] = day  # day number (0-31)
            day_vals[month][row, col] = d[1]  # day value (the heatmap data)

        if col == 6:
            row += 1

    return day_nums, day_vals, max_val


def create_year_calendar(day_nums,
                         day_vals,
                         maxval,
                         year,
                         title,
                         cmap,
                         save,
                         show_days=False):
    # fig, ax = plt.subplots(3, 4, figsize=(14.85, 10.5))
    # smaller
    fig, ax = plt.subplots(3, 4)

    for i, axs in enumerate(ax.flat):

        axs.imshow(day_vals[i + 1], cmap=cmap, vmin=1, vmax=365)  # heatmap
        axs.set_title(month_names[i], fontsize=10)

        # Labels
        axs.set_xticks(np.arange(len(days)))
        axs.set_xticklabels(days,
                            fontsize=8,
                            fontweight='bold',
                            color='#555555')
        axs.set_yticklabels([])

        # Tick marks
        axs.tick_params(axis=u'both', which=u'both',
                        length=0)  # remove tick marks
        axs.xaxis.tick_top()

        # Modify tick locations for proper grid placement
        axs.set_xticks(np.arange(-.5, 6, 1), minor=True)
        axs.set_yticks(np.arange(-.5, 5, 1), minor=True)
        axs.grid(which='minor', color='w', linestyle='-', linewidth=2.1)

        # Despine
        for edge in ['left', 'right', 'bottom', 'top']:
            axs.spines[edge].set_color('#FFFFFF')

        # Annotate
        for w in range(len(weeks)):
            for d in range(len(days)):
                day_val = day_vals[i + 1][w, d]
                day_num = day_nums[i + 1][w, d]

                if show_days:
                    # choose text color based on background color ensuring contrast
                    if day_val < maxval / 3:
                        color = 'k'
                    else:
                        color = 'w'

                    # Value label
                    axs.text(d,
                             w + 0.3,
                             f"{day_val:0.0f}",
                             ha="center",
                             va="center",
                             fontsize=6,
                             color=color,
                             alpha=0.8)

                # If value is 0, draw a grey patch
                if day_val == 0:
                    patch_coords = ((d - 0.5, w - 0.5), (d - 0.5, w + 0.5),
                                    (d + 0.5, w + 0.5), (d + 0.5, w - 0.5))

                    mark = Polygon(patch_coords, fc='#DDDDDD')
                    axs.add_artist(mark)

                if show_days:
                    # If day number is a valid calendar day, add an annotation
                    if not np.isnan(day_num):
                        axs.text(d + 0.45,
                                 w - 0.31,
                                 f"{day_num:0.0f}",
                                 ha="right",
                                 va="center",
                                 fontsize=6,
                                 color="#003333",
                                 alpha=0.8)  # day

                # Aesthetic background for calendar day number
                patch_coords = ((d - 0.1, w - 0.5), (d + 0.5, w - 0.5),
                                (d + 0.5, w + 0.1))

                triangle = Polygon(patch_coords, fc='w', alpha=0.7)
                axs.add_artist(triangle)

                # if holiday, draw a circle
                if not np.isnan(day_num):
                    if is_holiday(day_num, i + 1, year):
                        mark = Circle((d, w), 0.3, fc='none', ec='r')
                        axs.add_artist(mark)

    if title == "":
        title = str(year)

    # Final adjustments
    fig.suptitle(title, fontsize=12)
    plt.subplots_adjust(left=0.04, right=0.96, top=0.88, bottom=0.04)

    if save:
        # Save to file
        plt.savefig(save)
    else:
        plt.show()


def plot(df, year, title="", cmap="Greens", save=""):
    day_nums, day_vals, maxval = split_months(df, year)
    create_year_calendar(day_nums, day_vals, maxval, year, title, cmap, save)
