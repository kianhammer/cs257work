--Strongest Earthquakes that occured on January 1st 2023:
SELECT * FROM earthquakes WHERE quakedate = '2023-01-01' ORDER BY mag DESC;

--Deepest Earthquakes In South America:
SELECT * FROM earthquakes WHERE longitude BETWEEN -82 AND -32 AND latitude BETWEEN -55 AND 13
ORDER BY quakedepth DESC;

--Shallow but powerful earthquakes sorted by date:
SELECT * FROM earthquakes WHERE quakedepth < 20 AND mag > 5 ORDER BY quakedate DESC;
