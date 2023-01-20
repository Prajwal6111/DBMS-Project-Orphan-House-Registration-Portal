-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 20, 2023 at 06:03 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `orphan`
--

-- --------------------------------------------------------

--
-- Table structure for table `addorphanhouseuser`
--

CREATE TABLE `addorphanhouseuser` (
  `id` int(11) NOT NULL,
  `Ocode` varchar(20) NOT NULL,
  `ohname` varchar(50) NOT NULL,
  `ohdistrict` varchar(50) NOT NULL,
  `ohstate` varchar(50) NOT NULL,
  `ohpin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `addorphanhouseuser`
--

INSERT INTO `addorphanhouseuser` (`id`, `Ocode`, `ohname`, `ohdistrict`, `ohstate`, `ohpin`) VALUES
(3, 'NEWOH01', 'my new orphan house', 'chitradurga', 'karnataka', 577004),
(4, 'ABC121', 'akarshoh', 'CBPUR', 'karnataka', 123456);

-- --------------------------------------------------------

--
-- Table structure for table `orphanhouseuser`
--

CREATE TABLE `orphanhouseuser` (
  `id` int(11) NOT NULL,
  `Ocode` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orphanhouseuser`
--

INSERT INTO `orphanhouseuser` (`id`, `Ocode`, `email`, `password`) VALUES
(10, 'NEWOH01', 'prajwalmh13@gmail.com', 'pbkdf2:sha256:260000$nGkfjX1VgKsGZBw4$18a3db3bc6e1d7eca7b957f06c32d03da82f07ea944803ef8b9fdb38c3973856'),
(11, 'ABC121', 'akarshpradeep8551@gmail.com', 'pbkdf2:sha256:260000$jTmT8KtrAFaFSdSm$055225e341f1f2caed463b46a49b175aa75f87f989c06a13ed7f13f9c881f81b'),
(12, 'BLR01', 'prajwalmh6111@gmail.com', 'pbkdf2:sha256:260000$a9YD09Z1o53AYTEG$0894277f0c7f6eb29cdd228fd32fd6c610338bd6663190aa4b7aaa2e42254c2e'),
(13, 'NEWOH01', 'prajwalmh12@gmail.com', 'pbkdf2:sha256:260000$5u9O3BIr5dxwkRl9$a226d43c236783eb3797c24ac736c7ef1fb7c5feb84562672e717ee0d82cb0d3');

-- --------------------------------------------------------

--
-- Table structure for table `regorp`
--

CREATE TABLE `regorp` (
  `id` int(11) NOT NULL,
  `oname` varchar(20) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `uaddress` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `regorp`
--

INSERT INTO `regorp` (`id`, `oname`, `age`, `gender`, `uaddress`) VALUES
(4, 'Akarsh', 19, 'M', 'DSATM'),
(5, 'raj', 14, 'm', 'DSU'),
(6, 'jhon', 21, 'M', 'DSATM'),
(7, 'kapoor', 20, 'M', 'vajaralli');

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `orp` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `dob` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `orp`, `email`, `dob`) VALUES
(5, 'qwerty', 'prajwalmh12@gmail.com', 'pbkdf2:sha256:260000$O96IIicXH2VeTIsg$9e4984194fe5ce8d64856827a5a522551662597c51d8bb4abcd63cc16819549d');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addorphanhouseuser`
--
ALTER TABLE `addorphanhouseuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Ocode` (`Ocode`);

--
-- Indexes for table `orphanhouseuser`
--
ALTER TABLE `orphanhouseuser`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `regorp`
--
ALTER TABLE `regorp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `orp` (`orp`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addorphanhouseuser`
--
ALTER TABLE `addorphanhouseuser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `orphanhouseuser`
--
ALTER TABLE `orphanhouseuser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `regorp`
--
ALTER TABLE `regorp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
