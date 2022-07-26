from urllib.request import urlopen



myURL = urlopen("https://www.runoob.com/")
lines = myURL.readlines()
#for line in lines:
#    print(line)
print(myURL.getcode())

print(dir(myURL))

