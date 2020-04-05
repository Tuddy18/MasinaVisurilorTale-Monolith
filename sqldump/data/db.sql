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


CREATE TABLE IF NOT EXISTS Message (
    MessageId INT(50) NOT NULL AUTO_INCREMENT,
    MatchedContactId INT(50) NOT NULL,
    MessageDateTime DATETIME NOT NULL,
    MessageText VARCHAR(500) NOT NULL,
    MessageOwner INT(50) NOT NULL,
    CONSTRAINT PK_Message PRIMARY KEY (MessageId),
    CONSTRAINT FK_Message_MatchedContact FOREIGN KEY (MatchedContactId) REFERENCES MatchedContact(MatchedContactId),
    CONSTRAINT FK_Message_Owner FOREIGN KEY (MessageOwner) REFERENCES  Profile(ProfileId)
);

-- INSERT MOCKUP CARS INTO DB

INSERT INTO Account(Username, Password) VALUES('bmw', '$5$rounds=535000$2ZFeT0eS3yd35j//$xejm4M1kLWr1SzIx8ajNnSZLikVnwrsFNOQ8CINSd/2');
INSERT INTO Account(Username, Password) VALUES('chevy', '$5$rounds=535000$2ZFeT0eS3yd35j//$xejm4M1kLWr1SzIx8ajNnSZLikVnwrsFNOQ8CINSd/2');
INSERT INTO Account(Username, Password) VALUES('beetle', '$5$rounds=535000$2ZFeT0eS3yd35j//$xejm4M1kLWr1SzIx8ajNnSZLikVnwrsFNOQ8CINSd/2');
INSERT INTO Account(Username, Password) VALUES('mercedes', '$5$rounds=535000$2ZFeT0eS3yd35j//$xejm4M1kLWr1SzIx8ajNnSZLikVnwrsFNOQ8CINSd/2');

