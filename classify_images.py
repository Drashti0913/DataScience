
from classifier import classifier 


def classify_images(images_dir, results_dic, model):
    for key in results_dic:
        model_label = ""
        classified = classifier(images_dir+'/'+key,model)
 
        low_pet_image = classified.lower()
        

        word_list_pet_image = low_pet_image
       
        low_pet_image = low_pet_image.strip()
        model_label = low_pet_image
        
        truth = results_dic[key][0]
        
        if truth in model_label:
           results_dic[key].extend((model_label,1))
        else:
           results_dic[key].extend((model_label,0))
        
    print(results_dic)