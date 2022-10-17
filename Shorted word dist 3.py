class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        #base condition
        if len(set(wordsDict)) == 2: 
            return 1 
        
        
        indexes_of_word1 = []  #array that has all the indexes of word1 
        
        for i in range(len(wordsDict)): 
            if wordsDict[i] == word1: 
                indexes_of_word1.append(i)  
           
        min_array = [] #array that has all the minimums of respective indexes in 'indexes_of_word1'
        
        
        
        for i in indexes_of_word1: 
            
            global_min = 3 * (10**4)   
            p2 = i-1 
            p3 = i+1
            
            while p2>=0 or p3<=len(wordsDict)-1:  



                if p2>=0 and wordsDict[p2] == word2: 

                    if abs(p2 - i) < global_min: 

                        global_min = abs(p2-i) 

                elif p3<=len(wordsDict)-1 and wordsDict[p3] == word2: 

                    if abs(p3 - i) < global_min: 

                        global_min = abs(p3-i) 

                p2-=1 
                p3+=1    
                
                min_array.append(global_min)
                
            
        return min(min_array)

        #tc - o(n)
        #sc = o(1)