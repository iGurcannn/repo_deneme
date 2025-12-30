# xler sabit 1 o x e dönüsecek
# diğer o lar sabit kalacak
# parenttaki stringte değiştirilecek olan o ya en az bir x komşu olacak
# P parent c child L benim listem

# L = "OOXOO"
# s = "OXXOO"


def is_child(parent,child):
    my_count = 0
    changeabale_O = []
    
    for i in range(len(parent)):
        if parent[i] != child[i]:
            my_count += 1
            changeabale_O.append(i)
            
    if len(changeabale_O) != 1:
        return False
    
    i = changeabale_O[0]
    
    if parent[i] != "O" or child[i] != "X":
        return False
    
    my_left = i > 0 and parent[i - 1] == "X"
    my_right = i < len(parent) - 1 and parent[i + 1] == "X"
    
    if my_left or my_right:
        return True
    
        
    return False



# print(is_child("XOOOO", "XXOOO"))


def count_children(L):
    my_dict = {}
    
    for p in L:
        count = 0
        
        for c in L:
            if is_child(p, c):
                count += 1
            
        my_dict[p] = count
        
    return my_dict

L = [
 "OOXOO",
 "OOXXO",
 "OXXOO",
 "OOXXX",
 "OXXXO",
 "XXXOO",
 "OXXXX",
 "XXXXO",
 "XXXXX",
 "OXOXO"
] 

# print(count_children(L))


def list_of_children(L):
    my_list = []
    
    for p in L:
        my_list.append(p)
        not_constant_list = []
        for c in L:
            if is_child(p, c):
                
                not_constant_list.append(c)
        my_list.append(not_constant_list)
                
                
    return my_list
    
print(list_of_children(L))       
    
    








            
            
                    
        
        
    
        
    
        
        

    

           
            
        
