import re
class reformat:
  
 def GetPostalCode(postalcode):
     postalcode=re.sub(r"\s+", "", postalcode, flags=re.UNICODE)
     postalcode=re.sub(r"-", "", postalcode, flags=re.UNICODE)


     

     zipcode=""
     if(len(postalcode)==5 and postalcode.isdecimal()):
         zipcode=postalcode
     elif(len(postalcode)==4):
         zipcode="0"+postalcode
     elif(len(postalcode)>5 and postalcode.isdecimal()):
         zipcode=postalcode[0:5]    
     elif(bool(re.match('[a-zA-Z0-9]', postalcode) )) :
         zipcode=postalcode
     
     
     
     
     return zipcode

 
 def GetDomains(domains, emaildomain):
     domain=""
     if(len(domains)==0):
         domain=emaildomain

     else:
         domain=domains.replace("www.",'')

     return domain


 def GetWorkPhones(directphone, companyphone, mulk):
     number=""
     if (len(directphone)!=0):
         number=directphone
     elif(mulk=="United States" or mulk=="Canada"):
         number=companyphone
    
     result = re.sub('[^0-9]','', number)
     return result
