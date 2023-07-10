
def adjust_results4_isadog(results_dic, dogfile):
 
    dognames_dic = dict()

    with open(dogfile, "r") as infile:
        line = infile.readline()

        while line != "":

            pass

            pass 

            line = infile.readline()

                
    for key in results_dic:

        if results_dic[key][0] in dognames_dic:
         
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1, 1))

           
            else:
                pass

        else:
         
            if results_dic[key][1] in dognames_dic:
                pass

            else:
                pass
    