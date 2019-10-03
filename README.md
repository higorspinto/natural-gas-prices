# Natural Gas Price

Henry Hub Natural Gas Spot Price dataset including daily, monthly and annual.

## Data

## Source

https://www.eia.gov/dnav/ng/hist/rngwhhdm.htm

## Preparation

You can run the script yourself to update the data. The files are created in the data directory.

```
python data_wrangling_ngp.py
```

### Dependencies

Dependencies can be installed using pip install and the requirements.txt file in the scprits directory.

```
pip install requirements.txt
```

## Visualization

The file ngp_visualization.html produces a visualization from static files created by plot_ngp_data.py using matplotlib.
As the graphics are in static files, you need to run the script to update the images. The files are created in the static directory.

```
python plot_ngp_data.py
```