INSERT INTO Profile(AccountId, Name, ProfileType, Description ) VALUES(1, 'BMW', 'car', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas interdum venenatis bibendum. Maecenas id porta nibh. Quisque ut lorem viverra, maximus risus sit amet, aliquet nulla. Aliquam erat volutpat. Etiam ac pellentesque ante. Mauris condimentum molestie tristique. Phasellus sit amet vehicula metus.');
INSERT INTO Profile(AccountId, Name, ProfileType, Description ) VALUES(2, 'Chevy', 'car', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas interdum venenatis bibendum. Maecenas id porta nibh. Quisque ut lorem viverra, maximus risus sit amet, aliquet nulla. Aliquam erat volutpat. Etiam ac pellentesque ante. Mauris condimentum molestie tristique. Phasellus sit amet vehicula metus.');
INSERT INTO Profile(AccountId, Name, ProfileType, Description ) VALUES(3, 'Beetle', 'car', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas interdum venenatis bibendum. Maecenas id porta nibh. Quisque ut lorem viverra, maximus risus sit amet, aliquet nulla. Aliquam erat volutpat. Etiam ac pellentesque ante. Mauris condimentum molestie tristique. Phasellus sit amet vehicula metus.');
INSERT INTO Profile(AccountId, Name, ProfileType, Description ) VALUES(4, 'Mercedes', 'car', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas interdum venenatis bibendum. Maecenas id porta nibh. Quisque ut lorem viverra, maximus risus sit amet, aliquet nulla. Aliquam erat volutpat. Etiam ac pellentesque ante. Mauris condimentum molestie tristique. Phasellus sit amet vehicula metus.');


INSERT INTO Photo(ProfileId, Url) VALUES(1, 'https://www.bmw-m.com/content/dam/bmw/marketBMW_M/common/topics/magazine-article-pool/2019/bmw-m-wallpaper/bmw-m850i-individual-night-sky-gallery-01.jpg');

INSERT INTO Photo(ProfileId, Url) VALUES(2, 'https://media.apnarm.net.au/media/images/2018/09/10/b881570332z1_20180910142638_000gnu1850e21-0-q7lilirpso9msbdgxq2_fct2072x1554x622x452_t1880.jpg');
INSERT INTO Photo(ProfileId, Url) VALUES(2, 'https://drivetribe.imgix.net/RYeyMS-OS2-XkAX4R0grRg?w=1400&h=788&fm=webp&auto=compress&lossless=true&fit=crop&crop=faces');
INSERT INTO Photo(ProfileId, Url) VALUES(2, 'https://i.pinimg.com/originals/44/cb/09/44cb09ea1d4d22c32374cd04ced207c2.jpg');

INSERT INTO Photo(ProfileId, Url) VALUES(3, 'https://i.pinimg.com/originals/f8/f9/a1/f8f9a1412e58338778f8eac76dea1753.jpg');
INSERT INTO Photo(ProfileId, Url) VALUES(4, 'https://images.autotrader.com/scaler/620/420/cms/images/cars/bmw/3-series/20153seriesvs2015cclass/233385.jpg');

-- INSERT MOCKUP DRIVERS INTO DB

INSERT INTO Account(Username, Password) VALUES('ioan', '$5$rounds=535000$2ZFeT0eS3yd35j//$xejm4M1kLWr1SzIx8ajNnSZLikVnwrsFNOQ8CINSd/2');
INSERT INTO Account(Username, Password) VALUES('tuddy', '$5$rounds=535000$2ZFeT0eS3yd35j//$xejm4M1kLWr1SzIx8ajNnSZLikVnwrsFNOQ8CINSd/2');
INSERT INTO Account(Username, Password) VALUES('sinzi', '$5$rounds=535000$2ZFeT0eS3yd35j//$xejm4M1kLWr1SzIx8ajNnSZLikVnwrsFNOQ8CINSd/2');
INSERT INTO Account(Username, Password) VALUES('alex', '$5$rounds=535000$2ZFeT0eS3yd35j//$xejm4M1kLWr1SzIx8ajNnSZLikVnwrsFNOQ8CINSd/2');

INSERT INTO Profile(AccountId, Name, ProfileType, Description) VALUES(5, 'Ioan', 'driver', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas interdum venenatis bibendum. Maecenas id porta nibh. Quisque ut lorem viverra, maximus risus sit amet, aliquet nulla. Aliquam erat volutpat. Etiam ac pellentesque ante. Mauris condimentum molestie tristique. Phasellus sit amet vehicula metus.');
INSERT INTO Profile(AccountId, Name, ProfileType, Description ) VALUES(6, 'Tuddy', 'driver', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas interdum venenatis bibendum. Maecenas id porta nibh. Quisque ut lorem viverra, maximus risus sit amet, aliquet nulla. Aliquam erat volutpat. Etiam ac pellentesque ante. Mauris condimentum molestie tristique. Phasellus sit amet vehicula metus.');
INSERT INTO Profile(AccountId, Name, ProfileType, Description ) VALUES(7, 'Sinzi', 'driver', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas interdum venenatis bibendum. Maecenas id porta nibh. Quisque ut lorem viverra, maximus risus sit amet, aliquet nulla. Aliquam erat volutpat. Etiam ac pellentesque ante. Mauris condimentum molestie tristique. Phasellus sit amet vehicula metus.');
INSERT INTO Profile(AccountId, Name, ProfileType, Description ) VALUES(8, 'Alex', 'driver', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas interdum venenatis bibendum. Maecenas id porta nibh. Quisque ut lorem viverra, maximus risus sit amet, aliquet nulla. Aliquam erat volutpat. Etiam ac pellentesque ante. Mauris condimentum molestie tristique. Phasellus sit amet vehicula metus.');

INSERT INTO MatchedContact(FirstProfileId, SecondProfileId, FirstProfileLike, MatchDateTime)
VALUES (1, 3, true, '2017:10:10');
INSERT INTO MatchedContact(FirstProfileId, SecondProfileId, SecondProfileLike, MatchDateTime)
VALUES (4, 1, true, '2017:11:11');

insert into Message(MatchedContactId, MessageDateTime, MessageText, MessageOwner) value (1, '2018:10:10', 'ola', 1);

INSERT INTO Photo(ProfileId, Url)
VALUES (5, 'https://scontent.fclj2-1.fna.fbcdn.net/v/t1.0-9/p720x720/33513676_2012272232156426_7800492690730123264_o.jpg?_nc_cat=101&_nc_sid=85a577&_nc_ohc=xVKdrOGtaa4AX9qWypA&_nc_ht=scontent.fclj2-1.fna&_nc_tp=6&oh=ec9aa9b5423a182f52e81702aad6fec1&oe=5EAFC1F1'),
(6, 'https://scontent.fclj2-1.fna.fbcdn.net/v/t1.0-9/p960x960/37671320_1341827289253065_1612336641383333888_o.jpg?_nc_cat=104&_nc_sid=85a577&_nc_ohc=-tUaKMlCWrIAX9TNOIL&_nc_ht=scontent.fclj2-1.fna&_nc_tp=6&oh=81ba33b05fc417857913c7a731fbd814&oe=5EAD9B3D'),
(7, 'https://www.cowichanvalleycitizen.com/wp-content/uploads/2019/10/18804160_web1_praying-racoon-photo-winner-crop.jpg'),
(7, 'https://www.nps.gov/guis/images/110617_Racoon_Odom_01.jpg'),
(7, 'https://cdn.myalgoma.ca/wp-content/uploads/2019/09/racoon-1024x539.png'),
(8, 'https://scontent.fclj2-1.fna.fbcdn.net/v/t1.0-9/22448357_1743402509011466_2330955659544705067_n.jpg?_nc_cat=101&_nc_sid=85a577&_nc_ohc=SqOWmpy4M3gAX9pF6ea&_nc_ht=scontent.fclj2-1.fna&oh=236855cb6d0ddd8575e9206b06a63f0a&oe=5EAE7A74');


