
import requests




def scanheader(url):
    response=requests.get(url)
    header=response.headers
    print(header)



    checks={
        'X-Content-Type-Options': "Missing this can allow MIME-type attacks.",
        'Strict-Transport-Security': "Missing this weakens HTTPS implementation.",
        'Content-Security-Policy': "Missing this increases risk of XSS attacks.",
        'X-Frame-Options': "Missing this can allow clickjacking attacks.",
        'Referrer-Policy': "Missing this can leak information about previous pages.",
        'Permissions-Policy': "Missing this can allow misuse of APIs or features.",
        'Access-Control-Allow-Origin': "Missing this may result in cross-origin issues.",
        'Secure-Transport-Security': "Missing this can weaken secure transport security.",
        'Cross-Origin-Resource-Policy': "Missing this can expose resources to unauthorized cross-origin requests."
}

    
    grade=90
    for missing,Warning in checks.items():
        if missing not in header:
            print(f"missing {missing}")
            grade= grade -10

        else: 
            print(f"presented :{ missing}")
            if(missing=='Strict-Transport-Security'):
                value=response.headers.get(missing)
                svalues=value.lower()
                print("the value of value is :",svalues)
                result1 = False
                result2 = False
                if value:
                    if "includesubdomains" in svalues:
                        result1=True
                        parts=value.split(";")
                        for part in parts:
                            if "max-age" in part:
                                pairs=part.split("=")
                                number=int(pairs[1])
                                print (number)
                                if number > 1036800:
                                    result2=True
                if result1 and result2:
                    print("   strict-transport-security is secure")
                else:
                    print("   Strict-Transport-Security is not secure")

            if missing=="Content-Security-Policy":
                csp= response.headers.get(missing)
               
                if "default-src 'self' " in csp and 'script-src' in csp:
                    print("Content security policy is secured")
        
                else:
                    print("average secured")

            if missing=="X-Frame-Options":
                xframe=response.headers.get(missing)
                if "X-Frame-Options" or "DENY" in xframe:
                    print("  X-frame-option is secured")
            if missing=="Referrer-Policy":
                referrer=response.headers.get(missing)
                print(referrer)
                if "no-referrer" in referrer or "same-origin" in referrer:
                    print("full secured Referrer policy")
                elif "origin-when-cross-origin" in referrer:
                    print("average secured")
                else:
                    print("not secured")





# 'Referrer-Policy': 'origin-when-cross-origin', 









    # print(grade)
    # if grade ==60:
    #     print(" The website grade is A")
    # elif grade==50:
    #     print(" The website grade is b")
    # elif grade==40:
    #     print(" The website grade is c") 
    # elif grade==30:
    #     print("The website grade is c")
    # elif grade==20:
    #     print("The website grade is D")    
    # elif grade==10:
    #     print("The website grade is e")
    # elif grade==0:
    #     print("The website grade is F")
    # else:
    #     print("perfect grade")







if __name__ =="__main__":
    url="https://www.binance.com/en"
    scanheader(url)
