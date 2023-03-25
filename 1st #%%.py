# 
# from cgitb import text


# my_dist={}
# my_dist['animal']=['cats']
# my_dist['cast']=['openeds']
# print(my_dist)
# print(my_dist.keys())
# print(my_dist.values())
# # print(len(my_dist))
# my_tupple=(1,3,'fds',4,'fds',5,)
# print(my_tupple.index('fds'))
# print(my_tupple.count('fds'))

# my_file=open("sahil.txt","x")
# my_file.write("jd sh vs        hhfia")
# my_file.close()
# my_file=open("sahil.txt","r")
# my_file.read()
# myfile = open("c:\\Users\\slord\\Desktop\\firstcode.py\\1st.py")

# num1=5
# my_list=(1,3,4,5,6,7,8,8,9,90,2)
# for num in my_list:   
#    if num>num1:
#     print(num)

#    else:
#     print(f"less than {num1}")

# # /////////////////////////////////////////////////////////////
# month_dict={1:"january",2:"february",3:"march",4:"april",5:"may",6:"june",7:"july",8:"august",9:"september",10:"october",11:"november",12:"december"}
# for month in month_dict:
 
#     if month==2:
#       print(f"there are 28 days and in leap year there are 29 days in month {month}")
#     elif month<=7 and month%2==0 or month>7 and month%2==1:
#       print(f"there are 30 days in month {(month)}")
#     elif month<=7 or month>7 and month%2==0:
#       print(f"there are 31 days in month {(month)}")   

 # print(month_dict.value())
# //////////////////////////////////////////////////////////////////

# month_list=("january","feb","march","april","may","june","july","august","sep","oct","nov","dec")
# for month in month_list: 
#     if month=="feb":
#         print("month has 28 days and in leap year there are 29 days")
#     elif month=="january" or month=="march"or month=="may" or month=="oct" or month=="july" or month=="augest" or month=="dec":
#         print("months has 31")
#     else:
#         print("months has 30 days")

# ///////////////////////////////////////////////////////////////////////////////////
# month=int(input("enter the no:"))
# if month==2:
#       print(f"There are 28 days and in leap year there are 29 days in month {month}th")
# elif month<=7 and month%2==0:
#       print(f"There are 30 days in month {month}th")
# elif month<=7 :
#       print(f"There are 31 days in month {month}th")
# elif month>7 and month%2==0:
#       print(f"There are 31 days in month {month}th")
# elif month>12:
#       print("Don't you know there are only 12 months")
# else  :
#       print(f"There are 30 days in month {month}th ")
      


# x=int(input("1st prize count number of players"))
# y=int(input("2nd prize count number of players"))
# z=int(input("3rd prize count number of players"))
# count=int(input(" count number of player"))

# if count%z==0:
#       print("3rd prize")

# elif count%y==0:
#       print("2nd prize")

# elif count%x==0:
#       print("1st prize")




# mylist=[num for num in range(1,10)]
# print (mylist)



# result = [x if x%2==0  else "odd number" for x in range(1,11)]
# print (result)


# st='print only those words which start with s'
# for x in st.split():
#     if x[0]=='s':
#         print(x)


# for num in range(0,10):
#     if num%2==0:
#         print (num)
# for num in range(0,10,2):
#      print (num)



# for num in range(1,100):
#     if num%3==0 and num%5==0:
#         print("fizzbuzz") 
#     elif num%3==0:
#         print("fizz") 
#     elif num%5==0:
#         print("buzz") 
#     else :
#         print(num)


# st=' high   - low - medium  - low - high djhesk hgr nhfrb n'
# for word in st.split():
#     if word[0]=='h':
#         print(word)

# for num in range(0,11,2):
#    print(num)

# print(list(range(0,50,3))

# print([x for x in range(1,50) if x%3==0])

# s="dsd fsf d wd  d ede d  es  aqsakds  s s s sskeds sdk xwsd e swi s s"
# print([word[0] for word in s.split()])

# t=int(input("total no. of items"))
# tw=int(input(" total weight of the items"))
# for i in range(t):
   
#       x=(str(input("name of the items")))
   
