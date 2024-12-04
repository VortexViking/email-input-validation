# If you think this is ugly feel free to change it to fit your needs.

# email-input-validation
#  script writtenin python 

#  This script will validate the email input by the user. It will check only by domain @domain 

#  Some of the following domains are supported:

# - @gmail.com
# - @yahoo.com
# - @hotmail.com
# - @outlook.com
# - @aol.com
# - @icloud.com
# - @protonmail.com
# - @mail.com
# - @zoho.com
# - @yandex.com

# This only validates the proper domain. It does not validate whetger the email "username" is actually existing. 
# If you would like to add that functionality, fork the repository and make your changes. 

### Liscense under MPL2 license 


# ascii art for the email input

print('''                                        ,,    ,,                                                                             ,,    ,,        ,,                  ,,                     
`7MM"""YMM                               db  `7MM      `7MMF'                                  mm       `7MMF'   `7MF'      `7MM    db      `7MM           mm     db                     
  MM    `7                                     MM        MM                                    MM         `MA     ,V          MM              MM           MM                            
  MM   d    `7MMpMMMb.pMMMb.   ,6"Yb.  `7MM    MM        MM  `7MMpMMMb. `7MMpdMAo.`7MM  `7MM mmMMmm        VM:   ,V ,6"Yb.    MM  `7MM   ,M""bMM   ,6"Yb.mmMMmm `7MM  ,pW"Wq.`7MMpMMMb.  
  MMmmMM      MM    MM    MM  8)   MM    MM    MM        MM    MM    MM   MM   `Wb  MM    MM   MM           MM.  M'8)   MM    MM    MM ,AP    MM  8)   MM  MM     MM 6W'   `Wb MM    MM  
  MM   Y  ,   MM    MM    MM   ,pm9MM    MM    MM        MM    MM    MM   MM    M8  MM    MM   MM           `MM A'  ,pm9MM    MM    MM 8MI    MM   ,pm9MM  MM     MM 8M     M8 MM    MM  
  MM     ,M   MM    MM    MM  8M   MM    MM    MM        MM    MM    MM   MM   ,AP  MM    MM   MM            :MM;  8M   MM    MM    MM `Mb    MM  8M   MM  MM     MM YA.   ,A9 MM    MM  
.JMMmmmmMMM .JMML  JMML  JMML.`Moo9^Yo..JMML..JMML.    .JMML..JMML  JMML. MMbmmd'   `Mbod"YML. `Mbmo          VF   `Moo9^Yo..JMML..JMML.`Wbmd"MML.`Moo9^Yo.`Mbmo.JMML.`Ybmd9'.JMML  JMML.
                                                                          MM                                                                                                             
                                                                        .JMML.                  
''')

# Reference During Development
# - @gmail.com
# - @yahoo.com
# - @hotmail.com
# - @outlook.com
# - @aol.com
# - @icloud.com
# - @protonmail.com
# - @mail.com
# - @zoho.com
# - @yandex.com

domains = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@outlook.com', '@aol.com', '@icloud.com', '@protonmail.com', '@mail.com', '@zoho.com', '@yandex.com']

# Stores the input from the user
user_input = input("Enter your email address: ")

# Checks if the input matches any of the domains
if any(domain in user_input for domain in domains):
    print("Your email address is valid!")
else:
    print("Your email address is not valid!")
