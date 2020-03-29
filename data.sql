-- MySQL dump 10.13  Distrib 8.0.19, for Linux (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `records`
--

DROP TABLE IF EXISTS `records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `records` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `home_page` varchar(100) NOT NULL,
  `sites` varchar(400) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_page` (`home_page`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `records`
--

LOCK TABLES `records` WRITE;
/*!40000 ALTER TABLE `records` DISABLE KEYS */;
INSERT INTO `records` VALUES (1,'NIELIT Patna','http://nielit.gov.in/patna/',NULL,NULL),(2,'FDDI','https://www.fddiindia.com/index.php',NULL,NULL),(3,'National Institute of Technology Patna','http://www.nitp.ac.in/php/home.php ',NULL,'technology'),(4,'Birla Institute Of Technology','https://www.bitmesra.ac.in/BIT_Mesra?cid=8&pid=H ',NULL,'technology'),(5,'Patna University','https://www.patnauniversity.ac.in/',NULL,'university'),(6,'AIIMS Patna','https://aiimspatna.org',NULL,NULL),(7,'Aryabhatta Knowledge University','http://akubihar.ac.in',NULL,'university'),(8,'Chandragupt Institute of Management Patna','http://www.cimp.ac.in',NULL,'management'),(9,'Amity University Patna','https://amity.edu/Bihar/',NULL,'university'),(10,'Cybotech Campus','https://www.cybotechcampus.com',NULL,NULL),(11,'Central University of South Bihar','https://www.cusb.ac.in',NULL,'university'),(12,'Nalanda Medical College Hospital','http://nmchpatna.org',NULL,'medical college'),(13,'G.D. Goenka Public School','https://www.gdgoenkapatna.com',NULL,'school'),(14,'D A V Public School','http://davbsebpatna.org',NULL,'school'),(15,'May Flower School','https://www.mfspatna.com',NULL,'school'),(16,'ICAR RESEARCH COMPLEX FOR EASTERN REGION','https://icarrcer.in',NULL,'research'),(17,'RMRIMS Agamkuan','https://www.rmrims.org.in/',NULL,NULL),(18,'Central Potato Research Institute, Indian Council of Agricultural Research','http://ataripatna.res.in',NULL,'research'),(19,'New Government Polytechnic, Patna-13','https://www.ngpp.ac.in',NULL,NULL),(20,'Bakhtiyarpur College Of Engineering','https://bcebakhtiyarpur.org',NULL,'engineering college'),(21,'Sharda Group of Institutions (Regional Office)','https://www.sgei.org',NULL,NULL),(22,'Pratham Education Foundation','https://www.pratham.org',NULL,NULL),(23,'Institute of Marine Education & Research','http://imerpatna.com',NULL,'research'),(24,'Asian Development Research Institute','https://www.adriindia.org',NULL,'research'),(25,'A N Sinha Institute of Social Studies','http://ansiss.res.in ',NULL,'social'),(26,'Gyansarover International School','http://gyansarover.org',NULL,'school'),(27,'Delhi Public School','https://www.dpspatna.com',NULL,'school'),(28,'Indira Gandhi Institute of Medical Sciences','http://www.igims.org',NULL,'medical science'),(29,'Seth M. R. Jaipuria School, Patna','http://www.jaipuriaschoolpatna.in',NULL,'school'),(30,'Patna Doon Public School','http://patnadps.com',NULL,'school'),(31,'C Programming institute Patna','https://www.csdt.co.in',NULL,'computer');
/*!40000 ALTER TABLE `records` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-29 16:05:15
