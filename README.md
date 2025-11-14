# Open Source GIS Programming with Python: An Application of Wildfire Risk Assessment

Welcome to the Clemson Center for Geospatial Technology (CCGT) workshop!

<a target="_blank" href="https://colab.research.google.com/github/jingxuehan0707/ccgt-workshop-opensr-gis/blob/main/open-source-gis-with-python.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## About Me: Harvey (Xuehan) Jing

* **Ph.D. Student**, Civil Engineering @ Clemson University
* **Certified GIS Professional** (GISP)
* **10+ years** of professional GIS experience (Esri, Hikvision)
* **LinkedIn**: linkedin.com/in/jingxuehan0707
* **Hobby:** Hiking & music composition

## Why Open Source GIS?

* **Capability:** Perform powerful analysis without expensive licenses.
* **Community:** Get support from a massive global community of developers.
    - https://github.com/opengeos
* **Customization:** Build and share your own tools and workflows.
* **GenAI:** Modern AI tools are built to write and explain this code, making it easier than ever to learn.

## You Will Learn

* The core "Vector + Raster" analysis workflow using Python.
* How to **read, filter, and join** vector data (polygons, lines) with **GeoPandas**.
* How to **clip and analyze** raster data (GeoTIFFs) with **Rasterio**.
* A powerful GIS technique: **Zonal Statistics** with **Rasterstats**.
* How to create interactive web maps with **Leafmap** and `.explore()`.

### 💡 Tips for Success

* **Focus on concepts**, not memorizing code syntax.
* **Watch how I use GenAI** throughout the workshop to write, debug, and explain code.

## Workshop Overview: An Application of Wildfire Risk Assessment

We will answer a practical question: **"What populations and infrastructure in LA County are at high risk for wildfires?"**

### Our Workflow:
1.  **Prepare Data:** Load LA County boundaries, census tracts, railways, and a wildfire hazard raster.
2.  **Process Vectors (GeoPandas):**
    * Spatially select railways inside LA County (`.intersects`).
    * Join population data to census tract polygons (`.merge`).
3.  **Process Rasters (Rasterio):**
    * Clip the statewide wildfire raster to the LA County boundary (`rasterio.mask.mask`).
4.  **Analyze Risk (Rasterstats):**
    * **Zonal Stats 1:** Calculate the *percent of high-risk land* in each census tract.
    * **Zonal Stats 2:** Calculate the *percent of high-risk land* along railway buffers.
5.  **Visualize (Leafmap):**
    * Create interactive choropleth maps to find the most vulnerable areas.

## Resources

* **Workshop Book:** [Introduction to GIS Programming: A Practical Python Guide to Open Source Geospatial Tools.](https://gispro.gishub.org/#introduction)
    > Wu, Q. (2025). Introduction to GIS Programming: A Practical Python Guide to Open Source Geospatial Tools. Independently published. ISBN 979-8286979455. https://amazon.com/dp/B0FFW34LL3