DROP DATABASE masina_visurilor_tale;

CREATE DATABASE IF NOT EXISTS masina_visurilor_tale;
USE masina_visurilor_tale;

CREATE TABLE IF NOT EXISTS Account (
    AccountId INT(50) NOT NULL AUTO_INCREMENT,
    Username VARCHAR(500) NOT NULL UNIQUE,
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

CREATE TABLE IF NOT EXISTS Preferences (
    PreferenceId INT(50) NOT NULL AUTO_INCREMENT,
    ProfileId INT(50) NOT NULL,
    PreferenceText VARCHAR(500) NOT NULL,
    CONSTRAINT PK_Preference PRIMARY KEY (PreferenceId),
    CONSTRAINT FK_Preference_Profile FOREIGN KEY (ProfileId) REFERENCES Profile(ProfileId)
);

CREATE TABLE IF NOT EXISTS Features (
    FeatureId INT(50) NOT NULL AUTO_INCREMENT,
    ProfileId INT(50) NOT NULL,
    FeatureText VARCHAR(500) NOT NULL,
    CONSTRAINT PK_Feature PRIMARY KEY (FeatureId),
    CONSTRAINT FK_Feature_Profile FOREIGN KEY (ProfileId) REFERENCES Profile(ProfileId)
);

CREATE TABLE IF NOT EXISTS Message (
    MessageId INT(50) NOT NULL AUTO_INCREMENT,
    MatchedContactId INT(50) NOT NULL,
    MessageDateTime DATETIME NOT NULL,
    MessageText VARCHAR(500) NOT NULL,
    CONSTRAINT PK_Message PRIMARY KEY (MessageId),
    CONSTRAINT FK_Message_MatchedContact FOREIGN KEY (MatchedContactId) REFERENCES MatchedContact(MatchedContactId)
);

CREATE TABLE IF NOT EXISTS MatchedContact (
    MatchedContactId INT(50) NOT NULL AUTO_INCREMENT,
    FirstProfileId INT(50) NOT NULL,
    SecondProfileId INT(50) NOT NULL,
    FirstProfileLike BOOLEAN,
    SecondProfileLike BOOLEAN,
    MatchDateTime DATETIME NOT NULL,
    CONSTRAINT PK_MatchedContact PRIMARY KEY (MatchedContactId),
    CONSTRAINT FK_MatchedContact_First_Profile FOREIGN KEY (FirstProfileId) REFERENCES Profile(ProfileId),
    CONSTRAINT FK_MatchedContact_Second_Profile FOREIGN KEY (SecondProfileId) REFERENCES Profile(ProfileId)
);

INSERT INTO Account(Username, Password) VALUES('ioan', '$5$rounds=535000$2ZFeT0eS3yd35j//$xejm4M1kLWr1SzIx8ajNnSZLikVnwrsFNOQ8CINSd/2');
INSERT INTO Account(Username, Password) VALUES('tuddy', '$5$rounds=535000$2ZFeT0eS3yd35j//$xejm4M1kLWr1SzIx8ajNnSZLikVnwrsFNOQ8CINSd/2');
INSERT INTO Account(Username, Password) VALUES('sinzi', '$5$rounds=535000$2ZFeT0eS3yd35j//$xejm4M1kLWr1SzIx8ajNnSZLikVnwrsFNOQ8CINSd/2');
INSERT INTO Account(Username, Password) VALUES('alex', '$5$rounds=535000$2ZFeT0eS3yd35j//$xejm4M1kLWr1SzIx8ajNnSZLikVnwrsFNOQ8CINSd/2');

INSERT INTO Profile(AccountId, Name, ProfileType, Description ) VALUES(1, 'BMW', 'Car', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas interdum venenatis bibendum. Maecenas id porta nibh. Quisque ut lorem viverra, maximus risus sit amet, aliquet nulla. Aliquam erat volutpat. Etiam ac pellentesque ante. Mauris condimentum molestie tristique. Phasellus sit amet vehicula metus.');
INSERT INTO Profile(AccountId, Name, ProfileType, Description ) VALUES(2, 'Chevy', 'Car', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas interdum venenatis bibendum. Maecenas id porta nibh. Quisque ut lorem viverra, maximus risus sit amet, aliquet nulla. Aliquam erat volutpat. Etiam ac pellentesque ante. Mauris condimentum molestie tristique. Phasellus sit amet vehicula metus.');
INSERT INTO Profile(AccountId, Name, ProfileType, Description ) VALUES(3, 'Beatle', 'Car', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas interdum venenatis bibendum. Maecenas id porta nibh. Quisque ut lorem viverra, maximus risus sit amet, aliquet nulla. Aliquam erat volutpat. Etiam ac pellentesque ante. Mauris condimentum molestie tristique. Phasellus sit amet vehicula metus.');
INSERT INTO Profile(AccountId, Name, ProfileType, Description ) VALUES(4, 'Mercedes', 'Car', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas interdum venenatis bibendum. Maecenas id porta nibh. Quisque ut lorem viverra, maximus risus sit amet, aliquet nulla. Aliquam erat volutpat. Etiam ac pellentesque ante. Mauris condimentum molestie tristique. Phasellus sit amet vehicula metus.');

INSERT INTO Photo(ProfileId, Url) VALUES(1, 'https://www.bmw-m.com/content/dam/bmw/marketBMW_M/common/topics/magazine-article-pool/2019/bmw-m-wallpaper/bmw-m850i-individual-night-sky-gallery-01.jpg');

INSERT INTO Photo(ProfileId, Url) VALUES(2, 'https://media.apnarm.net.au/media/images/2018/09/10/b881570332z1_20180910142638_000gnu1850e21-0-q7lilirpso9msbdgxq2_fct2072x1554x622x452_t1880.jpg');
INSERT INTO Photo(ProfileId, Url) VALUES(2, 'https://drivetribe.imgix.net/RYeyMS-OS2-XkAX4R0grRg?w=1400&h=788&fm=webp&auto=compress&lossless=true&fit=crop&crop=faces');
INSERT INTO Photo(ProfileId, Url) VALUES(2, 'https://i.pinimg.com/originals/44/cb/09/44cb09ea1d4d22c32374cd04ced207c2.jpg');

INSERT INTO Photo(ProfileId, Url) VALUES(3, 'https://i.pinimg.com/originals/f8/f9/a1/f8f9a1412e58338778f8eac76dea1753.jpg');
INSERT INTO Photo(ProfileId, Url) VALUES(4, 'https://images.autotrader.com/scaler/620/420/cms/images/cars/bmw/3-series/20153seriesvs2015cclass/233385.jpg');

INSERT INTO MatchedContact(FirstProfileId, SecondProfileId, FirstProfileLike, MatchDateTime)
VALUES (1, 3, true, '2017:10:10');
INSERT INTO MatchedContact(FirstProfileId, SecondProfileId, SecondProfileLike, MatchDateTime)
VALUES (4, 1, true, '2017:11:11');
INSERT INTO MatchedContact(FirstProfileId, SecondProfileId, SecondProfileLike, MatchDateTime)
VALUES (3, 1, true, '2017:11:11');


