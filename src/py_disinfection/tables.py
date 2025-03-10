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
# First-level keys are max degrees C
# Second-level keys are max free chlorine concentrations
# Third-level keys are max pHs
# Values are CT values for 3-log inactivation of Giardia cysts by free chlorine in min-mg/L
giardia_ct_freechlorine = {
    0.5: {  # Degrees C
        0.4: {  # mg/L free chlorine
            6.0: 137,  # pH
            6.5: 163,
            7.0: 195,
            7.5: 237,
            8.0: 277,
            8.5: 329,
            9.0: 390,
        },
        0.6: {
            6.0: 141,
            6.5: 168,
            7.0: 200,
            7.5: 239,
            8.0: 286,
            8.5: 342,
            9.0: 407,
        },
        0.8: {
            6.0: 145,
            6.5: 172,
            7.0: 205,
            7.5: 246,
            8.0: 295,
            8.5: 354,
            9.0: 422,
        },
        1: {
            6.0: 148,
            6.5: 176,
            7.0: 210,
            7.5: 253,
            8.0: 304,
            8.5: 365,
            9.0: 437,
        },
        1.2: {
            6.0: 152,
            6.5: 180,
            7.0: 215,
            7.5: 259,
            8.0: 313,
            8.5: 376,
            9.0: 451,
        },
        1.4: {
            6.0: 155,
            6.5: 184,
            7.0: 221,
            7.5: 266,
            8.0: 321,
            8.5: 387,
            9.0: 464,
        },
        1.6: {
            6.0: 157,
            6.5: 189,
            7.0: 226,
            7.5: 273,
            8.0: 329,
            8.5: 397,
            9.0: 477,
        },
        1.8: {
            6.0: 162,
            6.5: 193,
            7.0: 231,
            7.5: 279,
            8.0: 338,
            8.5: 407,
            9.0: 489,
        },
        2: {
            6.0: 165,
            6.5: 197,
            7.0: 236,
            7.5: 286,
            8.0: 346,
            8.5: 417,
            9.0: 500,
        },
        2.2: {
            6.0: 169,
            6.5: 201,
            7.0: 242,
            7.5: 297,
            8.0: 353,
            8.5: 426,
            9.0: 511,
        },
        2.4: {
            6.0: 172,
            6.5: 205,
            7.0: 247,
            7.5: 298,
            8.0: 361,
            8.5: 435,
            9.0: 522,
        },
        2.6: {
            6.0: 175,
            6.5: 209,
            7.0: 252,
            7.5: 304,
            8.0: 368,
            8.5: 444,
            9.0: 533,
        },
        2.8: {
            6.0: 178,
            6.5: 213,
            7.0: 257,
            7.5: 310,
            8.0: 375,
            8.5: 452,
            9.0: 543,
        },
        3: {
            6.0: 181,
            6.5: 217,
            7.0: 261,
            7.5: 316,
            8.0: 382,
            8.5: 460,
            9.0: 552,
        },
    },
    5: {
        0.4: {
            6.0: 97,
            6.5: 117,
            7.0: 139,
            7.5: 166,
            8.0: 198,
            8.5: 236,
            9.0: 279,
        },
        0.6: {
            6.0: 100,
            6.5: 120,
            7.0: 143,
            7.5: 171,
            8.0: 204,
            8.5: 244,
            9.0: 291,
        },
        0.8: {
            6.0: 103,
            6.5: 122,
            7.0: 146,
            7.5: 175,
            8.0: 210,
            8.5: 252,
            9.0: 301,
        },
        1: {
            6.0: 105,
            6.5: 125,
            7.0: 149,
            7.5: 179,
            8.0: 216,
            8.5: 260,
            9.0: 312,
        },
        1.2: {
            6.0: 107,
            6.5: 127,
            7.0: 152,
            7.5: 183,
            8.0: 221,
            8.5: 267,
            9.0: 320,
        },
        1.4: {
            6.0: 109,
            6.5: 130,
            7.0: 155,
            7.5: 187,
            8.0: 227,
            8.5: 274,
            9.0: 329,
        },
        1.6: {
            6.0: 111,
            6.5: 132,
            7.0: 158,
            7.5: 192,
            8.0: 232,
            8.5: 281,
            9.0: 337,
        },
        1.8: {
            6.0: 114,
            6.5: 135,
            7.0: 162,
            7.5: 196,
            8.0: 238,
            8.5: 287,
            9.0: 345,
        },
        2: {
            6.0: 116,
            6.5: 138,
            7.0: 165,
            7.5: 200,
            8.0: 243,
            8.5: 294,
            9.0: 353,
        },
        2.2: {
            6.0: 118,
            6.5: 140,
            7.0: 169,
            7.5: 204,
            8.0: 248,
            8.5: 300,
            9.0: 361,
        },
        2.4: {
            6.0: 120,
            6.5: 143,
            7.0: 172,
            7.5: 209,
            8.0: 253,
            8.5: 306,
            9.0: 368,
        },
        2.6: {
            6.0: 122,
            6.5: 146,
            7.0: 175,
            7.5: 213,
            8.0: 258,
            8.5: 312,
            9.0: 375,
        },
        2.8: {
            6.0: 124,
            6.5: 148,
            7.0: 178,
            7.5: 217,
            8.0: 263,
            8.5: 318,
            9.0: 382,
        },
        3: {
            6.0: 126,
            6.5: 151,
            7.0: 182,
            7.5: 221,
            8.0: 268,
            8.5: 324,
            9.0: 389,
        },
    },
    10: {
        0.4: {
            6.0: 73,
            6.5: 88,
            7.0: 104,
            7.5: 125,
            8.0: 149,
            8.5: 177,
            9.0: 209,
        },
        0.6: {
            6.0: 75,
            6.5: 90,
            7.0: 107,
            7.5: 128,
            8.0: 153,
            8.5: 183,
            9.0: 218,
        },
        0.8: {
            6.0: 78,
            6.5: 92,
            7.0: 110,
            7.5: 131,
            8.0: 158,
            8.5: 189,
            9.0: 226,
        },
        1: {
            6.0: 79,
            6.5: 94,
            7.0: 112,
            7.5: 134,
            8.0: 162,
            8.5: 195,
            9.0: 234,
        },
        1.2: {
            6.0: 80,
            6.5: 95,
            7.0: 114,
            7.5: 137,
            8.0: 166,
            8.5: 200,
            9.0: 240,
        },
        1.4: {
            6.0: 82,
            6.5: 98,
            7.0: 116,
            7.5: 140,
            8.0: 170,
            8.5: 206,
            9.0: 247,
        },
        1.6: {
            6.0: 83,
            6.5: 99,
            7.0: 119,
            7.5: 144,
            8.0: 174,
            8.5: 211,
            9: 253,
        },
        1.8: {
            6.0: 86,
            6.5: 101,
            7.0: 122,
            7.5: 147,
            8.0: 179,
            8.5: 215,
            9.0: 259,
        },
        2: {
            6.0: 87,
            6.5: 104,
            7.0: 124,
            7.5: 150,
            8.0: 182,
            8.5: 221,
            9.0: 265,
        },
        2.2: {
            6.0: 89,
            6.5: 105,
            7.0: 127,
            7.5: 153,
            8.0: 186,
            8.5: 225,
            9.0: 271,
        },
        2.4: {
            6.0: 90,
            6.5: 107,
            7.0: 129,
            7.5: 157,
            8.0: 190,
            8.5: 230,
            9.0: 276,
        },
        2.6: {
            6.0: 92,
            6.5: 110,
            7.0: 131,
            7.5: 160,
            8.0: 194,
            8.5: 234,
            9.0: 281,
        },
        2.8: {
            6.0: 93,
            6.5: 111,
            7.0: 134,
            7.5: 163,
            8.0: 197,
            8.5: 239,
            9.0: 287,
        },
        3: {
            6.0: 95,
            6.5: 113,
            7.0: 137,
            7.5: 166,
            8.0: 201,
            8.5: 243,
            9.0: 292,
        },
    },
    15: {
        0.4: {
            6.0: 49,
            6.5: 59,
            7.0: 70,
            7.5: 83,
            8.0: 99,
            8.5: 118,
            9.0: 140,
        },
        0.6: {
            6.0: 50,
            6.5: 60,
            7.0: 72,
            7.5: 86,
            8.0: 102,
            8.5: 122,
            9.0: 146,
        },
        0.8: {
            6.0: 52,
            6.5: 61,
            7.0: 73,
            7.5: 88,
            8.0: 105,
            8.5: 126,
            9.0: 151,
        },
        1: {
            6.0: 53,
            6.5: 63,
            7.0: 75,
            7.5: 90,
            8.0: 108,
            8.5: 130,
            9.0: 156,
        },
        1.2: {
            6.0: 54,
            6.5: 64,
            7.0: 76,
            7.5: 92,
            8.0: 111,
            8.5: 134,
            9.0: 160,
        },
        1.4: {
            6.0: 55,
            6.5: 65,
            7.0: 78,
            7.5: 94,
            8.0: 114,
            8.5: 137,
            9.0: 165,
        },
        1.6: {
            6.0: 56,
            6.5: 66,
            7.0: 79,
            7.5: 96,
            8.0: 116,
            8.5: 141,
            9.0: 169,
        },
        1.8: {
            6.0: 57,
            6.5: 68,
            7.0: 81,
            7.5: 98,
            8.0: 119,
            8.5: 144,
            9.0: 173,
        },
        2: {
            6.0: 58,
            6.5: 69,
            7.0: 83,
            7.5: 100,
            8.0: 122,
            8.5: 147,
            9.0: 177,
        },
        2.2: {
            6.0: 59,
            6.5: 70,
            7.0: 85,
            7.5: 102,
            8.0: 124,
            8.5: 150,
            9.0: 181,
        },
        2.4: {
            6.0: 60,
            6.5: 72,
            7.0: 86,
            7.5: 105,
            8.0: 127,
            8.5: 153,
            9.0: 184,
        },
        2.6: {
            6.0: 61,
            6.5: 73,
            7.0: 88,
            7.5: 107,
            8.0: 129,
            8.5: 156,
            9.0: 188,
        },
        2.8: {
            6.0: 62,
            6.5: 74,
            7.0: 89,
            7.5: 109,
            8.0: 132,
            8.5: 159,
            9.0: 191,
        },
        3: {
            6.0: 63,
            6.5: 76,
            7.0: 91,
            7.5: 111,
            8.0: 134,
            8.5: 162,
            9.0: 195,
        },
    },
    20: {
        0.4: {
            6.0: 36,
            6.5: 44,
            7.0: 52,
            7.5: 62,
            8.0: 74,
            8.5: 89,
            9.0: 105,
        },
        0.6: {
            6.0: 38,
            6.5: 45,
            7.0: 54,
            7.5: 64,
            8.0: 77,
            8.5: 92,
            9.0: 109,
        },
        0.8: {
            6.0: 39,
            6.5: 46,
            7.0: 55,
            7.5: 66,
            8.0: 79,
            8.5: 95,
            9.0: 113,
        },
        1: {
            6.0: 39,
            6.5: 47,
            7.0: 56,
            7.5: 67,
            8.0: 81,
            8.5: 98,
            9.0: 117,
        },
        1.2: {
            6.0: 40,
            6.5: 48,
            7.0: 57,
            7.5: 69,
            8.0: 83,
            8.5: 100,
            9.0: 120,
        },
        1.4: {
            6.0: 41,
            6.5: 49,
            7.0: 58,
            7.5: 70,
            8.0: 85,
            8.5: 103,
            9.0: 123,
        },
        1.6: {
            6.0: 42,
            6.5: 50,
            7.0: 59,
            7.5: 72,
            8.0: 87,
            8.5: 105,
            9.0: 126,
        },
        1.8: {
            6.0: 43,
            6.5: 51,
            7.0: 61,
            7.5: 74,
            8.0: 89,
            8.5: 108,
            9.0: 129,
        },
        2: {
            6.0: 44,
            6.5: 52,
            7.0: 62,
            7.5: 75,
            8.0: 91,
            8.5: 110,
            9.0: 132,
        },
        2.2: {
            6.0: 44,
            6.5: 53,
            7.0: 63,
            7.5: 77,
            8.0: 93,
            8.5: 113,
            9.0: 135,
        },
        2.4: {
            6.0: 45,
            6.5: 54,
            7.0: 65,
            7.5: 78,
            8.0: 95,
            8.5: 115,
            9.0: 138,
        },
        2.6: {
            6.0: 46,
            6.5: 55,
            7.0: 66,
            7.5: 80,
            8.0: 97,
            8.5: 117,
            9.0: 141,
        },
        2.8: {
            6.0: 47,
            6.5: 56,
            7.0: 67,
            7.5: 81,
            8.0: 99,
            8.5: 119,
            9.0: 143,
        },
        3: {
            6.0: 47,
            6.5: 57,
            7.0: 68,
            7.5: 83,
            8.0: 101,
            8.5: 122,
            9.0: 146,
        },
    },
    25: {
        0.4: {
            6.0: 24,
            6.5: 29,
            7.0: 35,
            7.5: 42,
            8.0: 50,
            8.5: 59,
            9.0: 70,
        },
        0.6: {
            6.0: 25,
            6.5: 30,
            7.0: 36,
            7.5: 43,
            8.0: 51,
            8.5: 61,
            9.0: 73,
        },
        0.8: {
            6.0: 26,
            6.5: 31,
            7.0: 37,
            7.5: 44,
            8.0: 53,
            8.5: 63,
            9.0: 75,
        },
        1: {
            6.0: 26,
            6.5: 31,
            7.0: 37,
            7.5: 45,
            8.0: 54,
            8.5: 65,
            9.0: 78,
        },
        1.2: {
            6.0: 27,
            6.5: 32,
            7.0: 38,
            7.5: 46,
            8.0: 55,
            8.5: 67,
            9.0: 80,
        },
        1.4: {
            6.0: 27,
            6.5: 33,
            7.0: 39,
            7.5: 47,
            8.0: 57,
            8.5: 69,
            9.0: 82,
        },
        1.6: {
            6.0: 28,
            6.5: 33,
            7.0: 40,
            7.5: 48,
            8.0: 58,
            8.5: 70,
            9.0: 84,
        },
        1.8: {
            6.0: 29,
            6.5: 34,
            7.0: 41,
            7.5: 49,
            8.0: 59,
            8.5: 72,
            9.0: 86,
        },
        2: {
            6.0: 29,
            6.5: 35,
            7.0: 42,
            7.5: 50,
            8.0: 60,
            8.5: 74,
            9.0: 88,
        },
        2.2: {
            6.0: 30,
            6.5: 35,
            7.0: 43,
            7.5: 51,
            8.0: 61,
            8.5: 75,
            9.0: 90,
        },
        2.4: {
            6.0: 30,
            6.5: 36,
            7.0: 44,
            7.5: 52,
            8.0: 62,
            8.5: 77,
            9.0: 92,
        },
        2.6: {
            6.0: 31,
            6.5: 37,
            7.0: 45,
            7.5: 53,
            8.0: 63,
            8.5: 78,
            9.0: 94,
        },
        2.8: {
            6.0: 31,
            6.5: 37,
            7.0: 46,
            7.5: 54,
            8.0: 64,
            8.5: 79,
            9.0: 95,
        },
        3: {
            6.0: 32,
            6.5: 38,
            7.0: 46,
            7.5: 55,
            8.0: 65,
            8.5: 81,
            9.0: 97,
        },
    },
}


