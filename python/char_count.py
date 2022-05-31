from operator import countOf
import turtle
from collections import OrderedDict

def char_count(str):
      str=str.replace(" ", "")
      trueStr={} 
      for i in str:
        count=countOf(str, i)
        key=i
        #print(countOf(trueStr, key))
        if countOf(trueStr, key)< 1:
          obj={key:count}
          trueStr.update(obj)
      return trueStr
      #trueStr=OrderedDict(sorted(trueStr.items()))
      #print(trueStr)
        
      
print(char_count("aaabbc"))