import pytest
from friendly_bytes_function import friendly_bytes

def test_on_positive():
    assert(friendly_bytes( 212321 ) =='212.32 KB')
    assert(friendly_bytes( 45450 ) =='45.45 KB')
    assert(friendly_bytes( 903428347234 ) =='903.43 GB')
    assert(friendly_bytes( 238942.443 ) =='238.94 KB')
    assert(friendly_bytes( 8343493409.22212 ) =='8.34 GB')
    assert(friendly_bytes( 840933049 ) =='840.93 MB')
    assert(friendly_bytes( 0 ) =='0 B')
    assert(friendly_bytes( 0.0 ) =='0 B')
    assert(friendly_bytes( 483434093 ) =='483.43 MB')
    assert(friendly_bytes( 24 ) =='24.0 B')
    assert(friendly_bytes( 24.0 ) =='24.0 B')
    assert(friendly_bytes( 0.3 ) =='0.3 B')
    assert(friendly_bytes( 90.59438934 ) =='90.59 B')
    assert(friendly_bytes( 122133 ) =='122.13 KB')
    assert(friendly_bytes( 328939324239329234 ) =='328.94 PB')
    assert(friendly_bytes( 3434904393490 ) =='3.43 TB')
    assert(friendly_bytes( 349823093209 ) =='349.82 GB')
    assert(friendly_bytes( 332423.3232432 ) =='332.42 KB')
    assert(friendly_bytes( 48234023409 ) =='48.23 GB')
    assert(friendly_bytes( 32.3 ) =='32.3 B')
    assert(friendly_bytes( 239023932 ) =='239.02 MB')
    assert(friendly_bytes( 0 ) =='0 B')
    assert(friendly_bytes( 11 ) =='11.0 B')

def test_on_negative():
    assert(friendly_bytes(- 212321 ) =='-212.32 KB')
    assert(friendly_bytes(- 45450 ) =='-45.45 KB')
    assert(friendly_bytes(- 903428347234 ) =='-903.43 GB')
    assert(friendly_bytes(- 238942.443 ) =='-238.94 KB')
    assert(friendly_bytes(- 8343493409.22212 ) =='-8.34 GB')
    assert(friendly_bytes(- 840933049 ) =='-840.93 MB')
    assert(friendly_bytes(- 0 ) =='0 B')
    assert(friendly_bytes(- 0.0 ) =='0 B')
    assert(friendly_bytes(- 483434093 ) =='-483.43 MB')
    assert(friendly_bytes(- 24 ) =='-24.0 B')
    assert(friendly_bytes(- 24.0 ) =='-24.0 B')
    assert(friendly_bytes(- 0.3 ) =='-0.3 B')
    assert(friendly_bytes(- 90.59438934 ) =='-90.59 B')
    assert(friendly_bytes(- 122133 ) =='-122.13 KB')
    assert(friendly_bytes(- 328939324239329234 ) =='-328.94 PB')
    assert(friendly_bytes(- 3434904393490 ) =='-3.43 TB')
    assert(friendly_bytes(- 349823093209 ) =='-349.82 GB')
    assert(friendly_bytes(- 332423.3232432 ) =='-332.42 KB')
    assert(friendly_bytes(- 48234023409 ) =='-48.23 GB')
    assert(friendly_bytes(- 32.3 ) =='-32.3 B')
    assert(friendly_bytes(- 239023932 ) =='-239.02 MB')
    assert(friendly_bytes(- 0 ) =='0 B')
    assert(friendly_bytes(- 11 ) =='-11.0 B')

def test_on_decimals():
    assert(friendly_bytes( 43443.2334243 ) =='43.44 KB')
    assert(friendly_bytes( 43456.879889 ) =='43.46 KB')
    assert(friendly_bytes( 12223.889 ) =='12.22 KB')
    assert(friendly_bytes( 32324.009 ) =='32.32 KB')
    assert(friendly_bytes( 873489732.079067 ) =='873.49 MB')
    assert(friendly_bytes( 1283.003643 ) =='1.28 KB')
    assert(friendly_bytes( 38732.3402424 ) =='38.73 KB')
    assert(friendly_bytes( 11.22 ) =='11.22 B')
    assert(friendly_bytes( 32873298329.32 ) =='32.87 GB')
    assert(friendly_bytes( 3832.1 ) =='3.83 KB')

