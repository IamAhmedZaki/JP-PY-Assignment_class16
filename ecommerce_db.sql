-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: ecommerce_db
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(45) NOT NULL,
  `description` text,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Electronics',NULL),(2,'Furniture',NULL),(3,'Household Items',NULL),(4,'books',NULL);
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_details`
--

DROP TABLE IF EXISTS `order_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_details` (
  `order_details_id` int NOT NULL AUTO_INCREMENT,
  ` order_id` int NOT NULL,
  `product_id` int NOT NULL,
  `quantity` int NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`order_details_id`),
  KEY `order_id_idx` (` order_id`),
  KEY `product_id_idx` (`product_id`),
  CONSTRAINT `order_id` FOREIGN KEY (` order_id`) REFERENCES `orders` (`order_id`),
  CONSTRAINT `product_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_details`
--

LOCK TABLES `order_details` WRITE;
/*!40000 ALTER TABLE `order_details` DISABLE KEYS */;
INSERT INTO `order_details` VALUES (1,1,1,2,30000.00),(2,2,2,3,80000.00),(3,3,5,1,20000.00),(4,4,1,3,30000.00),(5,5,2,4,80000.00),(6,6,5,6,20000.00),(7,7,6,4,5000.00),(8,8,6,8,5000.00),(9,9,1,3,30000.00),(10,10,2,2,80000.00),(11,11,5,1,20000.00);
/*!40000 ALTER TABLE `order_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `order_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `status` enum('Pending','Shipped','Delivered','Cancelled') DEFAULT 'Pending',
  PRIMARY KEY (`order_id`),
  KEY `user_id_idx` (`user_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,'2024-09-07 05:12:03','Pending'),(2,2,'2024-09-07 05:18:55','Delivered'),(3,3,'2024-09-07 05:18:56','Shipped'),(4,4,'2024-09-07 05:18:56','Pending'),(5,5,'2024-09-07 05:18:56','Shipped'),(6,6,'2024-09-07 05:18:56','Delivered'),(7,7,'2024-09-07 05:18:56','Pending'),(8,8,'2024-09-07 05:18:56','Delivered'),(9,9,'2024-09-07 05:18:56','Shipped'),(10,10,'2024-09-07 05:18:56','Pending'),(11,2,'2024-09-07 05:29:20','Shipped');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `payment_id` int NOT NULL AUTO_INCREMENT,
  `order_id` int NOT NULL,
  `payment_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `amount` decimal(10,2) NOT NULL,
  `status` enum('Pending','Completed','Failed') NOT NULL DEFAULT 'Pending',
  PRIMARY KEY (`payment_id`),
  KEY `order_id_idx` (`order_id`),
  CONSTRAINT `fk_payments` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,1,'2024-09-07 05:38:57',30000.00,'Completed'),(2,2,'2024-09-07 05:38:57',80000.00,'Completed'),(3,3,'2024-09-07 05:38:57',20000.00,'Pending'),(4,4,'2024-09-07 05:38:57',30000.00,'Completed'),(5,5,'2024-09-07 05:38:57',80000.00,'Pending'),(6,6,'2024-09-07 05:38:57',20000.00,'Pending'),(7,7,'2024-09-07 05:38:57',5000.00,'Pending'),(8,8,'2024-09-07 05:38:57',5000.00,'Completed'),(9,9,'2024-09-07 05:38:57',30000.00,'Pending'),(10,10,'2024-09-07 05:38:57',80000.00,'Completed'),(11,11,'2024-09-07 05:38:57',20000.00,'Pending');
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(45) NOT NULL,
  `description` text,
  `price` decimal(10,2) NOT NULL,
  `stock_quantity` int NOT NULL,
  `category_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`product_id`),
  KEY `category_id_idx` (`category_id`),
  CONSTRAINT `category_id` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Smartphone',NULL,30000.00,15,1,'2024-09-06 21:11:09'),(2,'Laptop',NULL,80000.00,13,1,'2024-09-06 21:11:09'),(3,'Refrigerator',NULL,100000.00,7,1,'2024-09-06 21:11:09'),(4,'Chair',NULL,750.00,40,2,'2024-09-06 21:11:09'),(5,'Table',NULL,20000.00,10,2,'2024-09-06 21:13:21'),(6,'Kitchen Set',NULL,5000.00,11,3,'2024-09-06 21:13:21'),(7,'Bathroom Set',NULL,2000.00,11,3,'2024-09-06 21:13:21'),(8,'spatula',NULL,300.00,15,3,'2024-09-07 07:07:33');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `passwords` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `state` varchar(45) NOT NULL,
  `zip_code` varchar(45) NOT NULL,
  `country` varchar(45) NOT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Ahmed','Zaki','mahmedzaki@gmail.com','123456','gulistan-ej-ohar','Sydney','New South Wales','20000','Australia','034567554','2024-09-06 04:39:49'),(2,'Adnan','Khan','adnankhan@gmail.com','543216','gulshan-e-iqbal','Rio de Janerio','Sao Paulo',' 20040','Brazil','034567','2024-09-06 20:59:13'),(3,'Iqra','Waqas','iqra@gmail.com','3373456','saadi town','Vancouver','British Coloumbia','43534','Canada','032432443','2024-09-06 21:00:35'),(4,'Huda','Shariq','huda@gmail.com','432432','model colony','Mumbai','Maharashtra','56765','India','4345435','2024-09-06 21:01:58'),(5,'Mirha','Zaki','mirha@gamil.com','4325435','korangi','Munich','Bavaria','46557','Germany','86656435435','2024-09-06 21:15:49'),(6,'Dawood','McAlister','mcalister@gmail.com','654565','orangi','Los Angeles','Calafornia','546456','USA','23044356','2024-09-06 21:17:26'),(7,'Sara','Aazmi','sarah@gmail.com','8798789','nazimabad','Gauteng','Johannesburg','876878','South Africa','12321343234','2024-09-06 22:53:19'),(8,'Sarim','Mehmood','sarim@gmail.com','89729','hussainabad','Guadalajara','Jalisco','343244','Mexico','98978772344','2024-09-06 22:53:19'),(9,'Gojo','Satoru','gojo@gmail.com','999999','jujutsu high','Yokohama','Tokyo','234234','Japan','999999999','2024-09-06 22:53:19'),(10,'Lev','Yashin','lev@gmail.com','9883249','naya nazimabad','Saint Petersburg','Moscow Oblast','324455','Russua','888888','2024-09-06 22:53:19');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-07  7:35:23
