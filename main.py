# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# 1 exercise
def greet(name, greeting="Hello, <name>!"):
    greeting_arg= greeting[:greeting.find(",")]
    greeting_name= (F'{greeting_arg}, {name}!')
    
    print (greeting_name)
    
    return greeting_name

greet ('Lala')

# 2 exercise
def force (mass= float, body='Earth'):
    body_dic = {
        "Earth": 9.798,
        "Sun": 274,
        "Jupiter": 24.92,
        "Neptune": 11.15,
        "Saturn": 10.44,
        "Uranus": 8.87,
        "Venus": 8.87,
        "Mars": 3.71,
        "Mercury": 3.7,
        "Moon": 1.62,
        "Pluto": 0.58
    }
    
    gravity = round (body_dic.get(body),1)
    # print(gravity)
    force_tot= mass * gravity
    force_tot= ("{0:.2f}".format(force_tot))
    print (force_tot)
    return force_tot

force (0.1)

# 3 exercise
def pull (m1=float,m2=float,d=float):
    gravitational_constant = 6.674*10**-11
    Pull_Tot= gravitational_constant*(m1*m2/d**2)
    print (Pull_Tot)
    return Pull_Tot

pull (800,1500,3)