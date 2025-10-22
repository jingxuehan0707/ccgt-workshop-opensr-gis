import psycopg2
import geopandas as gpd
import rasterio
from rasterio.io import MemoryFile
from sqlalchemy import create_engine
import numpy as np
from typing import Optional


class PostGISConnection:
    """
    A class to handle PostgreSQL database connections with PostGIS extension.
    Provides methods to export spatial data as shapefiles and GeoTIFFs.
    """
    
    def __init__(self, user: str = 'gisadmin', host: str = '127.0.0.1', 
                 port: int = 5432, database: str = 'sedaag', password: Optional[str] = None):
        """
        Initialize the PostgreSQL connection.
        
        Parameters:
        -----------
        user : str
            Database username (default: 'gisadmin')
        host : str
            Database host (default: '127.0.0.1')
        port : int
            Database port (default: 5432)
        database : str
            Database name (default: 'sedaag')
        password : str, optional
            Database password (if None, will attempt connection without password)
        """
        self.user = user
        self.host = host
        self.port = port
        self.database = database
        self.password = password
        
        # Create connection string for psycopg2
        if password:
            self.conn_string = f"dbname='{database}' user='{user}' host='{host}' port='{port}' password='{password}'"
            self.uri = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        else:
            self.conn_string = f"dbname='{database}' user='{user}' host='{host}' port='{port}'"
            self.uri = f"postgresql://{user}@{host}:{port}/{database}"
        
        self.connection = None
        self.engine = None
    
    def connect(self):
        """Establish connection to the database."""
        try:
            self.connection = psycopg2.connect(self.conn_string)
            self.engine = create_engine(self.uri)
            print(f"Successfully connected to database '{self.database}'")
            return self.connection
        except Exception as e:
            print(f"Error connecting to database: {e}")
            raise
    
    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed")
    
    def export_shapefile(self, sql_query: str, output_path: str, geom_col: str = 'geom'):
        """
        Export the result of a SQL query to a shapefile.
        
        Parameters:
        -----------
        sql_query : str
            SQL query to execute. Must return geometry data.
        output_path : str
            Path where the shapefile will be saved (e.g., 'output.shp')
        geom_col : str
            Name of the geometry column (default: 'geom')
        
        Returns:
        --------
        str
            Path to the exported shapefile
        """
        try:
            # Ensure connection is established
            if not self.engine:
                self.connect()
            
            # Read spatial data using GeoPandas
            gdf = gpd.read_postgis(sql_query, self.engine, geom_col=geom_col)
            
            # Export to shapefile
            gdf.to_file(output_path, driver='ESRI Shapefile')
            print(f"Shapefile exported successfully to: {output_path}")
            return output_path
            
        except Exception as e:
            print(f"Error exporting shapefile: {e}")
            raise
    
    def export_geotiff(self, sql_query: str, output_path: str, 
                       rast_col: str = 'rast', band: int = 1):
        """
        Export the result of a SQL query containing raster data to a GeoTIFF.
        
        Parameters:
        -----------
        sql_query : str
            SQL query to execute. Must return raster data in PostGIS format.
            Example: "SELECT ST_AsGDALRaster(rast, 'GTiff') as rast FROM raster_table WHERE id = 1"
        output_path : str
            Path where the GeoTIFF will be saved (e.g., 'output.tif')
        rast_col : str
            Name of the raster column (default: 'rast')
        band : int
            Band number to export (default: 1)
        
        Returns:
        --------
        str
            Path to the exported GeoTIFF
        """
        try:
            # Ensure connection is established
            if not self.connection:
                self.connect()
            
            cursor = self.connection.cursor()
            
            # Execute query to get raster data
            cursor.execute(sql_query)
            result = cursor.fetchone()
            
            if result is None:
                raise ValueError("Query returned no results")
            
            # Get the raster bytes (assuming query returns GDAL raster format)
            raster_bytes = bytes(result[0])
            
            # Write to file
            with open(output_path, 'wb') as f:
                f.write(raster_bytes)
            
            cursor.close()
            print(f"GeoTIFF exported successfully to: {output_path}")
            return output_path
            
        except Exception as e:
            print(f"Error exporting GeoTIFF: {e}")
            raise
    
    def execute_query(self, sql_query: str, fetch_results: bool = True):
        """
        Execute a SQL query and return results.
        
        Parameters:
        -----------
        sql_query : str
            SQL query to execute
        fetch_results : bool
            Whether to fetch and return results (default: True)
            Set to False for commands like SET, CREATE, etc.
        
        Returns:
        --------
        list or None
            Query results if fetch_results=True, None otherwise
        """
        try:
            if not self.connection:
                self.connect()
            
            cursor = self.connection.cursor()
            cursor.execute(sql_query)
            
            if fetch_results:
                results = cursor.fetchall()
                cursor.close()
                return results
            else:
                self.connection.commit()
                cursor.close()
                return None
            
        except Exception as e:
            print(f"Error executing query: {e}")
            raise
    
    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


# Example usage:
if __name__ == "__main__":
    # Using context manager (recommended)
    with PostGISConnection(user='gisadmin', host='127.0.0.1', port=5432, database='sedaag') as db:
        # Export LA county boundary shapefile
        # sql_vector = "SELECT * FROM county WHERE \"NAME\" = 'Los Angeles'"
        # db.export_shapefile(sql_vector, "data/vector/la_county_boundary.shp", geom_col='geometry')

        # Export CA Census Tracts shapefile
        sql_vector = "SELECT * FROM tract WHERE \"STATEFP\" = '06'"
        db.export_shapefile(sql_vector, "data/vector/ca_census_tracts.shp", geom_col='geometry')

        # Export GeoTIFF - clip whp raster by California boundary
        # Enable GDAL drivers first
        # db.execute_query("SET postgis.gdal_enabled_drivers = 'ENABLE_ALL';", fetch_results=False)
        # db.execute_query("SET postgis.enable_outdb_rasters = True;", fetch_results=False)
        
        # sql_raster = """
        # SELECT ST_AsTIFF(ST_Clip(whp.rast, ST_Transform(state.geometry, 5070))) as rast
        # FROM whp, state
        # WHERE state."NAME" = 'California'
        # AND ST_Intersects(whp.rast, ST_Transform(state.geometry, 5070))
        # """
        # db.export_geotiff(sql_raster, "data/raster/ca_whp.tif")

