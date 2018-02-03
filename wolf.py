import wolframalpha
import webbrowser
key_data ='U2H3V8-WX82VX6VPY'
print("**made by AnonWiz**")
client = wolframalpha.Client(key_data)


try :
 def search(q):
  ans=''
  while True:
   res = client.query(q)
   for i in res.pods:
      for sub in i.subpod:
          ans=ans+str(sub.plaintext)+"      "
          if "'imagesource':" in str(sub):
            webbrowser.open(sub.imagesource)
   print(ans)
   process()
 def process():
    ans=''
    a=input('Wanna continue.. Y || N')
    if a=='n' or a=='N' :
     print('BYE')
     exit()
    input1()
 def input1():
  q=input(">>>")
  search(q)
except :
  print('Something went wrong..**NO RESULTS FOUND**')
  process()
input1()  
