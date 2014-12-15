from os import walk
import numpy as np

def hours_to_mins(str_hours):
    '''
    convert "HH:MM" into minutes
    '''
    h = int(str_hours[0:2])
    m = int(str_hours[3:])
    
    return str(m + 60 * h)

def mean(values_lst):
    '''
    Mean of the list of numbers
    '''
    if len(values_lst) == 0:
        return "-1"
    else:
        float_values_lst = [float(x[1]) for x in values_lst]
        return str(sum(float_values_lst)/len(float_values_lst))

def std(values_lst):
    '''
    Standard deviation of the list of numbers
    '''
    if len(values_lst) <= 1:
        return "-1"
    else:
        float_sq_values_lst = [float(x[1])*float(x[1]) for x in values_lst]
        float_values_lst = [float(x[1]) for x in values_lst]
        
        mean_sq = sum(float_sq_values_lst)/len(float_sq_values_lst)
        mean = sum(float_values_lst)/len(float_values_lst)
        
        return str(mean_sq - mean*mean)

def grad_mean(values_lst):
    '''
    Mean 'gradient' of the temporal attributes
    '''
    if len(values_lst) <= 1:
        return "-1"
    else:
        grad = [(float(values_lst[i][1])-float(values_lst[i-1][1]))/(float(values_lst[i][0])-float(values_lst[i-1][0])) for i in range(1, len(values_lst)) if (float(values_lst[i][0])-float(values_lst[i-1][0])) > 0]
        
        
        if len(grad) > 0:
            mean = sum(grad)/len(grad)        
            return str(mean)
        else:
            return "-1"

def grad_std(values_lst):
    '''
    Standard deviation of 'gradient' of the temporal attributes
    '''
    if len(values_lst) <= 1:
        return "-1"
    else:
        grad = [(float(values_lst[i][1])-float(values_lst[i-1][1]))/(float(values_lst[i][0])-float(values_lst[i-1][0])) for i in range(1, len(values_lst)) if (float(values_lst[i][0])-float(values_lst[i-1][0])) > 0]
        grad_sq = [g*g for g in grad]
        
        if len(grad) > 0:
            mean = sum(grad)/len(grad) 
            mean_sq =  sum(grad_sq)/len(grad_sq)       
            return str(mean_sq-mean*mean)
        else:
            return "-1"

def main():
    '''
    main function of the script
    '''
    # Initialisaton
    data = []
    X_file = open('X.csv', 'w')
    y_file = open('y.csv', 'w')
    Xy_file = open('Xy.csv', 'w')
    Xy_missing_file = open('Xy_missing.csv', 'w')
    Xy_missing_file_shuffle = open('Xy_missing_shuffle.csv', 'w')
    
    # Lists of all labels - unique and temporal
    attrs_labels = ['Age', 'Gender', 'Height', 'ICUType', 'Weight']
    temp_attrs_labels = ['Albumin', 'ALP', 'ALT', 'AST', 'Bilirubin', 'BUN', 'Cholesterol', 'Creatinine',
        'DiasABP', 'FiO2', 'GCS', 'Glucose', 'HCO3', 'HCT', 'HR', 'K', 'Lactate', 'Mg', 'MAP',
        'MechVent', 'Na', 'NIDiasABP', 'NIMAP', 'NISysABP', 'PaCO2','PaO2', 'pH', 'Platelets', 'RespRate',
        'SaO2', 'SysABP', 'Temp', 'TroponinI', 'TroponinT', 'Urine', 'WBC']
    
    # Importing all output into a dictionary 
    output_dict = {}
    with open("dataset_output.txt", 'r') as f:
        file_content = f.readlines()
        
        for line in file_content[1:]:
            line_values = line.strip().split(',')
            output_dict[line_values[0]] = line_values[1:]
    
    Xs = []
    ys = []
    
    # Loop through all files 
    for (root, _, files) in walk("dataset/"):
        for file_name in files:
            file_path = root + "/" + file_name
            
            with open(file_path, 'r') as f:
                file_content = f.readlines()
                
                x = []
                y = []
                xy = []
                
                ID = file_content[1].strip().split(',')[2]
                
                attrs = ["-1" for i in range(len(attrs_labels))]
                temp_attrs = [[] for i in range(len(temp_attrs_labels))]
                
                # Reading all attributes from dataset
                for line in file_content[2:]:
                    line_values = line.strip().split(',')
                    feature_label = line_values[1]
                    
                    if feature_label in attrs_labels:
                        feature_index = attrs_labels.index(feature_label)
                        attrs[feature_index] = line_values[2]
                    elif feature_label in temp_attrs_labels:
                        feature_index = temp_attrs_labels.index(feature_label)
                        temp_attrs[feature_index].append((hours_to_mins(line_values[0]), line_values[2]))
                    else:
                        print "GRAND ERROR"
                
                # Writing features
                for attr in attrs:
                    x.append(attr)
                for temp_attr in temp_attrs:
                    x.append(mean(temp_attr))
                    x.append(std(temp_attr))
                    x.append(grad_mean(temp_attr))
                    x.append(grad_std(temp_attr))
                
                # writing output
                y.append(output_dict[ID][4])
                
                # writing to files
                X_file.write(",".join(x) + "\n")
                if len(y) > 1:
                    y_file.write(",".join(y) + "\n")
                else:
                    y_file.write(y[0] + "\n")
                    
                xy = y + x
                Xy_file.write(",".join(xy) + "\n")
                    
                xy_missing = ["" if i == "-1" else i for i in xy]
                Xy_missing_file.write(",".join(xy_missing) + "\n")
                    
                Xs.append(x)
                ys.append(y)
                
    # randomly shuffle labels     
    ysnp = np.array(ys)
    np.random.shuffle(ysnp)
    ys = ysnp.tolist()
    
    # write randomly shuffled labels to file
    for i in range(len(Xs)):
        xy = ys[i] + Xs[i]
                        
        xy_missing = ["" if i == "-1" else i for i in xy]
        Xy_missing_file_shuffle.write(",".join(xy_missing) + "\n")
          
    # clos all files
    X_file.close()
    y_file.close()
    Xy_file.close()
    Xy_missing_file.close()
    Xy_missing_file_shuffle.close()

if __name__ == "__main__":
    main()