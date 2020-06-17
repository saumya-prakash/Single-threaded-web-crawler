-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.20

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
  `type` char(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_page` (`home_page`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `records`
--

LOCK TABLES `records` WRITE;
/*!40000 ALTER TABLE `records` DISABLE KEYS */;
INSERT INTO `records` VALUES (1,'NIELIT Patna','http://nielit.gov.in/patna/',NULL),(2,'FDDI','https://www.fddiindia.com/index.php',NULL),(3,'National Institute of Technology Patna','http://www.nitp.ac.in/php/home.php','technology'),(4,'Birla Institute Of Technology','https://www.bitmesra.ac.in/BIT_Mesra?cid=8&pid=H','technology'),(5,'Patna University','https://www.patnauniversity.ac.in/','university'),(6,'AIIMS Patna','https://aiimspatna.org',NULL),(7,'Aryabhatta Knowledge University','http://akubihar.ac.in','university'),(8,'Chandragupt Institute of Management Patna','http://www.cimp.ac.in','management'),(9,'Amity University Patna','https://amity.edu/Bihar/','university'),(10,'Cybotech Campus','https://www.cybotechcampus.com',NULL),(11,'Central University of South Bihar','https://www.cusb.ac.in','university'),(12,'Nalanda Medical College Hospital','http://nmchpatna.org','medical college'),(13,'G.D. Goenka Public School','https://www.gdgoenkapatna.com','school'),(14,'D A V Public School','http://davbsebpatna.org','school'),(15,'May Flower School','https://www.mfspatna.com','school'),(16,'ICAR RESEARCH COMPLEX FOR EASTERN REGION','https://icarrcer.in','research'),(17,'RMRIMS Agamkuan','https://www.rmrims.org.in/',NULL),(18,'Central Potato Research Institute, Indian Council of Agricultural Research','http://ataripatna.res.in','research'),(19,'New Government Polytechnic, Patna-13','https://www.ngpp.ac.in','polytechnic'),(20,'Bakhtiyarpur College Of Engineering','https://bcebakhtiyarpur.org','engineering college'),(21,'Sharda Group of Institutions (Regional Office)','https://www.sgei.org',NULL),(22,'Pratham Education Foundation','https://www.pratham.org',NULL),(23,'Institute of Marine Education & Research','http://imerpatna.com','research'),(24,'Asian Development Research Institute','https://www.adriindia.org','research'),(25,'A N Sinha Institute of Social Studies','http://ansiss.res.in','social'),(26,'Gyansarover International School','http://gyansarover.org','school'),(27,'Delhi Public School','https://www.dpspatna.com','school'),(28,'Indira Gandhi Institute of Medical Sciences','http://www.igims.org','medical science'),(29,'Seth M. R. Jaipuria School, Patna','http://www.jaipuriaschoolpatna.in','school'),(30,'Patna Doon Public School','http://patnadps.com','school'),(31,'C Programming institute Patna','https://www.csdt.co.in','computer'),(32,'Indian Institute of Technology Patna','https://www.iitp.ac.in/index.php/en-us/','technology'),(33,'Delhi Paramedical and Management Institute Patna','https://dpmipatna.com/','medical management'),(34,'Max Institute of Health Sciences & Technology (Best Paramedical College of Bihar) DMIT | DMLT | DOTT','http://www.maxedutech.com','technology medical college science'),(35,'Patliputra College Of Paramedical & Technology','http://patliputraanmandgnm.com/','technology medical college'),(36,'College of Physiotherapy PATNA PARAMEDICAL','https://www.patnaparamedical.com','medical college'),(37,'Mahavir Para Medical Training & Research Institute','http://mptri.org/','medical research training'),(38,'Mahavir Cancer Sansthan And Research Centre','https://www.mahavircancersansthan.com','research'),(39,'Training And Development Institute Of India','http://tdiofindia.org/','training'),(40,'B.D. College','http://bdcollegepatna.com/','college'),(41,'Impact College','https://www.impactcollege.co.in/','college'),(42,'Bihar National College','https://www.bncollegepatna.com','college'),(43,'Patna Women’s College','https://patnawomenscollege.in/','college'),(44,'L. P. Shahi College','https://www.lpshahicollege.in','college'),(45,'Patna College','http://patnacollege.org/','college'),(46,'Patna Science College','http://www.patnasciencecollege.org','college science'),(47,'Frameboxx Animation | Visual Effects Pvt. Ltd.','https://frameboxx.in/industry-jobs/','animation'),(48,'Bihar Skill Development Mission','https://skillmissionbihar.org/',NULL),(49,'Tata institute of Social sciences','https://www.sve.tiss.edu','science social'),(50,'Earth Tech Engineers & Consultants Pvt. Ltd','http://earth-tech.co.in/','engineering'),(51,'Mount Carmel High School','http://patnacarmel.com/','school'),(52,'St. Michael\'s High School','https://stmichaelspatna.edu.in/','school'),(53,'St. Xavier\'s College Of Management And Technology, Patna','http://xaviercollegepatna.org/','technology college management'),(54,'School Of Global Education','http://schoolofglobaleducation.com/','school'),(55,'Gyan Niketan Girls School,Patna','http://gngs.in/','school'),(56,'ACCURIZE MARKET RESEARCH PRIVATE LIMITED','https://www.accurizemarketresearch.com/','research'),(57,'St. Karen\'s High School','https://www.stkarenshighschool.com','school'),(58,'St Teresa International School','www.stisbihta.com','school'),(59,'St. Karens Collegiate School','http://stkarenscollegiateschool.com/','school'),(60,'St.Xavier\'s High School','http://stxavierspatna.in/#1','school'),(61,'St. Karen\'s Primary School','http://stkarensprimaryschool.com/','school'),(62,'Meteorological Center','http://amsskolkata.gov.in/mc/patna/','meteorology'),(63,'School of Creative Learning','http://creativelearning.in/','school'),(64,'Tool Room Training Center','https://patna.idtr.gov.in/','training'),(65,'Buddha Institute of Dental Sciences & Hospital','https://www.bidsh.org','science'),(66,'Dental College','http://www.patnadentalcollege.in','college'),(67,'DR. B.R. AMBEDKAR INSTITUTE OF DENTAL SCIENCES & HOSPITAL','http://ambedkardental.co.in/','science'),(68,'IISPL PATNA','http://www.iispl.org',NULL),(69,'SB GLOBAL INSTITUTE OF BANKING MANAGEMENT','https://sb-global-institute-of-banking.business.site/','management'),(70,'INDIGROW INSTITUTE OF PROFESSIONAL STUDIES (IIPS)','http://www.iipsindia.co.in','professional'),(71,'Indian Institute of Business Management','http://www.w.iibm.in/','management'),(72,'Development management Institute, Bihta Campus','https://dmi.ac.in/','management'),(73,'Asean Institute of Insurance and Risk Management','https://aiirm.org/','management'),(74,'Arcade Business College','https://www.abcollege.org/','college'),(75,'INTERNATIONAL SCHOOL OF MANAGEMENT PATNA','http://www.ismpatna.ac.in','school management'),(76,'INSTITUTE OF SPANISH STUDIES','https://www.instituteofspanishstudies.com',NULL),(77,'Patna High School','http://patnahighschool.blogspot.com/','school'),(78,'Children\'s Heaven High School','https://childrensheavenhighschool.com/','school'),(79,'Oxbridge Convent High School','https://www.oxbridgeconventhighschool.com','school'),(80,'Maple Bear Canadian Preschool','https://www.maplebearsouthasia.com/','school'),(81,'Students Public School','https://studentspublicschool-school.business.site/','school'),(82,'Bihta Public School','http://bpsbihta.com/','school'),(83,'A P N PUBLIC SCHOOL BIHTA','http://apnpublicschool.com/','school'),(84,'Syon Research Labs','https://syonlab.com/','research'),(85,'Photo Vatika','https://svmpatna.co.in/',NULL),(86,'Patna Collegiate School','http://patnacollegiateschool.com/','school');
/*!40000 ALTER TABLE `records` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sites`
--

DROP TABLE IF EXISTS `sites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sites` (
  `serial` int unsigned NOT NULL AUTO_INCREMENT,
  `id` int unsigned DEFAULT NULL,
  `link` varchar(100) NOT NULL,
  PRIMARY KEY (`serial`),
  UNIQUE KEY `link` (`link`),
  KEY `fk_1` (`id`),
  CONSTRAINT `fk_1` FOREIGN KEY (`id`) REFERENCES `records` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sites`
--

LOCK TABLES `sites` WRITE;
/*!40000 ALTER TABLE `sites` DISABLE KEYS */;
/*!40000 ALTER TABLE `sites` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-17 11:50:36
