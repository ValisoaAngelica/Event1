-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : sam. 07 déc. 2024 à 15:43
-- Version du serveur : 8.0.27
-- Version de PHP : 8.1.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `event`
--

-- --------------------------------------------------------

--
-- Structure de la table `evenement`
--

DROP TABLE IF EXISTS `evenement`;
CREATE TABLE IF NOT EXISTS `evenement` (
  `ID_EVENEMENT` int NOT NULL AUTO_INCREMENT,
  `ID_ORGANISATEUR` int NOT NULL,
  `TITRE` varchar(200) NOT NULL,
  `DESCRIPTION` text,
  `LIEU` varchar(200) DEFAULT NULL,
  `DATE_EVENEMENT` datetime NOT NULL,
  `CAPACITE` int NOT NULL,
  `PROGRAMME` text,
  `IMAGE` varchar(255) DEFAULT NULL,
  `DATE_CREATION` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_EVENEMENT`),
  KEY `ID_ORGANISATEUR` (`ID_ORGANISATEUR`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `s_inscrire_event`
--

DROP TABLE IF EXISTS `s_inscrire_event`;
CREATE TABLE IF NOT EXISTS `s_inscrire_event` (
  `ID_INSCRIRE` int NOT NULL AUTO_INCREMENT,
  `ID_EVENEMENT` int NOT NULL,
  `ID_UTILISATEUR` int NOT NULL,
  `DATE_INSCRIPTION` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_INSCRIRE`),
  KEY `ID_EVENEMENT` (`ID_EVENEMENT`),
  KEY `ID_UTILISATEUR` (`ID_UTILISATEUR`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `ID_UTILISATEUR` int NOT NULL AUTO_INCREMENT,
  `NOM_UTILISATEUR` varchar(100) NOT NULL,
  `EMAIL_UTILISATEUR` varchar(150) NOT NULL,
  `MDP_UTILISATEUR` varchar(255) NOT NULL,
  `ROLE` enum('organisateur','participant') NOT NULL,
  `DATE_CREATION` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_UTILISATEUR`),
  UNIQUE KEY `EMAIL_UTILISATEUR` (`EMAIL_UTILISATEUR`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
