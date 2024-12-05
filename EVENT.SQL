DROP DATABASE IF EXISTS event;

CREATE DATABASE IF NOT EXISTS event;
USE event;
# -----------------------------------------------------------------------------
#       TABLE : PARTICIPANT
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS PARTICIPANT
 (
   ID_PARTICIPANT INTEGER NOT NULL  AUTO_INCREMENT,
   NOM_PARTICIPANT TEXT NULL  ,
   EMAIL_PARTICIPANT TEXT NULL  ,
   MDP_PARTICIPANT TEXT NULL  ,
   ISORGANISTEUR TINYINT NULL  
   , PRIMARY KEY (ID_PARTICIPANT) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       TABLE : EVENEMENT
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS EVENEMENT
 (
   ID_EVENEMENT INTEGER NOT NULL AUTO_INCREMENT ,
   ID_ORGANISATEUR INTEGER NOT NULL  ,
   TITRE TEXT NULL  ,
   DESCRIPTION TEXT NULL  ,
   LIEU TEXT NULL  ,
   DATE_EVENEMENT DATE NULL  ,
   CAPACITE INTEGER NULL  ,
   PROGRAMME TEXT NULL  ,
   IMAGE TEXT NULL  
   , PRIMARY KEY (ID_EVENEMENT) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       INDEX DE LA TABLE EVENEMENT
# -----------------------------------------------------------------------------


CREATE  INDEX I_FK_EVENEMENT_ORGANISATEUR
     ON EVENEMENT (ID_ORGANISATEUR ASC);

# -----------------------------------------------------------------------------
#       TABLE : ORGANISATEUR
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS ORGANISATEUR
 (
   ID_ORGANISATEUR INTEGER NOT NULL  AUTO_INCREMENT,
   NOM_ORGANISATEUR TEXT NULL  ,
   EMAIL_ORGANISATEUR TEXT NULL  ,
   MDP_ORGANISATEUR TEXT NULL  ,
   ISORGNISATEUR TINYINT NULL  
   , PRIMARY KEY (ID_ORGANISATEUR) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       TABLE : INSCRIRE
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS INSCRIRE
 (
   ID_EVENEMENT INTEGER NOT NULL  ,
   ID_PARTICIPANT INTEGER NOT NULL  
   , PRIMARY KEY (ID_EVENEMENT,ID_PARTICIPANT) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       INDEX DE LA TABLE INSCRIRE
# -----------------------------------------------------------------------------


CREATE  INDEX I_FK_INSCRIRE_EVENEMENT
     ON INSCRIRE (ID_EVENEMENT ASC);

CREATE  INDEX I_FK_INSCRIRE_PARTICIPANT
     ON INSCRIRE (ID_PARTICIPANT ASC);


# -----------------------------------------------------------------------------
#       CREATION DES REFERENCES DE TABLE
# -----------------------------------------------------------------------------


ALTER TABLE EVENEMENT 
  ADD FOREIGN KEY FK_EVENEMENT_ORGANISATEUR (ID_ORGANISATEUR)
      REFERENCES ORGANISATEUR (ID_ORGANISATEUR) ;


ALTER TABLE INSCRIRE 
  ADD FOREIGN KEY FK_INSCRIRE_EVENEMENT (ID_EVENEMENT)
      REFERENCES EVENEMENT (ID_EVENEMENT) ;


ALTER TABLE INSCRIRE 
  ADD FOREIGN KEY FK_INSCRIRE_PARTICIPANT (ID_PARTICIPANT)
      REFERENCES PARTICIPANT (ID_PARTICIPANT) ;