# EPA Guidance Manual B-3
# Disinfection Profiling and Benchmarking
# Table B-2. CT Values* for 4-Log Inactivation of Viruses by Free Chlorine
# units are min-mg/L.
# First-level keys are max degrees C
# Second-level keys are max pH
# Values are CT values for 4-log inactivation of viruses by free chlorine (min-mg/L)
virus_ct_freechlorine = {
    0.5: {
        6: 0,
        9: 12,
        10: 90,
    },
    5: {
        6: 0,
        9: 8,
        10: 60,
    },
    10: {
        6: 0,
        9: 6,
        10: 45,
    },
    15: {
        6: 0,
        9: 4,
        10: 30,
    },
    20: {
        6: 0,
        9: 3,
        10: 22,
    },
    25: {
        6: 0,
        9: 2,
        10: 15,
    },
}

# EPA Guidance Manual B-3
# Disinfection Profiling and Benchmarking
# Table B-3. CT Values* for 3-Log Inactivation of Giardia Cysts by Chlorine Dioxide
# units are min-mg/L.
# Keys are max degrees C
# Values are CT values for 3-log inactivation of Giardia Cysts by Chlorine Dioxide (min-mg/L)
giardia_ct_chlorinedioxide = {
    1: 63,
    5: 26,
    10: 23,
    15: 19,
    20: 15,
    25: 11,
}

