-- 1. Total and average daily energy consumption by zone
SELECT Zone, 
       SUM(EnergyConsumed_kWh) AS TotalConsumption,
       AVG(EnergyConsumed_kWh) AS AvgConsumption
FROM smartcityenergy
GROUP BY Zone;

-- 2. Top 5 highest energy-consuming consumers by type
SELECT ConsumerType, MeterID, 
       SUM(EnergyConsumed_kWh) AS TotalConsumption
FROM smartcityenergy
GROUP BY ConsumerType, MeterID
ORDER BY TotalConsumption DESC
LIMIT 5;

-- 3. Monthly trend of consumption across zones
SELECT MONTH(Date) AS Month, Zone, 
       SUM(EnergyConsumed_kWh) AS MonthlyConsumption
FROM smartcityenergy
GROUP BY Month, Zone
ORDER BY Month;

-- 4. Average cost per zone (EnergyConsumed × TariffRate)
SELECT Zone, 
       AVG(EnergyConsumed_kWh * TariffRate) AS AvgCost
FROM smartcityenergy
GROUP BY Zone;

-- 5. Meters with highest number of faults/outages
SELECT MeterID, 
       COUNT(*) AS FaultCount, 
       SUM(OutageMinutes) AS TotalOutage
FROM smartcityenergy
WHERE MeterStatus = 'Faulty' OR OutageMinutes > 0
GROUP BY MeterID
ORDER BY FaultCount DESC, TotalOutage DESC;

-- 6. Zones with lowest energy efficiency
SELECT Zone, 
       SUM(EnergyConsumed_kWh) AS TotalUsage,
       SUM(OutageMinutes) AS TotalOutage
FROM smartcityenergy
GROUP BY Zone
ORDER BY TotalUsage DESC, TotalOutage DESC;

-- 7. Peak usage patterns weekdays vs weekends
SELECT CASE 
         WHEN DAYOFWEEK(Date) IN (1,7) THEN 'Weekend'
         ELSE 'Weekday'
       END AS DayType,
       AVG(PeakUsage_kW) AS AvgPeakUsage
FROM smartcityenergy
GROUP BY DayType;
