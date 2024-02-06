-- ranks country origins of bands, ordered
-- by the number of (non-unique) fans
SELECT origin, SUM(fans) AS _fans
FROM metal_bands
GROUP BY origin
ORDER BY _fans DESC;