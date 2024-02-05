/*
SQLyog Ultimate v13.1.1 (64 bit)
MySQL - 10.4.32-MariaDB : Database - school_mangement
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`school_mangement` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `school_mangement`;

/*Table structure for table `assignment_assign` */

DROP TABLE IF EXISTS `assignment_assign`;

CREATE TABLE `assignment_assign` (
  `id` int(11) NOT NULL,
  `assignby` int(11) DEFAULT NULL,
  `standard` int(11) DEFAULT NULL,
  `dates` date DEFAULT NULL,
  `assignment` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `assignby` (`assignby`),
  KEY `standard` (`standard`),
  KEY `assignment` (`assignment`),
  CONSTRAINT `assignment_assign_ibfk_1` FOREIGN KEY (`assignby`) REFERENCES `teacher_registration` (`id`),
  CONSTRAINT `assignment_assign_ibfk_2` FOREIGN KEY (`standard`) REFERENCES `standard` (`id`),
  CONSTRAINT `assignment_assign_ibfk_3` FOREIGN KEY (`assignment`) REFERENCES `assignment_master` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `assignment_assign` */

/*Table structure for table `assignment_master` */

DROP TABLE IF EXISTS `assignment_master`;

CREATE TABLE `assignment_master` (
  `id` int(11) NOT NULL,
  `subject` int(11) DEFAULT NULL,
  `topic` varchar(50) DEFAULT NULL,
  `createdby` int(11) DEFAULT NULL,
  `file` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `subject` (`subject`),
  KEY `createdby` (`createdby`),
  CONSTRAINT `assignment_master_ibfk_1` FOREIGN KEY (`subject`) REFERENCES `subject` (`id`),
  CONSTRAINT `assignment_master_ibfk_2` FOREIGN KEY (`createdby`) REFERENCES `teacher_registration` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `assignment_master` */

/*Table structure for table `attandance` */

DROP TABLE IF EXISTS `attandance`;

CREATE TABLE `attandance` (
  `id` int(11) NOT NULL,
  `attandances` int(11) DEFAULT NULL,
  `dates` date DEFAULT NULL,
  `sid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sid` (`sid`),
  CONSTRAINT `attandance_ibfk_1` FOREIGN KEY (`sid`) REFERENCES `student_registration` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `attandance` */

/*Table structure for table `marks` */

DROP TABLE IF EXISTS `marks`;

CREATE TABLE `marks` (
  `id` int(11) NOT NULL,
  `teacherid` int(11) DEFAULT NULL,
  `subject` int(11) DEFAULT NULL,
  `student` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `marks` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `teacherid` (`teacherid`),
  KEY `subject` (`subject`),
  KEY `student` (`student`),
  CONSTRAINT `marks_ibfk_1` FOREIGN KEY (`teacherid`) REFERENCES `teacher_registration` (`id`),
  CONSTRAINT `marks_ibfk_2` FOREIGN KEY (`subject`) REFERENCES `subject` (`id`),
  CONSTRAINT `marks_ibfk_3` FOREIGN KEY (`student`) REFERENCES `student_registration` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `marks` */

/*Table structure for table `notes` */

DROP TABLE IF EXISTS `notes`;

CREATE TABLE `notes` (
  `id` int(11) NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `createby` int(11) DEFAULT NULL,
  `standards` int(11) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `createby` (`createby`),
  KEY `standards` (`standards`),
  CONSTRAINT `notes_ibfk_1` FOREIGN KEY (`createby`) REFERENCES `teacher_registration` (`id`),
  CONSTRAINT `notes_ibfk_2` FOREIGN KEY (`standards`) REFERENCES `standard` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `notes` */

/*Table structure for table `principal_login` */

DROP TABLE IF EXISTS `principal_login`;

CREATE TABLE `principal_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `principal_login` */

/*Table structure for table `role` */

DROP TABLE IF EXISTS `role`;

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `rolename` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `role` */

insert  into `role`(`id`,`rolename`) values 
(1,'1');

/*Table structure for table `standard` */

DROP TABLE IF EXISTS `standard`;

CREATE TABLE `standard` (
  `id` int(11) NOT NULL,
  `studentname` varchar(30) DEFAULT NULL,
  `classteacher` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `classteacher` (`classteacher`),
  CONSTRAINT `standard_ibfk_1` FOREIGN KEY (`classteacher`) REFERENCES `teacher_registration` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `standard` */

/*Table structure for table `student_registration` */

DROP TABLE IF EXISTS `student_registration`;

CREATE TABLE `student_registration` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `phoneno1` varchar(50) DEFAULT NULL,
  `phoneno2` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `dateofbirth` date DEFAULT NULL,
  `admissiondate` date DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  `standards` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `standards` (`standards`),
  CONSTRAINT `student_registration_ibfk_1` FOREIGN KEY (`standards`) REFERENCES `standard` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `student_registration` */

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `id` int(11) NOT NULL,
  `subject_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `subject` */

insert  into `subject`(`id`,`subject_name`) values 
(0,NULL),
(1,'php');

/*Table structure for table `subject_teacher` */

DROP TABLE IF EXISTS `subject_teacher`;

CREATE TABLE `subject_teacher` (
  `id` int(11) NOT NULL,
  `sid` int(11) DEFAULT NULL,
  `tid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sid` (`sid`),
  KEY `tid` (`tid`),
  CONSTRAINT `subject_teacher_ibfk_1` FOREIGN KEY (`sid`) REFERENCES `subject` (`id`),
  CONSTRAINT `subject_teacher_ibfk_2` FOREIGN KEY (`tid`) REFERENCES `teacher_registration` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `subject_teacher` */

insert  into `subject_teacher`(`id`,`sid`,`tid`) values 
(1,1,1);

/*Table structure for table `teacher_registration` */

DROP TABLE IF EXISTS `teacher_registration`;

CREATE TABLE `teacher_registration` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `phoneno` varchar(50) DEFAULT NULL,
  `education` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `experience_in_month` int(11) DEFAULT NULL,
  `salary` double DEFAULT NULL,
  `dateofbirth` date DEFAULT NULL,
  `joiningdate` date DEFAULT NULL,
  `Gender` varchar(50) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  `role` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `role` (`role`),
  CONSTRAINT `teacher_registration_ibfk_1` FOREIGN KEY (`role`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `teacher_registration` */

insert  into `teacher_registration`(`id`,`first_name`,`last_name`,`email`,`password`,`phoneno`,`education`,`address`,`experience_in_month`,`salary`,`dateofbirth`,`joiningdate`,`Gender`,`photo`,`role`) values 
(1,'efsdg','dgdg','dgdg','dgdg','53533','tfytu','tfht',12,65757,'2020-02-03','2023-12-01','hj',NULL,1);

/*Table structure for table `timetable` */

DROP TABLE IF EXISTS `timetable`;

CREATE TABLE `timetable` (
  `id` int(11) NOT NULL,
  `standard` int(11) DEFAULT NULL,
  `subid` int(11) DEFAULT NULL,
  `teacherid` int(11) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `standard` (`standard`),
  KEY `subid` (`subid`),
  KEY `teacherid` (`teacherid`),
  CONSTRAINT `timetable_ibfk_1` FOREIGN KEY (`standard`) REFERENCES `standard` (`id`),
  CONSTRAINT `timetable_ibfk_2` FOREIGN KEY (`subid`) REFERENCES `subject` (`id`),
  CONSTRAINT `timetable_ibfk_3` FOREIGN KEY (`teacherid`) REFERENCES `teacher_registration` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `timetable` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
