import string
from collections import deque

encoded = "XITOVEYRLKKGFIWYYSZVGMOYCXJOCUOVCXSQDVYXKCBWRYPMFIWYYIXSUDLCBYJOWYXHQYHMSEDEPJMSKWMRWILDWURERSQRRMLUMLQSDISSGSSVHLDKCDXFSWDBSKKRWYXFOVEECGTYQDAYXRYDIJVCMELMGMKPICVMLQKMDXYWEIOCMEYLNIPCXYXHLOZCBKMXRYQMTOCMEYNXITOVEYRLKPCDCMEHMGRLOZCBKMXRYBYLKVMERBKRBNIQOVRISSXITOVEYRLKQYUIWYYABCLOZCBKMXRYCEWQSMNFWORCFIPQSLXEROPJKPGOELNLSBXWYYUOZCURMGRCKGFYXFOVDYVQYPMXKWYYPRIYBXQLICXEARMLQFSDCMEVCDSMCLWDSQKCGDMLCMBOACLSRROLYAURERCFCOREYMLQSLGIIXSUDLCQEKOELNACBIEYRLKTJKCGDELNMDISSKWIWIFYAGWJCOPGXKBYRRDIJVQCISSBIRYSZVMLNXMCICXITOVEYRLKKGFIWYYSZRCFIPQSLXEJOXWYYBYALXITOVEYRLKVSXEPYYLNELNHCCIPDCMERCFIPQSLXEKKOCISSMVWXITOVEYRLKWYIKMYHZIILOZCBKMXRYDIJVEJSIYXHFEVRISSXITOVEYRLKKGFIWYYSZRCFIPQSLXEJOXWYYBYALXITOVEYRLKVSXEPYYLNELNHCCIPDCMERCFIPQSLXEKKOCISSMVWXITOVEYRLKWYIKMYHZIILOZCBKMXRYDIJVEJSIYXHFEVRISSXITOVEYRLKKGFILOZCBKMXRYQMTOKGFIWYYSZSMRRCFIPQSLXEESZCXITOVEYRLKKGFIESZCISSETUOZCURMGRCKGFYXFOVDYVQYPMXKWYYPRIYBXQLICXEARMLQFSDCMEVCDSMCLWDSQKCGDMLCMBOACLSRROLYAURERCFCOREYMLQSLGIIXSUDLCQEKOELNACBIEYRLKTJKCGDMHEWRGELXEROPJISSRSUSQDOIJSREQSRDEKKOCISSERBOVQDELNRCFIPQSLXEESZCISSETLOZCBKMXRYVIRISSNSUXRCFIPQSLXEPERYBSSXHYXHBOWCBXWYYLOZCBKMXRYWEIOCMEGPIRCFIPQSLXEQKCEYSBLCCXITOVEYRLKXCVPYVMCKRBRYPDCMERCFIPQSLXEESZCISSETLOZCBKMXRYVIRISSNSUXRCFIPQSLXEPERYBSSXHYXHBOWCBXWYYLOZCBKMXRYWEIOCMEGPIRCFIPQSLXEQKCEYSBLCCXITOVEYRLKXCVPYVMCKRBRYPDCMERCFIPQSLXEESZCISSETLOZCBKMXRYVIRISSNSUXRCFIPQSLXEPERYBSSXHYXHBOWCBXWYYLOZCBKMXRYWEIOCMEGPI"
freq=[0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
key_combo = []
password_combo =[]
 
def best_one(cipher_array,interval,dic_reverse):
    j = 0
    total_statistics = []
    test_key = [0]*interval
    decryption_key_array = ["a"]*interval
    dic_array = ["a"]*interval
    fit_array = [0.0]*interval
    int_array = [0] * 26
    while j < interval:
        best_fit_value = 100.0
        int_array = [0] * 26
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
        items.rotate(-1)
        for i in range(0,26):
            items.rotate(1)
            curr_array = list(items)
            compare_value= 0.0          
            for match in range(0,26):              
                compare_value += ((curr_array[match] - freq[match])**2/freq[match])
            if (compare_value<best_fit_value):
                best_fit_value = compare_value
                test_key[j] = i#When it shifts back, it needs to be "key"+1 because we have a rota
                fit_array[j] = best_fit_value
        j+=1
    bfit_avg_result = sum(fit_array)/j
    for count in range(0,len(test_key)):
        decryption_key_array[count] = dic_reverse[test_key[count]]   
    reverse_password =''.join(map(str, decryption_key_array))
    password_combo.append(reverse_password)
    for ind in range(0,len(test_key)):
        test_key[ind] = (26 - test_key[ind])%26
    for count in range(0,interval):
        dic_array[count] = dic_reverse[test_key[count]]        
    key_string =''.join(map(str, dic_array))
    key_combo.append(key_string)
    return bfit_avg_result

def decrypt(decryption_key, cipher_text_int, reverse_dic,dic,key_length):
    copy = cipher_text_int
    string_copy = ["a"]*len(copy)
    int_key_array =[]
    for item in decryption_key:
        int_key_array.append(dic.get(item))       
    for i in range(0,len(copy)):
        index = i%(key_length)
        shift = int_key_array[index]
        copy[i]+= shift
        copy[i]%=26
        string_copy[i] = reverse_dic.get(copy[i])
    plaintext =''.join(map(str, string_copy))
    return plaintext

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
    combo = []
    k_length= 1
    while k_length < 26: 
        key_string = "0"*k_length
        curr_fit = best_one(cipher_integer,k_length,reverse_dic)
        if curr_fit < best_fit:
            best_fit = curr_fit
            final_key_length = k_length
        k_length+=1
    decryption_key = password_combo[final_key_length-1]  
    encryption_key = key_combo[final_key_length-1]
    plaintext = decrypt(decryption_key,cipher_integer,reverse_dic,dic,final_key_length)
    print("After cross correlation, best Key Length is:",final_key_length)   
    print("Professor used password : '",encryption_key, "' to encrypt the plaintext")
    print( "We could use decryption key '"  ,decryption_key , "' to decrypt message")   
    print("Here is the plaintext after decoding with the key:\n"+ plaintext)
if __name__== "__main__":
  main()
