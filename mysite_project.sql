-- phpMyAdmin SQL Dump
-- version 4.4.3
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 04, 2015 at 06:16 AM
-- Server version: 5.6.24
-- PHP Version: 5.6.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `personalwebsite`
--

-- --------------------------------------------------------

--
-- Table structure for table `mysite_project`
--

CREATE TABLE IF NOT EXISTS `mysite_project` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `tag` varchar(500) NOT NULL,
  `main_image` varchar(200) NOT NULL,
  `main_image_caption` varchar(400) NOT NULL,
  `folder` varchar(200) NOT NULL,
  `style` varchar(200) NOT NULL,
  `alt_text` varchar(500) NOT NULL,
  `link` varchar(500) NOT NULL,
  `display_rank` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `mysite_project`
--

INSERT INTO `mysite_project` (`id`, `name`, `tag`, `main_image`, `main_image_caption`, `folder`, `style`, `alt_text`, `link`, `display_rank`) VALUES
(1, 'DFC Query Builder', 'A mini-scale Database Engine', 'bptree.png', 'Indexing Using B+ Tree', 'dfc_query_builder', 'course', 'Screenshot of DFC Query Builder', 'https://github.com/Bug-Assassins/DFC_query_builder', 2),
(2, 'Web Service Retrieval', 'Search Engine for Web Services', 'vector.png', 'Vector Space Matching for Web Services', 'web_service_retrieval', 'course', 'Vector Space Method', 'https://github.com/Bug-Assassins/web_service_retrieval', 3),
(3, 'Chess Game', 'Java GUI Chess Game', 'game_in_progress.png', 'Chess Game in Progress', 'chess', 'course', 'Chess Game - Java GUI - Object Oriented', 'https://github.com/ashish1294/ChessOOP', 7),
(4, 'TAJ Defender', 'Sandboxing for C/C++ Codes', 'seccomp.gif', 'Linux SECCOMP - Secure Computing', 'taj_defender', 'course', 'C/C++ Sandbox', 'https://github.com/Bug-Assassins/TAJ-Defender', 15),
(5, 'FLINT & BLAS', 'Linear Algebra using BLAS', 'blas.jpg', 'Basic Linear Algebra Subroutine', 'flint', 'course', 'BLAS Image', 'https://github.com/Bug-Assassins/BLAS_Practice', 5),
(6, 'Galaxian', 'OpenGL based 2D shooting game', 'game_play.png', 'Galaxian Game in Progress', 'galaxian', 'course', 'Screenshot of the Game', 'https://github.com/Bug-Assassins/Galaxian', 6),
(7, 'Konnect', 'A mini-scale TCP/IP Stack', 'three_way.jpg', 'Three Way Handshaking Protocol', 'konnect', 'course', 'The TCP Implementation', 'https://github.com/Bug-Assassins/Konnect', 8),
(8, 'Digital Passbook', 'Android App for Bank Transactions', 'account_logo.png', 'Logo - Digital Passbook', 'digital_passbook', 'extra', 'Now maintain a passbook on mobile', 'https://github.com/ashish1294/DigitalPassbook', 9),
(9, 'Online Banking', 'Mini Scale Online Bank using PHP', 'home.png', 'Homepage of the Bank Website', 'online_banking', 'extra', 'Online Banking using PHP, HTML5, JS and CSS3', 'https://github.com/ashish1294/OnlineBankingPHP', 10),
(10, 'SGC APP', 'Android App for AAC Club, NITK', 'home.png', 'Home Activity of SGC App', 'sgc_app', 'extra', 'Star Gazing Club, NITK Surathkal', 'https://github.com/ashish1294/SGC-App', 11),
(11, 'CodeChef Code Now', 'Chrome Extension for Code-Chef', 'codechef.jpeg', 'Logo of Codechef', 'code_now', 'extra', 'Use your favorite IDE with CodeChef', 'https://github.com/ashish1294/code-now-CodeChef', 12),
(12, 'RDBMS Graph Storage', 'Graph Based Data Storage (RDBMS)', 'model.svg', 'Major components of the Graph Based Storage Engine', 'graph_storage_rdbms', 'course', 'RDBMS Graph Storage', 'https://github.com/Bug-Assassins/Relational-Graph-Database', 1),
(13, 'Drive Assist', 'Windows App for Road Safety', 'kinect.jpg', 'Microsoft Kinect v2 for Windows', 'drive_assist', 'extra', 'Drive Assist', 'https://drive.google.com/open?id=0B6A-3_6rwie9fkhLU04wbDFWREh0SlZBNkJlVXN6bURhRFNZWVRDNkFyeE5MM3JvOVFWaDQ&authuser=1', 4),
(14, 'Namma Bazaar', 'Super Market Management System', 'super1.jpg', 'Namma Bazar for Super Markets', 'namma_bazaar', 'course', 'Namma Bazaar', 'https://drive.google.com/folderview?id=0B6A-3_6rwie9fkNiNml1YUlzU3QydVFuZjhzNmdLM3FSTmszSGlOQVBrdmY5bzZJZUVCSjQ&usp=sharing', 13),
(15, 'Global Learning Factory', 'Service Search Engine for Disabled', 'screenshot.png', 'Screenshot of the Search Engine GUI', 'glf', 'extra', 'Global Learning Factory', 'https://drive.google.com/open?id=0B6A-3_6rwie9fnVTSEdRLWljb2JtSkNaaUdBdkVOVGtZNE1kM3RfeWxoMnlFQ2pISklldUU&authuser=1', 14);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mysite_project`
--
ALTER TABLE `mysite_project`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `folder` (`folder`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mysite_project`
--
ALTER TABLE `mysite_project`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=16;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
