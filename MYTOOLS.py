pi = "2.71828182845904523536028747135266249775724709369995957496696762772407663035354759457138217852516642742746639193"
pi_list = list(pi)
new_pi = []

for i in range(0,100,1):
    new_pi.append(pi_list[i+2])
    print(new_pi[i])


print(len(new_pi))

new_pi2 = "".join(str(element) for element in new_pi) 
print(new_pi2)
new_pi2 = int(new_pi2)
print(len(new_pi))
   

PI_INT = 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
E_INT = 7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274

ABC = str(PI_INT)


def pi_real(x):
    pi_int = str(PI_INT)
    pi_int = list(pi_int)
    pi_x = []
    abc = "3."
    for i in range(x):
        pi_x.append(pi_int[i])
    pix2 = "".join(str(element) for element in pi_x ) 
    pix2 = "3." + pix2
    print(pix2)
   

def e_real(x):
    pi_int = str(E_INT)
    pi_int = list(pi_int)
    pi_x = []
    abc = "3."
    for i in range(x):
        pi_x.append(pi_int[i])
    pix2 = "".join(str(element) for element in pi_x ) 
    pix2 = "2." + pix2
    print(pix2)

pi_real(5)
e_real(4)