-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2026 at 06:53 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smartcitydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `smartcityenergy`
--

CREATE TABLE `smartcityenergy` (
  `MeterID` int(3) DEFAULT NULL,
  `Zone` varchar(7) DEFAULT NULL,
  `ConsumerType` varchar(11) DEFAULT NULL,
  `Date` varchar(10) DEFAULT NULL,
  `EnergyConsumed_kWh` decimal(5,2) DEFAULT NULL,
  `PeakUsage_kW` decimal(4,2) DEFAULT NULL,
  `OutageMinutes` int(2) DEFAULT NULL,
  `MeterStatus` varchar(6) DEFAULT NULL,
  `TariffRate` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `smartcityenergy`
--

INSERT INTO `smartcityenergy` (`Zone`, `TotalConsumption`, `AvgConsumption`) VALUES
('Central', 4803.60, 114.371429),
('North', 5639.54, 115.092653),
('South', 6545.97, 110.948644);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

CREATE TABLE `smartcityenergy` (
  `MeterID` int(3) DEFAULT NULL,
  `Zone` varchar(7) DEFAULT NULL,
  `ConsumerType` varchar(11) DEFAULT NULL,
  `Date` varchar(10) DEFAULT NULL,
  `EnergyConsumed_kWh` decimal(5,2) DEFAULT NULL,
  `PeakUsage_kW` decimal(4,2) DEFAULT NULL,
  `OutageMinutes` int(2) DEFAULT NULL,
  `MeterStatus` varchar(6) DEFAULT NULL,
  `TariffRate` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `smartcityenergy`
--

INSERT INTO `smartcityenergy` (`ConsumerType`, `MeterID`, `TotalConsumption`) VALUES
('Industrial', 221, 199.73),
('Residential', 229, 199.63),
('Commercial', 166, 197.27),
('Residential', 167, 197.12),
('Commercial', 119, 194.77),
('Commercial', 128, 191.28),
('Industrial', 205, 190.54),
('Residential', 145, 188.37),
('Commercial', 149, 188.36),
('Residential', 218, 188.13),
('Industrial', 185, 186.49),
('Residential', 223, 184.89),
('Industrial', 140, 184.27),
('Residential', 242, 182.46),
('Residential', 104, 179.47),
('Industrial', 171, 178.42),
('Residential', 219, 178.09),
('Residential', 141, 177.34),
('Commercial', 243, 176.80),
('Industrial', 100, 176.34),
('Residential', 225, 176.30),
('Industrial', 161, 176.24),
('Residential', 138, 175.60),
('Residential', 109, 175.18),
('Commercial', 212, 174.21),
('Industrial', 122, 173.64),
('Residential', 107, 172.54),
('Residential', 181, 169.86),
('Commercial', 235, 169.34),
('Commercial', 234, 168.42),
('Commercial', 201, 167.32),
('Commercial', 113, 164.09),
('Commercial', 132, 163.98),
('Industrial', 220, 163.66),
('Commercial', 129, 163.01),
('Commercial', 249, 162.48),
('Industrial', 196, 162.10),
('Residential', 217, 161.20),
('Residential', 178, 160.85),
('Residential', 155, 160.55),
('Industrial', 239, 158.99),
('Residential', 200, 158.04),
('Commercial', 165, 157.05),
('Residential', 179, 156.83),
('Residential', 118, 153.26),
('Industrial', 116, 153.21),
('Residential', 175, 153.11),
('Industrial', 230, 152.73),
('Residential', 103, 148.79),
('Residential', 173, 146.93),
('Industrial', 123, 146.36),
('Industrial', 211, 145.33),
('Industrial', 197, 140.97),
('Commercial', 195, 138.81),
('Residential', 105, 137.21),
('Residential', 192, 136.99),
('Residential', 158, 136.41),
('Residential', 168, 135.76),
('Residential', 226, 135.20),
('Residential', 222, 132.70),
('Residential', 227, 132.46),
('Industrial', 130, 132.33),
('Commercial', 131, 131.29),
('Residential', 184, 129.77),
('Residential', 156, 124.83),
('Industrial', 124, 121.36),
('Residential', 153, 120.38),
('Commercial', 144, 118.87),
('Industrial', 244, 118.60),
('Residential', 136, 117.11),
('Residential', 114, 116.96),
('Commercial', 237, 116.49),
('Commercial', 231, 116.24),
('Industrial', 236, 115.45),
('Industrial', 117, 114.54),
('Residential', 193, 112.58),
('Residential', 233, 110.33),
('Residential', 216, 109.90),
('Commercial', 240, 109.64),
('Commercial', 121, 108.52),
('Commercial', 125, 107.65),
('Commercial', 151, 107.25),
('Residential', 170, 107.02),
('Industrial', 232, 105.91),
('Commercial', 177, 102.93),
('Commercial', 172, 102.35),
('Commercial', 101, 99.90),
('Industrial', 143, 99.63),
('Industrial', 112, 97.17),
('Industrial', 146, 96.44),
('Residential', 188, 95.30),
('Residential', 204, 93.91),
('Residential', 215, 92.62),
('Commercial', 152, 91.28),
('Commercial', 198, 88.95),
('Residential', 159, 86.98),
('Industrial', 115, 86.00),
('Commercial', 248, 82.56),
('Industrial', 120, 81.88),
('Commercial', 190, 81.04),
('Industrial', 228, 80.67),
('Industrial', 213, 80.38),
('Residential', 126, 77.03),
('Residential', 111, 76.73),
('Residential', 102, 76.64),
('Residential', 199, 76.42),
('Residential', 139, 76.26),
('Residential', 127, 74.90),
('Industrial', 160, 73.81),
('Residential', 207, 70.89),
('Commercial', 157, 69.76),
('Residential', 214, 69.69),
('Commercial', 108, 69.69),
('Commercial', 142, 67.43),
('Commercial', 180, 67.22),
('Industrial', 182, 64.43),
('Residential', 183, 63.18),
('Commercial', 162, 62.88),
('Industrial', 110, 62.65),
('Commercial', 187, 62.55),
('Commercial', 163, 60.88),
('Commercial', 106, 60.58),
('Residential', 208, 60.32),
('Residential', 206, 59.81),
('Industrial', 202, 59.19),
('Residential', 176, 58.86),
('Commercial', 209, 55.10),
('Industrial', 247, 54.56),
('Industrial', 135, 53.61),
('Commercial', 147, 52.89),
('Commercial', 241, 51.93),
('Commercial', 203, 51.79),
('Industrial', 224, 48.30),
('Residential', 148, 42.14),
('Industrial', 150, 40.20),
('Industrial', 154, 39.24),
('Industrial', 164, 38.83),
('Residential', 210, 36.52),
('Commercial', 169, 35.97),
('Residential', 191, 33.90),
('Industrial', 186, 33.40),
('Residential', 246, 30.66),
('Residential', 174, 30.57),
('Residential', 194, 28.08),
('Commercial', 133, 27.04),
('Industrial', 189, 24.13),
('Industrial', 245, 22.64),
('Residential', 238, 21.95),
('Industrial', 137, 21.71),
('Residential', 134, 21.66);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2026 at 06:52 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smartcitydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `smartcityenergy`
--

CREATE TABLE `smartcityenergy` (
  `MeterID` int(3) DEFAULT NULL,
  `Zone` varchar(7) DEFAULT NULL,
  `ConsumerType` varchar(11) DEFAULT NULL,
  `Date` varchar(10) DEFAULT NULL,
  `EnergyConsumed_kWh` decimal(5,2) DEFAULT NULL,
  `PeakUsage_kW` decimal(4,2) DEFAULT NULL,
  `OutageMinutes` int(2) DEFAULT NULL,
  `MeterStatus` varchar(6) DEFAULT NULL,
  `TariffRate` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `smartcityenergy`
--

INSERT INTO `smartcityenergy` (`Month`, `Zone`, `MonthlyConsumption`) VALUES
(1, 'Central', 4803.60),
(1, 'North', 5639.54),
(1, 'South', 6545.97);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2026 at 06:52 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smartcitydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `smartcityenergy`
--

CREATE TABLE `smartcityenergy` (
  `MeterID` int(3) DEFAULT NULL,
  `Zone` varchar(7) DEFAULT NULL,
  `ConsumerType` varchar(11) DEFAULT NULL,
  `Date` varchar(10) DEFAULT NULL,
  `EnergyConsumed_kWh` decimal(5,2) DEFAULT NULL,
  `PeakUsage_kW` decimal(4,2) DEFAULT NULL,
  `OutageMinutes` int(2) DEFAULT NULL,
  `MeterStatus` varchar(6) DEFAULT NULL,
  `TariffRate` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `smartcityenergy`
--

INSERT INTO `smartcityenergy` (`Zone`, `AvgCost`) VALUES
('Central', 773.926905),
('North', 809.959796),
('South', 804.755593);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2026 at 06:51 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smartcitydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `smartcityenergy`
--

CREATE TABLE `smartcityenergy` (
  `MeterID` int(3) DEFAULT NULL,
  `Zone` varchar(7) DEFAULT NULL,
  `ConsumerType` varchar(11) DEFAULT NULL,
  `Date` varchar(10) DEFAULT NULL,
  `EnergyConsumed_kWh` decimal(5,2) DEFAULT NULL,
  `PeakUsage_kW` decimal(4,2) DEFAULT NULL,
  `OutageMinutes` int(2) DEFAULT NULL,
  `MeterStatus` varchar(6) DEFAULT NULL,
  `TariffRate` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `smartcityenergy`
--

INSERT INTO `smartcityenergy` (`MeterID`, `FaultCount`, `TotalOutage`) VALUES
(191, 1, 60),
(146, 1, 59),
(181, 1, 59),
(171, 1, 56),
(101, 1, 56),
(215, 1, 56),
(224, 1, 56),
(204, 1, 55),
(197, 1, 55),
(221, 1, 55),
(140, 1, 54),
(175, 1, 54),
(203, 1, 53),
(176, 1, 53),
(202, 1, 52),
(149, 1, 52),
(102, 1, 52),
(199, 1, 52),
(136, 1, 52),
(160, 1, 52),
(151, 1, 51),
(128, 1, 51),
(233, 1, 51),
(138, 1, 50),
(169, 1, 50),
(147, 1, 49),
(243, 1, 49),
(100, 1, 49),
(106, 1, 48),
(145, 1, 48),
(110, 1, 47),
(141, 1, 46),
(205, 1, 46),
(223, 1, 46),
(192, 1, 46),
(121, 1, 45),
(212, 1, 44),
(206, 1, 44),
(231, 1, 43),
(208, 1, 43),
(117, 1, 42),
(142, 1, 42),
(239, 1, 42),
(184, 1, 42),
(168, 1, 41),
(209, 1, 41),
(186, 1, 40),
(234, 1, 40),
(172, 1, 40),
(241, 1, 40),
(227, 1, 39),
(182, 1, 39),
(190, 1, 39),
(167, 1, 39),
(153, 1, 39),
(122, 1, 38),
(132, 1, 38),
(120, 1, 38),
(232, 1, 38),
(124, 1, 37),
(119, 1, 37),
(193, 1, 37),
(173, 1, 36),
(229, 1, 36),
(143, 1, 36),
(144, 1, 36),
(200, 1, 36),
(116, 1, 35),
(238, 1, 35),
(207, 1, 35),
(148, 1, 34),
(188, 1, 34),
(244, 1, 33),
(118, 1, 33),
(228, 1, 32),
(103, 1, 32),
(225, 1, 32),
(159, 1, 31),
(134, 1, 30),
(189, 1, 29),
(177, 1, 29),
(114, 1, 27),
(240, 1, 27),
(210, 1, 26),
(218, 1, 26),
(180, 1, 26),
(158, 1, 26),
(127, 1, 26),
(170, 1, 25),
(247, 1, 25),
(196, 1, 24),
(163, 1, 23),
(156, 1, 23),
(109, 1, 23),
(113, 1, 23),
(115, 1, 22),
(131, 1, 21),
(179, 1, 21),
(222, 1, 21),
(217, 1, 21),
(248, 1, 20),
(183, 1, 19),
(161, 1, 19),
(164, 1, 18),
(246, 1, 17),
(130, 1, 16),
(187, 1, 16),
(104, 1, 16),
(126, 1, 15),
(129, 1, 15),
(211, 1, 14),
(108, 1, 14),
(107, 1, 13),
(139, 1, 12),
(112, 1, 12),
(105, 1, 12),
(198, 1, 11),
(216, 1, 11),
(137, 1, 11),
(154, 1, 10),
(195, 1, 9),
(135, 1, 9),
(249, 1, 8),
(235, 1, 7),
(236, 1, 7),
(237, 1, 7),
(174, 1, 7),
(162, 1, 6),
(178, 1, 6),
(213, 1, 6),
(111, 1, 6),
(194, 1, 5),
(155, 1, 5),
(214, 1, 5),
(226, 1, 4),
(242, 1, 4),
(125, 1, 4),
(152, 1, 4),
(185, 1, 4),
(219, 1, 3),
(220, 1, 3),
(165, 1, 3),
(150, 1, 3),
(166, 1, 3),
(201, 1, 3),
(133, 1, 2),
(123, 1, 1),
(157, 1, 1),
(245, 1, 1),
(230, 1, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2026 at 06:50 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smartcitydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `smartcityenergy`
--

CREATE TABLE `smartcityenergy` (
  `MeterID` int(3) DEFAULT NULL,
  `Zone` varchar(7) DEFAULT NULL,
  `ConsumerType` varchar(11) DEFAULT NULL,
  `Date` varchar(10) DEFAULT NULL,
  `EnergyConsumed_kWh` decimal(5,2) DEFAULT NULL,
  `PeakUsage_kW` decimal(4,2) DEFAULT NULL,
  `OutageMinutes` int(2) DEFAULT NULL,
  `MeterStatus` varchar(6) DEFAULT NULL,
  `TariffRate` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `smartcityenergy`
--

INSERT INTO `smartcityenergy` (`Zone`, `TotalUsage`, `TotalOutage`) VALUES
('South', 6545.97, 1781),
('North', 5639.54, 1433),
('Central', 4803.60, 1210);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2026 at 06:48 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smartcitydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `smartcityenergy`
--

CREATE TABLE `smartcityenergy` (
  `MeterID` int(3) DEFAULT NULL,
  `Zone` varchar(7) DEFAULT NULL,
  `ConsumerType` varchar(11) DEFAULT NULL,
  `Date` varchar(10) DEFAULT NULL,
  `EnergyConsumed_kWh` decimal(5,2) DEFAULT NULL,
  `PeakUsage_kW` decimal(4,2) DEFAULT NULL,
  `OutageMinutes` int(2) DEFAULT NULL,
  `MeterStatus` varchar(6) DEFAULT NULL,
  `TariffRate` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `smartcityenergy`
--

INSERT INTO `smartcityenergy` (`DayType`, `AvgPeakUsage`) VALUES
('Weekday', 14.542455),
('Weekend', 14.992750);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
