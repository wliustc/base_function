import os,sys
basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print basedir

print os.path.dirname(__file__)
#get your file's directory name

print __file__
#get your file name

print os.path.abspath('.')
#get the currently directory

print sys.stdout.encoding
print os.getcwd()
#get your system coding

#os.startfile('1.mp3')

if __name__=="__main__":
    print "Start from here"

