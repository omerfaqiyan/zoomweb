import csv
import pandas
import mysite.core.reformatfunctions as reformatfunctions
import mysite.core.codes as codes




def zoom(relativepath):
    absolutepath= str("C:\\Users\\Tabish\\zoomweb\\media\\")
    filename=str(relativepath)
    gg=filename[:-4]
    savepath=absolutepath+gg+"-output.csv"
    with open(savepath, 'a', encoding='utf-8') as outcsv:   
        #configure writer to write standard csv file
        
        writer = csv.writer(outcsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        header=["Email", "FirstName","LastName","CompanyName","JobTitle","Address1","City","State","Country","PostalCode","WorkPhone","NumberofEmployeesRange","Designation","JobFunction","Industry","DecisionRole","CompanyWebSiteURL","RegistrationWebsite","AreaName","Brand","EXPIRY_DATE","BuyersIndex","InterestedCategories","InterestedProducts","WorkExt","ContactID"]
        writer.writerow(header)
        readpath=absolutepath+filename
        
        for chunk in pandas.read_csv( readpath,chunksize=1000):

            import numpy as np
            df1 = chunk.replace(np.nan, '', regex=True)
            df1=df1.astype(str)        
            for row in df1.itertuples():
                email=''
                firstname=''
                lastname=''
                companyname=''
                jobtitle=''
                address=''
                city=''
                state=''
                country=''
                postalcode=''
                workphone=''
                employee=''
                designation=''
                jobfunction=''
                industry=''
                decision=''
                url=''
                ext=''
                contactid=''
                
                
                contactid=row[2]
                email=row[17]
                firstname=row[6]
                lastname=row[5]
                companyname=row[27]
                jobtitle=row[10]
                city=row[20]
                state=codes.zoomcodes.StateCodes(row[21])
                country=codes.zoomcodes.CountryCodes(row[23])
                postalcode=reformatfunctions.reformat.GetPostalCode(row[22])
                
        
        
                if(len(row[19])>0):
                    address=row[19]
                elif(row[34]=="United States" or row[34]=="Canada"):
                    address=row[30]
                    city=row[31]
                    state=codes.zoomcodes.StateCodes(row[32])
                    country=codes.zoomcodes.CountryCodes(row[34])
                    postalcode=reformatfunctions.reformat.GetPostalCode(row[33])
                
                industry=codes.zoomcodes.ZoomIndustryCodes(row[35])
                if (industry==None):
                    industry=''
                jobfunction=codes.zoomcodes.ZoomJobFunctionCodes(row[12])
                if (jobfunction==None):
                    jobfunction=''
                    
                designation=codes.zoomcodes.ZoomDesignationCodes(row[13])
                if (designation==None):
                    designation=''
                    
                url=reformatfunctions.reformat.GetDomains(row[28],row[51])
        
                if(row[15].find('ext.')!= -1):
                    ext=row[15][row[15].index('ext.')+5:len(row[15])]
                    phonenumber=row[15][0:row[15].index("ext.")-1]
                    workphone=reformatfunctions.reformat.GetWorkPhones(phonenumber,row[29],row[34])
                else:
                    workphone=reformatfunctions.reformat.GetWorkPhones(row[15],row[29],row[34])
        
                employee=codes.zoomcodes.ZoomEmployeeRangeCodes(row[42])
                
                designationroles=jobfunction+designation
        
                if(len(jobfunction)!=0 and len(designation)!=0) :
                    decision=codes.zoomcodes.ZoomDecisionCodes(designationroles)
                else:
                    decision=""
        
                data=[email,firstname,lastname,companyname,jobtitle,address,city,state,country,postalcode,workphone,employee,designation,jobfunction,industry,decision,url,"www.contanuity.com","PROS-Email-Contanuity0045","Prospect","","","","",ext,contactid]
                data1 = ["" if x == "nan" else x for x in data]
        
                writer.writerow(data1)           
def reformzoom(name):

  try:
      zoom(name)
      return 1
  except:
      return 0