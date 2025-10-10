# ccgt-workshop-opensr-gis
Why do we want to use open source programming

# Research question
* How much the popolation and building are exposed to wildfire in Los Angeles County?

# Quick start
In this section we will show case simple demo
* read vector
* read raster
* visualize the both vector and raster in a map
It is intended to give student a overview how the open source gis programming looks like

# Repeat the Quick start with help of GenAI
I will show how to use genai feature to write the code above. i will also use genai to instruct the following section across the workshop.

# Vector -> Socioeconomic Layers
Dataset used in this section
* LA county boundary dataset
* CA census Tract dataset
* CA building footprint

In this section we will introduce geopandas, and demostrate how to
* read LA county boundary from shp, duckdb, or download from openstreetmap api.
* explain the geopandas dataframe object
* select LA data by attribute, using GEOID
* select LA data by location, using LA county boundary
* export final data
* visualize final data using leafmap python package

# Raster -> Wildfire Risk Layers
Dataset used in this section
* Wildfire Hazard Potential (WHP) dataset. 1,2,3,4,5 represents very low, low, moderate, high, very high

In this section we will introduce rasterio, and demostrate how to
* read data and explain the rasterio data object
* clip the raster using LA county boundary

# Spatial analysis -> quantify the exposure and wildfire risk
In this section we will show student how to use both vector data and raster data to quantify the wildfire exposure and wildfire risk.
We will quantify the following using geopandas, raster, and rasterstats
* The population exposure in each census tract. using population density from census tract multiply by the census tract area overlapped with wildfire burned area.
* The building footprint exposure in each census tract. calculate the percentage of building exposed to wildfire burned area within each cenesus tract. % = number of building exposed/total number of building * 100
* Quantify the building WHP risk. summarize the WHP class majoriry of each building using summarize whp within each building footprint. join the calculated wildfire whp risk class back to original building footprint for future visualization

# Visualization and web map
Demonstrate how to display our final result using leafmap.
* display raw data
* display data using multiple symbology
* display raster data
* display map in 3d mode