# # print (x)
# #%%
# def sahil_1st_fun():
#     print("sahiil 1st function")
#     return sahil_1st_fun

# #%%
# sahil_1st_fun()


# def sahil_1st_fun_shuffle():
    
# #     sahil=[' ','0',' ']
# #     from random import shuffle
# #     shuffle(sahil)
# #     return sahil


# # def sahil_2nd_fun_input():
# #    taken_input=(int(input("please enter your guess as 0,1 or 2 : ")))
# #    print(taken_input)
# #    shuffle_sahil=sahil_1st_fun_shuffle()
# #    return shuffle_sahil[taken_input]




# # def sahil_3nd_fun_main():
# #     y=sahil_2nd_fun_input()
# #     if y==0:
# #         print("your guess is correct") 
# #     else :
# #         print("is the correct guess")
# #         sahil_1st_fun_shuffle()



# # sahil_3nd_fun_main()
# #%%
# def myfunc(*args):
#     z=[]
#     for i in args:
#         if i%2==0:
#             z.append(i)
#     return z

    
# myfunc(1,8,3,4,5,6)


# #%%
# def myfunc(a):
#     x=[]
#     for i in range(len(a)):
#         if i%2==0:
#             x.append(a[i].lower())
#         else:
#             x.append(a[i].upper())

#     return ''.join(x)
                 
            

# myfunc("sahil")
#  # %%


# def myfunc(a,b):
#     if a<b:
#         x=a
#     else:x=b

#     if a%2==0 & b%2==0:
#         return x
    
#     else:
#         if a>b:
#             x=a
#         else:x=b
#     return x
    

# myfunc(5,2)



# # %%
# def myfunc(a,b):
#     if a[0]==b[0]:
#         return True
#     else:return False

# myfunc("sahil","lord")
# # %%
# def myfunc(a,b):
#     if a+b==20 or a==20 or b==20:
#         return True
#     else:return False

# myfunc(19,1)

# # %%

# def myfunc(a):
#     x=[]
#     for i in range(0,len(a)):
#         if a[i]==a[0] or a[i]==a[3]:
#             x.append(a[i].upper())
#         else:
#             x.append(a[i])

#     return ''.join(x)

# myfunc('sahil')

# # %%
# def myfunc(a):
#     x=[]
#     for i in a.split()[::-1]:
#         x.append(i)
#     return ' '.join(x)

# myfunc('sahil is my name')
# # %%
# def myfunc(a):
#     return ' '.join(a.split()[::-1])
# myfunc('sahil is my name')
# # %%

# def myfunc(a):
#     x=(abs(100 -a)<=10) or (abs(200 -a)<=10)

#     return x

# myfunc(190)
# # %%
# def myfunc(*args):
#     for i in range(0, len(args)):
#         if args[i] ==3 and args[i+1] ==3:
#             return True
#         else :
#             pass
#     return False

# myfunc(3,33,6,3,3,22,4,5)

# # %%

# def myfunc(a,b,c):
#     if sum((a,b,c))<=21:
#         return sum((a,b,c))
#     elif sum((a,b,c))>=21 and 11 in (a,b,c):
#         x=sum((a,b,c))-10
#         while x>21:
#             return "bust"
#         return x
    
# myfunc(5,5,7)

                                           

# #%%

# def myfunc(*args):

#     x=0
#     y=True
#     for  i in args:
#         while   y:
#             if i!=6:
#                 x+= i
#                 break
                
#             else :
#                 y=False
#                 break
#         while not y:
#             if i!=9:
#                 break
#             else :
#                 y=True
#                 break
#     return x

# myfunc(1,2,6,6,7,8,9,1,3)



# # %%
# def myfunc(*args):
#     for i in range(len(args)):
#         if args[i]==0:
#             for j in range(i+1,len(args)):
#                 if args[j]==0:
#                     for k in range(j+1,len(args)):
#                         if args[k]==7:
#                             return True
#         else:
#             pass
#     return False

# myfunc(1,2,6,7,8,9,0,2,0,5,5,7)

# #%%
# def myfunc(a):
#     import sympy
#     x=list(sympy.primerange(0,a))
#     return x,len(x)
# myfunc(100)