def test_decimal_parameter():
    assert (friendly_bytes( 43443.2334243 ,decimals= 0 ) =='43 KB')
    assert (friendly_bytes( 43443.2334243 ,decimals= 1 ) =='43.4 KB')
    assert (friendly_bytes( 43443.2334243 ,decimals= 2 ) =='43.44 KB')
    assert (friendly_bytes( 43443.2334243 ,decimals= 3 ) =='43.443 KB')
    assert (friendly_bytes( 43443.2334243 ,decimals= 4 ) =='43.4432 KB')
    assert (friendly_bytes( 43443.2334243 ,decimals= 5 ) =='43.44323 KB')
    assert (friendly_bytes( 43443.2334243 ,decimals= 6 ) =='43.443233 KB')
    assert (friendly_bytes( 43443.2334243 ,decimals= 7 ) =='43.4432334 KB')
    assert (friendly_bytes( 43443.2334243 ,decimals= 8 ) =='43.44323342 KB')
    assert (friendly_bytes( 43443.2334243 ,decimals= 9 ) =='43.443233424 KB')
    assert (friendly_bytes( 43456.879889 ,decimals= 0 ) =='43 KB')
    assert (friendly_bytes( 43456.879889 ,decimals= 1 ) =='43.5 KB')
    assert (friendly_bytes( 43456.879889 ,decimals= 2 ) =='43.46 KB')
    assert (friendly_bytes( 43456.879889 ,decimals= 3 ) =='43.457 KB')
    assert (friendly_bytes( 43456.879889 ,decimals= 4 ) =='43.4569 KB')
    assert (friendly_bytes( 43456.879889 ,decimals= 5 ) =='43.45688 KB')
    assert (friendly_bytes( 43456.879889 ,decimals= 6 ) =='43.45688 KB')
    assert (friendly_bytes( 43456.879889 ,decimals= 7 ) =='43.4568799 KB')
    assert (friendly_bytes( 43456.879889 ,decimals= 8 ) =='43.45687989 KB')
    assert (friendly_bytes( 43456.879889 ,decimals= 9 ) =='43.456879889 KB')
    assert (friendly_bytes( 12223.889 ,decimals= 0 ) =='12 KB')
    assert (friendly_bytes( 12223.889 ,decimals= 1 ) =='12.2 KB')
    assert (friendly_bytes( 12223.889 ,decimals= 2 ) =='12.22 KB')
    assert (friendly_bytes( 12223.889 ,decimals= 3 ) =='12.224 KB')
    assert (friendly_bytes( 12223.889 ,decimals= 4 ) =='12.2239 KB')
    assert (friendly_bytes( 12223.889 ,decimals= 5 ) =='12.22389 KB')
    assert (friendly_bytes( 12223.889 ,decimals= 6 ) =='12.223889 KB')
    assert (friendly_bytes( 12223.889 ,decimals= 7 ) =='12.223889 KB')
    assert (friendly_bytes( 12223.889 ,decimals= 8 ) =='12.223889 KB')
    assert (friendly_bytes( 12223.889 ,decimals= 9 ) =='12.223889 KB')
    assert (friendly_bytes( 32324.009 ,decimals= 0 ) =='32 KB')
    assert (friendly_bytes( 32324.009 ,decimals= 1 ) =='32.3 KB')
    assert (friendly_bytes( 32324.009 ,decimals= 2 ) =='32.32 KB')
    assert (friendly_bytes( 32324.009 ,decimals= 3 ) =='32.324 KB')
    assert (friendly_bytes( 32324.009 ,decimals= 4 ) =='32.324 KB')
    assert (friendly_bytes( 32324.009 ,decimals= 5 ) =='32.32401 KB')
    assert (friendly_bytes( 32324.009 ,decimals= 6 ) =='32.324009 KB')
    assert (friendly_bytes( 32324.009 ,decimals= 7 ) =='32.324009 KB')
    assert (friendly_bytes( 32324.009 ,decimals= 8 ) =='32.324009 KB')
    assert (friendly_bytes( 32324.009 ,decimals= 9 ) =='32.324009 KB')
    assert (friendly_bytes( 873489732.079067 ,decimals= 0 ) =='873 MB')
    assert (friendly_bytes( 873489732.079067 ,decimals= 1 ) =='873.5 MB')
    assert (friendly_bytes( 873489732.079067 ,decimals= 2 ) =='873.49 MB')
    assert (friendly_bytes( 873489732.079067 ,decimals= 3 ) =='873.49 MB')
    assert (friendly_bytes( 873489732.079067 ,decimals= 4 ) =='873.4897 MB')
    assert (friendly_bytes( 873489732.079067 ,decimals= 5 ) =='873.48973 MB')
    assert (friendly_bytes( 873489732.079067 ,decimals= 6 ) =='873.489732 MB')
    assert (friendly_bytes( 873489732.079067 ,decimals= 7 ) =='873.4897321 MB')
    assert (friendly_bytes( 873489732.079067 ,decimals= 8 ) =='873.48973208 MB')
    assert (friendly_bytes( 873489732.079067 ,decimals= 9 ) =='873.489732079 MB')
    assert (friendly_bytes( 1283.003643 ,decimals= 0 ) =='1 KB')
    assert (friendly_bytes( 1283.003643 ,decimals= 1 ) =='1.3 KB')
    assert (friendly_bytes( 1283.003643 ,decimals= 2 ) =='1.28 KB')
    assert (friendly_bytes( 1283.003643 ,decimals= 3 ) =='1.283 KB')
    assert (friendly_bytes( 1283.003643 ,decimals= 4 ) =='1.283 KB')
    assert (friendly_bytes( 1283.003643 ,decimals= 5 ) =='1.283 KB')
    assert (friendly_bytes( 1283.003643 ,decimals= 6 ) =='1.283004 KB')
    assert (friendly_bytes( 1283.003643 ,decimals= 7 ) =='1.2830036 KB')
    assert (friendly_bytes( 1283.003643 ,decimals= 8 ) =='1.28300364 KB')
    assert (friendly_bytes( 1283.003643 ,decimals= 9 ) =='1.283003643 KB')
    assert (friendly_bytes( 38732.3402424 ,decimals= 0 ) =='38 KB')
    assert (friendly_bytes( 38732.3402424 ,decimals= 1 ) =='38.7 KB')
    assert (friendly_bytes( 38732.3402424 ,decimals= 2 ) =='38.73 KB')
    assert (friendly_bytes( 38732.3402424 ,decimals= 3 ) =='38.732 KB')
    assert (friendly_bytes( 38732.3402424 ,decimals= 4 ) =='38.7323 KB')
    assert (friendly_bytes( 38732.3402424 ,decimals= 5 ) =='38.73234 KB')
    assert (friendly_bytes( 38732.3402424 ,decimals= 6 ) =='38.73234 KB')
    assert (friendly_bytes( 38732.3402424 ,decimals= 7 ) =='38.7323402 KB')
    assert (friendly_bytes( 38732.3402424 ,decimals= 8 ) =='38.73234024 KB')
    assert (friendly_bytes( 38732.3402424 ,decimals= 9 ) =='38.732340242 KB')
    assert (friendly_bytes( 11.22 ,decimals= 0 ) =='11 B')
    assert (friendly_bytes( 11.22 ,decimals= 1 ) =='11.2 B')
    assert (friendly_bytes( 11.22 ,decimals= 2 ) =='11.22 B')
    assert (friendly_bytes( 11.22 ,decimals= 3 ) =='11.22 B')
    assert (friendly_bytes( 11.22 ,decimals= 4 ) =='11.22 B')
    assert (friendly_bytes( 11.22 ,decimals= 5 ) =='11.22 B')
    assert (friendly_bytes( 11.22 ,decimals= 6 ) =='11.22 B')
    assert (friendly_bytes( 11.22 ,decimals= 7 ) =='11.22 B')
    assert (friendly_bytes( 11.22 ,decimals= 8 ) =='11.22 B')
    assert (friendly_bytes( 11.22 ,decimals= 9 ) =='11.22 B')
    assert (friendly_bytes( 32873298329.32 ,decimals= 0 ) =='32 GB')
    assert (friendly_bytes( 32873298329.32 ,decimals= 1 ) =='32.9 GB')
    assert (friendly_bytes( 32873298329.32 ,decimals= 2 ) =='32.87 GB')
    assert (friendly_bytes( 32873298329.32 ,decimals= 3 ) =='32.873 GB')
    assert (friendly_bytes( 32873298329.32 ,decimals= 4 ) =='32.8733 GB')
    assert (friendly_bytes( 32873298329.32 ,decimals= 5 ) =='32.8733 GB')
    assert (friendly_bytes( 32873298329.32 ,decimals= 6 ) =='32.873298 GB')
    assert (friendly_bytes( 32873298329.32 ,decimals= 7 ) =='32.8732983 GB')
    assert (friendly_bytes( 32873298329.32 ,decimals= 8 ) =='32.87329833 GB')
    assert (friendly_bytes( 32873298329.32 ,decimals= 9 ) =='32.873298329 GB')
    assert (friendly_bytes( 3832.1 ,decimals= 0 ) =='3 KB')
    assert (friendly_bytes( 3832.1 ,decimals= 1 ) =='3.8 KB')
    assert (friendly_bytes( 3832.1 ,decimals= 2 ) =='3.83 KB')
    assert (friendly_bytes( 3832.1 ,decimals= 3 ) =='3.832 KB')
    assert (friendly_bytes( 3832.1 ,decimals= 4 ) =='3.8321 KB')
    assert (friendly_bytes( 3832.1 ,decimals= 5 ) =='3.8321 KB')
    assert (friendly_bytes( 3832.1 ,decimals= 6 ) =='3.8321 KB')
    assert (friendly_bytes( 3832.1 ,decimals= 7 ) =='3.8321 KB')
    assert (friendly_bytes( 3832.1 ,decimals= 8 ) =='3.8321 KB')
    assert (friendly_bytes( 3832.1 ,decimals= 9 ) =='3.8321 KB')

