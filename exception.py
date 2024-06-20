# myname="eMobilis"

# for i in myname:
#     if i !=k:
#         print(i)
jina=['banana', 'mangoes', 'apples']

for i in range(5):
    print(i,jina[i])
try:
    result = 1 / 0
except ZeroDivisionError as e:
    # code to handle exception
    print(f"An error has occurred {e}")
finally:
    # code that runs no matter what
    print("This will always be printed")