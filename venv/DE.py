file = open('C:/Users/bmanj/PycharmProjects/Practice/names.txt')
names= file.readlines()

def createMail(names,domain):
    return names+domain

for name in names:
    value=name.strip().lower().replace(" ", "_")
    mail[mail]=map(createMail(value,"@pydemo.com"),names)
    print(mail)

#print(List.strip().lower().replace(" ", "_") + domain)