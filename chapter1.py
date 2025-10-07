# On Dictionary and Sets

# A = {
#     "Name":"Lucky",
#     "Course":"BCA",
#     "From":"India",
#     25: 30
# }


# # print(A["Lucky"])
# # print(A.keys()) # returns what is stored on the left hand !!

# # B = A.copy()
# # print(B)

# # C= A.keys()
# # print(C)

# #Difference bw item and value 

# # C = A.items()
# # print(C)                print Every item :)

# # C= A.values()
# # print(C)                only prints the right hand side of dictionary

# C = A.pop("Name")
# print(C)                Jo bi key ke samne ka element hoga ussse return kr degi 

# C = A.popitem()
# print(C)         last mai bhara element remove kr deta hain!
# print(A)  from this particular line we got to know that dictionary is mutable!

# # C = A.update({"Height":5.8})
# # print(A)         add element in the end of the dictionary

# # C = A.setdefault("Height", )  ye bi dictionary ke end mai value add krta hai, maine yaha height ...
# #                             ....ke aage kuch nahi likha toh woh none return krega uss jagah pr
# # D =  A.setdefault("Lord", 0) yaha naya dict. ban jayegi 
# # print(A)

# # C = A.get("Name")  will get Lucky in return !!
# # print(C)












# -----------------------------------------------------------------------------------------------
# To Study Sets !!!


# A = set()
# print(type(A))  ^^empty sets bnane ka tarika^^



# B = {'apple', 'banana', 'cherry'}
# print(B)  # Output: (order varies)



#Methos on Sets/Operation on Sets

# A = {1,8,4,3,7,6,5,7,9}  # ^^this is the way to create a set with value ^^
# A.pop()   Remove random element from set.
# print(A)

# A = {"Lucky", "Vaid", "Radius", "Tailgating", "Raming"}
# A.add("Posture")
# print(A)


# A = {1,2,4,5,6,7,8}
# B = {4, 5, 6, 7}
# print(A.union(B)) when A | B, "|" symbol of union

# A = {1,2,4,5,6,7,8}
# B = {4, 5, 6, 7} 
# print(A | B)                with symbol

# A = {1,2,4,5,6,7,8}
# B = {4, 5, 6, 7}
# print(B.union(A))  when B | A, same as above!

# A = {1,2,4,5,6,7,8}
# B = {4, 5, 6, 7}       
# print(A.intersection(B))  Elements which are common on both sets !

# A = {1,2,4,5,6,7,8}
# B = {4, 5, 6, 7}
# print(A&B)                       with symbol

# A = {1,2,4,5,6,7,8}
# B = {4, 5, 6, 7}
# print(B.intersection(A))  Same as above doesnt matter the order :)

# A = {1,2,4,5,6,7,8}
# B = {4, 5, 6, 7}
# print(A - B)      Gives the element which are not present in B set, vice versa !!

# A = {1,2,3,4,5}
# B = {4,5,6,7,8,9}
# print(A.symmetric_difference(B))   Gives the value which are unique only for a set (not present in another)


# A = {1,2,3,4,5}
# B = {4,5,6,7,8,9}
# print(A.issubset(B))  Will return False

# A = {1,2,3,4,5}
# B = {1,2,3}
# print(B.issubset(A))  will return True

# A = {1,2,3,4,5}
# B = {1,2,3}     
# print(B<=A)   Same as above but with the Symbol  "<="

# A = {1,2,3,4,5}
# B = {1,2,3}
# print(B.issuperset(A))  B ke pass A ke sare element nhi hai eisliye False return hoga

# A = {1,2,3,4,5}
# B = {1,2,3}
# print(A.issuperset(B))   will return True

# A = {1,2,3,4,5}
# B = {1,2,3}
# print(A.isdisjoint({5}))   Ye given value ki existence nahi hogi toh true agr set mai hogi toh false return krega
 
# A = {1,2,3,4,5}
# print(25 in A)  
# Ye check krta hain ki A set ke andr x,y,z element hai ke nahi similar to disjoin lakin disjoint nah hone pr true return krega lakin 
# "in " uss value ke set mai hone pr True krega 









#------------------------------------------------------------------------------------------------------
#   Practice set



# A ={ 
#     "Nam":"Name",
#     "Ungli":"Finger",
#     "Ladki":"Girl"
# }

# B = input("Enter the word: ")
# print(A[B])


# A = set()

# B = int(input("Enter the No.1: "))
# A.add(B)
# C = int(input("Enter the No.2: "))
# A.add(C)
# D = int(input("Enter the No.3: "))
# A.add(D)
# E = int(input("Enter the No.3: "))
# A.add(E)
# F = int(input("Enter the No.4: "))
# A.add(F)
# G = int(input("Enter the No.5: "))
# A.add(G)
# H = int(input("Enter the No.6: "))
# A.add(H)
# J = int(input("Enter the No.7: "))
# A.add(J)

# print(A)

# A = {"18", 18}
# print(A)

# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(len(s))

# s = {}
# print(type(s))


# A = {}

# B = input("Enter your name: ")
# C = input("Enter your caste: ")
# A.update({B:C})

# D = input("Enter your name: ")
# E = input("Enter your caste: ")
# A.update({D:E})

# F= input("Enter your name: ")
# G= input("Enter your caste:")
# A.update({F:G})

# H= input("Enter your name: ")
# I= input("Enter your caste: ")
# A.update({H:I})

# J= input("Enter your name: ")
# K= input("Enter your caste: ")
# A.update({J:K})

# print(A)  Agr dosto ke dale hue name unique hain toh ye




# A = {}

# B = input("Enter your name: ")
# C = input("Enter your caste: ")
# A.update({B:C})

# D = input("Enter your name: ")
# E = input("Enter your caste: ")
# A.update({D:E})

# F= input("Enter your name: ")
# G= input("Enter your caste:")
# A.update({F:G})

# H= input("Enter your name: ")
# I= input("Enter your caste: ")
# A.update({H:I})

# J= input("Enter your name: ")
# K= input("Enter your caste: ")
# A.update({J:K})

# print(A)       agr same name repeat hoga user ki taraf se toh last mai dala hua update ho jayega phele wale se!!




# A = {}

# B = input("Enter your name: ")
# C = input("Enter your caste: ")
# A.update({B:C})

# D = input("Enter your name: ")
# E = input("Enter your caste: ")
# A.update({D:E})

# F= input("Enter your name: ")
# G= input("Enter your caste:")
# A.update({F:G})

# H= input("Enter your name: ")
# I= input("Enter your caste: ")
# A.update({H:I})

# J= input("Enter your name: ")
# K= input("Enter your caste: ")
# A.update({J:K})

# print(A)   
#-------------------------------------------------------------------------------------------------------------








# CONDITIONAL EXPRESSION





# A = int(input("Enter your age: "))

# if(A>=18):
#     print("Yes")

# elif(A<0):    
#     print("Age is invalid")

# elif(A<18):
#     print("You are Minor")



# number1 = int(input("Enter the No.1: "))
# number2 = int(input("Enter the No.2: "))
# number3 = int(input("Enter the No.3: "))
# number4 = int(input("Enter the No.4: "))

# if(number1>number2 and number1>number1 and number1>number4):
#     print("This is the Greatest Number:",number1)

# elif(number2>number1 and number2>number3 and number2>number4):
#     print("This is the Greatest Number:",number2)

# elif(number3>number1 and number3>number2 and number3>number4):
#     print("This is the Greatest Number:",number3)

# elif(number4>number1 and number4>number3 and number4>number2):
#     print("This is the Greatest Number:",number4)




# subject1 = int(input("Enter Marks for Subject 1: "))
# subject2 = int(input("Enter Marks for Subject 2: "))
# subject3 = int(input("Enter Marks for Subject 3: "))

# Sumup = (((subject1+subject2+subject3)/300)*100)

# if(Sumup>=40 and subject1>=33 and subject2>=33 and subject3>=33):
#     print("Congratulation you are passed", Sumup)

# elif(Sumup<40):
#     print("You are Failed")

# elif(subject1<33 or subject2<33 or subject3<33):
#     print("You are fail")




# a1= "make a lot of money"
# a2= "buy now"
# a3= "subscribe this"
# a4= "click this"

# user_input = input("Enter your comment: ")

# if(a1 in user_input.lower() or a2 in user_input.lower() or a3 in user_input.lower() or a4 in user_input.lower()):
#     print("This is Spam !!")

# else:
#     print("This is not a Spam :)")    




# user_input = input("Enter your password here: ")
# B= len(user_input)

# if(B>=10):
#     print("Your password is Strong")

# elif(B<10):
#     print("Your password is weak")    



# Name = ["Lucky", "Anuj", "Anubhav", "Ramniwas", "Riya", "Neel", "Harry"]

# user_input = input("Enter the Name: ")

# # if(Name in user_input):
# #     print("You are in the list")  ye eisliye galat hai kyuki ye puri list Lucky hai ya nahi check krega but ye niche wala

# if(user_input in Name):
#     print("You are in the list")
# else:
#     print("You are not in the list")    



# marks1 = int(input("Enter the Marks for subject: "))


# if(marks1<=100 and marks1>=90):
#     print("Excellent Grade")

# elif(marks1<=90 and marks1>=80):
#     print("A Grade")

# elif(marks1<=80 and marks1>=70):
#     print("B Grade")

# elif(marks1<=70 and marks1>=60):
#     print("C Grade")

# elif(marks1<=60 and marks1>=50):
#     print("D Grade")

# elif(marks1<=50):
#     print("F Grade")




# a = "Lucky"
# user_input = input("Enter here: ")

# if(a.lower() in user_input.lower()):
#     print("You are talking about Lucky")

# else:
#     print("You are not talking about Lucky")   


