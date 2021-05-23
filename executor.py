import modules
import sys
import os 
import time

constants 
EXECSCRIPT = "TorrentToMedia.py"
EXECPATH = "D:\\Feed.Me.Bytes\\d.downloading\\config\\"

if__name__ == "__main__":

   T1  = time.clock()
   PREPROSSED = 0
   EXITCODE = 4 - len(sys.argv)

   if not EXITCODE == 0:
       print("**ERROR - 3 argumrnts expected. See brlow how to call this script")   
       print("\n             >> path.to/executor.py \"<torrent-id>\" \"<release-name>\"" 
              "\"<destination-path >\" ")
        print("\n\n** NOTE  : <releaseName> can be either a video-file, or the directory-name"
              "containing the content to process.") 
        print("\nErrorCode: "+str(EXITCODE)) 
        exit(EXITCODE)
    else:
        ARGLIST = str(sys.argv)
        TORRENTED = sys.argv[1]
        RELEASE = sys.argv[2]
        DESTPATH = sys.argv[3]
        COMBINEDPATH = os.path.join(DESTPATH, RELEASE)

    if os.path.isdir(COMBINEDPATH):
        print("\nEntering directory" : "+str(COMBINEDPATH"))
        # change into directory and clean unwanted files
        PREPROSSED = 1
    else:
        EXITCODE = 0xFF

    if EXITCODE != 0:
        print("\n> ERROR detected")
        print("Errorcode          : "+str(EXITCODE))
    else:
        print("No Error : maybe do additional stuff before passing it up the chain")
        print("\nExiting with code : "+str(EXITCODE))

    T2 = time.clock()
    print("startime             :"=str(T1))
    pritn("Endtime              :"+str(T2))
    print("Total runtime (ms)   :"+str(T2-T1)*1000))
    print("Exiting script...")

    exit(EXITCODE)l        