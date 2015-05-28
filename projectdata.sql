-- MySQL dump 10.13  Distrib 5.5.43, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: personalwebsite
-- ------------------------------------------------------
-- Server version	5.5.43-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

--
-- Table structure for table `mysite_project`
--

DROP TABLE IF EXISTS `mysite_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysite_project` (
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysite_project`
--

LOCK TABLES `mysite_project` WRITE;
/*!40000 ALTER TABLE `mysite_project` DISABLE KEYS */;
INSERT INTO `mysite_project` VALUES (1,'DFC Query Builder','A mini-scale Database Engine','bptree.png','dfc_query_builder','course','Screenshot of DFC Query Builder','Indexing Using B+ Tree','https://github.com/Bug-Assassins/DFC_query_builder'),(2,'Web Service Retrieval','Search Engine for Web Services','vector.png','web_service_retrieval','course','Vector Space Method','Vector Space Matching for Web Services','https://github.com/Bug-Assassins/web_service_retrieval'),(3,'Chess Game','Java GUI Chess Game','game_in_progress.png','chess','course','Chess Game - Java GUI - Object Oriented','Chess Game in Progress','https://github.com/ashish1294/ChessOOP'),(4,'TAJ Defender','Sandboxing for C/C++ Codes','seccomp.gif','taj_defender','course','C/C++ Sandbox','Linux SECCOMP - Secure Computing','https://github.com/Bug-Assassins/TAJ-Defender'),(5,'FLINT & BLAS','Linear Algebra using BLAS','blas.jpg','flint','course','BLAS Image','Basic Linear Algebra Subroutine','https://github.com/Bug-Assassins/BLAS_Practice'),(6,'Galaxian','OpenGL based 2D shooting game','game_play.png','galaxian','course','Screenshot of the Game','Galaxian Game in Progress','https://github.com/Bug-Assassins/Galaxian'),(7,'Konnect','A mini-scale TCP/IP Stack','three_way.jpg','konnect','course','The TCP Implementation','Three Way Handshaking Protocol','https://github.com/Bug-Assassins/Konnect'),(8,'Digital Passbook','Android App for Bank Transactions','account_logo.png','digital_passbook','extra','Now maintain a passbook on mobile','Logo - Digital Passbook','https://github.com/ashish1294/DigitalPassbook'),(9,'Online Banking','Mini Scale Online Bank using PHP','home.png','online_banking','extra','Online Banking using PHP, HTML5, JS and CSS3','Homepage of the Bank Website','https://github.com/ashish1294/OnlineBankingPHP'),(10,'SGC APP','Android App for AAC Club, NITK','home.png','sgc_app','extra','Star Gazing Club, NITK Surathkal','Home Activity of SGC App','https://github.com/ashish1294/SGC-App'),(11,'CodeChef Code Now','Chrome Extension for Code-Chef','codechef.jpeg','code_now','extra','Use your favorite IDE with CodeChef','Logo of Codechef','https://github.com/ashish1294/code-now-CodeChef');
/*!40000 ALTER TABLE `mysite_project` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-05-25 20:28:23
