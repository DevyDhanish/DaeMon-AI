import colorama

# Define constants
ERROR = "red"
GOOD = "green"
WARNING = "yellow"

art = f'''
 ______         _                 _____                                  _ 
|  ____|       | |               |  __ \\                                | |  
| |__    _ __  | |_   ___  _ __  | |__) | _ __   ___   _ __ ___   _ __  | |_ 
|  __|  | '_ \\ | __| / _ \\| '__| |  ___/ | '__| / _ \\ | '_ ` _ \\ | '_ \\ | __|
| |____ | | | || |_ |  __/| |    | |     | |   | (_) || | | | | || |_) || |_ 
|______||_| |_| \\__| \\___||_|    |_|     |_|    \\___/ |_| |_| |_|| .__/  \\__|
                                                                 | |         
                                                                 |_|         
'''

skullart = f'''

          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '

Daemon.AI
'''

# Initialize colorama
colorama.init(autoreset=True)

# Function to print colored text
def write(text, color):
    match color:
        case "red":
            print(colorama.Fore.RED + text)
            pass
        case "green":
            print(colorama.Fore.GREEN + text)
            pass
        case "yellow":
            print(colorama.Fore.YELLOW + text)
            pass
        case _:
            print(text)