def test_binary_parameter():
    assert (friendly_bytes( 212321 , binary=True) =='207.34 KiB')
    assert (friendly_bytes( 45450 , binary=True) =='44.38 KiB')
    assert (friendly_bytes( 903428347234 , binary=True) =='841.38 GiB')
    assert (friendly_bytes( 238942.443 , binary=True) =='233.34 KiB')
    assert (friendly_bytes( 8343493409.22212 , binary=True) =='7.77 GiB')
    assert (friendly_bytes( 840933049 , binary=True) =='801.98 MiB')
    assert (friendly_bytes( 0 , binary=True) =='0 B')
    assert (friendly_bytes( 0.0 , binary=True) =='0 B')
    assert (friendly_bytes( 483434093 , binary=True) =='461.04 MiB')
    assert (friendly_bytes( 24 , binary=True) =='24.0 B')
    assert (friendly_bytes( 24.0 , binary=True) =='24.0 B')
    assert (friendly_bytes( 0.3 , binary=True) =='0.3 B')
    assert (friendly_bytes( 90.59438934 , binary=True) =='90.59 B')
    assert (friendly_bytes( 122133 , binary=True) =='119.27 KiB')
    assert (friendly_bytes( 328939324239329234 , binary=True) =='292.16 PiB')
    assert (friendly_bytes( 3434904393490 , binary=True) =='3.12 TiB')
    assert (friendly_bytes( 349823093209 , binary=True) =='325.8 GiB')
    assert (friendly_bytes( 332423.3232432 , binary=True) =='324.63 KiB')
    assert (friendly_bytes( 48234023409 , binary=True) =='44.92 GiB')
    assert (friendly_bytes( 32.3 , binary=True) =='32.3 B')
    assert (friendly_bytes( 239023932 , binary=True) =='227.95 MiB')
    assert (friendly_bytes( 0 , binary=True) =='0 B')
    assert (friendly_bytes( 11 , binary=True) =='11.0 B')

