"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """initialize SerialGenerator with a start number"""
        self.start = self.current_num = start

    def __repr__(self):
        """Show representation."""
        return f"<SerialGenerator start={self.start} next={self.current_num}>"

    def generate(self):
        """print next sequential number"""
        self.current_num += 1
        return self.current_num - 1
        
    def reset(self):
        """reset number back to the original start number"""
        self.current_num = self.start


################ ALTERNATE SOLUTION ########################################
    # def __init__(self, start):
    #     """initialize SerialGenerator with a start number"""
    #     self.start = start

    # def generate(self):
    #     """
    #     print the next sequential number
    #     add each number to serialnums.txt file
    #     """
    #     output_file = open("serialnums.txt", "a")
    #     output_file.write(f"{self.start}\n")
    #     self.start += 1
    #     output_file.close()
    #     return self.start -1
        
    # def reset(self):
    #     """
    #     set self.start back to the original start number by grabbing first 3 chars in in line 1 of serialnums.txt
    #     only works if original number is same number as the last output num
    #     """
    #     input_file = open("serialnums.txt", "r").readline()
    #     self.start = int(input_file)
    #     output_file = open("serialnums.txt", "w")
    #     output_file.write(f"{self.start}")
    #     output_file.close()