# EPA Guidance Manual B-3
# Disinfection Profiling and Benchmarking
# Table B-4. CT Values* for 4-Log Inactivation of Viruses by Chlorine Dioxide ph 6-9
# units are min-mg/L.
#
# Keys are max degrees C
# Values are CT values for 4-log inactivation of viruses by chlorine dioxide (min-mg/L)
virus_ct_chlorinedioxide = {1: 50.1, 5: 33.4, 10: 25.1, 15: 16.7, 20: 12.5, 25: 8.4}


# EPA Guidance Manual B-3
# Disinfection Profiling and Benchmarking
# Table B-5. CT Values* for 3-Log Inactivation of Giardia Cysts by Ozone
# units are min-mg/L.
# Keys are max degrees C
# Values are CT values for 3-log inactivation of Giardia Cysts by Ozone (min-mg/L)
giardia_ct_ozone = {1: 2.9, 5: 1.9, 10: 1.43, 15: 0.95, 20: 0.72, 25: 0.48}

# EPA Guidance Manual B-4
# Disinfection Profiling and Benchmarking
# Table B-6. CT Values* for 4-Log Inactivation of Viruses by Ozone
# units are min-mg/L.
# Keys are max degrees C
# Values are CT values for 4-log inactivation of viruses by ozone (min-mg/L)
virus_ct_ozone = {1: 1.8, 5: 1.2, 10: 1.0, 15: 0.6, 20: 0.5, 25: 0.3}

# EPA Guidance Manual B-4
# Disinfection Profiling and Benchmarking
# Table B-7. CT Values* for 3-Log Inactivation of Giardia Cysts by Chloramines pH 6-9
# units are min-mg/L.
# Keys are max degrees C
# Values are CT values for 3-log inactivation of Giardia cysts by chloramines (min-mg/L)
giardia_ct_chloramines = {
    1: 3800,
    5: 2200,
    10: 1850,
    15: 1500,
    20: 1000,
    25: 750,
}

# EPA Guidance Manual B-4
# Disinfection Profiling and Benchmarking
# Table B-8. CT Values* for 4-Log Inactivation of Viruses by Chloramines
# units are min-mg/L.
# Keys are max degrees C
# Values are CT values for 4-log inactivation of viruses by chloramines (min-mg/L)
virus_ct_chloramines = {
    1: 2883,
    5: 1988,
    10: 1491,
    15: 994,
    20: 746,
    25: 497,
}
