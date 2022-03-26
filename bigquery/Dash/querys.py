

POPULATION_BOGOTA = """
SELECT population, longitude_centroid, latitude_centroid, geog
FROM `bigquery-public-data.worldpop.population_grid_1km`
WHERE country_name='Colombia'
AND (latitude_centroid>4.36 AND latitude_centroid<4.832)
AND (longitude_centroid<-73.947 AND longitude_centroid>-74.252)
AND last_updated ='2020-01-01'
"""

POPULATION_WORLD = """
SELECT country_name, population, longitude_centroid, latitude_centroid --, geog
FROM `bigquery-public-data.worldpop.population_grid_1km`
WHERE last_updated ='2020-01-01' AND country_name IS NOT NULL
"""

def population_by_country(country, last_updated='2020-01-01'):
    return f"""
    SELECT population, longitude_centroid, latitude_centroid, geog
    FROM `bigquery-public-data.worldpop.population_grid_1km`
    WHERE country_name='{country}' AND last_updated ='{last_updated}'
    """