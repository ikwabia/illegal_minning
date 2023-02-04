//Adding my aoi shapefile and is repeated for all the three regions
var region = ee.FeatureCollection("users/Ikwabia/landuse");
Map.addLayer(region);
Map.centerObject(region,10);
var S2 = ee.ImageCollection("COPERNICUS/S2_SR");
var filtered = S2
       .filterDate('2020-01-01','2020-12-31')//changes the date for respective year
       .filterBounds(region)
       .filterMetadata('CLOUDY_PIXEL_PERCENTAGE','Less_than',1)
       .median();
       
//Color combination for natural color
Map.addLayer(filtered.clip(region),{min:0,max:2000,bands:(['B4','B3','B2'])});

//Determining Vegetation indices
var NIR = filtered.select('B8');
var RED = filtered.select('B4');
var NDVI = NIR.subtract(RED).divide(NIR.add(RED));
Map.addLayer(NDVI.clip(region));

var Vegetation = NDVI
Vegetation = ee.Image(1).mask(Vegetation.gte(0.3));
Map.addLayer(Vegetation.clip(region));

//calculating area of vegetation
var area_pxa = Vegetation.multiply(ee.Image.pixelArea())
         .reduceRegion(ee.Reducer.sum(),region,10,null,null,false,1e13)
         .get('constant');
         
         
area_pxa = ee.Number(area_pxa).divide(1e6);
print('Area using ee.Image.pixelArea(km2)',area_pxa);
print('Acres',area_pxa.multiply(247.1054));