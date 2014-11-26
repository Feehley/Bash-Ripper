#John Feehley
#I was hoping I could get everything to work properly...
import crypt, sys
if sys.argv[3] == 1:
	arg=("$1$" + sys.argv[2])
elif sys.argv[3] == 2:
	arg=("$2a$" + sys.argv[2])
elif sys.argv[3] == 5:
	arg=("$5$" + sys.argv[2])
else:
	arg =("$6$" + sys.argv[2])


print crypt.crypt(sys.argv[1], arg)
