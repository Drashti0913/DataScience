from os import listdir

def get_pet_labels(image_dir):
    in_files = listdir(image_dir)
    results_dic = dict()

    for idx in range(0, len(in_files), 1):
       
      
       if in_files[idx][0] != ".":

       
           low_pet_image = in_files[idx].lower()
           word_list_pet_image = low_pet_image.split("_")
           pet_name = ""
           for word in word_list_pet_image:
               if word.isalpha():
                   pet_name += word + " "
           pet_name = pet_name.strip()
           if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_name]
              
           else:
               print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])

        
     
    return results_dic