#israel karpel, 307859702, lavi hen zion
from hashlib import sha256
import math
org_len = 0
markel_tree = []
txta = input()
txt = txta.split()
exist = 0
while txt[0] != "5":
    if txt[0] == "1":
        markel_tree = []
        del txt[0]
        #creates the tree nodes
        for x in txt:
            markel_tree.append(x)
        org_len = (len(markel_tree))
        count = math.log(org_len, 2)
        j = 0
        r = 0
        h = 1
        #creates the tree with all his nodes
        while j < count:
            for i in range(r, len(markel_tree), 2):
                markel_tree.append(sha256(str(markel_tree[i] + markel_tree[i+1]).encode('UTF-8')).hexdigest())
            r = r + int(org_len/h)
            h = h * 2
            j = j + 1
        print(markel_tree[(org_len-1)*2])
        exist = 1

    if txt[0] == "2":
        num = int(txt[1])
        if exist == 0:
            print("No tree given")
            #if the node is even one, hash him with the previus nose, and vice verca
        if num % 2 == 0:
            current_path = sha256(str(markel_tree[num] + markel_tree[num+1]).encode('UTF-8')).hexdigest()
            print("r " + markel_tree[num+1], end=" ")
        else:
            current_path = sha256(str(markel_tree[num - 1] + markel_tree[num]).encode('UTF-8')).hexdigest()
            print("l " + markel_tree[num-1], end=" ")
        i = 0
        count = math.log(org_len, 2)
        #repeat as the height of the tree
        while i < count-1:
            j = org_len
            #as long as we didnt get the nose in the tree
            while current_path != markel_tree[j]:
                j = j + 1
            #for every node we check his evenity ans hash with his partner
            if j % 2 == 0:
                print("r " + markel_tree[j+1], end=" ")
                current_path = sha256(str(markel_tree[j] + markel_tree[j + 1]).encode('UTF-8')).hexdigest()
            else:
                print("l " + markel_tree[j-1], end=" ")
                current_path = sha256(str(markel_tree[j - 1] + markel_tree[j]).encode('UTF-8')).hexdigest()
            i = i + 1
        print("")

    if txt[0] == "3":
        #the first hash
        if txt[3] == "l":
            current_path = sha256(str(txt[4] + txt[1]).encode('UTF-8')).hexdigest()
        else:
            current_path = sha256(str(txt[1] + txt[4]).encode('UTF-8')).hexdigest()
            #as long as there are more nodes we check what his position and hash him accordingly
        if len(txt) > 5:
            i = 5
            while i < len(txt):
                if txt[i] == "l":
                    current_path = sha256(str(txt[i + 1] + current_path).encode('UTF-8')).hexdigest()
                else:
                    current_path = sha256(str(current_path + txt[i + 1]).encode('UTF-8')).hexdigest()
                i = i + 2
        if current_path == txt[2]:
            print("true")
        else:
            print("false")

    if txt[0] == "4":
        zeros_number = "0"
        i = 1
        #check how much 00 needed
        while not str(i) == txt[1]:
            zeros_number = zeros_number + "0"
            i = i + 1
        i = 0
        number = sha256(str(str(i) + markel_tree[len(markel_tree)-1]).encode('UTF-8')).hexdigest()
        #going over all the numbers until we get enough 00
        while not number.startswith(zeros_number):
            i = i + 1
            number = sha256(str(str(i) + markel_tree[len(markel_tree)-1]).encode('UTF-8')).hexdigest()
        print(i, end=" ")
        print(number)
    if txt[0] == "5":
        exit()
    txta = input()
    txt = txta.split()