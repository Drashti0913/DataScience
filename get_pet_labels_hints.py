from os import listdir


def get_pet_labels(image_dir):
    in_files = listdir(image_dir)
    
 
    results_dic = dict()
   
    
    for idx in range(0, len(in_files), 1):
       
     
       if in_files[idx][0] != ".":
           
           pet_label = ""

           pass

          
           if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_label]
              
           else:
               print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])
 
    return None
