import numpy as np

#PART 1:
def slice_concat(a):
    pass

#PART 2:
def thanks_global_warming(weather):
    pass

def main():
    #PART 1
    a = np.array([[1, 5, 4, 3, 4],
                    [6, 1, 3, 3, 3],
                    [6, 7, 1, 2, 2],
                    [1, 4, 2, 1, 2],
                    [2, 3, 2, 2, 1]])
    print(slice_concat(a))
    
    #PART 2: 
    weather_data = np.array([[51,54,59,61,62,64,67,68,68,70,71,75,79,78,74,74,70,68,66,66,64,62,53,53],
                             [53,58,61,62,64,64,66,71,72,72,44,74,75,77,76,69,68,67,64,63,62,61,57,51],
                             [53,55,55,57,59,63,64,65,66,66,66,79,79,80,77,75,71,63,62,62,54,53,52,52],
                            [51,52,54,58,58,60,62,62,63,65,67,68,74,80,80,78,66,65,62,61,60,60,55,54]])
    
    print(thanks_global_warming(weather_data))
    




if __name__ == "__main__":
    main()