Here is the raw markdown for the cheatsheet, broken up by package as requested.

---

# Open Source GIS with Python: Cheatsheet

This cheatsheet summarizes the key functions and methods used in the workshop, categorized by their main purpose.

## Package: `geopandas`

| Purpose | Function / Method | Example | Explanation |
| :--- | :--- | :--- | :--- |
| Data Management | `gpd.read_file()` | `gpd.read_file("data/tracts.shp")` | Reads a vector file (Shapefile, GeoJSON, etc.) into a GeoDataFrame. |
| Data Management | `.to_crs()` | `gdf = gdf.to_crs(epsg=3857)` | Reprojects (transforms) a GeoDataFrame to a new Coordinate Reference System (CRS). |
| Data Management | `.merge()` | `gdf.merge(df, on='GISJOIN', how='left')` | Joins a GeoDataFrame with a standard DataFrame using a common column (like a SQL join). |
| Data Management | `.loc[]` (accessor) | `row = gdf.loc[0, 'COLUMN_NAME']` | Accesses a group of rows and columns by label(s) or a boolean array. |
| Data Management | `[]` (filtering) | `subset_gdf = gdf[gdf['POP'] > 1000]` | Selects a subset of rows based on an attribute condition (a boolean mask). |
| Analysis | `.intersects()` | `mask = gdf1.geometry.intersects(geom2)` | Performs a spatial query. Returns `True` for geometries in `gdf1` that intersect `geom2`. |
| Analysis | `.buffer()` | `gdf['geometry'] = gdf.geometry.buffer(270)` | Creates a buffer polygon around each geometry at a specified distance (in CRS units). |
| Analysis | `.centroid` (property) | `centroids = gdf.geometry.centroid` | Calculates the geometric center (centroid) of each geometry. |
| Analysis | `.dissolve()` | `single_geom_gdf = gdf.dissolve()` | Merges multiple geometries into a single feature, similar to "Dissolve" in desktop GIS. |
| Analysis | `.apply()` | `gdf['new_col'] = gdf.apply(my_func, axis=1)` | Applies a custom function (`my_func`) to every row (`axis=1`) to calculate new values. |
| Visualization | `.plot()` | `gdf.plot(column='POP_KM2', cmap='viridis')` | Creates a static map (using matplotlib) of the geometries. Can create choropleth maps. |
| Visualization | `.explore()` | `gdf.explore(column='WHP_PCT', cmap='Reds')` | Creates an interactive web map (using folium/leafmap) of the geometries. |

## Package: `pandas`

| Purpose | Function / Method | Example | Explanation |
| :--- | :--- | :--- | :--- |
| Data Management | `pd.read_csv()` | `pd.read_csv("data/table.csv")` | Reads a tabular CSV file into a standard DataFrame. |

## Package: `rasterio`

| Purpose | Function / Method | Example | Explanation |
| :--- | :--- | :--- | :--- |
| Data Management | `rasterio.open()` | `with rasterio.open("img.tif") as src:` | Opens a raster file (GeoTIFF) for reading or writing. Used with a `with` statement. |
| Data Management | `.meta` (property) | `meta = src.meta` | Accesses a raster's metadata (CRS, transform, count, data type, etc.). |
| Data Management | `.read()` | `data = src.read(1)` | Reads pixel data from a specific raster band (e.g., band 1) into a NumPy array. |
| Data Management | `.write()` | `dest.write(clipped_image)` | Writes a NumPy array to an open raster file (opened in `'w'` mode). |
| Analysis | `rasterio.mask.mask()` | `img, trans = mask(src, shapes, crop=True)` | Clips (masks) a raster (`src`) using a list of vector geometries (`shapes`). |
| Visualization | `rasterio.plot.show()` | `show(raster_array, transform=src.transform)` | Creates a static plot (using matplotlib) of a raster NumPy array. |

## Package: `rasterstats`

| Purpose | Function / Method | Example | Explanation |
| :--- | :--- | :--- | :--- |
| Analysis | `zonal_stats()` | `stats = zonal_stats(gdf, "img.tif", categorical=True)` | Calculates statistics from a raster for each vector polygon. `categorical=True` counts the pixels of each unique value (e.g., risk class) within each polygon. |

## Package: `leafmap`

| Purpose | Function / Method | Example | Explanation |
| :--- | :--- | :--- | :--- |
| Visualization | `leafmap.Map()` | `m = leafmap.Map(center=[y, x], zoom=10)` | Creates a new interactive map object to which layers can be added. |
| Visualization | `.add_gdf()` | `m.add_gdf(gdf, layer_name="Tracts")` | Adds a GeoDataFrame as a vector layer to an interactive map. |
| Visualization | `.add_raster()` | `m.add_raster("img.tif", colormap='terrain')` | Adds a GeoTIFF as a raster layer to an interactive map. |
| Visualization | `.add_data()` | `m.add_data(gdf, column='RISK', cmap='Reds')` | A powerful function to add vector data and automatically create a choropleth map. |
| Visualization | `.add_legend()` | `m.add_legend(title="Legend", colors=c, labels=l)` | Adds a custom color legend to the interactive map. |

## Package: `viewgeom` (CLI)

| Purpose | Function / Method | Example | Explanation |
| :--- | :--- | :--- | :--- |
| Visualization | `!viewgeom` (CLI) | `!viewgeom data/vector/la_county.shp` | Command Line Tool: Quickly previews vector data attributes and geometry in the terminal. |

## Package: `viewtif` (CLI)

| Purpose | Function / Method | Example | Explanation |
| :--- | :--- | :--- | :--- |
| Visualization | `!viewtif` (CLI) | `!viewtif data/raster/la_whp.tif` | Command Line Tool: Quickly previews raster metadata (CRS, bands, etc.) in the terminal. |