def test_false_binary_parameter():
    assert(friendly_bytes( 212321 , binary=False) =='212.32 KB')
    assert(friendly_bytes( 45450 , binary=False) =='45.45 KB')
    assert(friendly_bytes( 903428347234 , binary=False) =='903.43 GB')
    assert(friendly_bytes( 238942.443 , binary=False) =='238.94 KB')
    assert(friendly_bytes( 8343493409.22212 , binary=False) =='8.34 GB')
    assert(friendly_bytes( 840933049 , binary=False) =='840.93 MB')
    assert(friendly_bytes( 0 , binary=False) =='0 B')
    assert(friendly_bytes( 0.0 , binary=False) =='0 B')
    assert(friendly_bytes( 483434093 , binary=False) =='483.43 MB')
    assert(friendly_bytes( 24 , binary=False) =='24.0 B')
    assert(friendly_bytes( 24.0 , binary=False) =='24.0 B')
    assert(friendly_bytes( 0.3 , binary=False) =='0.3 B')
    assert(friendly_bytes( 90.59438934 , binary=False) =='90.59 B')
    assert(friendly_bytes( 122133 , binary=False) =='122.13 KB')
    assert(friendly_bytes( 328939324239329234 , binary=False) =='328.94 PB')
    assert(friendly_bytes( 3434904393490 , binary=False) =='3.43 TB')
    assert(friendly_bytes( 349823093209 , binary=False) =='349.82 GB')
    assert(friendly_bytes( 332423.3232432 , binary=False) =='332.42 KB')
    assert(friendly_bytes( 48234023409 , binary=False) =='48.23 GB')
    assert(friendly_bytes( 32.3 , binary=False) =='32.3 B')
    assert(friendly_bytes( 239023932 , binary=False) =='239.02 MB')
    assert(friendly_bytes( 0 , binary=False) =='0 B')
    assert(friendly_bytes( 11 , binary=False) =='11.0 B')

