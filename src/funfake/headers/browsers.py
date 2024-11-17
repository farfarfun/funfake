from random import randint as rint

chrome_ver = [
    "87.0",
    "87.0",
    "86.0.4240",
    "85.0.4183",
    "84.0.4147",
    "83.0.4103",
    "81.0.4044",
    "80.0.3987",
    "79.0.3945",
    "78.0.3904",
    "77.0.3865",
    "77.0",
    "77.0",
    "76.0.3809",
    "75.0.3770",
    "74.0.3729",
    "73.0.3683",
    "72.0.3626",
    "71.0.3578.80",
    "71.0.3578.98",
    "70.0.3538.102",
    "70.0.3538.80",
    "70.0.3538.67",
    "70.0.3538.77",
    "70.0.3538.110",
    "69.0.3497.100",
    "69.0.3497.81",
    "69.0.3497.92",
    "68.0.3440.91",
    "68.0.3440.106",
    "68.0.3440.84",
    "68.0.3440.1805",
    "68.0.3440.75",
    "67.0.3396.87",
    "67.0.3396.99",
    "67.0.3396.79",
    "67.0.3396.62",
    "66.0.3359.117",
    "66.0.3359.139",
    "66.0.3359.181",
    "66.0.3359.158",
    "66.0.3359.170",
    "65.0.3325.181",
    "65.0.3325.109",
    "65.0.3325.162",
    "64.0.3282.186",
    "64.0.3282.140",
    "64.0.3282.137",
    "64.0.3282.167",
    "64.0.3282.119",
    "63.0.3239.83",
    "63.0.3239.111",
    "63.0.3239.108",
    "63.0.3239.84",
    "63.0.3239.132",
    "62.0.3202.94",
    "62.0.3202.89",
    "62.0.3202.84",
    "62.0.3202.62",
    "61.0.3163.100",
    "61.0.3163.79",
    "61.0.3163.98",
    "60.0.3112.78",
    "60.0.3112.90",
    "60.0.3112.113",
    "60.0.3112.116",
]


def firefox() -> str:
    main = "Mozilla/5.0 (%PLAT%; rv:%VER%) Gecko/20100101 Firefox/%VER%"

    ver = [
        "80.0",
        "80.0.1",
        "79.0",
        "78.0",
        "78.0.1",
        "78.0.2",
        "77.0",
        "77.0.1",
        "76.0",
        "76.0.1",
        "75.0",
        "74.0",
        "74.0.1",
        "73.0",
        "73.0.1",
        "72.0",
        "72.0.1",
        "72.0.2",
        "71.0",
        "70.0",
        "70.0.1",
        "69.0",
        "69.0.1",
        "69.0.2",
        "69.0.3",
        "68.0",
        "68.0.1",
        "68.0.2",
        "68.1.0",
        "68.2.0",
        "68.3.0",
        "68.4.0",
        "68.4.1",
        "68.4.2",
        "68.5.0",
        "68.6.0",
        "68.6.1",
        "68.7.0",
        "68.8.0",
        "68.9.0",
        "68.10.0",
        "68.11.0",
        "68.12.0",
        "67.0",
        "67.0.1",
        "67.0.2",
        "67.0.3",
        "67.0.4",
        "67.0",
        "67.0.1",
        "67.0.2",
        "66.0",
        "66.0.1",
        "66.0.2",
        "66.0.3",
        "66.0.4",
        "66.0.5",
        "65.0",
        "65.0.1",
        "64.0",
        "64.0.2",
        "63.0",
        "63.0.1",
        "63.0.3",
        "62.0",
        "62.0.2",
        "62.0.3",
        "61.0",
        "61.0.1",
        "61.0.2",
        "60.0",
        "60.0.1",
        "60.0.2",
        "60.1.0",
        "60.2.0",
        "60.2.1",
        "60.2.2",
        "60.3.0",
        "60.4.0",
        "60.5.0",
        "60.5.1",
        "60.5.2",
        "59.0",
        "59.0.1",
        "59.0.2",
        "59.0.3",
        "58.0",
        "58.0.1",
        "58.0.2",
        "57.0",
        "57.0.1",
        "57.0.2",
        "57.0.3",
        "57.0.4",
        "56.0",
        "56.0.1",
        "56.0.2",
        "55.0",
        "55.0.1",
        "55.0.2",
        "55.0.3",
        "54.0",
        "54.0.1",
        "53.0",
        "53.0.2",
        "53.0.3",
        "52.0",
        "52.0.1",
        "52.0.2",
        "52.1.0",
        "52.1.1",
        "52.1.2",
        "52.2.0",
        "52.2.1",
        "52.3.0",
        "52.4.0",
        "52.4.1",
        "52.5.0",
        "52.5.2",
        "52.5.3",
        "52.6.0",
        "52.7.0",
        "52.7.1",
        "52.7.2",
        "52.7.3",
        "52.7.4",
        "52.8.0",
        "52.8.1",
        "52.9.0",
        "51.0",
        "51.0.1",
        "50.0",
        "50.0.1",
        "50.0.2",
    ]

    return main.replace("%VER%", ver[rint(0, len(ver) - 1)])


def chrome() -> str:
    main = (
        "Mozilla/5.0 (%PLAT%) AppleWebKit/537.36 (KHTML,"
        + " like Gecko) Chrome/%VER% Safari/537.36"
    )

    return main.replace("%VER%", chrome_ver[rint(0, len(chrome_ver) - 1)])


def opera() -> str:
    main = (
        "Mozilla/5.0 (%PLAT%) AppleWebKit/537.36 (KHTML, like Gecko) "
        + "Chrome/%CVER% Safari/537.36 OPR/%OVER%"
    )

    ver = [
        "67.0.3575.130",
        "66.0.3515.72",
        "66.0.3515.44",
        "62.0.3331.72",
        "60.0.3255.170",
        "58.0.3135.127",
        "58.0.3135.107",
        "57.0.3098.116",
        "57.0.3098.106",
        "57.0.3098.91",
        "56.0.3051.36",
        "56.0.3051.104",
        "56.0.3051.52",
        "56.0.3051.116",
        "56.0.3051.116",
        "56.0.3051.99",
        "56.0.3051.43",
        "56.0.3051.52",
        "55.0.2994.37",
        "55.0.2994.47",
        "55.0.2994.44",
        "55.0.2994.61",
        "55.0.2994.61",
        "54.0.2952.71",
        "54.0.2952.51",
        "54.0.2952.64",
        "54.0.2952.54",
        "54.0.2952.64",
        "54.0.2952.60",
        "53.0.2907.68",
        "53.0.2907.99",
        "53.0.2907.106",
        "53.0.2907.110",
        "52.0.2871.99",
        "52.0.2871.64",
        "52.0.2871.40",
        "51.0.2830.34",
        "51.0.2830.55",
        "51.0.2830.40",
        "50.0.2762.58",
        "50.0.2762.67",
    ]

    ua = rint(0, len(ver) - 1)
    main = main.replace("%OVER%", ver[ua])
    main = main.replace("%CVER%", chrome_ver[ua])

    return main


def random_browser() -> str:
    os = [chrome, opera, firefox]
    return os[rint(0, 2)]()
