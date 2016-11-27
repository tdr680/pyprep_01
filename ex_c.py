
# TODO 1) run this and explain:
###
#        r = 40 * "*"
#        r += "\n"
#        r += 40 * "*"
#        print r
###
#        print "a\tb\tc\td"
###
#        a = "walk east"
#        print a.split()
###
#        h = []
#        h.append((100, "12:30"))
#        h.append((-40, "12:35"))
#        print h
###
#        while (True):
#            answer = raw_input("> ")
#            if answer == "q":
#                break
#            else:
#                print answer.upper()
###
#        def what_do_i_calculate(a, b):
#            return (a**2 + b**2)**0.5
#        print what_do_i_calculate(3, 4)
###
#        a = 1
#        a *= 10
#        a /= 3
#        a -= 10
#        print a
###
#        f = open("ex_c.py")
#        print f.read().upper()
###
#        def whats_there(*a, **b):
#           print a
#           print b
#        whats_there(1, 2, 3, a=10, b=20, c=30)
###

# TODO 2) write class Address having attributes recipient_name, street_name, number, postal_code, city and country
#
# class Address(object):
#
#     def __init__(self, ...):
#         ...

#     def format(self):
#         result = 40 * "-" + "\n"
#         result += ...
#         return result
#
# a1 = Address(recipient_name = "Monsieur Pierre Dupont",
#              street_name = "Rue Pepinet",
#              number = "34c",
#              postal_code = 1003,
#              city = "Lausanne",
#              country = "Suisse")
#
# print a1.format() # should output following envelop address label like follows:
#
# ---------------------------------------
# Monsieur Pierre Dupont
# Rue Pépinet 10
# 1003 Lausanne
# Suisse

# TODO 3) write class Vector having attributes x and y. Hints: http://natureofcode.com/book/chapter-1-vectors
#
# class Vector(object):
#
#     def __init__(self, x, ...):
#         self.x = ...
#         ...
#
#     def len(self):
#         return (self.x**2...
#
#     def add(self, vector):
#         self.x += ...
#         ...
#
#     def mult(self, scalar):
#         self.x *= scalar
#         ...
#
# v1 = Vector(1, 1)
# v2 = Vector(2, 3)
# v1.add(v2)
# v1.mult(10)
# print v1.len() # prints 50.0

# TODO 4) write class Konto having attributes balance and history
#
# from datetime import datetime
#
# class Konto(object):
#
#     def __init__(self):
#         ...
#
#     def deposit(self, amount):
#         ...
#         timestamp = str(datetime.now())
#         self.history.append((amount, timestamp))
#
#     def withdraw(self, amount):
#         ...
#
# k1 = Konto()
# k1.deposit(1000)
# k1.deposit(200)
# k1.withdraw(400)
#
# print k1.balance
# print k1.history
#
# output:
# 800
# [(1000, '2016-11-27 21:07:15.835977'), (200, '2016-11-27 21:07:15.836359'), (-400, '2016-11-27 21:07:15.836377')]


