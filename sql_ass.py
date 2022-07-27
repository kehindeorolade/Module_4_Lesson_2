import sqlite3

#check
#print ("sqlite3 imported successfully")

konn = sqlite3.connect("sga_1_3_learners.db")

#check
#print("connection created successfully")

#create a cursor object
cursor = konn.cursor()

#check 
#print("cursor created successfully")


#create a database table
#cursor.execute(
     #"""
     #create table ds1_3_learners(
         #first_name text,
         #last_name text,
         #email_address text,
         #course text


     #)

 #"""
 #)

#check
#print("ds1_3_learners table created successfully")

Students_list = [
    ("Abubakar", "Adisa", "adisaabubakar@gmail.com", "data science"),
    ("Ade", "Afolabi", "wasola.afolabi@yahoo.com", "data science"),
    ("Adedoyin", "Abass", "doyinabass@yahoo.com", "data science"),
    ("Amure", "Faith", "amuretalodabif@gmail.com", "data science"),
    ("Angela", "Emmanuel", "akhaneyelliemmanuel@gmail.com", "data science"),
    ("Awonaike", "Tawakalitu", "purpleduralumin@gmail.com", "data science"),
    ("Awoniran", "Omowunmi", "mowunmi1@gmail.com", "data science"),
    ("Binta", "Umar", "ubinta63@yahoo.com", "data science"),
    ("Christian", "Uzondu", "bukolam.ajayi@gmail.com", "data science"),
    ("Deborah", "Idowu", "idsworld@yahoo.com", "data science"),
    ("Eniola", "Osadare", "dorcasosadare@gmail.com", "data science"),
    ("Esther", "Akapanowo", "estherakpanowo@gmail.com", "data science"),
    ("Kehinde", "Orolade", "kehindeorolade@gmail.com", "data science"),
    ("Ganiyat", "Shittu", "ganiyatas@gmail.com", "data science"),
    ("Gideon", "Uko", "ukogideon@gmail.com", "data science"),
    ("Iretioluwa", "Olawuyi", "iretioluwa.olawuyi@outlook.com", "data science"),
    ("Jide", "Adesugba", "jide_ade@hotmail.com", "data science"),
    ("Joyce", "Ezeonwu", "joyceokore@gmail.com", "data science"),
    ("Kafayat", "Ibrahim", "kafayatadenike10@gmail.com", "data science"),
    ("Olorunishola", "Deborah", "deboraholuwatobi247@gmail.com", "data science"),
    ("Placidus", "Ali", "placidusali@gmail.com", "data science"),
    ("Praise", "Emmanuel", "praiseemmanuel9ic@gmail.com", "data science"),
    ("Ekeocha", "Prince", "prince.ekeocha@gmail.com", "data science"),
    ("Ramotallah", "Jubril", "jubrilramotallah03@gmail.com", "data science"),
    ("Rashidat", "Sikiru", "rasheedatsikiru@gmail.com", "data science"),
    ("Abubakar", "Adisa", "adisaabubakar@gmail.com", "data science"),
    ("Sheriff", "Olaitan", "sheriffolaitan71@gmail.com", "data science"),
    ("Stephen", "Ogungbile", "stephenfunso@gmail.com", "data science"),
    ("Temitope", "Bamiddele", "bamideletemitope42@gmail.com", "data science"),
    ("Theresa", "Karamor", "teriekarie@gmail.com", "data science"),
    ("Tina", "Uyateide", "tinauyats@gmail.com", "data science"),
    ("Victoria", "Chukwuno", "chukwunovictoria@gmail.com", "data science")
]

#cursor.executemany(
 #"""
 #insert into ds1_3_learners
 #values(?, ?, ?, ?)

 #""",
 #Students_list 

 #)

# print("sucessful")




cursor.execute("select * from ds1_3_learners")



items = cursor.fetchall()
for item in items:
    print(item)


konn.commit()