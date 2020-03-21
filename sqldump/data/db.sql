CREATE DATABASE IF NOT EXISTS masina_visurilor_tale;
USE masina_visurilor_tale;

CREATE TABLE IF NOT EXISTS Account (
    AccountId INT(50) NOT NULL AUTO_INCREMENT,
    Username VARCHAR(500) NOT NULL,
    Password VARCHAR(500) NOT NULL,
    CONSTRAINT PK_Account PRIMARY KEY (AccountId)
);

CREATE TABLE IF NOT EXISTS Profile (
    ProfileId INT(50) NOT NULL AUTO_INCREMENT,
    AccountId INT(50) NOT NULL,
    Name VARCHAR(500) NOT NULL,
    ProfileType VARCHAR(500) NOT NULL,
    Description VARCHAR(500),
    CONSTRAINT PK_Profile PRIMARY KEY (ProfileId),
    CONSTRAINT FK_Profile_Account FOREIGN KEY (AccountId) REFERENCES Account(AccountId)
);

CREATE TABLE IF NOT EXISTS Photo (
    PhotoId INT(50) NOT NULL AUTO_INCREMENT,
    ProfileId INT(50) NOT NULL,
    Url VARCHAR(500) NOT NULL,
    CONSTRAINT PK_Photo PRIMARY KEY (PhotoId),
    CONSTRAINT FK_Photo_Profile FOREIGN KEY (ProfileId) REFERENCES Profile(ProfileId)
);

CREATE TABLE IF NOT EXISTS Statistics (
    StatisticsId INT(50) NOT NULL AUTO_INCREMENT,
    ProfileId INT(50) NOT NULL,
    CONSTRAINT PK_Statistics PRIMARY KEY (StatisticsId),
    CONSTRAINT FK_Statistics_Profile FOREIGN KEY (ProfileId) REFERENCES Profile(ProfileId)
);

CREATE TABLE IF NOT EXISTS Preference (
    PreferenceId INT(50) NOT NULL AUTO_INCREMENT,
    ProfileId INT(50) NOT NULL,
    CONSTRAINT PK_Preference PRIMARY KEY (PreferenceId),
    CONSTRAINT FK_Preference_Profile FOREIGN KEY (ProfileId) REFERENCES Profile(ProfileId)
);

CREATE TABLE IF NOT EXISTS Message (
    MessageId INT(50) NOT NULL AUTO_INCREMENT,
    FirstProfileId INT(50) NOT NULL,
    SecondProfileId INT(50) NOT NULL,
    CONSTRAINT PK_Message PRIMARY KEY (MessageId),
    CONSTRAINT FK_Message_First_Profile FOREIGN KEY (FirstProfileId) REFERENCES Profile(ProfileId),
    CONSTRAINT FK_Message_Second_Profile FOREIGN KEY (SecondProfileId) REFERENCES Profile(ProfileId)
);

CREATE TABLE IF NOT EXISTS MatchedContact (
    MatchedContactId INT(50) NOT NULL AUTO_INCREMENT,
    FirstProfileId INT(50) NOT NULL,
    SecondProfileId INT(50) NOT NULL,
    MatchDateTime DATETIME NOT NULL,
    CONSTRAINT PK_MatchedContact PRIMARY KEY (MatchedContactId),
    CONSTRAINT FK_MatchedContact_First_Profile FOREIGN KEY (FirstProfileId) REFERENCES Profile(ProfileId),
    CONSTRAINT FK_MatchedContact_Second_Profile FOREIGN KEY (SecondProfileId) REFERENCES Profile(ProfileId)
);