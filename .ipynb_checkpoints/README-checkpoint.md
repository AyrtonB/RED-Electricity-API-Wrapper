# The REData API Wrapper

<br>

This module creates a Python wrapper for the new Red Eléctrica de España electricity data API. Currently the API only has a few streams up and running, for this reason the wrapper has been designed to be highly generalisable as new streams are added.

<br>

### Imports

```python
from REData import REData
```

<br>

### Querying the API

There is a standardised API to query any of the data streams and retrieve a dataframe of the results

```python
category = 'balance' 
widget = 'balance-electrico' 

start_date = '2019-01-01T00:00'
end_date = '2019-01-12T00:00'
time_trunc = 'day'

RED_stream = REData(category, widget)
df = RED_stream.query_REData(start_date, end_date, time_trunc)

df.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Hydro</th>
      <th>Wind</th>
      <th>Solar photovoltaic</th>
      <th>Thermal solar</th>
      <th>Hydroeolian</th>
      <th>Other renewables</th>
      <th>Renewable waste</th>
      <th>Renewable generation</th>
      <th>Pumped storage</th>
      <th>Nuclear</th>
      <th>Combined cycle</th>
      <th>Coal</th>
      <th>Fuel + Gas</th>
      <th>Cogeneration</th>
      <th>Non-renewable waste</th>
      <th>Non-renewable generation</th>
      <th>Pumped storage consumption</th>
      <th>Cross-border exchange balance</th>
      <th>Demand at busbars</th>
    </tr>
    <tr>
      <th>datetime</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2019-01-01 00:00:00+01:00</th>
      <td>53722.120</td>
      <td>78024.599</td>
      <td>19037.740</td>
      <td>7457.265</td>
      <td>16.410</td>
      <td>8432.490</td>
      <td>2661.1455</td>
      <td>169351.7695</td>
      <td>825.588</td>
      <td>145065.884</td>
      <td>102405.013</td>
      <td>46490.345</td>
      <td>15296.578</td>
      <td>65180.123</td>
      <td>5881.8945</td>
      <td>381145.4255</td>
      <td>-8556.568</td>
      <td>41009.179</td>
      <td>582949.806</td>
    </tr>
    <tr>
      <th>2019-01-02 00:00:00+01:00</th>
      <td>61294.768</td>
      <td>195509.161</td>
      <td>18819.394</td>
      <td>7592.590</td>
      <td>13.481</td>
      <td>8440.714</td>
      <td>2627.5065</td>
      <td>294297.6145</td>
      <td>5146.511</td>
      <td>144935.411</td>
      <td>101005.855</td>
      <td>65173.359</td>
      <td>16756.131</td>
      <td>81637.709</td>
      <td>6193.4215</td>
      <td>420848.3975</td>
      <td>-13556.968</td>
      <td>40610.363</td>
      <td>742199.407</td>
    </tr>
    <tr>
      <th>2019-01-03 00:00:00+01:00</th>
      <td>82981.951</td>
      <td>111015.260</td>
      <td>16813.988</td>
      <td>6419.244</td>
      <td>5.994</td>
      <td>9215.684</td>
      <td>2605.2615</td>
      <td>229057.3825</td>
      <td>9632.887</td>
      <td>147271.468</td>
      <td>143640.176</td>
      <td>82277.309</td>
      <td>18236.381</td>
      <td>88044.425</td>
      <td>6904.3125</td>
      <td>496006.9585</td>
      <td>204.628</td>
      <td>62495.994</td>
      <td>787764.963</td>
    </tr>
    <tr>
      <th>2019-01-04 00:00:00+01:00</th>
      <td>94301.940</td>
      <td>79621.037</td>
      <td>18271.437</td>
      <td>6109.126</td>
      <td>4.697</td>
      <td>9434.681</td>
      <td>2633.5645</td>
      <td>210376.4825</td>
      <td>10894.167</td>
      <td>150097.415</td>
      <td>182524.379</td>
      <td>94253.889</td>
      <td>18796.975</td>
      <td>90680.246</td>
      <td>6955.1415</td>
      <td>554202.2125</td>
      <td>369.975</td>
      <td>31061.365</td>
      <td>796010.035</td>
    </tr>
    <tr>
      <th>2019-01-05 00:00:00+01:00</th>
      <td>58822.692</td>
      <td>116501.377</td>
      <td>19538.384</td>
      <td>7205.657</td>
      <td>14.331</td>
      <td>9411.312</td>
      <td>2678.8940</td>
      <td>214172.6470</td>
      <td>256.618</td>
      <td>150843.671</td>
      <td>117718.032</td>
      <td>86777.689</td>
      <td>16965.448</td>
      <td>85813.533</td>
      <td>6698.1630</td>
      <td>465073.1540</td>
      <td>-1153.945</td>
      <td>42937.795</td>
      <td>721029.651</td>
    </tr>
  </tbody>
</table>
    
<br>
     
Sometimes you may want to access the raw response so that functionality has been made available as well

```python
r = RED_stream.make_request(start_date, end_date, time_trunc)
```

<br>

Additionaly, rather than re-initialising the class each time you want to query a new set of data you could instead simply update the stream info</p>

```python
category = 'demanda'
widget = 'evolucion'

RED_stream.update_stream(category, widget)
df = RED_stream.query_REData(start_date, end_date, time_trunc)

df.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Demand</th>
    </tr>
    <tr>
      <th>datetime</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2019-01-01 00:00:00+01:00</th>
      <td>582949.806</td>
    </tr>
    <tr>
      <th>2019-01-02 00:00:00+01:00</th>
      <td>742199.407</td>
    </tr>
    <tr>
      <th>2019-01-03 00:00:00+01:00</th>
      <td>787764.963</td>
    </tr>
    <tr>
      <th>2019-01-04 00:00:00+01:00</th>
      <td>796010.035</td>
    </tr>
    <tr>
      <th>2019-01-05 00:00:00+01:00</th>
      <td>721029.651</td>
    </tr>
  </tbody>
</table>