def test_eb_to_yb_sizes():
    assert(friendly_bytes( 0 , binary=False) =='0 B')
    assert(friendly_bytes( 1230000000000000000 , binary=False) =='1.23 EB')
    assert(friendly_bytes( 2460000000000000000 , binary=False) =='2.46 EB')
    assert(friendly_bytes( 3690000000000000000 , binary=False) =='3.69 EB')
    assert(friendly_bytes( 4920000000000000000 , binary=False) =='4.92 EB')
    assert(friendly_bytes( 6150000000000000000 , binary=False) =='6.15 EB')
    assert(friendly_bytes( 7380000000000000000 , binary=False) =='7.38 EB')
    assert(friendly_bytes( 0 , binary=False) =='0 B')
    assert(friendly_bytes( 4300000000000000000000 , binary=False) =='4.3 ZB')
    assert(friendly_bytes( 8600000000000000000000 , binary=False) =='8.6 ZB')
    assert(friendly_bytes( 12900000000000000000000 , binary=False) =='12.9 ZB')
    assert(friendly_bytes( 17200000000000000000000 , binary=False) =='17.2 ZB')
    assert(friendly_bytes( 21500000000000000000000 , binary=False) =='21.5 ZB')
    assert(friendly_bytes( 25800000000000000000000 , binary=False) =='25.8 ZB')
    assert(friendly_bytes( 0 , binary=False) =='0 B')
    assert(friendly_bytes( 1000000000000000000000000 , binary=False) =='1.0 YB')
    assert(friendly_bytes( 2000000000000000000000000 , binary=False) =='2.0 YB')
    assert(friendly_bytes( 3000000000000000000000000 , binary=False) =='3.0 YB')
    assert(friendly_bytes( 4000000000000000000000000 , binary=False) =='4.0 YB')
    assert(friendly_bytes( 5000000000000000000000000 , binary=False) =='5.0 YB')
    assert(friendly_bytes( 6000000000000000000000000 , binary=False) =='6.0 YB')
    assert(friendly_bytes( 0 , binary=False) =='0 B')
    assert(friendly_bytes( 51000000000000000000000000 , binary=False) =='51.0 YB')
    assert(friendly_bytes( 102000000000000000000000000 , binary=False) =='102.0 YB')
    assert(friendly_bytes( 153000000000000000000000000 , binary=False) =='153.0 YB')
    assert(friendly_bytes( 204000000000000000000000000 , binary=False) =='204.0 YB')
    assert(friendly_bytes( 255000000000000000000000000 , binary=False) =='255.0 YB')
    assert(friendly_bytes( 306000000000000000000000000 , binary=False) =='306.0 YB')