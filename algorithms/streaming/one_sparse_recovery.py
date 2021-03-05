""" Non-negative 1-sparse recovery problem. This algorithm assumes we have a non negative dynamic stream.
Given a stream of tuples, where each tuple contains a number and a sign (+/-), it check if the stream is 1-sparse, meaning if the elements 
in the stream cancel eacheother out in such a way that ther is only a unique number at the end. 

Examples:
If the stream consists of [(4,'+'), (2,'+'),(2,'-'),(4,'+'),(3,'+'),(3,'-')], the algorithm will return 4, since the 2s and 3s will cancel eachother out
and there will only be 4s left

If the stream consists of [(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+')], the algorithm returns 2, since the stream only consists of the same number and sign

If the stream consists of [(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(1,'+')], the algorithm returns None, since there will be 2 different number remaining 


"""

def one_sparse(array):
  sum_signs = 0 
  bitsum = [0]*32 
  sum_values = 0 
  for val,sign in array: 
    if sign == "+": 
      sum_signs += 1
      sum_values += val
    else:
      sum_signs -= 1 
      sum_values -= val
    
    _get_bit_sum(bitsum,val,sign)
  
  if sum_signs > 0 and _check_every_number_in_bitsum(bitsum,sum_signs):
    return int(sum_values/sum_signs)
  else:
    return None
   
#Helper function to check that every entry in the list is either 0 or  the same as the
#sum of signs
def _check_every_number_in_bitsum(bitsum,sum_signs):
  for val in bitsum: 
    if val != 0 and val != sum_signs : 
      return False
  return True

# Adds bit representation value to bitsum array
def _get_bit_sum(bitsum,val,sign):
  i = 0 
  if sign == "+":
    while(val):
      bitsum[i] += val & 1
      i +=1
      val >>=1
  else :
    while(val):
      bitsum[i] -= val & 1
      i +=1
      val >>=1


