'''
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's 
code or Caesar shift, is one of the simplest and most widely known encryption techniques. 
It is a type of substitution cipher in which each letter in the plaintext is replaced by a 
letter some fixed number of positions down the alphabet. For example, with a left shift 
of 3, D would be replaced by A, E would become B, and so on. The method is named after 
Julius Caesar, who used it in his private correspondence.

Write a Python program to create a Caesar encryption.

This might be updated with other methods
'''


class CaesarCipher():

    def __init__(self, shift):

        encoder: list = [None] * 26
        decoder: list = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord("A"))
            decoder[k] = chr((k - shift) % 26 + ord("A"))
        self._forward = "".join(encoder)
        self._backward = "".join(decoder)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    @staticmethod
    def _transform(original, code):

        msg = list(original)

        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]

        return "".join(msg)