# # %%
# def myfunc(a):
#     return  a**2>20
# list(filter(myfunc,num))
# # %%
# num=91,2,3,4,5,6
# list(map(lambda x:x**2,num))
# # %%

# # 
# #%%
# def myfunc(r):
#     pi= 3.14
#     x=(4/3)*(pi)*(r**3)
#     return x
# myfunc(2)
# # %%
# def myfunc(a,low, high):
#     return low<a<high
        
# myfunc(4,2,6)
# # %%

# # %%
# def func(a):
#     x=0
#     y=0
#     for i in a.split():
#         for j in i:
#             if j ==j.upper():
#                 x+=1
#             elif j ==j.lower():
#                 y+=1
#             else:
#                 pass
#     return 'total no. of lower numbers: %d' %x +'total no. of upper numbers: %d' %y

# func("hist is my F")
# # %%
# def myfunc(a):
#     x=[]
#     for i in range(len(a)):
#         if a[i] not in x:
#                 x.append(a[i])
#         else:
#             pass
#     return x


# myfunc([1,1,3,4,4,33,34,4,4,2])


# # %%
# def myfunc(*a):
#     x=1
#     for i in range(len(a)):
#         x*=a[i]
#     return x
# myfunc(1,1,3,-3,4,)
# # %%
# def myfunc(a):
#     return a==a[::-1]
# myfunc("cannac")
# %%
# def no_extra(a):
#     x=[]
#     for i in range(len(a)):
#         if a[i] not in x:
#                 x.append(a[i])
#         else:
#             pass
#     return x

# def myfunc(args):
#         alpha=("abcdefghijklmnopqrstuvwxyz")
#         args=args.replace(" ",'')
#         # args=no_extra(args)
#         print(set(alpha)==set(args))
#         print (args)
#         print(alpha)
                 

# myfunc("the quick brown fox jumps over the lazy dog")


#%%
def tic_tac_too_input():
    count1="sahil"
    count2="katkar"

    count1=(input("enter the row number(0,1 or 2):\n"))
    while count1.isdigit()==False:
        print("please enter number :\n")
        count1=(input("enter the row number(0,1 or 2):\n"))

    while count1 not in ['0','1','2']:
        print("please enter number (0,1 o 2):\n")
        count1=(input("enter the row number(0,1 or 2):\n"))


    
    count2=(input("enter the column number(0,1 or 2)\n"))
    while count2.isdigit()==False :
        print("please enter number  :\n")
        count2=(input("enter the column number(0,1 or 2):\n"))
    
    if count2 not in ['0','1','2']:
        print("please enter number (0,1 or 2):\n")
        count1=(input("enter the column number(0,1 or 2):\n"))
    
    return int(count1),int(count2)



def main():
 row0=[' ',' ',' ']
 row1=[' ',' ',' ']
 row2=[' ',' ',' ']
 play=input("if playing, press 'y' else press 'n':\n")
 if play=='y':

    
   
    print(row0)
    print(row1)
    print(row2)
 
 
    num=tic_tac_too_input()
    
 
    def entry():
      if num[0]==0 and row0[num[1]]==' ':
           row0[num[1]]='x'
      elif num[0]==1 and row1[num[1]]==' ':
          row1[num[1]]='x'
      elif num[0]==2 and row2[num[1]]==' ':
         row2[num[1]]='x'
      else:
          print(" its already occupied plz \nEnter 1st players choice symbol(o) again:\n")
          num=tic_tac_too_input()
          entry()
    
    entry()


    print(row0)
    print(row1)
    print(row2)


    num=tic_tac_too_input()
    

    def entry1():
     if num[0]==0 and row0[num[1]]==' ':
         row0[num[1]]='o'
     elif num[0]==1 and row1[num[1]]==' ':
         row1[num[1]]='o'
     elif num[0]==2 and row2[num[1]]==' ':
         row2[num[1]]='o'
     else:
         print(" its already occupied plz \nEnter 2st players choice symbol(o):\n")
         num=tic_tac_too_input()
         entry1()

    entry1()

    print(row0)
    print(row1)
    print(row2)
    main()

 elif play=='n':
    print ("have a good day")
 
 else:
    main()


main()





# %%
