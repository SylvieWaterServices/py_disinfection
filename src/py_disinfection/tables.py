# Source: https://www.epa.gov/system/files/documents/2022-02/disprof_bench_3rules_final_508.pdf
# EPA Guidance Manual
# Disinfection Profiling and Benchmarking
# Office of Water (4606M)
# EPA 815-R-20-003
# June 2020


# EPA Guidance Manual B-2
# Disinfection Profiling and Benchmarking
# Page B-2
# Table B-1. CT Values* for 3-Log Inactivation of Giardia Cysts by Free Chlorine

# x is max degrees C
# y is max free chlorine concentrations
# z is max pHs
# units are min-mg/L.

maxC = [0.5, 5, 10, 15, 20, 25]
maxFreeChlorine = [0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3]
maxpH = [6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9]


giardia_3log_ct_values_free_chlorine = [
    [  # max of 0.5 degrees C
        [137, 163, 195, 237, 277, 329, 390],  # Chlorine 0.4
        [141, 168, 200, 239, 286, 342, 407],  # 0.6
        [145, 172, 205, 246, 295, 354, 422],  # 0.8
        [148, 176, 210, 253, 304, 365, 437],  # 1
        [152, 180, 215, 259, 313, 376, 451],  # 1.2
        [155, 184, 221, 266, 321, 387, 464],  # 1.4
        [157, 189, 226, 273, 329, 397, 477],  # 1.6
        [162, 193, 231, 279, 338, 407, 489],  # 1.8
        [165, 197, 236, 286, 346, 417, 500],  # 2.0
        [169, 201, 242, 297, 353, 426, 511],  # 2.2
        [172, 205, 247, 298, 361, 435, 522],  # 2.4
        [175, 209, 252, 304, 368, 444, 533],  # 2.6
        [178, 213, 257, 310, 375, 452, 543],  # 2.8
        [181, 217, 261, 316, 382, 460, 552],  # 3
    ],
    [  # max of 5 degrees C
        [97, 117, 139, 166, 198, 236, 279],  # 0.4
        [100, 120, 143, 171, 204, 244, 291],  # 0.6
        [103, 122, 146, 175, 210, 252, 301],  # 0.8
        [105, 125, 149, 179, 216, 260, 312],  # 1
        [107, 127, 152, 183, 221, 267, 320],  # 1.2
        [109, 130, 155, 187, 227, 274, 329],  # 1.4
        [111, 132, 158, 192, 232, 281, 337],  # 1.6
        [114, 135, 162, 196, 238, 287, 345],  # 1.8
        [116, 138, 165, 200, 243, 294, 353],  # 2
        [118, 140, 169, 204, 248, 300, 361],  # 2.2
        [120, 143, 172, 209, 253, 306, 368],  # 2.4
        [122, 146, 175, 213, 258, 312, 375],  # 2.6
        [124, 148, 178, 217, 263, 318, 382],  # 2.8
        [126, 151, 182, 221, 268, 324, 389],  # 3
    ],
    [  # max of 10 degrees C
        [73, 88, 104, 125, 149, 177, 209],  # 0.4
        [75, 90, 107, 128, 153, 183, 218],  # 0.6
        [78, 92, 110, 131, 158, 189, 226],  # 0.8
        [79, 94, 112, 134, 162, 195, 234],  # 1
        [80, 95, 114, 137, 166, 200, 240],  # 1.2
        [82, 98, 116, 140, 170, 206, 247],  # 1.4
        [83, 99, 119, 144, 174, 211, 253],  # 1.6
        [86, 101, 122, 147, 179, 215, 259],  # 1.8
        [87, 104, 124, 150, 182, 221, 265],  # 2
        [89, 105, 127, 153, 186, 225, 271],  # 2.2
        [90, 107, 129, 157, 190, 230, 276],  # 2.4
        [92, 110, 131, 160, 194, 234, 281],  # 2.6
        [93, 111, 134, 163, 197, 239, 287],  # 2.8
        [95, 113, 137, 166, 201, 243, 292],  # 3
    ],
    [  # max of 15 degrees C
        [49, 59, 70, 83, 99, 118, 140],  # 0.4
        [50, 60, 72, 86, 102, 122, 146],  # 0.6
        [52, 61, 73, 88, 105, 126, 151],  # 0.8
        [53, 63, 75, 90, 108, 130, 156],  # 1.0
        [54, 64, 76, 92, 111, 134, 160],  # 1.2
        [55, 65, 78, 94, 114, 137, 165],  # 1.4
        [56, 66, 79, 96, 116, 141, 169],  # 1.6
        [57, 68, 81, 98, 119, 144, 173],  # 1.8
        [58, 69, 83, 100, 122, 147, 177],  # 2.0
        [59, 70, 85, 102, 124, 150, 181],  # 2.2
        [60, 72, 86, 105, 127, 153, 184],  # 2.4
        [61, 73, 88, 107, 129, 156, 188],  # 2.6
        [62, 74, 89, 109, 132, 159, 191],  # 2.8
        [63, 76, 91, 111, 134, 162, 195],  # 3
    ],
    [  # max of 20 degrees C
        [36, 44, 52, 62, 74, 89, 105],  # 0.4
        [38, 45, 54, 64, 77, 92, 109],  # 0.6
        [39, 46, 55, 66, 79, 95, 113],  # 0.8
        [39, 47, 56, 67, 81, 98, 117],  # 1.0
        [40, 48, 57, 69, 83, 100, 120],  # 1.2
        [41, 49, 58, 70, 85, 103, 123],  # 1.4
        [42, 50, 59, 72, 87, 105, 126],  # 1.6
        [43, 51, 61, 74, 89, 108, 129],  # 1.8
        [44, 52, 62, 75, 91, 110, 132],  # 2.0
        [44, 53, 63, 77, 93, 113, 135],  # 2.2
        [45, 54, 65, 78, 95, 115, 138],  # 2.4
        [46, 55, 66, 80, 97, 117, 141],  # 2.6
        [47, 56, 67, 81, 99, 119, 143],  # 2.8
        [47, 57, 68, 83, 101, 122, 146],  # 3.0
    ],
    [  # max of 25 degrees C
        [24, 29, 35, 42, 50, 59, 70],  # 0.4
        [25, 30, 36, 43, 51, 61, 73],  # 0.6
        [26, 31, 37, 44, 53, 63, 75],  # 0.8
        [26, 31, 37, 45, 54, 65, 78],  # 1.0
        [27, 32, 38, 46, 55, 67, 80],  # 1.2
        [27, 33, 39, 47, 57, 69, 82],  # 1.4
        [28, 33, 40, 48, 58, 70, 84],  # 1.6
        [29, 34, 41, 49, 60, 72, 86],  # 1.8
        [29, 35, 41, 50, 61, 74, 88],  # 2.0
        [30, 35, 42, 51, 62, 75, 90],  # 2.2
        [30, 36, 43, 52, 63, 77, 92],  # 2.4
        [31, 37, 44, 53, 65, 78, 94],  # 2.6
        [31, 37, 45, 54, 66, 80, 96],  # 2.8
        [32, 38, 46, 55, 67, 81, 97],  # 3.0
    ],
]

