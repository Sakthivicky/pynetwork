
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
        'Access-Control-Allow-Origin': "Missing this may result in cross-origin issues."

    }
    grade=70
    for missing,Warning in checks.items():
        if missing not in header:
            print(f"missing {missing}")
            grade= grade -10

        else:
            print(f"presented :{ missing}")

    print(grade)
    if grade ==60:
        print(" The website grade is A")
    elif grade==50:
        print(" The website grade is b")
    elif grade==40:
        print(" The website grade is c") 
    elif grade==30:
        print("The website grade is c")
    elif grade==20:
        print("The website grade is D")    
    elif grade==10:
        print("The website grade is e")
    elif grade==0:
        print("The website grade is F")
    else:
        print("perfect grade")







if __name__ =="__main__":
    url="https://www.happymonial.com/"
    scanheader(url)
