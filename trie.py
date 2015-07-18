class Node (object):
    
    def __init__(self, letter):
        self.letter = letter
        self.children = [None] * 26
        self.isWord = False
        
    def __str__(self):
        return str(self.letter)
        
        
class Trie (object):

    def __init__(self):
        self.headNode = Node(' ')

    def insert(self, word):
        """inserts a word into the trie"""
 
        # first remove '\n' and then make sure all of the letters are char a-z
        word = word.strip()
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for letter in word:
            if letter not in alphabet:
                word = word.replace(letter, "") # other characters are removed       
        
        temp = self.headNode
        
        for letter in word:
            index = ord(letter)-97
            if temp.children[index] is None:
                temp.children[index] = Node(letter)
                temp = temp.children[index]
            else:
                temp = temp.children[index]
               
        temp.isWord = True
            
    def isWord(self, word):
        """returns true if the word is an accepting node in the trie"""
        
        # first remove '\n' and then make sure all of the letters are char a-z
        word = word.strip()
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for letter in word:
            if letter not in alphabet:
                word = word.replace(letter, "") # other characters are removed               
                
        temp = self.headNode

        for letter in word:
            index = ord(letter)-97
            if temp.children[index] is None:
                return False
            else:
                temp = temp.children[index]

        return temp.isWord
        
        
if __name__ == "__main__":
    t = Trie()
    t.insert('cat')
    t.insert('cartoon')
    print 'cat is word?'
    print t.isWord('cat')
    print 'rabbit is word?'
    print t.isWord('rabbit')

    
