-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 03, 2015 at 10:06 AM
-- Server version: 5.6.19-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.9

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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `tag` varchar(500) NOT NULL,
  `main_image` varchar(200) NOT NULL,
  `folder` varchar(200) NOT NULL,
  `style` varchar(200) NOT NULL,
  `alt_text` varchar(500) NOT NULL,
  `main_image_caption` varchar(400) NOT NULL,
  `link` varchar(500) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `folder` (`folder`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Dumping data for table `mysite_project`
--

INSERT INTO `mysite_project` (`id`, `name`, `tag`, `main_image`, `folder`, `style`, `alt_text`, `main_image_caption`, `link`) VALUES
(1, 'DFC Query Builder', 'A mini-scale Database Engine', 'bptree.png', 'dfc_query_builder', 'course', 'Screenshot of DFC Query Builder', 'Indexing Using B+ Tree', 'https://github.com/Bug-Assassins/DFC_query_builder'),
(2, 'Web Service Retrieval', 'Search Engine for Web Services', 'vector.png', 'web_service_retrieval', 'course', 'Vector Space Method', 'Vector Space Matching for Web Services', 'https://github.com/Bug-Assassins/web_service_retrieval'),
(3, 'Chess Game', 'Java GUI Chess Game', 'game_in_progress.png', 'chess', 'course', 'Chess Game - Java GUI - Object Oriented', 'Chess Game in Progress', 'https://github.com/ashish1294/ChessOOP'),
(4, 'TAJ Defender', 'Sandboxing for C/C++ Codes', 'seccomp.gif', 'taj_defender', 'course', 'C/C++ Sandbox', 'Linux SECCOMP - Secure Computing', 'https://github.com/Bug-Assassins/TAJ-Defender'),
(5, 'FLINT & BLAS', 'Linear Algebra using BLAS', 'blas.jpg', 'flint', 'course', 'BLAS Image', 'Basic Linear Algebra Subroutine', 'https://github.com/Bug-Assassins/BLAS_Practice'),
(6, 'Galaxian', 'OpenGL based 2D shooting game', 'game_play.png', 'galaxian', 'course', 'Screenshot of the Game', 'Galaxian Game in Progress', 'https://github.com/Bug-Assassins/Galaxian'),
(7, 'Konnect', 'A mini-scale TCP/IP Stack', 'three_way.jpg', 'konnect', 'course', 'The TCP Implementation', 'Three Way Handshaking Protocol', 'https://github.com/Bug-Assassins/Konnect'),
(8, 'Digital Passbook', 'Android App for Bank Transactions', 'account_logo.png', 'digital_passbook', 'extra', 'Now maintain a passbook on mobile', 'Logo - Digital Passbook', 'https://github.com/ashish1294/DigitalPassbook'),
(9, 'Online Banking', 'Mini Scale Online Bank using PHP', 'home.png', 'online_banking', 'extra', 'Online Banking using PHP, HTML5, JS and CSS3', 'Homepage of the Bank Website', 'https://github.com/ashish1294/OnlineBankingPHP'),
(10, 'SGC APP', 'Android App for AAC Club, NITK', 'home.png', 'sgc_app', 'extra', 'Star Gazing Club, NITK Surathkal', 'Home Activity of SGC App', 'https://github.com/ashish1294/SGC-App'),
(11, 'CodeChef Code Now', 'Chrome Extension for Code-Chef', 'codechef.jpeg', 'code_now', 'extra', 'Use your favorite IDE with CodeChef', 'Logo of Codechef', 'https://github.com/ashish1294/code-now-CodeChef'),
(12, 'RDBMS Graph Storage', 'Graph Based Data Storage (RDBMS)', 'model.svg', 'graph_storage_rdbms', 'course', 'RDBMS Graph Storage', 'Major components of the Graph Based Storage Engine', 'https://github.com/Bug-Assassins/Relational-Graph-Database'),
(13, 'Drive Assist', 'Windows App for Road Safety', 'kinect.jpg', 'drive_assist', 'extra', 'Drive Assist', 'Microsoft Kinect v2 for Windows', 'https://drive.google.com/open?id=0B6A-3_6rwie9fkhLU04wbDFWREh0SlZBNkJlVXN6bURhRFNZWVRDNkFyeE5MM3JvOVFWaDQ&authuser=1'),
(14, 'Namma Bazaar', 'Super Market Management System', 'super1.jpg', 'namma_bazaar', 'course', 'Namma Bazaar', 'Namma Bazar for Super Markets', 'https://drive.google.com/folderview?id=0B6A-3_6rwie9fkNiNml1YUlzU3QydVFuZjhzNmdLM3FSTmszSGlOQVBrdmY5bzZJZUVCSjQ&usp=sharing'),
(15, 'Global Learning Factory', 'Search Engine for Intellectually Disabled', 'screenshot.jpg', 'glf', 'extra', 'Global Learning Factory', 'Screenshot of the Search Engine GUI', 'https://drive.google.com/open?id=0B6A-3_6rwie9fnVTSEdRLWljb2JtSkNaaUdBdkVOVGtZNE1kM3RfeWxoMnlFQ2pISklldUU&authuser=1');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
