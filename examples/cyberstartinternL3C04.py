import requests

#get strings from the sites
r_one = requests.get('https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D')
r_two = requests.get('https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D')
r_three = requests.get('https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D')
r_four = requests.get('https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D')
r_five = requests.get('https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D')

#checking the strings
print(r_one.text)
print(r_two.text)
print(r_three.text)
print(r_four.text)
print(r_five.text)

#concat aka join the strings together
validation = r_one.text + r_two.text + r_three.text + r_four.text + r_five.text
print(validation)

# send request to the verification server with cat string as part of the url

# headerdata = {'verify':'Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D','string':str(validation)}
flag = requests.get('https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string='+validation)

print(flag.text)
