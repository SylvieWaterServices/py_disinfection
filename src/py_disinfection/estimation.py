# Conservative Estimate
import math
from py_disinfection.tables import (
    giardia_3log_ct_values_free_chlorine,
    virus_4log_ct_values_free_chlorine,
    maxC,
    maxpH,
    maxFreeChlorine,
    max_virus_C,
    max_virus_pH,
)


# Conservative Method
def conservative_giardia_ct(temp, ph, chlorine_conc):
    rounded_temp = max(
        t for t in maxC if t <= temp
    )  # Round down temperature - take the highest value of the values less than or equal to the temperature
    rounded_ph = min(
        p for p in maxpH if p >= ph
    )  # Round up pH - take the lowest value of the values greater than or equal to the pH
    rounded_chlorine = min(
        c for c in maxFreeChlorine if c >= chlorine_conc
    )  # Round up chlorine - take the lowest value of the values more than or equal to the chlorine concentration
    # This is counter-intuitive but results in a conservative estimate

    temp_idx = maxC.index(rounded_temp)
    chlorine_idx = maxFreeChlorine.index(rounded_chlorine)
    ph_idx = maxpH.index(rounded_ph)

    return giardia_3log_ct_values_free_chlorine[temp_idx][chlorine_idx][ph_idx]


# Interpolation Method
def interpolate_giardia_ct(temp, ph, chlorine_conc):

    def linear_interpolate(x1, x2, y1, y2, x):
        return y1 + (y2 - y1) * ((x - x1) / (x2 - x1)) if x2 != x1 else y1

    def find_next_lowest_and_highest(values, target):
        lower = max([v for v in values if v <= target], default=values[0])
        upper = min([v for v in values if v >= target], default=values[-1])
        return lower, upper

    temp_low, temp_high = find_next_lowest_and_highest(maxC, temp)
    chlorine_low, chlorine_high = find_next_lowest_and_highest(
        maxFreeChlorine, chlorine_conc
    )
    ph_low, ph_high = find_next_lowest_and_highest(maxpH, ph)

    temp_low_idx, temp_high_idx = maxC.index(temp_low), maxC.index(temp_high)
    chlorine_low_idx, chlorine_high_idx = maxFreeChlorine.index(
        chlorine_low
    ), maxFreeChlorine.index(chlorine_high)
    ph_low_idx, ph_high_idx = maxpH.index(ph_low), maxpH.index(ph_high)

    # Step 1: Interpolate CT between pH values at the next lowest temp & next lowest chlorine residual
    ct1_low_cl = linear_interpolate(
        ph_low,
        ph_high,
        giardia_3log_ct_values_free_chlorine[temp_low_idx][chlorine_low_idx][
            ph_low_idx
        ],
        giardia_3log_ct_values_free_chlorine[temp_low_idx][chlorine_low_idx][
            ph_high_idx
        ],
        ph,
    )

    # Step 2: Interpolate CT between pH values at the next highest temp & next lowest chlorine residual
    ct2_low_cl = linear_interpolate(
        ph_low,
        ph_high,
        giardia_3log_ct_values_free_chlorine[temp_high_idx][chlorine_low_idx][
            ph_low_idx
        ],
        giardia_3log_ct_values_free_chlorine[temp_high_idx][chlorine_low_idx][
            ph_high_idx
        ],
        ph,
    )

    # Step 3: Interpolate CT between temp values from Steps 1 & 2
    ct_low_cl = linear_interpolate(temp_low, temp_high, ct1_low_cl, ct2_low_cl, temp)

    # Step 4: Interpolate CT between pH values at the next lowest temp & next highest chlorine residual
    ct1_high_cl = linear_interpolate(
        ph_low,
        ph_high,
        giardia_3log_ct_values_free_chlorine[temp_low_idx][chlorine_high_idx][
            ph_low_idx
        ],
        giardia_3log_ct_values_free_chlorine[temp_low_idx][chlorine_high_idx][
            ph_high_idx
        ],
        ph,
    )

    # Step 5: Interpolate CT between pH values at the next highest temp & next highest chlorine residual
    ct2_high_cl = linear_interpolate(
        ph_low,
        ph_high,
        giardia_3log_ct_values_free_chlorine[temp_high_idx][chlorine_high_idx][
            ph_low_idx
        ],
        giardia_3log_ct_values_free_chlorine[temp_high_idx][chlorine_high_idx][
            ph_high_idx
        ],
        ph,
    )

    # Step 6: Interpolate CT between temp values from Steps 4 & 5
    ct_high_cl = linear_interpolate(temp_low, temp_high, ct1_high_cl, ct2_high_cl, temp)

    # Step 7: Final interpolation between chlorine residual values
    return linear_interpolate(
        chlorine_low, chlorine_high, ct_low_cl, ct_high_cl, chlorine_conc
    )


# Regression Method
def regression_giardia_ct(temp, ph, chlorine_conc, log_inactivation=3):
    if temp < 12.5:
        return (0.353 * log_inactivation) * (
            12.006 + math.exp(2.46 - 0.073 * temp + 0.125 * chlorine_conc + 0.389 * ph)
        )
    else:
        return (0.361 * log_inactivation) * (
            -2.261 + math.exp(2.69 - 0.065 * temp + 0.111 * chlorine_conc + 0.361 * ph)
        )


def conservative_viruses_ct(temp, ph):
    rounded_temp = max(
        t for t in max_virus_C if t <= temp
    )  # Round down temperature - take the highest value of the values less than or equal to the temperature
    rounded_ph = min(
        p for p in max_virus_pH if p >= ph
    )  # Round up pH - take the lowest value of the values greater than or equal to the pH
    # This is counter-intuitive but results in a conservative estimate

    temp_idx = max_virus_C.index(rounded_temp)
    ph_idx = max_virus_pH.index(rounded_ph)

    return virus_4log_ct_values_free_chlorine[temp_idx][ph_idx]
