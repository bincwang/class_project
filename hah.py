import string
from collections import deque
encoded = "XITOVEYRLKKGFIWYYSZVGMOYCXJOCUOVCXSQDVYXKCBWRYPMFIWYYIXSUDLCBYJOWYXHQYHMSEDEPJMSKWMRWILDWURERSQRRMLUMLQSDISSGSSVHLDKCDXFSWDBSKKRWYXFOVEECGTYQDAYXRYDIJVCMELMGMKPICVMLQKMDXYWEIOCMEYLNIPCXYXHLOZCBKMXRYQMTOCMEYNXITOVEYRLKPCDCMEHMGRLOZCBKMXRYBYLKVMERBKRBNIQOVRISSXITOVEYRLKQYUIWYYABCLOZCBKMXRYCEWQSMNFWORCFIPQSLXEROPJKPGOELNLSBXWYYUOZCURMGRCKGFYXFOVDYVQYPMXKWYYPRIYBXQLICXEARMLQFSDCMEVCDSMCLWDSQKCGDMLCMBOACLSRROLYAURERCFCOREYMLQSLGIIXSUDLCQEKOELNACBIEYRLKTJKCGDELNMDISSKWIWIFYAGWJCOPGXKBYRRDIJVQCISSBIRYSZVMLNXMCICXITOVEYRLKKGFIWYYSZRCFIPQSLXEJOXWYYBYALXITOVEYRLKVSXEPYYLNELNHCCIPDCMERCFIPQSLXEKKOCISSMVWXITOVEYRLKWYIKMYHZIILOZCBKMXRYDIJVEJSIYXHFEVRISSXITOVEYRLKKGFIWYYSZRCFIPQSLXEJOXWYYBYALXITOVEYRLKVSXEPYYLNELNHCCIPDCMERCFIPQSLXEKKOCISSMVWXITOVEYRLKWYIKMYHZIILOZCBKMXRYDIJVEJSIYXHFEVRISSXITOVEYRLKKGFILOZCBKMXRYQMTOKGFIWYYSZSMRRCFIPQSLXEESZCXITOVEYRLKKGFIESZCISSETUOZCURMGRCKGFYXFOVDYVQYPMXKWYYPRIYBXQLICXEARMLQFSDCMEVCDSMCLWDSQKCGDMLCMBOACLSRROLYAURERCFCOREYMLQSLGIIXSUDLCQEKOELNACBIEYRLKTJKCGDMHEWRGELXEROPJISSRSUSQDOIJSREQSRDEKKOCISSERBOVQDELNRCFIPQSLXEESZCISSETLOZCBKMXRYVIRISSNSUXRCFIPQSLXEPERYBSSXHYXHBOWCBXWYYLOZCBKMXRYWEIOCMEGPIRCFIPQSLXEQKCEYSBLCCXITOVEYRLKXCVPYVMCKRBRYPDCMERCFIPQSLXEESZCISSETLOZCBKMXRYVIRISSNSUXRCFIPQSLXEPERYBSSXHYXHBOWCBXWYYLOZCBKMXRYWEIOCMEGPIRCFIPQSLXEQKCEYSBLCCXITOVEYRLKXCVPYVMCKRBRYPDCMERCFIPQSLXEESZCISSETLOZCBKMXRYVIRISSNSUXRCFIPQSLXEPERYBSSXHYXHBOWCBXWYYLOZCBKMXRYWEIOCMEGPI"

freq=[0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

fit_combo = []
key_combo = []



    
def best_one(cipher_array,interval,dic_reverse):
    
    #This function is used for finding the best matching key in given length
    #How: Use brute force to find the best match here
    #return my_array(key string)
    
    
    j = 0
    total_statistics = []
    test_key = [0]*interval
    dic_array = ["a"]*interval
    fit_array = [0.0]*interval
    int_array = [0] * 26
    while j < interval:
        best_fit_value = 100.0
        int_array = [0] * 26
        # First loop taking out all integers
        #Second loop, build a string array called testkey
           #Now we could start using brute force

  #This is used for calculating the difference
                            #between given array with average English letter frequency
        float_array = [0.0] * 26
        compare_array = []
        for num in range(j,len(cipher_array),interval):           
            index = cipher_array[num] 
            int_array[index]+=1
        words_count = sum(int_array)
        
        for i in range(0,26):
            if(int_array[i]==0):
                int_array[i] = 1
            float_array[i] = int_array[i]/words_count


        items = deque(float_array)
        
        #Time to play with shift, test from a to z 
        for i in range(0,26):
            items.rotate(1)
            curr_array = list(items)
            compare_value= 0.0
            
            for match in range(0,26):
               
                compare_value += ((curr_array[match] - freq[match])**2/freq[match])

                #I think someone to check if compare_value is using
                #The right algorithm to compare string similarity
                #Cross correlation
            if (compare_value<best_fit_value):
                best_fit_value = compare_value
                test_key[j] = i
                fit_array[j] = best_fit_value
        j+=1
    bfit_avg_result = sum(fit_array)/j

    for ind in range(0,len(test_key)):
        test_key[ind] = 25 - test_key[ind]
    
    for count in range(0,interval):
        dic_array[count] = dic_reverse[test_key[count]]


    
        
    key_string =''.join(map(str, dic_array))
    key_combo.append(key_string)
    return bfit_avg_result
    
                                  
            
        

        
        #Now Float array holds the frequency of each alphabetic letters in each interval


    return 
    #Suppose to return a key pair
           
    # We are using cipher_integer here
    #We are trying to take out all those single characters among interval

def decrypt():
    return 0
 
def main():
    final_key_length = 0
    best_fit = 1000
    best_key = ""

    
    cipher= encoded.lower()
    alpha = list(map(chr, range(97, 123)))     
    number = []
    fit_array = [] #The lowest integer in there will be the best fit
    for i in range(0,26):
        number.append(i)
    dic = dict(zip(alpha,number)) # Dic is {'a'->0, 'b'->1,...'z'-25
    reverse_dic = dict(zip(number,alpha))
    cipher_integer =[]  #cipher integer contains "encoded" integer format
    for item in cipher:
        cipher_integer.append((dic.get(item)))
        #Now, cipher_integer holds every char in encoded.lower() with a integer string format


    combo = []

    k_length= 1
    while k_length < 26: #test key from length one to length 10, when it's too
                         #big, it will have some problem with statistics.
        key_string = "0"*k_length
        curr_fit = best_one(cipher_integer,k_length,reverse_dic)
        #After we store fir number into fit_array, we compare and find the best one
        if curr_fit < best_fit:
            best_fit = curr_fit
            final_key_length = k_length
            #Compare the best fit with the curr fit 
        k_length+=1
        #Keep looping
    print("Final Key Length is:",final_key_length)
    
    print("Professor used password : '",key_combo[final_key_length-1], "' to encrypt the plaintext")
    

 
if __name__== "__main__":
  main()
