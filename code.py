#RLE
i=0
def encode(message):
    count=1
    String=""
    s=None
    i=len(message)-1
    if(len(message)==1):
        s="1"+message[0]
        String=String+s
    else:    
        for i in range(0,(len(message)-1)):
            
            if(message[i]==message[i+1]):
                count=count+1
                
            else:
                s=str(count)+message[i]
                String=String+s
                count=1
                s=""
        j=i+1
        if(j==(len(message)-1) and (message[j]!=message[j-1])):
                s="1"+message[j]
                String=String+s

    return String        
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
