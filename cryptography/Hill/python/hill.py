from typing import List

class Hill:
    
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix


    def encrypt(self, message: str):
        # Convert message to a list of characters
        char_list = [char for char in message]

        # Convert the list of characters to a list of numbers (from 1 to 26, corresponding to the alphabet)
        number_list = [(ord(letter) % 96) for letter in char_list]

        # Initialize the encrypted message
        encrypted_message = []

        # Encrypt 
        for i in range(0, len(message), 2):
            c1 = (self.matrix[0][0] * number_list[i] + self.matrix[0][1] * number_list[i+1]) % 26
            c2 = (self.matrix[1][0] * number_list[i] + self.matrix[1][1] * number_list[i+1]) % 26
            encrypted_message.append(c1)
            encrypted_message.append(c2)
            
        # return the encrypted message by converting the list of numbers to an ASCII string and also return the matrix
        return ''.join([chr(number + 96) for number in encrypted_message]), self.matrix

    def decrypt(self, message: str):
        inverted_matrix = self._invert_matrix()
        
        # ad - bc
        determinant = (inverted_matrix[0][0] * inverted_matrix[1][1]) - (inverted_matrix[0][1] * inverted_matrix[1][0])

        # Calculate modulo
        modulo = 0
        for value in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
            if ((determinant * value) % 26 == 1):
                modulo = value
                break

        if modulo == 0:
            return 'error : modulo could not be found.'
        
        decrypt_matrix = [
            [(modulo * inverted_matrix[0][0]) % 26, (modulo * inverted_matrix[0][1]) % 26],
            [(modulo * inverted_matrix[1][0]) % 26, (modulo * inverted_matrix[1][1]) % 26]
        ]

        # Convert message to a list of characters
        char_list = [char for char in message]

        # Convert the list of characters to a list of numbers (from 1 to 26, corresponding to the alphabet)
        number_list = [(ord(letter) % 96) for letter in char_list]

        decrypted_message = []

        # Decrypt
        for i in range(0, len(message), 2):
            p1 = (decrypt_matrix[0][0] * number_list[i] + decrypt_matrix[0][1] * number_list[i+1]) % 26
            p2 = (decrypt_matrix[1][0] * number_list[i] + decrypt_matrix[1][1] * number_list[i+1]) % 26
            decrypted_message.append(p1)
            decrypted_message.append(p2)

        # return the decrypted message by converting the list of numbers to an ASCII string and also return the matrix
        return ''.join([chr(number + 96) for number in decrypted_message]), decrypt_matrix

    def _invert_matrix(self):
        row1 = [self.matrix[1][1], self.matrix[0][1] * -1]
        row2 = [self.matrix[1][0] * -1, self.matrix[0][0]]
        return [row1, row2]


if __name__ == "__main__":
    hill = Hill([[9, 4], [5, 7]])
    encrypted_message, encrypt_matrix = hill.encrypt('aaaaaacesi')
    decrypted_message, decrypt_matrix = hill.decrypt(encrypted_message)
    print('Encrypted message:', encrypted_message, encrypt_matrix)
    print('Decrypted message:', decrypted_message, decrypt_matrix)