# EPA Guidance Manual B-3
# Disinfection Profiling and Benchmarking
# Table B-2. CT Values* for 4-Log Inactivation of Viruses by Free Chlorine
# units are min-mg/L.

# x is max degrees C
# y is max pH
max_virus_C = [0.5, 5, 10, 15, 20, 25]
max_virus_pH = [6, 9, 10]

virus_4log_ct_values_free_chlorine = [
    [0, 12, 90],  # max of 0.5 degrees C
    [0, 8, 60],  # max of 5 degrees C
    [0, 6, 45],  # max of 10 degrees C
    [0, 4, 30],  # max of 15 degrees C
    [0, 3, 22],  # max of 20 degrees C
    [0, 2, 15],  # max of 25 degrees C
]

# EPA Guidance Manual B-3
# Disinfection Profiling and Benchmarking
# Table B-3. CT Values* for 3-Log Inactivation of Giardia Cysts by Chlorine Dioxide
# units are min-mg/L.

# x is max degrees C: [1, 5, 10, 15, 20, 25]
max_chlorine_dioxide_C = [1, 5, 10, 15, 20, 25]
giardia_3log_ct_values_chlorine_dioxide = [63, 26, 23, 19, 15, 11]

# EPA Guidance Manual B-3
# Disinfection Profiling and Benchmarking
# Table B-4. CT Values* for 4-Log Inactivation of Viruses by Chlorine Dioxide ph 6-9
# units are min-mg/L.
#
# x is max degrees C: [1, 5, 10, 15, 20, 25]
virus_4log_ct_values_chlorine_dioxide = [50.1, 33.4, 25.1, 16.7, 12.5, 8.4]


# EPA Guidance Manual B-3
# Disinfection Profiling and Benchmarking
# Table B-5. CT Values* for 3-Log Inactivation of Giardia Cysts by Ozone
# units are min-mg/L.
#
# x is max degrees C: [1, 5, 10, 15, 20, 25]
giardia_3log_ct_values_ozone = [2.9, 1.9, 1.43, 0.95, 0.72, 0.48]

# EPA Guidance Manual B-4
# Disinfection Profiling and Benchmarking
# Table B-6. CT Values* for 4-Log Inactivation of Viruses by Ozone
# units are min-mg/L.
#
# x is max degrees C: [1, 5, 10, 15, 20, 25]
virus_4log_ct_values_ozone = [1.8, 1.2, 1.0, 0.6, 0.5, 0.3]

# EPA Guidance Manual B-4
# Disinfection Profiling and Benchmarking
# Table B-7. CT Values* for 3-Log Inactivation of Giardia Cysts by Chloramines pH 6-9
# units are min-mg/L.
#
# x is max degrees C: [1, 5, 10, 15, 20, 25]
max_chloramines_C = [1, 5, 10, 15, 20, 25]
giardia_3log_ct_values_chloramines = [3800, 2200, 1850, 1500, 100, 750]

# EPA Guidance Manual B-4
# Disinfection Profiling and Benchmarking
# Table B-8. CT Values* for 4-Log Inactivation of Viruses by Chloramines
# units are min-mg/L.
#
# x is max degrees C: [1, 5, 10, 15, 20, 25]
virus_4log_ct_values_chloramines = [2883, 1988, 1491, 994, 746, 497]
